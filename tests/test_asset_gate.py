"""Run with: python -m unittest discover -s tests -v"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from asset_gate import inspect_assets  # noqa: E402


class AssetGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def put(self, path, size):
        file = self.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        with file.open("wb") as output:
            output.truncate(size)

    def test_empty_directory_continues(self):
        report = inspect_assets(self.root, "json-base64")
        self.assertEqual((report["asset_count"], report["decision"]), (0, "continue"))

    def test_small_icon_does_not_require_handoff(self):
        self.put("icon.png", 100)
        report = inspect_assets(
            self.root, "json-base64", single_limit=256, batch_limit=512
        )
        self.assertEqual(report["decision"], "continue")
        self.assertEqual(report["base64_estimated_bytes"], 136)

    def test_large_json_base64_handoff_before_upload(self):
        self.put("large.png", 1024)
        report = inspect_assets(
            self.root, "json-base64", single_limit=256, batch_limit=4096
        )
        self.assertEqual(report["decision"], "human-handoff")
        self.assertTrue(report["no_bytes_read_or_uploaded"])

    def test_same_assets_binary_continue(self):
        self.put("large.png", 1024)
        report = inspect_assets(
            self.root, "binary", single_limit=256, batch_limit=4096
        )
        self.assertEqual(report["decision"], "continue")

    def test_unknown_transport_checks_capabilities(self):
        self.put("large.png", 1024)
        report = inspect_assets(
            self.root, "auto", single_limit=256, batch_limit=4096
        )
        self.assertEqual(report["decision"], "check-transport")

    def test_non_assets_and_git_directory_excluded(self):
        self.put("notes.txt", 9000)
        self.put(".git/big.png", 9000)
        self.put("assets/icon.PNG", 9)
        report = inspect_assets(self.root, "json-base64")
        self.assertEqual(report["asset_count"], 1)
        self.assertEqual(report["largest_files"][0]["path"], "assets/icon.PNG")

    def test_invalid_threshold_rejected(self):
        with self.assertRaises(ValueError):
            inspect_assets(self.root, single_limit=0)


if __name__ == "__main__":
    unittest.main()
