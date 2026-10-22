#!/usr/bin/env python3
"""Add inline SVG diagrams to selected topics across subjects."""
import json
import pathlib

C = pathlib.Path(__file__).resolve().parent.parent / "content"

S = 'stroke="#e8ecf4" stroke-width="2" fill="none"'
DASH = 'stroke="#5a6478" stroke-width="1.5" stroke-dasharray="5 4" fill="none"'
ACC = "#4da3ff"; GRN = "#7ee0a8"; YEL = "#ffcf5c"; RED = "#ff7a7a"
TXT = 'fill="#e8ecf4" font-family="system-ui,sans-serif" font-size="14"'
BIG = 'fill="#e8ecf4" font-family="system-ui,sans-serif" font-size="15" font-weight="600"'

D = {}

D[("maths", "pythagoras")] = (
    '<svg viewBox="0 0 400 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Right-angled triangle with sides a, b and hypotenuse c">'
    '<polygon points="70,190 330,190 330,60" fill="none" stroke="' + ACC + '" stroke-width="2.5"/>'
    '<rect x="316" y="178" width="14" height="12" fill="none" stroke="' + GRN + '" stroke-width="2"/>'
    '<text x="195" y="213" text-anchor="middle" ' + TXT + '>a</text>'
    '<text x="345" y="128" ' + TXT + '>b</text>'
    '<text x="185" y="115" ' + TXT + ' fill="' + YEL + '">c (hypotenuse)</text>'
    '<text x="292" y="206" ' + TXT + ' fill="' + GRN + '">90&#176;</text>'
    '<text x="70" y="34" ' + BIG + '>a&#178; + b&#178; = c&#178;</text>'
    '</svg>',
    "The hypotenuse is always opposite the right angle. Add the squares to find it; subtract to find a shorter side.")

D[("maths", "trig-bearings")] = (
    '<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bearing measured clockwise from north">'
    '<circle cx="190" cy="130" r="4" fill="' + ACC + '"/>'
    '<line x1="190" y1="130" x2="190" y2="34" ' + S + '/>'
    '<text x="190" y="24" text-anchor="middle" ' + TXT + ' fill="' + ACC + '">North</text>'
    '<line x1="190" y1="130" x2="316" y2="192" stroke="' + GRN + '" stroke-width="2.5"/>'
    '<path d="M190 78 A52 52 0 0 1 228 158" fill="none" stroke="' + YEL + '" stroke-width="2"/>'
    '<text x="242" y="104" ' + TXT + ' fill="' + YEL + '">bearing</text>'
    '<text x="258" y="212" ' + TXT + ' fill="' + GRN + '">direction of travel</text>'
    '<text x="18" y="30" ' + TXT + ' fill="#9aa4bb">Clockwise from North</text>'
    '</svg>',
    "Bearings are measured clockwise from North at each point, and written as three digits.")

D[("maths", "arcs-sectors")] = (
    '<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sector of a circle with radius and arc">'
    '<circle cx="200" cy="128" r="95" ' + S + ' stroke="#5a6478"/>'
    '<path d="M200 128 L295 128 A95 95 0 0 0 247.5 45.7 Z" fill="' + ACC + '" fill-opacity="0.22" stroke="' + ACC + '" stroke-width="2.5"/>'
    '<circle cx="200" cy="128" r="3.5" fill="' + GRN + '"/>'
    '<text x="246" y="150" ' + TXT + ' fill="' + GRN + '">r</text>'
    '<text x="288" y="72" ' + TXT + ' fill="' + ACC + '">arc</text>'
    '<text x="226" y="114" ' + TXT + ' fill="' + YEL + '">&#952;</text>'
    '<text x="30" y="228" ' + TXT + ' fill="#9aa4bb">fraction of circle = &#952; / 360</text>'
    '</svg>',
    "Arc length and sector area are the fraction theta/360 of the full circle.")

