#!/usr/bin/env python3
"""Draw entry.png: a 1024x1024 newspaper front page summing up
Saturday 21 November 2026 world news. All facts were verified
against Reuters / AP / CNN / One Turn / Horizon on 21 Nov 2026.
Deterministic: no network, no random, no timestamps in the image.
Run: python3 draw.py  -> writes entry.png next to this file.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W = H = 1024
BASE = os.path.dirname(os.path.abspath(__file__))
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def f(path, size):
    return ImageFont.truetype(path, size)

PAPER = (253, 248, 238)
INK = (17, 17, 17)
RED = (185, 28, 28)
BLUE = (30, 58, 95)
DARK = (20, 28, 38)
GREY = (90, 90, 86)
LIGHT = (238, 232, 216)
GOLD = (176, 141, 26)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def para(x, y, text, font, max_w, leading, color=INK):
    for line in wrap(text, font, max_w):
        d.text((x, y), line, font=font, fill=color)
        y += leading
    return y

def headline(x, y, text, font, max_w, leading, color=INK):
    return para(x, y, text, font, max_w, leading, color)

def label(x, y, text, color=RED):
    d.text((x, y), text, font=f(SANS_B, 11), fill=color)
    return y + 16

def rule(x, y, w, color=INK, width=2):
    d.line([(x, y), (x + w, y)], fill=color, width=width)
    return y

# ---- header ----
d.rectangle([0, 0, W, 108], fill=DARK)
d.text((28, 14), "THE WORLD TODAY", font=f(SERIF_B, 52), fill=(253, 248, 238))
d.text((28, 74), "SATURDAY 21 NOVEMBER 2026", font=f(SANS_B, 16), fill=(255, 255, 255))
d.text((560, 78), "33 STORIES  •  7 REGIONS  •  MOOD: UNEASY", font=f(SANS_B, 13), fill=(255, 196, 0))
d.rectangle([0, 108, W, 112], fill=RED)
y = 122
d.text((28, y), "ONE DAY, ONE PAGE — THE WORLD IN A SINGLE IMAGE", font=f(SANS_B, 13), fill=RED)
y = 142
d.text((28, y), "S&P 500  6,910  -3.7%    Nasdaq  -5.28%    Nikkei  -5.06%    FTSE  -1.02%    Gold  $3,515  -4.6%    Brent  $89.95", font=f(SANS, 12), fill=INK)
rule(28, 166, 968, RED, 2)

# ---- hero row: Russia / Poland (left) + AI rout (right) ----
y = 178
label(28, y, "WAR IN EUROPE  •  KYIV  •  POLAND")
headline(28, 196, "Russia fires 400+ drones", f(SERIF_B, 30), 620, 34)
headline(28, 230, "and 110 missiles; two land", f(SERIF_B, 30), 620, 34)
headline(28, 264, "in NATO Poland", f(SERIF_B, 30), 620, 34)
para(28, 302, "At least 8 killed in Kyiv; bridges and rail stations hit. A later strike on Kryvyi Rih wounded about 20. Poland: two Russian missiles and a suspected drone came down in the south-east; PM Tusk called it a deliberate provocation. NATO called it a grave airspace violation and scrambled jets. No one was hurt in Poland.", f(SANS, 13), 620, 18)

# AI box
d.rectangle([672, 178, 996, 386], fill=DARK)
d.text((690, 190), "MARKETS  •  NEW YORK", font=f(SANS_B, 11), fill=(255, 196, 0))
d.text((690, 210), "THE AI ROUT", font=f(SERIF_B, 26), fill=(255, 255, 255))
para(690, 244, "S&P 500 fell 3.7% into correction; Dow also in correction. Nasdaq -5.28%, worst week since 2020.", f(SANS, 12), 288, 17, (235, 235, 235))
d.text((690, 312), "Nvidia  -14%    Anthropic  -8.5%", font=f(SANS_B, 13), fill=(255, 255, 255))
d.text((690, 334), "a day after its $2tn IPO debut", font=f(SANS, 11), fill=(200, 200, 200))
d.text((690, 356), "Chip stocks lost $2.3tn in a week.", font=f(SANS, 11), fill=(200, 200, 200))
rule(28, 392, 968, INK, 1)

# ---- middle row: 3 columns ----
y = 404
cols = [
    (28, 300, "CLIMATE  •  ANTALYA, TURKEY", "COP31 in overtime", "The UN summit missed its Friday deadline. A draft deal stripped out every mention of fossil fuels after objections from Saudi Arabia and other oil producers. A third draft was due Saturday morning; ~200 nations still split on finance for poorer countries.", RED),
    (352, 300, "JUSTICE  •  THE HAGUE", "ICJ: Myanmar guilty of genocide", "In a historic first, the World Court ruled 9-6 that Myanmar committed genocide against the Rohingya in 2017. About 10,000 killed; 700,000+ fled to Bangladesh. Myanmar must allow returns and pay reparations.", RED),
    (676, 300, "DISASTER  •  PERU", "M6.7 quake shakes Peru", "A magnitude 6.7-6.8 quake struck Junin in the Andes, felt in Lima, where residents ran into the streets. Depth 108-129 km. No deaths or major damage reported at first; no tsunami threat.", RED),
]
for x, w, lab, head, body, col in cols:
    label(x, y, lab, col)
    headline(x, y + 18, head, f(SERIF_B, 19), w, 22)
    para(x, y + 64, body, f(SANS, 12), w, 16)
rule(28, 566, 968, INK, 1)

# ---- second row: 3 columns ----
y = 578
cols2 = [
    (28, 300, "MIDDLE EAST  •  RIYADH", "3 Houthi missiles intercepted", "The Saudi-led coalition said it shot down three ballistic missiles aimed at Riyadh early Saturday, the third straight night of emergency alerts. Saudi strikes hit Hodeidah, Sanaa, Saada and Taiz in Yemen.", RED),
    (352, 300, "EUROPE  •  BRUSSELS", "UK-EU sign biggest post-Brexit deal", "PM Andy Burnham and EU leaders signed three deals: food and farm trade, linked carbon markets from Jan 2028, and a youth mobility scheme for up to 100,000 people aged 18-31 each side.", RED),
    (676, 300, "USA  •  CYBER", "FBI and USDA hacked", "The FBI's criminal database and the US Department of Agriculture were hacked, CNN reported, amid a week of US tech outages. Bayer agreed a $7.25bn Roundup settlement, approved by a US judge.", RED),
]
for x, w, lab, head, body, col in cols2:
    label(x, y, lab, col)
    headline(x, y + 18, head, f(SERIF_B, 18), w, 21)
    para(x, y + 62, body, f(SANS, 12), w, 16)
rule(28, 736, 968, INK, 1)

# ---- regions grid: 7 regions, 30+ stories ----
y = 748
d.text((28, y), "THE DAY BY REGION — 25 MORE STORIES, ALL DATED 21 NOVEMBER 2026", font=f(SANS_B, 13), fill=BLUE)
y += 24
regions = [
    ("NORTH AMERICA", "Trump defends Putin/Xi ties after Shenzhen; threatens tax on US firms building AI centres abroad. Palisades fire: man convicted; 12 killed in 2025."),
    ("LATIN AMERICA", "Peru quake (above). Salvadoran troops in Haiti lose soldiers to explosives. Argentina risk tops 1,000. Nigeria boat capsizes, at least 4 dead."),
    ("EUROPE", "Gen Z protests in 25 countries. Spain heads to 29 Nov election. Estonia closes Russia border crossings. Denmark expels Russian diplomat."),
    ("MIDDLE EAST", "Israeli strikes in Gaza; West Bank violence. Iran says it downed a US MQ-9 over Hormuz. Iraq: Basra power plant fire kills at least 4."),
    ("AFRICA", "Tanzania: Lissu convicted of sedition. South Africa: nearly 600 women killed in 3 months. Kenya starts onshore crude drilling in Turkana."),
    ("ASIA", "Nepal PM Shah to visit India. South Korea moves to impeach chief justice. India: 11 dead after adulterated alcohol. Indonesia fires: 7.1m acres."),
    ("SCIENCE & SPORT", "Pancreatic pill: tumours undetectable in 1 in 12. Anthropic claims AI proof of Riemann hypothesis, unverified. CERN ultra-rare decay. Alcaraz unbeaten."),
]
# two columns of region blocks, 4 left / 3 right, no duplicates
left = regions[:4]
right = regions[4:]
# layout: left column x=28 w=470, right x=526 w=470, stacked
yy = y
for name, txt in left:
    d.text((28, yy), name, font=f(SANS_B, 11), fill=RED)
    yy = para(28, yy + 15, txt, f(SANS, 11), 470, 14) + 6
yy2 = y
for name, txt in right:
    d.text((526, yy2), name, font=f(SANS_B, 11), fill=RED)
    yy2 = para(526, yy2 + 15, txt, f(SANS, 11), 470, 14) + 6

# footer
fy = 986
d.rectangle([0, fy, W, H], fill=DARK)
d.text((28, 994), "Sources: Reuters, AP, CNN, BBC, One Turn, Horizon  •  All stories reported 21 Nov 2026; ICJ ruling delivered 19 Nov, Myanmar response 20 Nov.", font=f(SANS, 10), fill=(220, 220, 220))
d.text((28, 1008), "THE WORLD TODAY  •  21 NOVEMBER 2026", font=f(SANS_B, 9), fill=(255, 196, 0))

out = os.path.join(BASE, "entry.png")
img.save(out, "PNG", optimize=True)
print(out, os.path.getsize(out), "bytes")
