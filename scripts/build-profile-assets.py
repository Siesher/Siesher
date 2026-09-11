"""Build self-contained GitHub-compatible SVG layouts around the original 3D art."""
from pathlib import Path
import base64
from html import escape

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ART = base64.b64encode((ASSETS / 'grimoire-3d.png').read_bytes()).decode()
PALETTES = {
    'dark': dict(bg='#14131a', panel='#171621', panel2='#242133', ink='#f4f0ff', muted='#aaa4be', accent='#c4b0ff', line='#393246', glow='#8661d5', tint='#252033', chip='#242030'),
    'light': dict(bg='#f5f3ef', panel='#ffffff', panel2='#e6dff2', ink='#302640', muted='#786d88', accent='#7853b4', line='#dfd5ed', glow='#b49add', tint='#eee9f1', chip='#eee7f7'),
}

for theme, p in PALETTES.items():
    hero = '''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="440" viewBox="0 0 1200 440" role="img" aria-labelledby="title desc">
<title id="title">Maksim / Siesher — Data Scientist &amp; ML Engineer</title>
<desc id="desc">An animated three-dimensional silver grimoire in a lavender glass orbit. Inspired by Frieren.</desc>
<defs>
  <linearGradient id="backdrop" x2="1" y2="1"><stop stop-color="{bg}"/><stop offset="1" stop-color="{tint}"/></linearGradient>
  <radialGradient id="aura"><stop stop-color="{glow}" stop-opacity=".42"/><stop offset="1" stop-color="{glow}" stop-opacity="0"/></radialGradient>
  <radialGradient id="floor"><stop stop-color="{glow}" stop-opacity=".28"/><stop offset="1" stop-color="{glow}" stop-opacity="0"/></radialGradient>
  <linearGradient id="rim"><stop stop-color="{line}"/><stop offset=".5" stop-color="{accent}" stop-opacity=".7"/><stop offset="1" stop-color="{line}"/></linearGradient>
  <clipPath id="frame"><rect x="1" y="1" width="1198" height="438" rx="28"/></clipPath>
  <g id="blueflower"><g fill="#93b8d2"><ellipse cy="-8" rx="5" ry="10"/><ellipse cy="-8" rx="5" ry="10" transform="rotate(72)"/><ellipse cy="-8" rx="5" ry="10" transform="rotate(144)"/><ellipse cy="-8" rx="5" ry="10" transform="rotate(216)"/><ellipse cy="-8" rx="5" ry="10" transform="rotate(288)"/></g><circle r="3" fill="#d8c497"/></g>
  <path id="star" d="M0-7 Q1.5-1.5 7 0 Q1.5 1.5 0 7 Q-1.5 1.5-7 0 Q-1.5-1.5 0-7Z"/>
</defs>
<style>
  .art {{ animation: levitate 7s ease-in-out infinite; transform-origin: 920px 220px; }}
  .shadow {{ animation: breathe 7s ease-in-out infinite; transform-origin: 935px 378px; }}
  .spark {{ animation: shimmer 4s ease-in-out infinite; }} .late {{ animation-delay: -2s; }}
  @keyframes levitate {{ 0%,100% {{ transform: translateY(3px) rotate(-1deg); }} 50% {{ transform: translateY(-11px) rotate(1deg); }} }}
  @keyframes breathe {{ 0%,100% {{ opacity: .75; transform: scaleX(1); }} 50% {{ opacity: .4; transform: scaleX(.86); }} }}
  @keyframes shimmer {{ 0%,100% {{ opacity: .25; }} 50% {{ opacity: .9; }} }}
  @media(max-width:600px) {{ .eyebrow,.note,.folio {{ display:none; }} .name {{ font-size:114px; }} .role {{ font-size:30px; }} .tagline {{ font-size:24px; }} }}
  @media(prefers-reduced-motion:reduce) {{ .art,.shadow,.spark {{ animation:none; }} }}
</style>
<g clip-path="url(#frame)">
  <rect width="1200" height="440" fill="url(#backdrop)"/>
  <ellipse cx="935" cy="214" rx="325" ry="245" fill="url(#aura)"/>
  <g fill="none" stroke="{line}" opacity=".65">
    <ellipse cx="935" cy="378" rx="270" ry="58"/><ellipse cx="935" cy="378" rx="220" ry="37"/>
    <path d="M665 378 H1205 M935 320 V441"/>
  </g>
  <ellipse class="shadow" cx="935" cy="389" rx="215" ry="28" fill="url(#floor)"/>
  <g font-family="Arial, Helvetica, sans-serif">
    <circle cx="53" cy="51" r="4" fill="{accent}"/>
    <text class="eyebrow" x="69" y="56" font-size="13" letter-spacing="2.7" fill="{muted}">MAKSIM / SIESHER</text>
    <text class="folio" x="1144" y="56" font-size="12" letter-spacing="2" text-anchor="end" fill="{muted}">DATA SCIENCE &amp; ML</text>
    <text class="name" x="46" y="192" font-size="106" font-weight="700" letter-spacing="-6" fill="{ink}">Siesher<tspan fill="{accent}">.</tspan></text>
    <text class="role" x="54" y="244" font-size="28" letter-spacing="-.5" fill="{ink}">Data Scientist / ML Engineer</text>
    <text class="tagline" x="54" y="283" font-size="21" fill="{muted}">Данные. Языковые модели. AI-системы.</text>
    <g class="note">
      <rect x="54" y="322" width="73" height="32" rx="16" fill="{chip}" stroke="{line}"/>
      <rect x="136" y="322" width="103" height="32" rx="16" fill="{chip}" stroke="{line}"/>
      <rect x="248" y="322" width="113" height="32" rx="16" fill="{chip}" stroke="{line}"/>
      <text x="90" y="343" text-anchor="middle" fill="{accent}" font-size="12">LLMs</text>
      <text x="187" y="343" text-anchor="middle" fill="{accent}" font-size="12">Graph ML</text>
      <text x="304" y="343" text-anchor="middle" fill="{accent}" font-size="12">Local AI</text>
    </g>
    <text class="note" x="54" y="405" fill="{muted}" font-size="13" letter-spacing=".5">Inspired by Frieren. Built through research.</text>
  </g>
  <image class="art" x="726" y="55" width="435" height="339" preserveAspectRatio="xMidYMid meet" xlink:href="data:image/png;base64,{art}"/>
  <g opacity=".9"><path d="M697 416Q707 389 692 368M700 404Q720 385 727 378" fill="none" stroke="#93a99a" stroke-width="1.3"/><use xlink:href="#blueflower" transform="translate(692 366) rotate(-15)"/><use xlink:href="#blueflower" transform="translate(728 377) scale(.7) rotate(15)"/></g>
  <g fill="{accent}">
    <use xlink:href="#star" x="780" y="113" class="spark"/>
    <use xlink:href="#star" x="1120" y="319" class="spark late"/>
    <circle cx="1045" cy="112" r="2" class="spark"/>
    <circle cx="728" cy="302" r="2" class="spark late"/>
  </g>
</g>
<rect x="1" y="1" width="1198" height="438" rx="28" fill="none" stroke="url(#rim)"/>
</svg>
'''.format(**p, art=ART)
    (ASSETS / f'header-{theme}.svg').write_text(hero)

    projects = [
        ('mits', '01', 'MITS', 'AI ДЛЯ ОБРАЗОВАНИЯ', 'Сократический STEM-тьютор', 'с мультиагентной архитектурой.', 'Qwen3.5 / FastAPI / RL', 'book'),
        ('dmezo', '02', 'D-MeZO-N', 'ИССЛЕДОВАНИЯ LLM', 'Федеративный fine-tuning', 'без обратного прохода.', 'PyTorch / ZO optimization', 'orbit'),
        ('supcom', '03', 'SupCom AI', 'ПРИКЛАДНЫЕ AI-СИСТЕМЫ', 'LLM-стратегия, Lua-рефлексы', 'и C++ мост к игровому движку.', 'Qwen / C++ / Lua', 'cube'),
        ('opencode', '04', 'OpenCode', 'ЛОКАЛЬНЫЕ ИНСТРУМЕНТЫ', 'AI-разработка и модели', 'на собственном железе.', 'llama.cpp / MCP / Routing', 'layers'),
    ]
    # Native interface ornaments use gradients and extruded geometry, not external icon services.
    ornaments = {
        'book': '<g transform="translate(352 74) rotate(-15)"><path d="M-44-27 L0-15 0 39-44 26Z" fill="url(#glass)"/><path d="M0-15 L44-27 44 26 0 39Z" fill="url(#metal)"/><path d="M-44 26 L0 39 44 26 44 33 0 46-44 33Z" fill="{accent}" opacity=".5"/><path d="M0-15 V39 M-35-14-9-7 M-35-3-9 4 M9-7 35-14 M9 4 35-3" stroke="{ink}" opacity=".5" fill="none"/></g>',
        'orbit': '<g transform="translate(355 74)"><circle r="27" fill="url(#sphere)"/><ellipse rx="61" ry="21" transform="rotate(-32)" fill="none" stroke="url(#metal)" stroke-width="9"/><circle cx="-49" cy="22" r="11" fill="url(#sphere)"/><circle cx="48" cy="-35" r="7" fill="url(#sphere)"/></g>',
        'cube': '<g transform="translate(355 72)"><path d="M0-44 43-20 0 6-43-20Z" fill="url(#metal)"/><path d="M-43-20 0 6 0 53-43 28Z" fill="url(#glass)"/><path d="M0 6 43-20 43 28 0 53Z" fill="{accent}" opacity=".5"/><path d="M0-44 43-20 43 28 0 53-43 28-43-20Z M-43-20 0 6 43-20 M0 6V53" fill="none" stroke="{ink}" stroke-opacity=".4"/><path d="M-25 1-13 8-25 16" fill="none" stroke="{ink}" stroke-width="3"/></g>',
        'layers': '<g transform="translate(355 77)"><g transform="translate(0 25)"><path d="M0-39 56-10 0 20-56-10Z" fill="url(#glass)" stroke="{accent}" stroke-opacity=".5"/></g><g transform="translate(0 4)"><path d="M0-39 56-10 0 20-56-10Z" fill="url(#metal)" opacity=".8"/></g><g transform="translate(0 -18)"><path d="M0-39 56-10 0 20-56-10Z" fill="url(#glass)" stroke="{ink}" stroke-opacity=".5"/></g></g>',
    }
    for slug, num, title, category, line1, line2, stack, ornament in projects:
        card = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="286" viewBox="0 0 480 286" role="img" aria-labelledby="title desc">
