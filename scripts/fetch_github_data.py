#!/usr/bin/env python3
"""Pull real GitHub metadata into assets/generated/*.json.

Requires the `gh` CLI, authenticated (`gh auth status`). Re-run any time to
refresh the snapshots that docs/design-dna.md and the topology/instrument
prototypes read from. Nothing here is fabricated — every number downstream
traces back to one of these three files.

Usage:
    python3 scripts/fetch_github_data.py [github-username]
"""
import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "assets" / "generated"

# Repos whose language byte counts are dominated by vendored/bundled
# dependencies rather than authored code (e.g. a committed virtualenv).
# Excluded from the language topology so the diagram stays honest — see
# docs/design-dna.md, Mathematical DNA, for the reasoning.
VENDORED_BLOB_REPOS = {"cs340Project4"}


def run_gh_graphql(query: str) -> dict:
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={query}"],
        capture_output=True, text=True, check=True,
    )
    return json.loads(result.stdout)


def fetch_repos_and_languages(username: str) -> tuple[list, dict]:
    query = f'''
    query {{
      user(login: "{username}") {{
        repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {{
          nodes {{
            name
            description
            pushedAt
            stargazerCount
            primaryLanguage {{ name }}
            languages(first: 10) {{ edges {{ size node {{ name }} }} }}
          }}
        }}
      }}
    }}
    '''
    data = run_gh_graphql(query)
    repos = data["data"]["user"]["repositories"]["nodes"]

    totals: dict[str, int] = {}
    for r in repos:
        if r["name"] in VENDORED_BLOB_REPOS:
            continue
        for edge in r["languages"]["edges"]:
            lang = edge["node"]["name"]
            totals[lang] = totals.get(lang, 0) + edge["size"]

    total_bytes = sum(totals.values())
    languages = [
        {"language": lang, "bytes": size, "share_pct": round(size / total_bytes * 100, 1)}
        for lang, size in sorted(totals.items(), key=lambda kv: -kv[1])
    ]
    return repos, {
        "excluded_repos": sorted(VENDORED_BLOB_REPOS),
        "exclusion_reason": "vendored/bundled dependency blob, not authored code",
        "total_bytes": total_bytes,
        "languages": languages,
    }


def fetch_contribution_calendar(username: str) -> dict:
    query = f'''
    query {{
      user(login: "{username}") {{
        contributionsCollection {{
          contributionCalendar {{
            totalContributions
            weeks {{ contributionDays {{ date contributionCount }} }}
          }}
        }}
      }}
    }}
    '''
    data = run_gh_graphql(query)
    cal = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = cal["weeks"]
    week_totals = [sum(d["contributionCount"] for d in w["contributionDays"]) for w in weeks]
    week_start_dates = [w["contributionDays"][0]["date"] for w in weeks]
    return {
        "total_contributions": cal["totalContributions"],
        "weeks": len(weeks),
        "week_start_dates": week_start_dates,
        "week_totals": week_totals,
        "peak_week": max(week_totals),
        "active_weeks": sum(1 for w in week_totals if w > 0),
    }


def main():
    username = sys.argv[1] if len(sys.argv) > 1 else "xinyuezhang-shirley"
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Fetching repositories + languages for {username}...")
    repos, languages = fetch_repos_and_languages(username)
    (OUT_DIR / "repos.json").write_text(json.dumps(repos, indent=2))
    (OUT_DIR / "languages.json").write_text(json.dumps(languages, indent=2))
    print(f"  wrote {len(repos)} repos -> assets/generated/repos.json")
    print(f"  wrote {len(languages['languages'])} languages -> assets/generated/languages.json")

    print(f"Fetching contribution calendar for {username}...")
    calendar = fetch_contribution_calendar(username)
    (OUT_DIR / "contribution-calendar.json").write_text(json.dumps(calendar, indent=2))
    print(f"  wrote {calendar['weeks']} weeks -> assets/generated/contribution-calendar.json")


if __name__ == "__main__":
    main()
