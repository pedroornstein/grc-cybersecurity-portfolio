#!/usr/bin/env python3
"""Illustrative offboarding SLA test on wholly synthetic records. Python 3.10+."""
import argparse
import csv
import json
import math
from collections import Counter
from datetime import datetime
from pathlib import Path

COLUMNS = {"case_id", "system", "termination_utc", "identity_disabled_utc"}


def utc_datetime(value):
    """Parse an explicit UTC time; reject local/naive timestamps."""
    if not value.endswith("Z"):
        raise ValueError("timestamp must end in Z (UTC)")
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def analyze(csv_path, sla_hours=4):
    if not isinstance(sla_hours, (int, float)) or not math.isfinite(sla_hours) or sla_hours <= 0:
        raise ValueError("SLA must be a finite positive number of hours")
    with open(csv_path, newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not COLUMNS.issubset(reader.fieldnames):
            raise ValueError(f"Required CSV columns: {sorted(COLUMNS)}")
        if len(reader.fieldnames) != len(set(reader.fieldnames)) or any(
            not name.strip() for name in reader.fieldnames
        ):
            raise ValueError("Duplicate or blank CSV header")
        results, seen = [], set()
        for row_number, row in enumerate(reader, start=2):
            # DictReader otherwise silently stores surplus fields under None
            # and fills absent columns with None, compromising audit integrity.
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"Malformed CSV row {row_number}: missing or extra fields")
            case_id = (row.get("case_id") or "").strip()
            if not case_id or case_id in seen:
                raise ValueError(f"Blank or duplicate case ID: {case_id!r}")
            seen.add(case_id)
            if not (row.get("system") or "").strip():
                raise ValueError(f"{case_id}: system missing")
            terminated = utc_datetime((row.get("termination_utc") or "").strip())
            disabled_text = (row.get("identity_disabled_utc") or "").strip()
            if not disabled_text:
                status, hours = "MISSING_EVIDENCE", None
            else:
                disabled = utc_datetime(disabled_text)
                elapsed = disabled - terminated
                if elapsed.total_seconds() < 0:
                    raise ValueError(f"{case_id}: disablement predates termination")
                # Compare unrounded duration so records just past the SLA do not pass.
                status = "PASS" if elapsed.total_seconds() <= sla_hours * 3600 else "LATE"
                hours = round(elapsed.total_seconds() / 3600, 4)
            results.append({
                "case_id": case_id,
                "system": row["system"].strip(),
                "hours_to_disable": hours,
                "status": status,
            })
    if not results:
        raise ValueError("No records found")
    counts = Counter(record["status"] for record in results)
    return {
        "scope": "synthetic single-system offboarding population",
        "sla_hours": sla_hours,
        "total": len(results),
        "pass": counts["PASS"],
        "late": counts["LATE"],
        "missing_evidence": counts["MISSING_EVIDENCE"],
        "rows": results,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=Path(__file__).with_name("synthetic-offboarding.csv"))
    parser.add_argument("--sla-hours", type=float, default=4)
    parser.add_argument("--json", action="store_true", help="Emit machine-readable results")
    args = parser.parse_args()
    try:
        report = analyze(args.csv, args.sla_hours)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print("SYNTHETIC OFFBOARDING CONTROL TEST — NOT A REAL AUDIT")
        print(f"Scope: {report['scope']}; SLA: {report['sla_hours']:g} hours")
        for row in report["rows"]:
            span = "no record" if row["hours_to_disable"] is None else f"{row['hours_to_disable']:g} h"
            print(f"{row['case_id']}: {row['status']:16} {span}")
        print(f"SUMMARY: {report['total']} records | {report['pass']} pass | "
              f"{report['late']} late | {report['missing_evidence']} missing evidence")
        print("Any missing timestamp is INCONCLUSIVE pending follow-up, not proof of active access.")


if __name__ == "__main__":
    main()
