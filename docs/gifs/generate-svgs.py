#!/usr/bin/env python3
"""Generate SVG terminal recordings for README documentation."""

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def make_svg(
    lines,
    title="Terminal",
    width=720,
    line_height=20,
    pad_top=48,
    pad_bottom=16,
    pad_x=16,
    read_pause=4.0,
    fade_dur=0.5,
):
    """Create a looping SVG terminal animation.

    Each line is a tuple: (text, color, [delay_ms])
    The animation cycles: lines appear sequentially, pause for reading,
    all fade out, then restart.
    """
    height = pad_top + len(lines) * line_height + pad_bottom

    # Calculate total cycle: max delay + appear time + read pause + fade out
    max_delay = max((l[2] if len(l) > 2 else 0) for l in lines) / 1000
    appear_end = max_delay + 0.3  # last line finishes appearing
    total = appear_end + read_pause + fade_dur  # full cycle duration

    text_elements = []
    for i, line in enumerate(lines):
        text = line[0]
        color = line[1] if len(line) > 1 else "#a6adc8"
        delay_ms = line[2] if len(line) > 2 else 0
        delay = delay_ms / 1000
        y = pad_top + i * line_height

        # Build keyTimes and values for looping opacity animation
        # 0..delay: invisible, delay..delay+0.3: fade in, stay visible, total-fade..total: fade out
        if delay > 0:
            t_appear = delay / total
            t_visible = min((delay + 0.3) / total, (total - fade_dur) / total)
            t_fade_start = (total - fade_dur) / total
            kt = f"0;{t_appear:.4f};{t_visible:.4f};{t_fade_start:.4f};1"
            vals = "0;0;1;1;0"
        else:
            # Immediately visible lines: visible from start, fade at end
            t_fade_start = (total - fade_dur) / total
            kt = f"0;{t_fade_start:.4f};1"
            vals = "1;1;0"

        anim = (
            f'<animate attributeName="opacity" values="{vals}" '
            f'keyTimes="{kt}" dur="{total:.1f}s" repeatCount="indefinite"/>'
        )

        if isinstance(text, list):
            spans = []
            for seg in text:
                spans.append(f'<tspan fill="{seg[1]}">{esc(seg[0])}</tspan>')
            init_opacity = "0" if delay > 0 else "1"
            text_elements.append(
                f"  <text x=\"{pad_x}\" y=\"{y}\" font-family=\"'SF Mono','Fira Code','Cascadia Code',monospace\" "
                f'font-size="13" fill="{color}" opacity="{init_opacity}">'
                + "".join(spans)
                + anim
                + "</text>"
            )
        else:
            init_opacity = "0" if delay > 0 else "1"
            text_elements.append(
                f"  <text x=\"{pad_x}\" y=\"{y}\" font-family=\"'SF Mono','Fira Code','Cascadia Code',monospace\" "
                f'font-size="13" fill="{color}" opacity="{init_opacity}">{esc(text)}{anim}</text>'
            )

    return f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{width}" height="{height}" rx="10" fill="#1e1e2e"/>
  <rect width="{width}" height="32" rx="10" fill="#313244"/>
  <rect y="22" width="{width}" height="10" fill="#313244"/>
  <circle cx="20" cy="16" r="6" fill="#f38ba8"/>
  <circle cx="40" cy="16" r="6" fill="#f9e2af"/>
  <circle cx="60" cy="16" r="6" fill="#a6e3a1"/>
  <text x="{width // 2}" y="20" font-family="\'SF Mono\',monospace" font-size="12" fill="#6c7086" text-anchor="middle">{esc(title)}</text>
{"chr(10)".join(text_elements)}
</svg>'''


def esc(s):
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _anim(delay_ms, total, fade_dur=0.5):
    """Return (initial_opacity, animate_tag) for looping opacity animation."""
    delay = delay_ms / 1000
    if delay > 0:
        t_appear = delay / total
        t_visible = min((delay + 0.3) / total, (total - fade_dur) / total)
        t_fade = (total - fade_dur) / total
        return "0", (
            f'<animate attributeName="opacity" values="0;0;1;1;0" '
            f'keyTimes="0;{t_appear:.4f};{t_visible:.4f};{t_fade:.4f};1" '
            f'dur="{total:.1f}s" repeatCount="indefinite"/>'
        )
    t_fade = (total - fade_dur) / total
    return "1", (
        f'<animate attributeName="opacity" values="1;1;0" '
        f'keyTimes="0;{t_fade:.4f};1" '
        f'dur="{total:.1f}s" repeatCount="indefinite"/>'
    )


def make_chat_svg(
    messages, channel="decisions", width=540, read_pause=5.0, fade_dur=0.5
):
    """Chat bubble SVG (Slack/Discord style).

    messages: list of dicts. Each is either:
      {"user": "You", "time": "Feb 3", "lines": ["..."], "bar": "#color", "delay": 0}
      {"divider": "6 weeks later", "delay": 2000}
    """
    FONT = "'SF Mono','Fira Code','Cascadia Code',monospace"
    PAD = 16
    LINE_H = 18

    y = 48
    max_delay_ms = 0
    layout = []

    for msg in messages:
        if "divider" in msg:
            layout.append(
                {
                    "type": "divider",
                    "text": msg["divider"],
                    "delay": msg.get("delay", 0),
                    "y": y,
                }
            )
            y += 36
        else:
            lines = msg["lines"] if isinstance(msg["lines"], list) else [msg["lines"]]
            h = 18 + len(lines) * LINE_H
            layout.append({"type": "msg", "msg": msg, "y": y, "lines": lines, "h": h})
            y += h + 12
        max_delay_ms = max(max_delay_ms, msg.get("delay", 0))

    height = y + PAD
    total = max_delay_ms / 1000 + 0.3 + read_pause + fade_dur

    els = []
    els.append(f'<rect width="{width}" height="{height}" rx="8" fill="#1e1e2e"/>')
    els.append(f'<rect width="{width}" height="36" rx="8" fill="#313244"/>')
    els.append(f'<rect y="28" width="{width}" height="8" fill="#313244"/>')
    els.append(
        f'<text x="{PAD}" y="23" font-family="{FONT}" font-size="13" '
        f'fill="#89b4fa" font-weight="bold"># {esc(channel)}</text>'
    )

    for item in layout:
        if item["type"] == "divider":
            init, anim = _anim(item["delay"], total, fade_dur)
            dy = item["y"]
            text = item["text"]
            cx = width // 2
            tw = len(text) * 4 + 16
            els.append(
                f'<g opacity="{init}">'
                f'<line x1="{PAD}" y1="{dy + 18}" x2="{cx - tw}" y2="{dy + 18}" '
                f'stroke="#45475a" stroke-width="1"/>'
                f'<text x="{cx}" y="{dy + 22}" font-family="{FONT}" font-size="11" '
                f'fill="#6c7086" text-anchor="middle">{esc(text)}</text>'
                f'<line x1="{cx + tw}" y1="{dy + 18}" x2="{width - PAD}" y2="{dy + 18}" '
                f'stroke="#45475a" stroke-width="1"/>'
                f"{anim}</g>"
            )
        else:
            msg = item["msg"]
            dy = item["y"]
            lines = item["lines"]
            h = item["h"]
            delay = msg.get("delay", 0)
            bar = msg.get("bar", "#6c7086")
            user = msg["user"]
            time_str = msg.get("time", "")
            text_color = msg.get("color", "#cdd6f4")
            init, anim = _anim(delay, total, fade_dur)
            inner = (
                f'<rect x="{PAD}" y="{dy}" width="3" height="{h}" rx="1" fill="{bar}"/>'
            )
            inner += (
                f'<text x="{PAD + 12}" y="{dy + 13}" font-family="{FONT}" '
                f'font-size="12" fill="{bar}" font-weight="bold">{esc(user)}</text>'
            )
            if time_str:
                ux = PAD + 12 + len(user) * 7.5 + 8
                inner += (
                    f'<text x="{ux}" y="{dy + 13}" font-family="{FONT}" '
                    f'font-size="10" fill="#6c7086">{esc(time_str)}</text>'
                )
            for j, line in enumerate(lines):
                inner += (
                    f'<text x="{PAD + 12}" y="{dy + 13 + (j + 1) * LINE_H}" '
                    f'font-family="{FONT}" font-size="12" fill="{text_color}">'
                    f"{esc(line)}</text>"
                )
            els.append(f'<g opacity="{init}">{inner}{anim}</g>')

    return (
        f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
        + "\n".join(f"  {e}" for e in els)
        + "\n</svg>"
    )


def make_versus_svg(
    left_items,
    right_items,
    title="",
    left_label="",
    right_label="",
    verdict="",
    width=640,
    read_pause=5.0,
    fade_dur=0.5,
):
    """Two-column VS comparison card."""
    FONT = "'SF Mono','Fira Code','Cascadia Code',monospace"
    PAD = 24
    MID = width // 2
    ROW_H = 52

    n_rows = max(len(left_items), len(right_items))
    row_start = 76
    verdict_y = row_start + n_rows * ROW_H + 16
    height = verdict_y + (36 if verdict else 12)

    max_item_delay = 0
    for items in [left_items, right_items]:
        for item in items:
            max_item_delay = max(max_item_delay, item.get("delay", 0))
    verdict_delay = max_item_delay + 400
    max_delay_ms = verdict_delay if verdict else max_item_delay
    total = max_delay_ms / 1000 + 0.3 + read_pause + fade_dur

    els = []
    els.append(f'<rect width="{width}" height="{height}" rx="10" fill="#1e1e2e"/>')

    init0, anim0 = _anim(0, total, fade_dur)
    els.append(
        f'<text x="{MID}" y="30" font-family="{FONT}" font-size="15" fill="#cdd6f4" '
        f'text-anchor="middle" font-weight="bold" opacity="{init0}">{esc(title)}{anim0}</text>'
    )
    els.append(
        f'<line x1="{MID}" y1="48" x2="{MID}" y2="{verdict_y - 8}" stroke="#313244" '
        f'stroke-width="1" opacity="{init0}">{anim0}</line>'
    )
    els.append(
        f'<text x="{MID // 2}" y="56" font-family="{FONT}" font-size="12" '
        f'fill="#f38ba8" text-anchor="middle" opacity="{init0}">{esc(left_label)}{anim0}</text>'
    )
    els.append(
        f'<text x="{MID + MID // 2}" y="56" font-family="{FONT}" font-size="12" '
        f'fill="#a6e3a1" text-anchor="middle" opacity="{init0}">{esc(right_label)}{anim0}</text>'
    )

    for i, item in enumerate(left_items):
        y = row_start + i * ROW_H
        init, anim = _anim(item.get("delay", 0), total, fade_dur)
        els.append(
            f'<g opacity="{init}">'
            f'<text x="{PAD}" y="{y + 14}" font-family="{FONT}" font-size="13" '
            f'fill="#f38ba8">{esc(item["text"])}</text>'
            f'<text x="{PAD}" y="{y + 32}" font-family="{FONT}" font-size="11" '
            f'fill="#6c7086">{esc(item.get("sub", ""))}</text>'
            f"{anim}</g>"
        )

    for i, item in enumerate(right_items):
        y = row_start + i * ROW_H
        init, anim = _anim(item.get("delay", 0), total, fade_dur)
        els.append(
            f'<g opacity="{init}">'
            f'<text x="{MID + PAD}" y="{y + 14}" font-family="{FONT}" font-size="13" '
            f'fill="#a6e3a1">{esc(item["text"])}</text>'
            f'<text x="{MID + PAD}" y="{y + 32}" font-family="{FONT}" font-size="11" '
            f'fill="#6c7086">{esc(item.get("sub", ""))}</text>'
            f"{anim}</g>"
        )

    els.append(
        f'<line x1="{PAD}" y1="{verdict_y - 4}" x2="{width - PAD}" y2="{verdict_y - 4}" '
        f'stroke="#313244" stroke-width="1" opacity="{init0}">{anim0}</line>'
    )

    if verdict:
        init_v, anim_v = _anim(verdict_delay, total, fade_dur)
        els.append(
            f'<text x="{MID}" y="{verdict_y + 18}" font-family="{FONT}" font-size="13" '
            f'fill="#cba6f7" text-anchor="middle" opacity="{init_v}">{esc(verdict)}{anim_v}</text>'
        )

    return (
        f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
        + "\n".join(f"  {e}" for e in els)
        + "\n</svg>"
    )


def make_receipt_svg(
    sections, footer_lines=None, width=400, read_pause=5.0, fade_dur=0.5
):
    """Receipt/invoice style SVG."""
    FONT = "'SF Mono','Fira Code','Cascadia Code',monospace"
    PAD = 32
    LINE_H = 22
    RIGHT = width - PAD

    y = 16
    max_delay_ms = 0
    items_layout = []

    items_layout.append(("title", "AGENT OPERATIONS", 0, y))
    y += 24
    items_layout.append(("dashes", None, 0, y))
    y += 16

    for sec in sections:
        delay = sec.get("delay_start", 0)
        items_layout.append(("section_title", sec["title"], delay, y))
        y += LINE_H + 4
        for j, (item_text, item_price) in enumerate(sec["items"]):
            d = delay + (j + 1) * 200
            items_layout.append(("item", (item_text, item_price), d, y))
            y += LINE_H
            max_delay_ms = max(max_delay_ms, d)
        y += 4
        items_layout.append(("line", None, delay, y))
        y += 8
        st_delay = delay + (len(sec["items"]) + 1) * 200
        items_layout.append(
            (
                "subtotal",
                sec["subtotal"],
                st_delay,
                y,
                sec.get("subtotal_color", "#cdd6f4"),
            )
        )
        max_delay_ms = max(max_delay_ms, st_delay)
        y += LINE_H + 12

    if footer_lines:
        items_layout.append(("double_line", None, 0, y))
        y += 12
        for fl in footer_lines:
            fd = max_delay_ms + 400
            items_layout.append(("footer", fl, fd, y))
            max_delay_ms = fd
            y += LINE_H

    height = y + PAD
    total = max_delay_ms / 1000 + 0.3 + read_pause + fade_dur

    els = []
    els.append(f'<rect width="{width}" height="{height}" rx="4" fill="#1e1e2e"/>')
    els.append(
        f'<rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="3" '
        f'fill="none" stroke="#313244" stroke-width="1"/>'
    )

    for it in items_layout:
        kind = it[0]
        if kind == "title":
            _, text, delay, iy = it
            init, anim = _anim(delay, total, fade_dur)
            els.append(
                f'<text x="{width // 2}" y="{iy + 14}" font-family="{FONT}" '
                f'font-size="14" fill="#cdd6f4" text-anchor="middle" font-weight="bold" '
                f'opacity="{init}">{esc(text)}{anim}</text>'
            )
        elif kind == "dashes":
            _, _, delay, iy = it
            init, anim = _anim(delay, total, fade_dur)
            els.append(
                f'<line x1="{PAD}" y1="{iy}" x2="{RIGHT}" y2="{iy}" '
                f'stroke="#45475a" stroke-dasharray="3" opacity="{init}">{anim}</line>'
            )
        elif kind == "section_title":
            _, text, delay, iy = it
            init, anim = _anim(delay, total, fade_dur)
            els.append(
                f'<text x="{PAD}" y="{iy + 14}" font-family="{FONT}" font-size="12" '
                f'fill="#a6adc8" opacity="{init}">{esc(text)}{anim}</text>'
            )
        elif kind == "item":
            _, (text, price), delay, iy = it
            init, anim = _anim(delay, total, fade_dur)
            els.append(
                f'<g opacity="{init}">'
                f'<text x="{PAD}" y="{iy + 14}" font-family="{FONT}" font-size="12" '
                f'fill="#cdd6f4">{esc(text)}</text>'
                f'<text x="{RIGHT}" y="{iy + 14}" font-family="{FONT}" font-size="12" '
                f'fill="#cdd6f4" text-anchor="end">{esc(price)}</text>'
                f"{anim}</g>"
            )
        elif kind == "line":
            _, _, delay, iy = it
            init, anim = _anim(delay, total, fade_dur)
            els.append(
                f'<line x1="{PAD}" y1="{iy}" x2="{RIGHT}" y2="{iy}" '
                f'stroke="#45475a" stroke-width="1" opacity="{init}">{anim}</line>'
            )
        elif kind == "subtotal":
            _, (text, price), delay, iy, color = it
            init, anim = _anim(delay, total, fade_dur)
            els.append(
                f'<g opacity="{init}">'
                f'<text x="{PAD}" y="{iy + 14}" font-family="{FONT}" font-size="12" '
                f'fill="{color}" font-weight="bold">{esc(text)}</text>'
                f'<text x="{RIGHT}" y="{iy + 14}" font-family="{FONT}" font-size="12" '
                f'fill="{color}" font-weight="bold" text-anchor="end">{esc(price)}</text>'
                f"{anim}</g>"
            )
        elif kind == "double_line":
            _, _, _, iy = it
            init, anim = _anim(0, total, fade_dur)
            els.append(
                f'<line x1="{PAD}" y1="{iy}" x2="{RIGHT}" y2="{iy}" '
                f'stroke="#45475a" stroke-width="1" opacity="{init}">{anim}</line>'
            )
            els.append(
                f'<line x1="{PAD}" y1="{iy + 3}" x2="{RIGHT}" y2="{iy + 3}" '
                f'stroke="#45475a" stroke-width="1" opacity="{init}">{anim}</line>'
            )
        elif kind == "footer":
            _, (text, price, color), delay, iy = it
            init, anim = _anim(delay, total, fade_dur)
            inner = (
                f'<text x="{PAD}" y="{iy + 14}" font-family="{FONT}" font-size="13" '
                f'fill="{color}" font-weight="bold">{esc(text)}</text>'
            )
            if price:
                inner += (
                    f'<text x="{RIGHT}" y="{iy + 14}" font-family="{FONT}" '
                    f'font-size="13" fill="{color}" font-weight="bold" '
                    f'text-anchor="end">{esc(price)}</text>'
                )
            els.append(f'<g opacity="{init}">{inner}{anim}</g>')

    return (
        f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
        + "\n".join(f"  {e}" for e in els)
        + "\n</svg>"
    )


def make_figure_svg(
    mappings, caption="", footnote="", width=640, read_pause=6.0, fade_dur=0.5
):
    """Academic figure style with box-arrow-box mappings."""
    FONT = "'SF Mono','Fira Code','Cascadia Code',monospace"
    PAD = 20
    BOX_W = 220
    BOX_H = 44
    ROW_H = 60
    LEFT_X = PAD + 10
    RIGHT_X = width - PAD - BOX_W - 10

    caption_h = 36
    row_start = caption_h + 10
    height = row_start + len(mappings) * ROW_H + (40 if footnote else 16)

    max_delay_ms = max(m.get("delay", 0) for m in mappings)
    fn_delay = max_delay_ms + 600
    total_delay = fn_delay if footnote else max_delay_ms
    total = total_delay / 1000 + 0.3 + read_pause + fade_dur

    els = []
    els.append(f'<rect width="{width}" height="{height}" rx="10" fill="#1e1e2e"/>')

    init0, anim0 = _anim(0, total, fade_dur)
    els.append(
        f'<text x="{PAD}" y="22" font-family="{FONT}" font-size="12" '
        f'fill="#a6adc8" font-style="italic" opacity="{init0}">{esc(caption)}{anim0}</text>'
    )

    for i, m in enumerate(mappings):
        y = row_start + i * ROW_H
        delay = m.get("delay", 0)
        init, anim = _anim(delay, total, fade_dur)
        lx = LEFT_X
        rx = RIGHT_X
        left_cx = lx + BOX_W // 2
        right_cx = rx + BOX_W // 2
        arrow_x1 = lx + BOX_W + 4
        arrow_x2 = rx - 4
        arrow_y = y + BOX_H // 2
        inner = (
            f'<rect x="{lx}" y="{y}" width="{BOX_W}" height="{BOX_H}" rx="4" '
            f'fill="#313244" stroke="#45475a" stroke-width="1"/>'
            f'<text x="{left_cx}" y="{y + 18}" font-family="{FONT}" font-size="11" '
            f'fill="#cdd6f4" text-anchor="middle">{esc(m["left"])}</text>'
            f'<text x="{left_cx}" y="{y + 34}" font-family="{FONT}" font-size="10" '
            f'fill="#6c7086" text-anchor="middle">{esc(m.get("left_sub", ""))}</text>'
            f'<line x1="{arrow_x1}" y1="{arrow_y}" x2="{arrow_x2 - 6}" y2="{arrow_y}" '
            f'stroke="#6c7086" stroke-width="1"/>'
            f'<polygon points="{arrow_x2 - 8},{arrow_y - 4} {arrow_x2},{arrow_y} '
            f'{arrow_x2 - 8},{arrow_y + 4}" fill="#6c7086"/>'
            f'<rect x="{rx}" y="{y}" width="{BOX_W}" height="{BOX_H}" rx="4" '
            f'fill="#313244" stroke="#89b4fa" stroke-width="1"/>'
            f'<text x="{right_cx}" y="{y + 18}" font-family="{FONT}" font-size="11" '
            f'fill="#89b4fa" text-anchor="middle">{esc(m["right"])}</text>'
            f'<text x="{right_cx}" y="{y + 34}" font-family="{FONT}" font-size="10" '
            f'fill="#6c7086" text-anchor="middle">{esc(m.get("right_sub", ""))}</text>'
        )
        els.append(f'<g opacity="{init}">{inner}{anim}</g>')

    if footnote:
        fn_y = row_start + len(mappings) * ROW_H + 16
        init_fn, anim_fn = _anim(fn_delay, total, fade_dur)
        els.append(
            f'<text x="{width // 2}" y="{fn_y}" font-family="{FONT}" font-size="12" '
            f'fill="#cba6f7" text-anchor="middle" font-style="italic" '
            f'opacity="{init_fn}">{esc(footnote)}{anim_fn}</text>'
        )

    return (
        f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
        + "\n".join(f"  {e}" for e in els)
        + "\n</svg>"
    )


# -- Session Save --
session_save = make_svg(
    [
        ([("$ ", "#89b4fa"), ("/session-save", "#cdd6f4")], "#cdd6f4"),
        ("", "#1e1e2e"),
        ("Detecting project... my-app (matched: keyword 'dashboard')", "#6c7086", 400),
        ("", "#1e1e2e"),
        ("Gathering context:", "#a6adc8", 800),
        ("  git log    : 7 commits today", "#a6e3a1", 1000),
        ("  git diff   : 3 files modified", "#a6e3a1", 1100),
        ("  session    : 23 messages exchanged", "#a6e3a1", 1200),
        ("", "#1e1e2e"),
        ("Updating dossier... done", "#a6adc8", 1600),
        ("Updating observations:", "#a6adc8", 1900),
        ("  + [decision] Chose Postgres over SQLite for multi-user", "#cba6f7", 2100),
        ("  + [feature]  Added /api/users endpoint", "#89b4fa", 2300),
        ("  + [bugfix]   Fixed race condition in auth middleware", "#a6e3a1", 2500),
        ("Syncing MEMORY.md... done", "#a6adc8", 2800),
        ("", "#1e1e2e"),
        ("Session saved. 3 observations recorded.", "#a6e3a1", 3200),
    ],
    title="session-save",
    width=640,
)

# -- Search Memory --
search_memory = make_svg(
    [
        (
            [
                ("$ ", "#89b4fa"),
                ("/search-memory type:decision project:my-app", "#cdd6f4"),
            ],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Searching observations... 4 matches in my-app", "#6c7086", 400),
        ("", "#1e1e2e"),
        (
            "| #  | Date       | Type     | Summary                          |",
            "#a6adc8",
            800,
        ),
        (
            "|----|------------|----------|----------------------------------|",
            "#6c7086",
            800,
        ),
        (
            "| 12 | 2026-02-18 | decision | Chose Postgres over SQLite       |",
            "#cdd6f4",
            1000,
        ),
        (
            "| 9  | 2026-02-14 | decision | JWT tokens, 15min expiry         |",
            "#cdd6f4",
            1100,
        ),
        (
            "| 6  | 2026-02-10 | decision | React over Vue for frontend      |",
            "#cdd6f4",
            1200,
        ),
        (
            "| 3  | 2026-02-03 | decision | Monorepo with Turborepo          |",
            "#cdd6f4",
            1300,
        ),
        ("", "#1e1e2e"),
        ("Show details for which entry? (number or 'all')", "#6c7086", 1700),
    ],
    title="search-memory",
    width=640,
)

# -- Directors --
directors = make_svg(
    [
        (
            [
                ("$ ", "#89b4fa"),
                ("/directors AI-powered code review tool for small teams", "#cdd6f4"),
            ],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Launching 5 directors in parallel...", "#6c7086", 400),
        ("  Murati     evaluating...", "#f9e2af", 600),
        ("  Sutskever  evaluating...", "#f9e2af", 700),
        ("  Cherny     evaluating...", "#f9e2af", 800),
        ("  Karpathy   evaluating...", "#f9e2af", 900),
        ("  Ive        evaluating...", "#f9e2af", 1000),
        ("", "#1e1e2e"),
        ("All 5 evaluations received. Synthesizing...", "#a6e3a1", 3000),
        ("", "#1e1e2e"),
        ("## Board Verdict", "#cba6f7", 3500),
        ("", "#1e1e2e"),
        (
            "Consensus: verification loops are the moat, not AI generation",
            "#a6e3a1",
            3800,
        ),
        ("Disagreement: Sutskever vs Murati on pricing model", "#f38ba8", 4100),
        ("Top question: what happens when the model improves 10x?", "#f9e2af", 4400),
    ],
    title="directors",
    width=640,
)

# -- Orchestrate --
orchestrate = make_svg(
    [
        (
            [
                ("$ ", "#89b4fa"),
                ("/orchestrate Find best practices for RAG in 2026", "#cdd6f4"),
            ],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Selecting agents: researcher, triangulator", "#6c7086", 400),
        ("Launching 2 agents in parallel...", "#6c7086", 700),
        ("", "#1e1e2e"),
        ("  [researcher]    searching web...   12 sources found", "#89b4fa", 1200),
        ("  [triangulator]  verifying claims... 8 claims checked", "#cba6f7", 1500),
        ("", "#1e1e2e"),
        ("All agents completed. Synthesizing...", "#a6e3a1", 3000),
        ("", "#1e1e2e"),
        ("Key findings:", "#cdd6f4", 3500),
        ("  1. Hybrid search (vector + BM25) outperforms pure vector", "#a6adc8", 3700),
        ("  2. Chunk size 512-1024 tokens optimal for most use cases", "#a6adc8", 3900),
        ("  3. Re-ranking with cross-encoders adds 15-20% accuracy", "#a6adc8", 4100),
        ("", "#1e1e2e"),
        (
            "Confidence: 0.87 (3 sources agree, 1 partially contradicts)",
            "#a6e3a1",
            4500,
        ),
    ],
    title="orchestrate",
    width=640,
)

# -- Research --
research = make_svg(
    [
        (
            [
                ("$ ", "#89b4fa"),
                ('/research "Is Bun faster than Node for HTTP servers?"', "#cdd6f4"),
            ],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Classifying query... comparative, technical", "#6c7086", 400),
        ("Searching 4 engines in parallel...", "#6c7086", 700),
        ("  Progress: [=========>        ] 6/11 pages", "#89b4fa", 1500),
        ("  Progress: [==================] 11/11 pages analyzed", "#a6e3a1", 3000),
        ("", "#1e1e2e"),
        ("Sources scored:", "#a6adc8", 3500),
        ("  [0.92] Official Bun benchmarks (bun.sh)", "#a6e3a1", 3700),
        ("  [0.88] TechEmpower Round 23 results", "#a6e3a1", 3800),
        ("  [0.71] Medium article with custom benchmarks", "#f9e2af", 3900),
        ("  [0.45] Reddit thread (anecdotal)", "#f38ba8", 4000),
        ("", "#1e1e2e"),
        ("Contradiction detected: official vs independent benchmarks", "#f9e2af", 4400),
        ("Generating comparison table...", "#6c7086", 4700),
    ],
    title="researching-web",
    width=640,
)

# -- Triangulate --
triangulate = make_svg(
    [
        (
            [
                ("$ ", "#89b4fa"),
                (
                    '/triangulate "React Server Components reduce bundle size by 30%"',
                    "#cdd6f4",
                ),
            ],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Claim type: FACT (quantitative, verifiable)", "#6c7086", 400),
        ("", "#1e1e2e"),
        ("Searching 3+ independent sources...", "#6c7086", 800),
        ("  Source 1: Next.js docs (primary)         confirms", "#a6e3a1", 1200),
        ("  Source 2: Vercel blog (same ecosystem)    confirms", "#f9e2af", 1500),
        ("  Source 3: Chrome DevRel benchmark         PARTIAL", "#f9e2af", 1800),
        ("  Source 4: Independent audit (BuilderIO)   30-40% range", "#a6e3a1", 2100),
        ("", "#1e1e2e"),
        ("Warning: echo bias (sources 1-2 share ecosystem)", "#f38ba8", 2800),
        ("", "#1e1e2e"),
        ("Verdict: PARTIAL CONFIRMATION", "#f9e2af", 3200),
        ("Confidence: 0.72", "#a6adc8", 3400),
        ("  Consensus:  +0.25  (3/4 confirm direction)", "#6c7086", 3500),
        ("  Evidence:   +0.30  (benchmarks exist)", "#6c7086", 3600),
        ("  Bias:       -0.15  (echo between sources)", "#6c7086", 3700),
        ("  Precision:  -0.08  (range is 25-40%, not exactly 30%)", "#6c7086", 3800),
    ],
    title="triangulate",
    width=680,
)

# -- Action Items --
action_items = make_svg(
    [
        (
            [("$ ", "#89b4fa"), ("/action-items meeting-notes-feb20.txt", "#cdd6f4")],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Reading file... 847 lines, 4 participants detected", "#6c7086", 400),
        ("Extracting tasks...", "#6c7086", 800),
        ("", "#1e1e2e"),
        ("## P0: Blockers", "#f38ba8", 1200),
        ("- [ ] Fix auth flow before launch  @alex  | Mon Feb 24", "#cdd6f4", 1400),
        ('      > "we cannot ship until the login redirect works"', "#6c7086", 1500),
        ("", "#1e1e2e"),
        ("## P1: Urgent", "#f9e2af", 1800),
        ("- [ ] Update API docs for v2 endpoints  @maria  | Feb 28", "#cdd6f4", 2000),
        ("- [ ] Load test the new caching layer    @alex   | Feb 26", "#cdd6f4", 2100),
        ("", "#1e1e2e"),
        ("## Unanswered Questions", "#cba6f7", 2500),
        ("- Do we need GDPR compliance for the EU launch?", "#a6adc8", 2700),
        ("- Who owns the monitoring dashboard?", "#a6adc8", 2800),
        ("", "#1e1e2e"),
        ("Found: 2 blockers, 5 urgent, 3 normal, 2 questions", "#a6e3a1", 3200),
    ],
    title="action-items",
    width=640,
)

# -- Checkup --
checkup = make_svg(
    [
        ([("$ ", "#89b4fa"), ("/checkup --full", "#cdd6f4")], "#cdd6f4"),
        ("", "#1e1e2e"),
        ("Scanning ~/.claude/skills/... 16 skills found", "#6c7086", 400),
        ("", "#1e1e2e"),
        ("Phase 0 (binary):", "#a6adc8", 800),
        ("  All file references valid", "#a6e3a1", 1000),
        ("  All paths resolve", "#a6e3a1", 1100),
        ("", "#1e1e2e"),
        ("Phase 1 (structural):", "#a6adc8", 1400),
        ("  [!] frameworks: description exceeds 500 chars", "#f9e2af", 1600),
        ("  [x] old-skill: references deleted file utils.py", "#f38ba8", 1800),
        ("", "#1e1e2e"),
        ("Phase 2 (semantic):", "#a6adc8", 2200),
        ("  [~] research + triangulate: similar descriptions", "#cba6f7", 2400),
        ("  15/16 skills healthy", "#a6e3a1", 2600),
        ("", "#1e1e2e"),
        ("1 broken, 1 warning, 1 suggestion", "#f9e2af", 3000),
    ],
    title="skill-checkup",
    width=640,
)

# -- Proposal --
proposal = make_svg(
    [
        (
            [
                ("$ ", "#89b4fa"),
                ("/proposal product.md call-transcript.txt", "#cdd6f4"),
            ],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Reading product description... done", "#6c7086", 400),
        ("Reading transcript... 2,340 lines, 47 min call", "#6c7086", 700),
        ("", "#1e1e2e"),
        ("Extracting pain points:", "#a6adc8", 1100),
        ("  Trigger:  manual reporting takes 3 days/month", "#f38ba8", 1300),
        ("  Active:   no real-time visibility into pipeline", "#f9e2af", 1500),
        ("  Latent:   team scaling will break current process", "#6c7086", 1700),
        ("", "#1e1e2e"),
        ("--- Checkpoint 1: confirm pains? (yes/edit) ---", "#cba6f7", 2200),
        ([("$ ", "#89b4fa"), ("yes", "#a6e3a1")], "#cdd6f4"),
        ("", "#1e1e2e"),
        ("Mapping solutions... generating architecture...", "#6c7086", 2800),
        ("Writing proposal.md... done", "#a6e3a1", 3500),
        ("Writing architecture.md... done", "#a6e3a1", 3700),
        ("Building prototype.html... done (Tailwind, dark theme)", "#a6e3a1", 4200),
        ("", "#1e1e2e"),
        ("3 files created. Open prototype.html in browser.", "#a6e3a1", 4600),
    ],
    title="transcript-to-proposal",
    width=640,
)

# -- AQAL Review --
aqal_review = make_svg(
    [
        ([("$ ", "#89b4fa"), ("/aqal-review", "#cdd6f4")], "#cdd6f4"),
        ("", "#1e1e2e"),
        ("Gathering week data...", "#6c7086", 400),
        ("  3 projects active, 28 commits, 5 sessions", "#a6adc8", 700),
        ("", "#1e1e2e"),
        ("Quadrant Assessment:", "#cdd6f4", 1100),
        ("  I  (Interior)     75  up    reflection improved", "#a6e3a1", 1300),
        ("  WE (Collective)   70  --    client call missed", "#f9e2af", 1500),
        ("  IT (Technical)    82  up    new CI pipeline", "#a6e3a1", 1700),
        ("  ITS (Systems)     68  down  staging broke twice", "#f38ba8", 1900),
        ("", "#1e1e2e"),
        ("Development Lines:", "#cdd6f4", 2300),
        ("  cognitive: 85%  technical: 78%  product: 82%", "#a6adc8", 2500),
        ("  emotional: 65%  interpersonal: 70%", "#a6adc8", 2600),
        ("", "#1e1e2e"),
        ("Week status: NORMAL (2 up, 1 stable, 1 down)", "#f9e2af", 3000),
        ("Focus next week: system stability, client follow-up", "#a6adc8", 3200),
        ("", "#1e1e2e"),
        ("Saved to ~/.claude/aqal-history.json (week 8)", "#a6e3a1", 3600),
    ],
    title="aqal-review",
    width=640,
)

# -- Memory Init --
memory_init = make_svg(
    [
        ([("$ ", "#89b4fa"), ("/memory-init", "#cdd6f4")], "#cdd6f4"),
        ("", "#1e1e2e"),
        ("Creating directory structure...", "#6c7086", 400),
        ("  ~/.claude/memory/              created", "#a6e3a1", 600),
        ("  ~/.claude/memory/projects/     created", "#a6e3a1", 700),
        ("  ~/.claude/memory/tests/        created", "#a6e3a1", 800),
        ("", "#1e1e2e"),
        ("Scanning for git projects...", "#6c7086", 1200),
        ("  Found: my-app       (~/projects/my-app)", "#a6adc8", 1500),
        ("  Found: landing-page (~/projects/landing-page)", "#a6adc8", 1700),
        ("  Found: api-server   (~/work/api-server)", "#a6adc8", 1900),
        ("", "#1e1e2e"),
        ("Generated:", "#a6adc8", 2300),
        ("  memory-config.json    3 projects mapped", "#a6e3a1", 2500),
        ("  MEMORY.md             index created", "#a6e3a1", 2600),
        ("  general.md            starter dossier", "#a6e3a1", 2700),
        ("", "#1e1e2e"),
        (
            "Memory system ready. Start working, /session-save when done.",
            "#a6e3a1",
            3100,
        ),
    ],
    title="memory-init",
    width=640,
)

# -- Install --
install = make_svg(
    [
        ([("$ ", "#89b4fa"), ("bash install.sh", "#cdd6f4")], "#cdd6f4"),
        ("", "#1e1e2e"),
        ("Welcome to Miracle Infrastructure", "#cdd6f4", 300),
        ("16 skills for Claude Code that solve actual problems.", "#6c7086", 300),
        ("", "#1e1e2e"),
        ("Available packs:", "#a6adc8", 600),
        ("  [1] memory       5 skills + 3 rules", "#89b4fa", 700),
        ("  [2] thinking     4 skills", "#89b4fa", 800),
        ("  [3] research     3 skills", "#89b4fa", 900),
        ("  [4] business     1 skill", "#89b4fa", 1000),
        ("  [5] content      1 skill", "#89b4fa", 1100),
        ("  [6] productivity 1 skill", "#89b4fa", 1200),
        ("  [7] meta         1 skill", "#89b4fa", 1300),
        ("  [A] All packs", "#a6e3a1", 1400),
        ("", "#1e1e2e"),
        (
            [("Select packs (e.g., 1 3 7 or A): ", "#a6adc8"), ("A", "#a6e3a1")],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Installing... 16 skills, 3 rules, templates, tests", "#6c7086", 1800),
        ("Done. Open Claude Code and try: /session-save", "#a6e3a1", 2400),
    ],
    title="install.sh",
    width=640,
)

# -- Frameworks --
frameworks = make_svg(
    [
        (
            [
                ("$ ", "#89b4fa"),
                (
                    "/frameworks My SaaS is at MVP stage, preparing for launch",
                    "#cdd6f4",
                ),
            ],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Detecting stage... Stage 3: MVP / First Launch", "#6c7086", 400),
        ("Activating 8 frameworks:", "#a6adc8", 800),
        ("", "#1e1e2e"),
        ("  Worse is Better    ship the 80% version now", "#a6e3a1", 1000),
        ("  YAGNI              cut the admin panel, nobody asked", "#a6e3a1", 1200),
        ("  Build-Measure-     deploy, watch metrics, iterate", "#a6e3a1", 1400),
        ("  Pareto 80/20       3 features cover 80% of use cases", "#a6e3a1", 1600),
        ("  Fail Fast          add error tracking before launch", "#f9e2af", 1800),
        ("", "#1e1e2e"),
        ("Conflict detected:", "#f38ba8", 2400),
        ("  YAGNI vs Design-for-future: YAGNI wins at MVP stage", "#f9e2af", 2600),
        ("  (build flexibility into interfaces, not features)", "#6c7086", 2700),
        ("", "#1e1e2e"),
        ("Recommendations:", "#cdd6f4", 3100),
        ("  1. Remove admin panel from v1       <- YAGNI", "#a6adc8", 3300),
        ("  2. Add Sentry before launch         <- Fail Fast", "#a6adc8", 3500),
        ("  3. Ship to 10 users this week       <- BML", "#a6adc8", 3700),
    ],
    title="frameworks",
    width=640,
)


# -- Insight: Structure > Freedom (VS card) --
insight_structure = make_versus_svg(
    left_items=[
        {"text": "free-form notes", "sub": "unnavigable in 2 weeks", "delay": 400},
        {"text": "optional context fields", "sub": "always left empty", "delay": 800},
        {"text": "unlimited tags", "sub": "nobody tags anything", "delay": 1200},
    ],
    right_items=[
        {"text": "typed observations", "sub": "useful 6 months later", "delay": 600},
        {"text": "mandatory Before/After", "sub": "gold for debugging", "delay": 1000},
        {"text": "5 observation types", "sub": "searchable by pattern", "delay": 1400},
    ],
    title="STRUCTURE vs FREEDOM  (1,169 sessions)",
    left_label="freedom",
    right_label="structure",
    verdict="less freedom = better data. the structure IS the value.",
    width=640,
    read_pause=5.0,
)

# -- Insight: Operator = Bottleneck --
insight_bottleneck = make_svg(
    [
        ([("$ ", "#89b4fa"), ("diagnose --system bottleneck", "#cdd6f4")], "#cdd6f4"),
        ("", "#1e1e2e"),
        ("Running system diagnostics...", "#6c7086", 400),
        ("", "#1e1e2e"),
        ("AI subsystem:", "#a6adc8", 800),
        ("  context window    200k tokens    OK", "#a6e3a1", 1000),
        ("  reasoning         multi-step     OK", "#a6e3a1", 1100),
        ("  memory recall     from dossier   OK", "#a6e3a1", 1200),
        ("  parallel agents   up to 5        OK", "#a6e3a1", 1300),
        ("", "#1e1e2e"),
        ("Human subsystem:", "#a6adc8", 1700),
        ("  context window    ~7 items       WARNING", "#f9e2af", 1900),
        ("  attention span    variable       WARNING", "#f9e2af", 2100),
        ("  working memory    fragile        WARNING", "#f9e2af", 2300),
        ("  parallel tasks    1 (optimistic) CRITICAL", "#f38ba8", 2500),
        ("", "#1e1e2e"),
        ("Bottleneck identified: you.", "#cba6f7", 3100),
        ("System compensates: auto-load, auto-capture, auto-remind.", "#a6e3a1", 3400),
    ],
    title="lesson #2",
    width=640,
    read_pause=5.0,
)

# -- Insight: Precision, Not Power (receipt) --
insight_precision = make_receipt_svg(
    sections=[
        {
            "title": "APPROACH A: LAUNCH EVERYTHING",
            "items": [
                ("5 directors", "$1.80"),
                ("4 researchers", "$1.60"),
                ("3 developers", "$0.80"),
            ],
            "subtotal": ("12 reports, 90% overlap", "$4.20"),
            "subtotal_color": "#f38ba8",
            "delay_start": 400,
        },
        {
            "title": "APPROACH B: PRECISION SELECTION",
            "items": [
                ("1 researcher", "$0.20"),
                ("1 triangulator", "$0.15"),
            ],
            "subtotal": ("Verified claim, 3 sources", "$0.35"),
            "subtotal_color": "#a6e3a1",
            "delay_start": 2000,
        },
    ],
    footer_lines=[
        ("YOU SAVED", "$3.85", "#cba6f7"),
        ("precision > power", "", "#6c7086"),
    ],
    width=400,
    read_pause=5.0,
)


# -- Insight: Memory prevents re-derivation (chat bubbles) --
insight_memory = make_chat_svg(
    [
        {
            "user": "You",
            "time": "Feb 3",
            "bar": "#a6e3a1",
            "color": "#cdd6f4",
            "lines": ["Should we use JWT or sessions?"],
            "delay": 0,
        },
        {
            "user": "Agent",
            "time": "Feb 3",
            "bar": "#89b4fa",
            "color": "#cdd6f4",
            "lines": ["Evaluated both. JWT wins.", "Recording decision."],
            "delay": 600,
        },
        {"divider": "6 weeks later", "delay": 1800},
        {
            "user": "Agent",
            "time": "no memory",
            "bar": "#f38ba8",
            "color": "#f38ba8",
            "lines": [
                "Should we consider session-based auth?",
                "Let me evaluate the options...",
            ],
            "delay": 2400,
        },
        {
            "user": "You",
            "time": "",
            "bar": "#f38ba8",
            "color": "#f38ba8",
            "lines": ["We already decided this. JWT.", "15 min wasted."],
            "delay": 3000,
        },
        {"divider": "same day, with memory", "delay": 3800},
        {
            "user": "Agent",
            "time": "with memory",
            "bar": "#a6e3a1",
            "color": "#a6e3a1",
            "lines": [
                "Loading dossier... JWT (decided Feb 3)",
                "Continuing where we left off. 0 min wasted.",
            ],
            "delay": 4400,
        },
    ],
    channel="project / auth decisions",
    width=540,
    read_pause=5.0,
)

# -- Insight: Research Concept Mapping (academic figure) --
insight_research = make_figure_svg(
    mappings=[
        {
            "left": "progressive disclosure",
            "left_sub": "load by query, not corpus",
            "right": "RAG without vectors",
            "right_sub": "structured retrieval",
            "delay": 400,
        },
        {
            "left": "auto-observe",
            "left_sub": "typed events + context",
            "right": "episodic memory",
            "right_sub": "experience replay",
            "delay": 1000,
        },
        {
            "left": "directors (5 prompts)",
            "left_sub": "same model, real divergence",
            "right": "mixture-of-experts",
            "right_sub": "prompt as architecture",
            "delay": 1600,
        },
        {
            "left": "decision dossiers",
            "left_sub": "prevents re-derivation",
            "right": "persistent belief store",
            "right_sub": "survives context reset",
            "delay": 2200,
        },
        {
            "left": "constraints > freedom",
            "left_sub": "structure improves output",
            "right": "instruction tuning",
            "right_sub": "specificity > coverage",
            "delay": 2800,
        },
        {
            "left": "human = bottleneck",
            "left_sub": "system compensates for you",
            "right": "HITL as limiting factor",
            "right_sub": "not the other way",
            "delay": 3400,
        },
    ],
    caption="Fig. 1. Emergent parallels: practitioner infrastructure vs ML research",
    footnote="n = 1,169 sessions. Not designed. Discovered.",
    width=640,
    read_pause=6.0,
)


# -- Unstuck --
unstuck = make_chat_svg(
    [
        {
            "user": "You",
            "lines": ["I don't know how to organize the API for the new project"],
            "bar": "#f38ba8",
            "color": "#f38ba8",
            "delay": 0,
        },
        {
            "user": "Agent",
            "time": "/unstuck",
            "lines": ["Diagnosed: fog. Starting deep interview."],
            "bar": "#89b4fa",
            "delay": 600,
        },
        {
            "user": "Agent",
            "time": "Q1 of ~7",
            "lines": [
                "Who will consume this API?",
                "  Your frontend only / External devs / Both",
            ],
            "bar": "#89b4fa",
            "delay": 1200,
        },
        {
            "user": "You",
            "lines": ["Just my frontend"],
            "bar": "#a6e3a1",
            "delay": 2000,
        },
        {
            "user": "Agent",
            "time": "Q2 of ~7",
            "lines": ["Speed now or clean architecture?"],
            "bar": "#89b4fa",
            "delay": 2600,
        },
        {"divider": "5 questions later", "delay": 3400},
        {
            "user": "Agent",
            "time": "synthesis",
            "lines": [
                "Pattern in your answers: simplicity > correctness.",
                "You want REST, no abstractions, auto-generated types.",
                "You already knew. You just needed permission.",
            ],
            "bar": "#a6e3a1",
            "delay": 4000,
        },
    ],
    channel="unstuck / api-design",
    width=640,
    read_pause=5.0,
)

# Generate all SVGs
svgs = {
    "session-save.svg": session_save,
    "search-memory.svg": search_memory,
    "directors.svg": directors,
    "orchestrate.svg": orchestrate,
    "research.svg": research,
    "triangulate.svg": triangulate,
    "action-items.svg": action_items,
    "checkup.svg": checkup,
    "proposal.svg": proposal,
    "aqal-review.svg": aqal_review,
    "memory-init.svg": memory_init,
    "install.svg": install,
    "frameworks.svg": frameworks,
    "insight-structure.svg": insight_structure,
    "insight-bottleneck.svg": insight_bottleneck,
    "insight-precision.svg": insight_precision,
    "insight-memory.svg": insight_memory,
    "insight-research.svg": insight_research,
    "unstuck.svg": unstuck,
}

for name, svg in svgs.items():
    path = os.path.join(SCRIPT_DIR, name)
    with open(path, "w") as f:
        f.write(svg)
    print(f"  [ok] {name}")

print(f"\nGenerated {len(svgs)} SVGs in {SCRIPT_DIR}")
