import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from semrange import core


class SemrangeTest(unittest.TestCase):
    def test_parse_plain_version(self):
        self.assertEqual(core.parse("1.2.3"), (1, 2, 3))

    def test_parse_rejects_short(self):
        self.assertIsNone(core.parse("1.2"))

    def test_single_condition_matches(self):
        out = core.report(["1.5.0"], ">=1.0.0", core.Counter())
        self.assertEqual(out["matched"], ["1.5.0"])

    def test_empty_candidates(self):
        out = core.report([], ">=1.0.0", core.Counter())
        self.assertEqual(out["matched"], [])
        self.assertIsNone(out["best"])

    def test_render_has_best_line(self):
        out = core.report(["1.5.0"], ">=1.0.0", core.Counter())
        self.assertIn("best:", core.render(out))


if __name__ == "__main__":
    unittest.main()