D[("maths", "sine-cosine-rule")] = (
    '<svg viewBox="0 0 400 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Triangle labelled A B C with opposite sides a b c">'
    '<polygon points="62,190 348,190 152,48" fill="none" stroke="' + ACC + '" stroke-width="2.5"/>'
    '<text x="54" y="206" ' + BIG + '>A</text>'
    '<text x="352" y="206" ' + BIG + '>B</text>'
    '<text x="148" y="40" ' + BIG + '>C</text>'
    '<text x="204" y="212" ' + TXT + ' fill="' + GRN + '">c</text>'
    '<text x="240" y="112" ' + TXT + ' fill="' + GRN + '">a</text>'
    '<text x="96" y="114" ' + TXT + ' fill="' + GRN + '">b</text>'
    '<text x="18" y="26" ' + TXT + ' fill="#9aa4bb">a / sin A = b / sin B = c / sin C</text>'
    '<text x="18" y="46" ' + TXT + ' fill="#9aa4bb">a&#178; = b&#178; + c&#178; &#8722; 2bc cos A</text>'
    '</svg>',
    "Side a is opposite angle A, and so on. With no matching side-angle pair, use the cosine rule.")

D[("maths", "straight-line")] = (
    '<svg viewBox="0 0 400 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Straight line on axes showing the gradient triangle">'
    '<line x1="50" y1="195" x2="370" y2="195" ' + S + ' stroke="#5a6478"/>'
    '<line x1="50" y1="195" x2="50" y2="30" ' + S + ' stroke="#5a6478"/>'
    '<text x="356" y="216" ' + TXT + ' fill="#9aa4bb">x</text>'
    '<text x="30" y="40" ' + TXT + ' fill="#9aa4bb">y</text>'
    '<line x1="50" y1="170" x2="330" y2="55" stroke="' + ACC + '" stroke-width="2.5"/>'
    '<line x1="150" y1="145" x2="250" y2="145" stroke="' + GRN + '" stroke-width="2" stroke-dasharray="4 3"/>'
    '<line x1="250" y1="145" x2="250" y2="83" stroke="' + GRN + '" stroke-width="2" stroke-dasharray="4 3"/>'
    '<text x="193" y="163" text-anchor="middle" ' + TXT + ' fill="' + GRN + '">run</text>'
    '<text x="262" y="118" ' + TXT + ' fill="' + GRN + '">rise</text>'
    '<text x="170" y="42" ' + BIG + ' fill="' + YEL + '">gradient = rise / run</text>'
    '</svg>',
    "Gradient is the vertical change divided by the horizontal change.")

D[("maths", "quadratic-graphs")] = (
    '<svg viewBox="0 0 400 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Parabola showing two roots and the turning point">'
    '<line x1="30" y1="152" x2="380" y2="152" ' + S + ' stroke="#5a6478"/>'
    '<line x1="200" y1="212" x2="200" y2="28" ' + S + ' stroke="#5a6478"/>'
    '<path d="M96 42 Q200 300 304 42" fill="none" stroke="' + ACC + '" stroke-width="2.5"/>'
    '<circle cx="127" cy="152" r="5" fill="' + GRN + '"/>'
    '<circle cx="273" cy="152" r="5" fill="' + GRN + '"/>'
    '<text x="108" y="174" ' + TXT + ' fill="' + GRN + '">root</text>'
    '<text x="262" y="174" ' + TXT + ' fill="' + GRN + '">root</text>'
    '<circle cx="200" cy="124" r="4.5" fill="' + YEL + '"/>'
    '<text x="210" y="120" ' + TXT + ' fill="' + YEL + '">turning point</text>'
    '<text x="20" y="222" ' + TXT + ' fill="#9aa4bb">a &gt; 0 opens up (minimum) &#183; a &lt; 0 opens down (maximum)</text>'
    '</svg>',
    "Roots are where y = 0, and a quadratic usually has two.")

D[("maths", "vectors")] = (
    '<svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vector broken into horizontal and vertical components">'
    '<defs><marker id="ah" markerWidth="10" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0 0 L10 4 L0 8 z" fill="' + ACC + '"/></marker></defs>'
    '<line x1="70" y1="176" x2="300" y2="176" ' + DASH + '/>'
    '<line x1="300" y1="176" x2="300" y2="66" ' + DASH + '/>'
    '<line x1="70" y1="176" x2="300" y2="66" stroke="' + ACC + '" stroke-width="2.5" marker-end="url(#ah)"/>'
    '<text x="178" y="194" ' + TXT + ' fill="' + GRN + '">x</text>'
    '<text x="312" y="126" ' + TXT + ' fill="' + GRN + '">y</text>'
    '<text x="120" y="106" ' + BIG + ' fill="' + YEL + '">|v| = &#8730;(x&#178; + y&#178;)</text>'
    '<text x="70" y="34" ' + TXT + ' fill="#9aa4bb">2D: (x, y) &#183; 3D: (x, y, z)</text>'
    '</svg>',
    "Magnitude comes from Pythagoras on the components.")

