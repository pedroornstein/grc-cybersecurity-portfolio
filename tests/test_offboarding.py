"""Regression tests for a synthetic, non-production offboarding example."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "11-synthetic-offboarding-test"))
from analyze_offboarding import analyze, utc_datetime  # noqa: E402

FIELDS = ["case_id", "system", "termination_utc", "identity_disabled_utc"]
BASE = {"case_id": "SYN-T01", "system": "Microsoft 365",
        "termination_utc": "2026-09-01T12:00:00Z",
        "identity_disabled_utc": "2026-09-01T16:00:00Z"}


class OffboardingTests(unittest.TestCase):
    def evaluate(self, rows, sla_hours=4):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "data.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            return analyze(path, sla_hours)

    def evaluate_csv_text(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "data.csv"
            path.write_text(text, encoding="utf-8")
            return analyze(path)

    def test_truncated_row_rejected_not_misclassified_as_missing_evidence(self):
        csv_text = (",".join(FIELDS) + "\n"
                    + "SYN-T01,Microsoft 365,2026-09-01T12:00:00Z\n")
        with self.assertRaisesRegex(ValueError, "Malformed CSV row 2"):
            self.evaluate_csv_text(csv_text)

    def test_missing_value_for_extra_named_column_rejected(self):
        csv_text = (",".join(FIELDS) + ",notes\n"
                    + "SYN-T01,Microsoft 365,2026-09-01T12:00:00Z,"
                    + "2026-09-01T16:00:00Z\n")
        with self.assertRaisesRegex(ValueError, "Malformed CSV row 2"):
            self.evaluate_csv_text(csv_text)

    def test_surplus_unnamed_csv_field_rejected(self):
        csv_text = (",".join(FIELDS) + "\n"
                    + "SYN-T01,Microsoft 365,2026-09-01T12:00:00Z,"
                    + "2026-09-01T16:00:00Z,EXTRA\n")
        with self.assertRaisesRegex(ValueError, "Malformed CSV row 2"):
            self.evaluate_csv_text(csv_text)

    def test_duplicate_header_rejected(self):
        csv_text = ("case_id,system,system,termination_utc,identity_disabled_utc\n"
                    "SYN-T01,Microsoft 365,Microsoft 365,"
                    "2026-09-01T12:00:00Z,2026-09-01T16:00:00Z\n")
        with self.assertRaisesRegex(ValueError, "Duplicate or blank CSV header"):
            self.evaluate_csv_text(csv_text)

    def test_blank_header_rejected(self):
        csv_text = ("case_id,system,termination_utc,identity_disabled_utc,\n"
                    "SYN-T01,Microsoft 365,2026-09-01T12:00:00Z,"
                    "2026-09-01T16:00:00Z,\n")
        with self.assertRaisesRegex(ValueError, "Duplicate or blank CSV header"):
            self.evaluate_csv_text(csv_text)

    def test_explicitly_blank_evidence_stays_inconclusive(self):
        csv_text = (",".join(FIELDS) + "\n"
                    + "SYN-T01,Microsoft 365,2026-09-01T12:00:00Z,\n")
        self.assertEqual(self.evaluate_csv_text(csv_text)["missing_evidence"], 1)

    def test_sample_dataset_expected_totals(self):
        path = Path(__file__).resolve().parents[1] / "11-synthetic-offboarding-test" / "synthetic-offboarding.csv"
        result = analyze(path)
        self.assertEqual((result["total"], result["pass"], result["late"],
                          result["missing_evidence"]), (12, 9, 2, 1))

    def test_exact_boundary_passes(self):
        self.assertEqual(self.evaluate([BASE])["rows"][0]["status"], "PASS")

    def test_over_boundary_is_late(self):
        row = {**BASE, "identity_disabled_utc": "2026-09-01T16:00:01Z"}
        self.assertEqual(self.evaluate([row])["rows"][0]["status"], "LATE")

    def test_missing_timestamp_is_inconclusive(self):
        row = {**BASE, "identity_disabled_utc": ""}
        report = self.evaluate([row])
        self.assertEqual(report["missing_evidence"], 1)
        self.assertIsNone(report["rows"][0]["hours_to_disable"])

    def test_negative_elapsed_time_rejected(self):
        row = {**BASE, "identity_disabled_utc": "2026-09-01T11:59:59Z"}
        with self.assertRaisesRegex(ValueError, "predates termination"):
            self.evaluate([row])

    def test_duplicate_identifiers_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate case ID"):
            self.evaluate([BASE, BASE])

    def test_blank_system_rejected(self):
        with self.assertRaisesRegex(ValueError, "system missing"):
            self.evaluate([{**BASE, "system": ""}])

    def test_no_records_rejected(self):
        with self.assertRaisesRegex(ValueError, "No records"):
            self.evaluate([])

    def test_invalid_sla_rejected(self):
        with self.assertRaisesRegex(ValueError, "positive"):
            self.evaluate([BASE], 0)


    def test_subsecond_over_boundary_is_late(self):
        row = {**BASE, "identity_disabled_utc": "2026-09-01T16:00:00.000001Z"}
        self.assertEqual(self.evaluate([row])["rows"][0]["status"], "LATE")

    def test_subsecond_before_termination_rejected(self):
        row = {**BASE, "identity_disabled_utc": "2026-09-01T11:59:59.999999Z"}
        with self.assertRaisesRegex(ValueError, "predates termination"):
            self.evaluate([row])

    def test_nonfinite_sla_rejected(self):
        for sla in (float("nan"), float("inf"), float("-inf")):
            with self.subTest(sla=sla):
                with self.assertRaisesRegex(ValueError, "finite positive"):
                    self.evaluate([BASE], sla)

    def test_naive_timestamp_rejected(self):
        with self.assertRaisesRegex(ValueError, "UTC"):
            utc_datetime("2026-09-01T12:00:00")

    def test_non_utc_offset_rejected(self):
        with self.assertRaisesRegex(ValueError, "UTC"):
            utc_datetime("2026-09-01T12:00:00+01:00")


if __name__ == "__main__":
    unittest.main()
