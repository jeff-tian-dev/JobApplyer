"""Pull new internship postings from the SimplifyJobs list and print the ones
that match your targets and aren't already in your tracker.

Usage:
  python find_roles.py --config targets.json [--tracker agent-workbook.xlsx] [--out new_roles.csv]
"""
import argparse, csv, json, sys, urllib.request
from datetime import datetime, timezone, timedelta

LISTINGS = ("https://raw.githubusercontent.com/SimplifyJobs/"
            "{repo}/dev/.github/scripts/listings.json")


def load_listings(repo):
    with urllib.request.urlopen(LISTINGS.format(repo=repo), timeout=60) as r:
        return json.load(r)


def tracked_urls(path):
    if not path:
        return set()
    urls = set()
    if path.endswith(".xlsx"):
        from openpyxl import load_workbook
        wb = load_workbook(path, read_only=True)
        for name in ("Discovery", "Agent Queue", "Applications"):
            if name not in wb.sheetnames:
                continue
            rows = wb[name].iter_rows(values_only=True)
            header = [str(h or "").strip().lower() for h in next(rows)]
            if "role url" not in header:
                continue
            i = header.index("role url")
            urls |= {str(r[i]).split("?")[0] for r in rows if r and len(r) > i and r[i]}
    else:
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                link = {k.strip().lower(): v for k, v in row.items() if k}.get("role url") or {k.strip().lower(): v for k, v in row.items() if k}.get("link")
                if link:
                    urls.add(link.split("?")[0])
    return urls


def matches(job, cfg, cutoff):
    if not (job.get("active") and job.get("is_visible", True)):
        return False
    if job.get("date_posted", 0) < cutoff:
        return False
    cats = [c.lower() for c in cfg.get("categories", [])]
    if cats and not any(c in job.get("category", "").lower() for c in cats):
        return False
    terms = cfg.get("terms", [])
    if terms and not set(terms) & set(job.get("terms", [])):
        return False
    text = (job["title"] + " " + job["company_name"]).lower()
    inc = [k.lower() for k in cfg.get("include_keywords", [])]
    if inc and not any(k in text for k in inc):
        return False
    if any(k.lower() in text for k in cfg.get("exclude_keywords", [])):
        return False
    if any(c.lower() == job["company_name"].lower() for c in cfg.get("exclude_companies", [])):
        return False
    locs = [l.lower() for l in cfg.get("locations", [])]
    if locs and not any(l in " ".join(job.get("locations", [])).lower() for l in locs):
        return False
    if cfg.get("needs_sponsorship") and job.get("sponsorship") in (
            "Does Not Offer Sponsorship", "U.S. Citizenship is Required"):
        return False
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--tracker")
    ap.add_argument("--out", default="new_roles.csv")
    a = ap.parse_args()
    cfg = json.load(open(a.config, encoding="utf-8"))
    days = cfg.get("posted_within_days", 2)
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).timestamp()
    seen = tracked_urls(a.tracker)
    jobs = [j for j in load_listings(cfg.get("repo", "Summer2027-Internships"))
            if matches(j, cfg, cutoff) and j["url"].split("?")[0] not in seen]
    jobs.sort(key=lambda j: j["date_posted"], reverse=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Employer", "Role", "Location", "Posted", "Terms", "Role URL",
                    "Source", "First seen at (UTC)"])
        for j in jobs:
            w.writerow([j["company_name"], j["title"], "; ".join(j.get("locations", [])),
                        datetime.fromtimestamp(j["date_posted"]).strftime("%Y-%m-%d"),
                        ", ".join(j.get("terms", [])), j["url"], "SimplifyJobs", now])
    print(f"{len(jobs)} new matching roles written to {a.out}")


if __name__ == "__main__":
    sys.exit(main())
