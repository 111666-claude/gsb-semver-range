"""命令行入口。"""

import argparse

from . import core, samples


def main(argv=None):
    ap = argparse.ArgumentParser(prog="semrange")
    ap.add_argument("--sample", choices=["multi", "prerelease", "order", "work"])
    sub = ap.add_subparsers(dest="cmd")
    report_parser = sub.add_parser("report")
    report_parser.add_argument("--candidates", required=True)
    report_parser.add_argument("--range", required=True)
    args = ap.parse_args(argv)

    if args.sample:
        return samples.run(args.sample)
    if args.cmd is None:
        ap.print_help()
        return 2

    with open(args.candidates, encoding="utf-8") as fh:
        candidates = [line.strip() for line in fh if line.strip()]
    print(core.render(core.report(candidates, args.range, core.Counter())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
