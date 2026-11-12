"""Point every page at the matching official guide URL, with a visible notice."""
from __future__ import annotations

import re
from html import escape
from pathlib import Path

CANON_SITE = "https://aipmandy.github.io/how-to-become-an-executive"
CANON_REPO = "https://github.com/AIPMAndy/how-to-become-an-executive"
START = "<!-- seo-meta -->"
END = "<!-- /seo-meta -->"
NOTE_START = "<!-- seo-canonical-notice -->"
NOTE_END = "<!-- /seo-canonical-notice -->"

# Exact path matches first. Renamed seven-stage chapters map to the
# official guide's imported roadmap (guides/10-roadmap.html). Evidence
# pages map to the official evidence library. Everything else → homepage.
PATH_MAP = {
    "guides/01-position.html": "guides/10-roadmap.html",
    "guides/02-expert.html": "guides/10-roadmap.html",
    "guides/03-owner.html": "guides/10-roadmap.html",
    "guides/04-manager.html": "guides/10-roadmap.html",
    "guides/06-promotion.html": "guides/10-roadmap.html",
    "guides/07-onboard.html": "guides/10-roadmap.html",
    "evidence/CASE_STUDIES.html": "evidence/index.html",
    "evidence/DATA_VISUALIZATIONS.html": "evidence/index.html",
    "evidence/RESEARCH_ATLAS.html": "evidence/index.html",
}

CANON_HTML = {
    "CONTENT_LICENSE.html",
    "REFERENCES.html",
    "guides/00-start.html",
    "guides/05-business.html",
    "index.html",
    "tracks/ai-product.html",
    "tracks/finance-hr-technology.html",
    "tracks/product-operations.html",
    "evidence/index.html",
    "guides/01-ladder.html",
    "guides/02-results.html",
    "guides/03-influence.html",
    "guides/04-people.html",
    "guides/06-communication.html",
    "guides/07-internal.html",
    "guides/08-external.html",
    "guides/09-90days.html",
    "guides/10-roadmap.html",
    "read.html",
}


def canonical_url(rel: str) -> str:
    rel = rel.replace("\\", "/")
    if rel in PATH_MAP:
        target = PATH_MAP[rel]
    elif rel in CANON_HTML:
        target = rel
    else:
        target = "index.html"
    if target in ("index.html", ""):
        return CANON_SITE + "/"
    return f"{CANON_SITE}/{target}"


def notice(url: str) -> str:
    return (
        f"{NOTE_START}"
        '<div role="note" style="margin:0;padding:12px 18px;background:#0d2146;color:#fff;'
        "font:15px/1.6 -apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;"
        'text-align:center;z-index:99">'
        "本页是旧版，已停止更新。正式版请看 "
        f'<a href="{escape(url, quote=True)}" style="color:#fff;font-weight:700;text-decoration:underline">'
        "普通人成为高管保姆级指南（正式版）</a>。"
        "</div>"
        f"{NOTE_END}"
    )


def block_for(url: str) -> str:
    return (
        f"{START}"
        f'<link rel="canonical" href="{escape(url, quote=True)}">'
        f"{END}"
    )


def inject_html(path: Path, root: Path) -> None:
    html = path.read_text(encoding="utf-8")
    html = re.sub(re.escape(START) + r".*?" + re.escape(END), "", html, flags=re.S)
    html = re.sub(re.escape(NOTE_START) + r".*?" + re.escape(NOTE_END), "", html, flags=re.S)
    rel = path.relative_to(root).as_posix()
    url = canonical_url(rel)
    block = block_for(url)
    banner = notice(url)
    if re.search(r"<head[^>]*>", html, re.I):
        html = re.sub(r"(<head[^>]*>)", r"\1" + block, html, count=1, flags=re.I)
    else:
        html = block + html
    if re.search(r"<body[^>]*>", html, re.I):
        html = re.sub(r"(<body[^>]*>)", r"\1" + banner, html, count=1, flags=re.I)
    else:
        html = html + banner
    path.write_text(html, encoding="utf-8")


def apply(root: Path | None = None) -> None:
    root = Path(root or Path(__file__).resolve().parent)
    for p in sorted(root.rglob("*.html")):
        if ".git" in p.parts:
            continue
        inject_html(p, root)


if __name__ == "__main__":
    apply()