D[("maths", "circle-angles")] = (
    '<svg viewBox="0 0 400 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Circle with a tangent meeting a radius at ninety degrees">'
    '<circle cx="185" cy="118" r="85" ' + S + '/>'
    '<circle cx="185" cy="118" r="3.5" fill="' + ACC + '"/>'
    '<text x="166" y="112" ' + TXT + ' fill="' + ACC + '">O</text>'
    '<line x1="185" y1="118" x2="270" y2="118" ' + S + ' stroke="' + GRN + '"/>'
    '<line x1="152" y1="222" x2="358" y2="76" stroke="' + YEL + '" stroke-width="2.5"/>'
    '<rect x="270" y="106" width="12" height="12" fill="none" stroke="' + RED + '" stroke-width="2"/>'
    '<text x="250" y="100" ' + TXT + ' fill="' + RED + '">90&#176;</text>'
    '<text x="274" y="144" ' + TXT + ' fill="' + GRN + '">radius</text>'
    '<text x="296" y="62" ' + TXT + ' fill="' + YEL + '">tangent</text>'
    '<text x="18" y="226" ' + TXT + ' fill="#9aa4bb">centre angle = 2 &#215; circumference angle on the same arc</text>'
    '</svg>',
    "A tangent always meets a radius at 90 degrees.")

D[("physics", "velocity-time")] = (
    '<svg viewBox="0 0 400 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Velocity-time graph with the area shaded showing displacement">'
    '<line x1="55" y1="192" x2="370" y2="192" ' + S + ' stroke="#5a6478"/>'
    '<line x1="55" y1="192" x2="55" y2="30" ' + S + ' stroke="#5a6478"/>'
    '<text x="358" y="214" ' + TXT + ' fill="#9aa4bb">time</text>'
    '<text x="18" y="38" ' + TXT + ' fill="#9aa4bb">v</text>'
    '<polygon points="55,192 150,84 280,84 280,192" fill="' + ACC + '" fill-opacity="0.2" stroke="' + ACC + '" stroke-width="2.5"/>'
    '<line x1="150" y1="84" x2="280" y2="84" stroke="' + ACC + '" stroke-width="3"/>'
    '<text x="168" y="122" ' + BIG + ' fill="' + YEL + '">area = displacement</text>'
    '<line x1="150" y1="84" x2="150" y2="192" stroke="' + GRN + '" stroke-width="2" stroke-dasharray="4 3"/>'
    '<text x="120" y="212" ' + TXT + ' fill="' + GRN + '">gradient = acceleration</text>'
    '</svg>',
    "Area under a velocity-time graph is displacement; gradient is acceleration.")

D[("physics", "circuits")] = (
    '<svg viewBox="0 0 400 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Series and parallel circuits compared">'
    '<text x="18" y="26" ' + BIG + '>Series</text>'
    '<line x1="40" y1="156" x2="40" y2="70" ' + S + '/><line x1="40" y1="70" x2="100" y2="70" ' + S + '/>'
    '<line x1="100" y1="70" x2="100" y2="96" ' + S + '/><line x1="100" y1="126" x2="100" y2="156" ' + S + '/>'
    '<rect x="90" y="96" width="20" height="30" fill="none" stroke="' + YEL + '" stroke-width="2"/>'
    '<line x1="100" y1="156" x2="40" y2="156" ' + S + '/>'
    '<rect x="26" y="101" width="26" height="22" fill="none" stroke="' + GRN + '" stroke-width="2"/>'
    '<text x="30" y="188" ' + TXT + ' fill="#9aa4bb">same current everywhere</text>'
    '<text x="228" y="26" ' + BIG + '>Parallel</text>'
    '<line x1="248" y1="70" x2="364" y2="70" ' + S + '/>'
    '<line x1="248" y1="156" x2="364" y2="156" ' + S + '/>'
    '<line x1="248" y1="70" x2="248" y2="98" ' + S + '/><line x1="248" y1="128" x2="248" y2="156" ' + S + '/>'
    '<rect x="238" y="98" width="20" height="30" fill="none" stroke="' + GRN + '" stroke-width="2"/>'
    '<line x1="292" y1="70" x2="292" y2="94" ' + S + '/><line x1="292" y1="124" x2="292" y2="156" ' + S + '/>'
    '<rect x="282" y="94" width="20" height="30" fill="none" stroke="' + YEL + '" stroke-width="2"/>'
    '<line x1="364" y1="70" x2="364" y2="156" ' + S + '/>'
    '<text x="232" y="188" ' + TXT + ' fill="#9aa4bb">same voltage across each branch</text>'
    '</svg>',
    "Series: current is the same everywhere. Parallel: voltage is the same across each branch.")