<title id="title">{title} — {category}</title><desc id="desc">{line1} {line2} {stack}</desc>
<defs>
  <linearGradient id="surface" x2="1" y2="1"><stop stop-color="{panel}"/><stop offset="1" stop-color="{panel2}"/></linearGradient>
  <linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{ink}" stop-opacity=".85"/><stop offset=".45" stop-color="{accent}" stop-opacity=".6"/><stop offset="1" stop-color="{glow}" stop-opacity=".15"/></linearGradient>
  <linearGradient id="metal" x2="1" y2="1"><stop stop-color="{ink}"/><stop offset=".3" stop-color="{accent}"/><stop offset=".5" stop-color="{panel2}"/><stop offset=".72" stop-color="{ink}"/><stop offset="1" stop-color="{accent}"/></linearGradient>
  <radialGradient id="sphere" cx="30%" cy="25%"><stop stop-color="#fff"/><stop offset=".28" stop-color="{accent}"/><stop offset=".8" stop-color="{glow}"/><stop offset="1" stop-color="{panel2}"/></radialGradient>
  <radialGradient id="halo"><stop stop-color="{glow}" stop-opacity=".3"/><stop offset="1" stop-color="{glow}" stop-opacity="0"/></radialGradient>
</defs>
<style>
.object{{animation:float 6s ease-in-out infinite;animation-delay:-{num}s}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-5px)}}}}
@media(max-width:300px){{.description,.category,.stack{{display:none}} .heading{{font-size:48px}} .number{{font-size:25px}} }}
@media(prefers-reduced-motion:reduce){{.object{{animation:none}}}}
</style>
<rect x="5" y="8" width="470" height="276" rx="22" fill="{bg}"/>
<rect x="1" y="1" width="478" height="276" rx="22" fill="url(#surface)" stroke="{line}"/>
<path d="M25 2 H455" stroke="{ink}" stroke-opacity=".2"/>
<ellipse cx="352" cy="82" rx="120" ry="80" fill="url(#halo)"/>
<g class="object">{ornament}</g>
<g font-family="Arial, Helvetica, sans-serif">
  <text class="number" x="27" y="41" font-size="14" fill="{accent}" letter-spacing="2">{num} /</text>
  <text class="category" x="27" y="87" font-size="11" fill="{muted}" letter-spacing="1.5">{category}</text>
  <text class="heading" x="25" y="143" font-size="39" fill="{ink}" font-weight="700" letter-spacing="-1.3">{title}</text>
  <g class="description" fill="{muted}" font-size="19"><text x="27" y="181">{line1}</text><text x="27" y="207">{line2}</text></g>
  <path d="M27 231 H452" stroke="{line}"/>
  <text class="stack" x="27" y="256" fill="{accent}" font-size="12" letter-spacing=".5">{stack}</text>
  <path d="M428 254 444 238 M430 238H444V252" fill="none" stroke="{accent}" stroke-width="1.5"/>
</g></svg>
'''.format(**p, title=escape(title), category=category, num=num, line1=line1, line2=line2, stack=stack, ornament=ornaments[ornament].format(**p))
        (ASSETS / f'project-{slug}-{theme}.svg').write_text(card)

print('Built two animated headers and eight project cards.')
