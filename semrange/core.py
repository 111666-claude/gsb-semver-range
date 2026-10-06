"""候选版本与范围条件求交。"""


class Counter:
    """记录本轮扫描过的候选条数。"""

    def __init__(self):
        self.scanned = 0


def parse(text):
    if "-" in text:
        return None
    parts = text.split(".")
    if len(parts) != 3:
        return None
    try:
        return tuple(int(p) for p in parts)
    except ValueError:
        return None


def satisfies(version, expr):
    for cond in expr.split():
        op = "="
        for candidate in (">=", "<=", ">", "<", "="):
            if cond.startswith(candidate):
                op = candidate
                break
        want = parse(cond[len(op):])
        if want is None:
            return False
        if op == ">=":
            ok = version >= want
        elif op == "<=":
            ok = version <= want
        elif op == ">":
            ok = version > want
        elif op == "<":
            ok = version < want
        else:
            ok = version == want
        if not ok:
            return False
    return True


def report(candidates, expr, counter):
    matched = []
    seen = set()
    for text in candidates:
        counter.scanned += 1
        version = parse(text)
        if version is None:
            continue
        if not satisfies(version, expr):
            continue
        if version in seen:
            continue
        seen.add(version)
        matched.append((version, text))
    matched.sort(key=lambda item: item[0])
    return {
        "matched": [text for _, text in matched],
        "best": matched[-1][1] if matched else None,
        "scanned": counter.scanned,
    }


def render(result):
    lines = ["matched:"]
    for text in result["matched"]:
        lines.append("  " + text)
    lines.append("best: " + (result["best"] or "-"))
    return "\n".join(lines)
