"""Validate this project's simple skill metadata and D0 coordination links/graph.
Uses stdlib only. This is not a general YAML parser or semantic design approval.
Run from anywhere: python .../scripts/validate_planning.py --root <workspace>.
"""
from pathlib import Path
import argparse
import re

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    root = ap.parse_args().root.resolve()
    package = root / "Game_att2_Codex_Handoff_v0_6"
    skillroot = root / ".agents/skills"
    names = ("game-att2-production", "grill-me", "to-spec", "to-tickets",
             "find-skills", "frontend-ui-engineering", "playwright-interactive",
             "debug-interactive-demo")
    errors = []
    for name in names:
        path = skillroot / name / "SKILL.md"
        content = path.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---\n", content, re.S)
        if not match:
            errors.append(f"{name}: missing metadata")
            continue
        fields = {}
        for line in match[1].splitlines():
            key, sep, value = line.partition(":")
            if not sep or key not in ("name", "description") or key in fields:
                errors.append(f"{name}: unsupported/duplicate metadata; use full YAML validator")
                continue
            fields[key] = value.strip().strip('"')
        if fields.get("name") != name:
            errors.append(f"{name}: directory/name mismatch")
        desc = fields.get("description", "")
        if not desc or len(desc) > 1024 or any(c in desc for c in "<>"):
            errors.append(f"{name}: invalid description")
        if "[TODO:" in content:
            errors.append(f"{name}: unfinished scaffold")
    plan = package / "docs/planning/D0_EXECUTION_PLAN_2026-09-06.md"
    tickets = sorted((package / "docs/planning/tickets").glob("T[0-9][0-9].md"))
    plantext = plan.read_text(encoding="utf-8")
    qids = set(re.findall(r"^\| (Q\d{2}) \|", plantext, re.M))
    rids = set(re.findall(r"^\| (R\d{2}) \|", plantext, re.M))
    graph, qcover, rcover = {}, set(), set()
    for path in tickets:
        content = path.read_text(encoding="utf-8")
        def field(key):
            match = re.search(r"^" + re.escape(key) + r": (.+)$", content, re.M)
            if not match:
                errors.append(f"{path.name}: missing {key}")
                return ""
            return match[1]
        deps = set(re.findall(r"T\d{2}", field("Blocked by")))
        qs = set(re.findall(r"Q\d{2}", field("Decision IDs")))
        rs = set(re.findall(r"R\d{2}", field("Requirement IDs")))
        graph[path.stem] = deps
        qcover.update(qs)
        rcover.update(rs)
        if qs - qids or rs - rids:
            errors.append(f"{path.name}: unknown decision/requirement")
        if field("Type") == "runtime" and field("Status") != "BLOCKED-OWNER":
            errors.append(f"{path.name}: current unopened runtime gate requires blocked status")
        if "- [ ] " not in content:
            errors.append(f"{path.name}: no acceptance cases")
    if qids != qcover or rids != rcover:
        errors.append(f"Uncovered decisions {qids-qcover}, requirements {rids-rcover}")
    visiting, visited = set(), set()
    def visit(key):
        if key in visiting:
            errors.append(f"Dependency cycle at {key}")
            return
        if key in visited:
            return
        if key not in graph:
            errors.append(f"Missing ticket {key}")
            return
        visiting.add(key)
        for dep in graph[key]:
            visit(dep)
        visiting.remove(key)
        visited.add(key)
    for key in graph:
        visit(key)
    files = list((package / "docs/planning").rglob("*.md"))
    files += [package / "docs/README.md", package / "research/skill_audit_2026-09-06.md"]
    for name in names:
        files += list((skillroot / name).rglob("*.md"))
    links = 0
    for path in files:
        if not path.exists():
            errors.append(f"Missing document {path}")
            continue
        # Fenced code samples aren't documentation links.
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", text):
            target = target.strip("<>").split("#")[0]
            if not target or re.match(r"^[a-z]+://|^mailto:", target, re.I):
                continue
            links += 1
            if not (path.parent / target).resolve().exists():
                errors.append(f"{path.relative_to(root)}: broken link {target}")
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)
    print(f"PASS: {len(names)} simple two-field skill metadata checks")
    print(f"PASS: {len(tickets)} tickets; {len(qids)} decisions; {len(rids)} requirements covered")
    print("PASS: missing-ID and dependency-cycle checks; current runtime statuses blocked")
    print(f"PASS: {links} local link occurrences across {len(files)} Markdown files")
    print("LIMIT: no general YAML, heading-anchor, runtime, human-play, or automatic discovery verification")

if __name__ == "__main__":
    main()
