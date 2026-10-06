"""固定场景，用来复现题面里的锚点。"""

import json

from . import core


def _line(obj):
    print(json.dumps(obj, ensure_ascii=False))


def run(name):
    if name == "multi":
        out = core.report(["2.5.0"], ">=1.0.0 <2.0.0", core.Counter())
        _line({"matched": out["matched"]})
        return 0
    if name == "prerelease":
        out = core.report(["1.0.0-beta"], ">=1.0.0", core.Counter())
        _line({"matched": out["matched"]})
        return 0
    if name == "order":
        out = core.report(["1.10.0", "1.9.0"], ">=1.0.0", core.Counter())
        _line({"matched": out["matched"], "best": out["best"]})
        return 0
    if name == "work":
        candidates = ["1.%d.0" % i for i in range(2000)]
        out = core.report(candidates, ">=1.0.0", core.Counter())
        _line({"candidates": 2000, "scanned": out["scanned"]})
        return 0
    raise SystemExit("未知场景：" + name)