D[("physics", "wave-parameters")] = (
    '<svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sine wave with wavelength and amplitude labelled">'
    '<line x1="30" y1="120" x2="380" y2="120" ' + S + ' stroke="#5a6478"/>'
    '<path d="M40 120 Q70 38 100 120 Q130 202 160 120 Q190 38 220 120 Q250 202 280 120 Q310 38 340 120" fill="none" stroke="' + ACC + '" stroke-width="2.5"/>'
    '<line x1="100" y1="40" x2="220" y2="40" stroke="' + YEL + '" stroke-width="2"/>'
    '<text x="124" y="32" ' + TXT + ' fill="' + YEL + '">wavelength &#955;</text>'
    '<line x1="368" y1="120" x2="368" y2="60" stroke="' + GRN + '" stroke-width="2"/>'
    '<text x="286" y="204" ' + TXT + ' fill="' + GRN + '">amplitude</text>'
    '<text x="20" y="212" ' + BIG + ' fill="' + ACC + '">v = f &#955;</text>'
    '</svg>',
    "Wavelength is one full cycle; amplitude is the height from the centre line.")

D[("physics", "refraction")] = (
    '<svg viewBox="0 0 400 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Light ray refracting at a boundary and bending toward the normal">'
    '<line x1="20" y1="124" x2="380" y2="124" ' + S + ' stroke="' + GRN + '" stroke-width="2"/>'
    '<text x="322" y="116" ' + TXT + ' fill="' + GRN + '">boundary</text>'
    '<line x1="200" y1="22" x2="200" y2="218" ' + DASH + '/>'
    '<text x="206" y="38" ' + TXT + ' fill="#9aa4bb">normal</text>'
    '<line x1="82" y1="44" x2="200" y2="124" stroke="' + YEL + '" stroke-width="2.5"/>'
    '<line x1="200" y1="124" x2="268" y2="206" stroke="' + YEL + '" stroke-width="2.5"/>'
    '<text x="46" y="38" ' + TXT + ' fill="' + YEL + '">incident ray</text>'
    '<text x="248" y="202" ' + TXT + ' fill="' + YEL + '">refracted ray</text>'
    '<text x="212" y="100" ' + TXT + ' fill="' + ACC + '">slower medium</text>'
    '</svg>',
    "Entering a slower medium the ray bends toward the normal.")

D[("dm", "graphics")] = (
    '<svg viewBox="0 0 400 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Isometric cube beside orthographic front and plan views">'
    '<text x="16" y="24" ' + BIG + '>Isometric</text>'
    '<polygon points="60,150 130,185 130,115 60,80" fill="' + ACC + '" fill-opacity="0.15" stroke="' + ACC + '" stroke-width="2"/>'
    '<polygon points="130,185 200,150 200,80 130,115" fill="' + ACC + '" fill-opacity="0.25" stroke="' + ACC + '" stroke-width="2"/>'
    '<polygon points="60,80 130,115 200,80 130,45" fill="' + ACC + '" fill-opacity="0.35" stroke="' + ACC + '" stroke-width="2"/>'
    '<text x="250" y="24" ' + BIG + '>Orthographic</text>'
    '<rect x="250" y="60" width="92" height="52" fill="none" stroke="' + GRN + '" stroke-width="2"/>'
    '<text x="278" y="93" ' + TXT + ' fill="' + GRN + '">front</text>'
    '<rect x="250" y="128" width="92" height="52" fill="none" stroke="' + YEL + '" stroke-width="2"/>'
    '<text x="282" y="161" ' + TXT + ' fill="' + YEL + '">plan</text>'
    '</svg>',
    "Isometric shows 3D; orthographic shows separate flat views carrying the dimensions.")

applied = 0
for (subj, slug), (svg, cap) in D.items():
    f = C / (subj + ".json")
    d = json.loads(f.read_text(encoding="utf-8"))
    hit = False
    for t in d["topics"]:
        if t["slug"] == slug:
            t["diagram"] = svg.replace("\n", "")
            t["diagram_caption"] = cap
            hit = True
            applied += 1
            break
    if not hit:
        print("  MISS:", subj, slug)
    f.write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")

print("diagrams applied:", applied, "of", len(D))
