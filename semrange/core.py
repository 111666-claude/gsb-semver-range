"""候选版本与范围条件求交。"""


class Counter:
    """记录本轮检查过的已匹配版本条数。"""

    def __init__(self):
        self.scanned = 0


def parse(text):
    body = text
    if "-" in body:
        body = body.split("-", 1)[0]
    parts = body.split(".")
    if len(parts) != 3:
        return None
    try:
        return tuple(int(p) for p in parts)
    except ValueError:
        return None


def satisfies(version, expr):
    cond = expr.split()[0]
    op = "="
    for candidate in (">=", "<=", ">", "<", "="):
        if cond.startswith(candidate):
            op = candidate
            break
    want = parse(cond[len(op):])
    if want is None:
        return False
    if op == ">=":
        return version >= want
    if op == "<=":
        return version <= want
    if op == ">":
        return version > want
    if op == "<":
        return version < want
    return version == want


def report(candidates, expr, counter):
    matched = []
    for text in candidates:
        version = parse(text)
        if version is None:
            continue
        if not satisfies(version, expr):
            continue
        dup = False
        for seen, _ in matched:
            counter.scanned += 1
            if seen == version:
                dup = True
                break
        if not dup:
            matched.append((version, text))
    matched.sort(key=lambda item: item[1])
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
