import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="🗻 東京・富士山 2026",
    page_icon="🗻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────────────────────────────────────────
# DATA
# ──────────────────────────────────────────────────────────────────────────────

ITINERARY = [
    {
        "day": 1, "date": "07/03（五）", "title": "東京抵達",
        "location": "tokyo",
        "activities": [
            {"time": "抵達", "icon": "✈️", "name": "成田機場落地", "detail": "搭 Narita Express 進東京市區，約 60 分鐘"},
            {"time": "傍晚", "icon": "🏨", "name": "入住飯店，輕鬆晚餐", "detail": "整理行李，熟悉環境"},
            {"time": "晚上", "icon": "😴", "name": "早睡調時差", "detail": "明天起，精彩正式開始！"},
        ],
    },
    {
        "day": 2, "date": "07/04（六）", "title": "新宿 → 河口湖",
        "location": "kawaguchiko",
        "activities": [
            {"time": "上午", "icon": "🚃", "name": "富士回遊號出發", "detail": "新宿搭特急，約 1 小時 53 分直達河口湖"},
            {"time": "14:00", "icon": "🌸", "name": "大石公園", "detail": "湖邊漫步，遠眺富士山，7月薰衣草正盛開"},
            {"time": "15:30", "icon": "🚡", "name": "富士山全景纜車", "detail": "俯瞰河口湖與富士山全景，來回約 20 分鐘"},
            {"time": "16:30", "icon": "🍪", "name": "Fujiyama Cookie", "detail": "纜車站旁，富士山造型餅乾，¥180 起"},
            {"time": "晚上", "icon": "♨️", "name": "旅館溫泉", "detail": "早睡備戰！明天開始登山"},
        ],
    },
    {
        "day": 3, "date": "07/05（日）", "title": "登富士山 ↑",
        "location": "fuji",
        "activities": [
            {"time": "早上", "icon": "🚌", "name": "巴士前往五合目", "detail": "河口湖搭巴士，約 50 分鐘（吉田口五合目，海拔 2,390m）"},
            {"time": "14:00前", "icon": "🔒", "name": "通過登山閘門", "detail": "⚠️ 閘門 14:00 關閉，務必提前抵達！住山屋者另有安排"},
            {"time": "下午", "icon": "⛰️", "name": "吉田路線上山", "detail": "目標八合目，預計 5–7 小時（含休息）"},
            {"time": "傍晚", "icon": "🛖", "name": "入住簾岩館", "detail": "海拔 3,100m 山屋。充分休息，備戰凌晨攻頂"},
        ],
    },
    {
        "day": 4, "date": "07/06（一）", "title": "御來光攻頂 → 回河口湖",
        "location": "fuji",
        "activities": [
            {"time": "凌晨", "icon": "🌅", "name": "攻頂・御來光", "detail": "從山屋出發，登頂日出（海拔 3,776m）——此生難忘"},
            {"time": "早上", "icon": "🌋", "name": "火山口環繞", "detail": "頂峰環走，四周壯麗雲海"},
            {"time": "上午", "icon": "⬇️", "name": "下山返回五合目", "detail": "約 3–4 小時，搭巴士回河口湖"},
            {"time": "13:00", "icon": "🍵", "name": "忍野八海", "detail": "八個清澈湧泉群，世界遺產，傳統村落，食蕎麥麵"},
            {"time": "17:00", "icon": "🗻", "name": "富士吉田本町通", "detail": "直街盡頭就是富士山，黃昏光線最美"},
            {"time": "晚上", "icon": "♨️", "name": "旅館溫泉休息", "detail": "犒勞辛苦的雙腳，好好泡一下"},
        ],
    },
    {
        "day": 5, "date": "07/07（二）", "title": "回東京 × 下北澤",
        "location": "tokyo",
        "activities": [
            {"time": "上午", "icon": "🚃", "name": "富士回遊號返新宿", "detail": "入住東京飯店，放行李"},
            {"time": "14:00", "icon": "🛍️", "name": "Bonus Track", "detail": "獨立商店街，咖啡館、發酵食品店、藝廊，有戶外座位"},
            {"time": "15:30", "icon": "📖", "name": "B&B（Book & Beer）", "detail": "Bonus Track 2F，邊喝啤酒邊看書，超放鬆"},
            {"time": "16:30", "icon": "🎸", "name": "Village Vanguard", "detail": "亞文化雜貨聖地，奇奇怪怪的東西都有"},
            {"time": "17:30", "icon": "📚", "name": "TSUTAYA 下北澤", "detail": "有品味的選書蔦屋書店，附設咖啡"},
            {"time": "晚上", "icon": "🍶", "name": "下北澤居酒屋晚餐", "detail": "享受本町獨特文青氛圍"},
        ],
    },
    {
        "day": 6, "date": "07/08（三）", "title": "清澄白河咖啡聚落",
        "location": "tokyo",
        "activities": [
            {"time": "10:00", "icon": "☕", "name": "ARiSE Coffee Roasters", "detail": "在地烘豆師，手沖依當日豆單推薦，東南亞氛圍"},
            {"time": "11:00", "icon": "☕", "name": "Blue Bottle Coffee 旗艦店", "detail": "日本第一家，老倉庫改建，挑高空間，必朝聖"},
            {"time": "13:00", "icon": "🎨", "name": "東京都現代美術館（MOT）", "detail": "步行約 10 分鐘，展覽品質高，值得半天"},
            {"time": "15:00+", "icon": "🚶", "name": "清澄白河周邊漫步", "detail": "這裡咖啡館一間接一間，慢慢探索"},
            {"time": "晚上", "icon": "🍽️", "name": "自由行程", "detail": "可前往上野、秋葉原或銀座晚餐"},
        ],
    },
    {
        "day": 7, "date": "07/09（四）", "title": "返台",
        "location": "tokyo",
        "activities": [
            {"time": "上午", "icon": "🛍️", "name": "退房 + 最後購物", "detail": "別忘了伴手禮！藥妝、零食、文具"},
            {"time": "出發", "icon": "🚃", "name": "前往成田機場", "detail": "成田特快或利木津巴士，建議提前 2 小時"},
            {"time": "✈️", "icon": "🛫", "name": "成田 → 台北桃園", "detail": "一路平安，下次見！"},
        ],
    },
]

EXPERIENCES = [
    {"icon": "🌅", "title": "御來光", "desc": "凌晨攻頂，在海拔 3,776m 親眼見證日出"},
    {"icon": "🌸", "title": "薰衣草海", "desc": "大石公園 7 月盛開，富士山為背景"},
    {"icon": "♨️", "title": "富士溫泉", "desc": "河口湖旅館，泡湯遠眺富士山影"},
    {"icon": "☕", "title": "精品咖啡", "desc": "清澄白河，Tokyo 精品咖啡聖地"},
    {"icon": "📚", "title": "下北澤文化", "desc": "古著、書店、音樂、居酒屋，文青天堂"},
    {"icon": "🍵", "title": "忍野八海", "desc": "世界遺產湧泉群，傳統村落風情"},
]

WEATHER = [
    {"loc": "東京市區", "alt": "0 m", "temp": "25–33°C", "note": "梅雨尾聲，午後陣雨，體感炎熱"},
    {"loc": "河口湖", "alt": "900 m", "temp": "17–28°C", "note": "比東京涼 5–8°C，早晚需薄外套"},
    {"loc": "五合目", "alt": "2,390 m", "temp": "5–12°C", "note": "常年有雲，午後雷雨頻率高"},
    {"loc": "八合目（山屋）", "alt": "3,100 m", "temp": "1–7°C", "note": "強風常見，風速可達 20m/s+"},
    {"loc": "山頂・劍峰", "alt": "3,776 m", "temp": "-3–6°C", "note": "接近 0°C，冬季裝備必備"},
]

FUJI_STATIONS = [
    {"name": "五合目（出發）", "alt": 2390, "note": "吉田口，巴士抵達", "summit": False},
    {"name": "六合目", "alt": 2390, "note": "安全指導中心", "summit": False},
    {"name": "七合目", "alt": 2700, "note": "花小屋（花子館）", "summit": False},
    {"name": "八合目 ⛺ 山屋", "alt": 3100, "note": "簾岩館，住宿這裡", "summit": False},
    {"name": "九合目", "alt": 3400, "note": "鳥居", "summit": False},
    {"name": "山頂・劍峰 🌅", "alt": 3776, "note": "御來光！", "summit": True},
]

CHECKLISTS = {
    "🏨 住宿預訂": [
        "東京飯店（7/3 入住）",
        "東京飯店（7/7、7/8 入住）",
        "河口湖旅館（7/4、7/6）—— 建議選有溫泉",
        "富士山山屋：簾岩館（7/5）—— 越早越好！",
    ],
    "🎫 票券交通": [
        "富士山吉田路線線上通行預約（每人 ¥4,000）",
        "富士回遊號特急券（新宿↔河口湖，建議提前）",
        "成田機場交通（Narita Express 或利木津巴士）",
        "日本 SIM 卡或 Wi-Fi 分享器",
    ],
    "💊 醫藥準備": [
        "高山症藥（乙醯唑胺，請先諮詢醫師，出發前 2 天服用）",
        "止痛藥、腸胃藥",
        "暈車藥（富士山巴士山路蜿蜒）",
    ],
    "🥾 登山裝備": [
        "防滑防水登山鞋",
        "防風防水外套（冬季等級，山頂接近 0°C）",
        "頭燈 + 備用電池（夜間攻頂必備）",
        "雨衣（午後雷陣雨機率高）",
        "飲用水 2L 以上",
        "行動糧食（能量棒、巧克力）",
        "防沙腳套（下山砂地用）",
        "保暖手套 + 帽子",
        "防曬乳 SPF50+",
        "登山杖 × 2",
    ],
}

LOC_COLORS = {
    "tokyo": {"badge": "#DD792E", "light": "#FFF4EE", "border": "#DD792E"},
    "kawaguchiko": {"badge": "#3C828F", "light": "#EEF8FA", "border": "#3C828F"},
    "fuji": {"badge": "#438B48", "light": "#EDF7EE", "border": "#438B48"},
}

# ──────────────────────────────────────────────────────────────────────────────
# CSS
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Kiwi+Maru:wght@300;400;500&family=Noto+Sans+TC:wght@300;400;500;700&family=Noto+Serif+TC:wght@400;600&display=swap');

*, *::before, *::after { box-sizing: border-box; }

.stApp { background: #F5F0E8 !important; }
[data-testid="stHeader"]    { display: none !important; }
[data-testid="stToolbar"]   { display: none !important; }
footer                      { display: none !important; }
.stDeployButton             { display: none !important; }

.block-container {
    padding-top: 0.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1100px !important;
}

/* ── Section header ─────────────────────────── */
.sec-title {
    font-family: 'Kiwi Maru', serif;
    font-size: 1.6rem;
    color: #1e2e1e;
    text-align: center;
    margin: 52px 0 6px;
}
.sec-title::after {
    content: '';
    display: block;
    width: 56px;
    height: 4px;
    background: linear-gradient(90deg, #438B48, #DD792E);
    margin: 8px auto 0;
    border-radius: 2px;
}
.sec-sub {
    text-align: center;
    color: #78A95B;
    font-size: 0.82rem;
    letter-spacing: 0.12em;
    margin: 0 0 28px;
    font-family: 'Noto Sans TC', sans-serif;
}

/* ── Stat cards ─────────────────────────────── */
.stat-card {
    background: white;
    border-radius: 18px;
    padding: 28px 16px 22px;
    text-align: center;
    box-shadow: 0 4px 24px rgba(67,139,72,.10);
    border-top: 5px solid #438B48;
    transition: transform .2s;
    height: 100%;
}
.stat-card:hover { transform: translateY(-5px); }
.stat-icon  { font-size: 2.4rem; margin-bottom: 10px; }
.stat-num   { font-family: 'Noto Serif TC', serif; font-size: 2rem; font-weight: 700; color: #1e2e1e; line-height: 1; }
.stat-label { font-size: .82rem; color: #78A95B; margin-top: 5px; font-family: 'Noto Sans TC', sans-serif; }

/* ── Day accordion ──────────────────────────── */
.day-wrap { margin-bottom: 10px; }
details.day-card {
    background: white;
    border-radius: 16px;
    box-shadow: 0 2px 14px rgba(67,139,72,.08);
    overflow: hidden;
}
details.day-card summary {
    list-style: none;
    cursor: pointer;
    padding: 16px 22px;
    display: flex;
    align-items: center;
    gap: 14px;
    user-select: none;
    transition: background .15s;
}
details.day-card summary::-webkit-details-marker { display: none; }
details.day-card[open] > summary { border-bottom: 1px dashed #E8E2DA; }

.day-badge {
    font-family: 'Kiwi Maru', serif;
    font-size: .82rem;
    color: white;
    padding: 4px 13px;
    border-radius: 20px;
    white-space: nowrap;
    font-weight: 500;
    letter-spacing: .04em;
}
.day-date  { font-size: .78rem; color: #999; white-space: nowrap; font-family: 'Noto Sans TC', sans-serif; }
.day-title { font-size: 1rem; font-weight: 600; color: #1e2e1e; flex: 1; font-family: 'Noto Sans TC', sans-serif; }
.day-caret { font-size: 1rem; color: #aaa; transition: transform .25s; flex-shrink: 0; }
details.day-card[open] .day-caret { transform: rotate(90deg); }

.day-body {
    padding: 8px 22px 20px 56px;
    border-left: 4px solid transparent;
    margin: 4px 16px 0 36px;
    border-radius: 0 0 8px 8px;
}
.activity {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 9px 0;
    border-bottom: 1px solid #F5F1EC;
}
.activity:last-child { border-bottom: none; }
.act-time  { font-size: .72rem; color: #aaa; min-width: 46px; padding-top: 3px; font-family: 'Noto Sans TC', sans-serif; }
.act-icon  { font-size: 1.1rem; flex-shrink: 0; }
.act-name  { font-size: .93rem; font-weight: 600; color: #1e2e1e; margin-bottom: 2px; font-family: 'Noto Sans TC', sans-serif; }
.act-det   { font-size: .80rem; color: #5E7960; line-height: 1.55; font-family: 'Noto Sans TC', sans-serif; }

/* ── Experience cards ───────────────────────── */
.exp-card {
    background: white;
    border-radius: 16px;
    padding: 26px 18px 20px;
    text-align: center;
    box-shadow: 0 4px 18px rgba(67,139,72,.09);
    border-bottom: 4px solid #FFDF76;
    transition: transform .2s;
    height: 100%;
}
.exp-card:hover { transform: translateY(-5px); }
.exp-icon  { font-size: 2.4rem; margin-bottom: 10px; }
.exp-title { font-family: 'Noto Serif TC', serif; font-size: 1rem; font-weight: 600; color: #1e2e1e; margin-bottom: 6px; }
.exp-desc  { font-size: .80rem; color: #78A95B; line-height: 1.55; font-family: 'Noto Sans TC', sans-serif; }

/* ── Weather table ──────────────────────────── */
.wtable {
    width: 100%; border-collapse: collapse;
    border-radius: 16px; overflow: hidden;
    box-shadow: 0 4px 20px rgba(67,139,72,.08);
    font-family: 'Noto Sans TC', sans-serif; font-size: .88rem;
}
.wtable thead tr { background: #438B48; color: white; }
.wtable th { padding: 13px 16px; text-align: left; letter-spacing: .04em; }
.wtable tbody tr:nth-child(odd)  { background: white; }
.wtable tbody tr:nth-child(even) { background: #F5FAF5; }
.wtable td { padding: 11px 16px; border-bottom: 1px solid #EDF2ED; color: #2a3a2a; }
.wtable td:first-child { font-weight: 700; color: #438B48; }
.tbadge {
    background: linear-gradient(135deg,#3C828F,#5BA5B0);
    color: white; padding: 3px 10px;
    border-radius: 12px; font-size: .80rem; font-weight: 700;
}

/* ── Fuji elevation chart ───────────────────── */
.fuji-chart { background: white; border-radius: 16px; padding: 28px 24px; box-shadow: 0 4px 20px rgba(67,139,72,.08); }
.frow { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
.fstation { font-size: .85rem; font-weight: 600; color: #1e2e1e; min-width: 150px; text-align: right; font-family: 'Noto Sans TC', sans-serif; }
.fbar-bg { flex: 1; background: #EDF0ED; border-radius: 8px; height: 34px; overflow: hidden; }
.fbar {
    height: 100%; border-radius: 8px;
    background: linear-gradient(90deg,#78A95B,#438B48);
    display: flex; align-items: center; padding-left: 10px;
}
.fbar.summit { background: linear-gradient(90deg,#DD792E,#C96820); }
.fbar-label { font-size: .78rem; color: white; font-weight: 700; white-space: nowrap; font-family: 'Noto Sans TC', sans-serif; }
.fnote { font-size: .76rem; color: #78A95B; min-width: 150px; font-family: 'Noto Sans TC', sans-serif; }

/* ── Info / warning boxes ───────────────────── */
.info-box {
    background: #EAF5EA; border-left: 4px solid #438B48;
    border-radius: 0 12px 12px 0; padding: 13px 18px;
    margin: 14px 0; font-size: .86rem; color: #1a3a1a;
    font-family: 'Noto Sans TC', sans-serif;
}
.warn-box {
    background: #FFF8ED; border-left: 4px solid #DD792E;
    border-radius: 0 12px 12px 0; padding: 13px 18px;
    margin: 14px 0; font-size: .86rem; color: #5E3A10;
    font-family: 'Noto Sans TC', sans-serif;
}
.warn-box strong, .info-box strong { font-weight: 700; }

/* ── Checklist section ──────────────────────── */
.cl-header {
    font-family: 'Noto Serif TC', serif;
    font-size: 1rem; color: white;
    background: #438B48; padding: 10px 20px;
    border-radius: 12px 12px 0 0;
    margin-bottom: 0; font-weight: 600;
}
.cl-box {
    background: white;
    border-radius: 0 0 12px 12px;
    padding: 16px 20px 12px;
    box-shadow: 0 4px 16px rgba(67,139,72,.08);
    margin-bottom: 20px;
}

/* Streamlit checkbox tweak */
[data-testid="stCheckbox"] label {
    font-family: 'Noto Sans TC', sans-serif !important;
    font-size: .88rem !important;
    color: #000000 !important;
}

/* ── Route strip ────────────────────────────── */
.route-strip {
    background: white; border-radius: 20px;
    box-shadow: 0 4px 20px rgba(67,139,72,.08);
    padding: 24px 32px; margin-bottom: 20px;
    display: flex; align-items: center; justify-content: center; gap: 0;
}
.rstop { text-align: center; }
.rdot {
    width: 68px; height: 68px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.8rem; margin: 0 auto 8px;
    box-shadow: 0 4px 14px rgba(0,0,0,.12);
}
.rdot-tokyo  { background: linear-gradient(135deg,#DD792E,#E8974A); }
.rdot-lake   { background: linear-gradient(135deg,#3C828F,#5BA5B0); }
.rdot-fuji   { background: linear-gradient(135deg,#438B48,#5A9E5A); }
.rname   { font-weight: 700; color: #1e2e1e; font-size: .95rem; margin-bottom: 3px; font-family: 'Noto Sans TC', sans-serif; }
.rnights { font-size: .72rem; color: #78A95B; background: #EAF5EA; padding: 2px 9px; border-radius: 10px; display: inline-block; font-family: 'Noto Sans TC', sans-serif; }
.rarrow {
    flex: 1; min-width: 80px;
    display: flex; flex-direction: column; align-items: center; padding: 0 8px;
}
.rline {
    width: 100%; height: 2px;
    background: repeating-linear-gradient(90deg,#78A95B 0,#78A95B 7px,transparent 7px,transparent 13px);
    position: relative; margin-bottom: 4px;
}
.rline::after { content:'▶'; position:absolute; right:-7px; top:-9px; color:#78A95B; font-size:.75rem; }
.rtrans { font-size: .68rem; color: #5E7960; text-align: center; white-space: nowrap; font-family: 'Noto Sans TC', sans-serif; }

/* ── Footer ─────────────────────────────────── */
.page-footer {
    text-align: center; padding: 36px 20px;
    color: #78A95B; font-size: .80rem;
    border-top: 2px dashed #C8DCC8; margin-top: 60px;
    font-family: 'Noto Sans TC', sans-serif;
}
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# HELPERS
# ──────────────────────────────────────────────────────────────────────────────

def activities_html(acts):
    rows = ""
    for a in acts:
        rows += (
            f'<div class="activity">'
            f'<span class="act-time">{a["time"]}</span>'
            f'<span class="act-icon">{a["icon"]}</span>'
            f'<div><div class="act-name">{a["name"]}</div>'
            f'<div class="act-det">{a["detail"]}</div></div>'
            f'</div>'
        )
    return rows


def day_card_html(d):
    c = LOC_COLORS[d["location"]]
    badge_style = f"background:{c['badge']}"
    body_style  = f"border-left:4px solid {c['border']}"
    acts = activities_html(d["activities"])
    open_attr = "open" if d["day"] == 1 else ""
    return (
        f'<div class="day-wrap">'
        f'<details class="day-card" {open_attr}>'
        f'<summary>'
        f'<span class="day-badge" style="{badge_style}">Day {d["day"]}</span>'
        f'<span class="day-date">{d["date"]}</span>'
        f'<span class="day-title">{d["title"]}</span>'
        f'<span class="day-caret">&#9658;</span>'
        f'</summary>'
        f'<div class="day-body" style="{body_style}">{acts}</div>'
        f'</details></div>'
    )


def weather_table_html():
    rows = ""
    for w in WEATHER:
        rows += (
            f'<tr><td>{w["loc"]}</td><td>{w["alt"]}</td>'
            f'<td><span class="tbadge">{w["temp"]}</span></td>'
            f'<td>{w["note"]}</td></tr>'
        )
    return (
        f'<table class="wtable">'
        f'<thead><tr><th>地點</th><th>海拔</th><th>7月氣溫</th><th>注意事項</th></tr></thead>'
        f'<tbody>{rows}</tbody></table>'
    )


def fuji_chart_html():
    max_alt = 3776
    rows = ""
    for s in FUJI_STATIONS:
        pct = s["alt"] / max_alt * 100
        bar_cls = "fbar summit" if s["summit"] else "fbar"
        rows += (
            f'<div class="frow">'
            f'<span class="fstation">{s["name"]}</span>'
            f'<div class="fbar-bg">'
            f'<div class="{bar_cls}" style="width:{pct:.1f}%">'
            f'<span class="fbar-label">{s["alt"]:,} m</span>'
            f'</div></div>'
            f'<span class="fnote">{s["note"]}</span>'
            f'</div>'
        )
    return f'<div class="fuji-chart">{rows}</div>'


# ──────────────────────────────────────────────────────────────────────────────
# HERO
# ──────────────────────────────────────────────────────────────────────────────

HERO_HTML = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Kiwi+Maru:wght@400;500&family=Noto+Sans+TC:wght@400;600&family=Noto+Serif+TC:wght@400;600&display=swap" rel="stylesheet">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { background:transparent; overflow:hidden; }
.hero {
  position: relative;
  width: 100%;
  height: 300px;
  background: linear-gradient(180deg, #10283a 0%, #1e4a5a 30%, #3C828F 65%, #5BAAB5 85%, #4A9E55 100%);
  border-radius: 16px;
  overflow: hidden;
}
/* Stars */
.star { position:absolute; border-radius:50%; background:white; }
/* Moon */
.moon { position:absolute; top:28px; right:110px; width:34px; height:34px; border-radius:50%; background:#FFFBE6; opacity:.88; }
.moon-cut { position:absolute; top:23px; right:97px; width:30px; height:30px; border-radius:50%; background:#2a5a6a; }
/* Clouds */
.cloud { position:absolute; border-radius:50%; background:white; }
/* Mt Fuji */
.fuji {
  position: absolute;
  bottom: 55px; right: 5%;
  width: 520px; height: 260px;
  background: linear-gradient(180deg, #E8E8E8 0%, #C8B8A8 22%, #A09080 55%, #806050 80%, #6A5040 100%);
  clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
}
.snow {
  position: absolute;
  bottom: 258px; right: calc(5% + 130px);
  width: 260px; height: 110px;
  background: rgba(255,255,255,.95);
  clip-path: polygon(50% 0%, 5% 100%, 95% 100%);
}
.snow-wisp1 {
  position: absolute;
  bottom: 248px; right: calc(5% + 105px);
  width: 120px; height: 60px;
  background: rgba(255,255,255,.45);
  clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
}
.snow-wisp2 {
  position: absolute;
  bottom: 252px; right: calc(5% + 235px);
  width: 100px; height: 55px;
  background: rgba(255,255,255,.38);
  clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
}
/* Green hills */
.hill-base  { position:absolute; bottom:0; left:0; right:0; height:65px; background:#316635; }
.hill-left  { position:absolute; bottom:25px; left:-60px; width:480px; height:110px; background:linear-gradient(180deg,#4A9E55,#3A7A40); border-radius:50% 50% 0 0; }
.hill-right { position:absolute; bottom:28px; right:-40px; width:360px; height:95px; background:linear-gradient(180deg,#438B48,#316635); border-radius:50% 50% 0 0; }
/* Trees */
.tree { position:absolute; width:0; height:0; border-left:10px solid transparent; border-right:10px solid transparent; }
/* Lake */
.lake { position:absolute; border-radius:50%; background:#3C828F; opacity:.3; }
/* Text box */
.textbox {
  position: absolute;
  top: 50%; left: 5%;
  transform: translateY(-50%);
  background: rgba(245,240,232,.90);
  border-radius: 16px;
  padding: 20px 28px;
  border-left: 5px solid #DD792E;
  max-width: 340px;
  backdrop-filter: blur(8px);
}
.label  { font-family:'Noto Sans TC',sans-serif; font-size:.72rem; color:#78A95B; letter-spacing:.14em; margin-bottom:4px; }
.title  { font-family:'Kiwi Maru',serif; font-size:2.2rem; color:#1e2e1e; line-height:1.15; margin-bottom:4px; }
.sub    { font-family:'Noto Serif TC',serif; font-size:.9rem; color:#438B48; font-weight:600; letter-spacing:.06em; margin-bottom:10px; }
.people { font-family:'Noto Sans TC',sans-serif; font-size:.82rem; color:#5E7960; margin-bottom:6px; }
.dates  { font-family:'Noto Serif TC',serif; font-size:.95rem; color:#DD792E; font-weight:700; }
</style>
</head>
<body>
<div class="hero">
  <!-- Stars -->
  <div class="star" style="top:22px;left:75px;width:4px;height:4px;opacity:.55;"></div>
  <div class="star" style="top:12px;left:168px;width:3px;height:3px;opacity:.45;"></div>
  <div class="star" style="top:38px;right:280px;width:4px;height:4px;opacity:.60;"></div>
  <div class="star" style="top:16px;right:190px;width:3px;height:3px;opacity:.50;"></div>
  <div class="star" style="top:50px;left:340px;width:2px;height:2px;opacity:.35;"></div>

  <!-- Moon -->
  <div class="moon"></div>
  <div class="moon-cut"></div>

  <!-- Clouds left -->
  <div class="cloud" style="top:65px;left:50px;width:185px;height:52px;opacity:.75;"></div>
  <div class="cloud" style="top:54px;left:82px;width:148px;height:46px;opacity:.80;"></div>
  <div class="cloud" style="top:72px;left:35px;width:100px;height:38px;opacity:.70;"></div>

  <!-- Cloud right -->
  <div class="cloud" style="top:60px;right:330px;width:130px;height:40px;opacity:.52;"></div>
  <div class="cloud" style="top:50px;right:348px;width:100px;height:34px;opacity:.48;"></div>

  <!-- Mt Fuji -->
  <div class="fuji"></div>
  <div class="snow"></div>
  <div class="snow-wisp1"></div>
  <div class="snow-wisp2"></div>

  <!-- Hills and base -->
  <div class="hill-left"></div>
  <div class="hill-right"></div>
  <div class="hill-base"></div>

  <!-- Trees left -->
  <div class="tree" style="bottom:63px;left:42px;border-bottom:28px solid #2A6030;"></div>
  <div class="tree" style="bottom:63px;left:62px;border-bottom:32px solid #2A6030;"></div>
  <div class="tree" style="bottom:63px;left:84px;border-bottom:26px solid #2A6030;"></div>
  <div class="tree" style="bottom:63px;left:104px;border-bottom:30px solid #2A6030;"></div>

  <!-- Trees right -->
  <div class="tree" style="bottom:63px;right:50px;border-bottom:28px solid #2A6030;"></div>
  <div class="tree" style="bottom:63px;right:30px;border-bottom:32px solid #2A6030;"></div>
  <div class="tree" style="bottom:63px;right:70px;border-bottom:26px solid #2A6030;"></div>

  <!-- Lake -->
  <div class="lake" style="bottom:68px;left:200px;width:130px;height:16px;"></div>

  <!-- Lavender dots -->
  <div style="position:absolute;bottom:66px;left:155px;display:flex;gap:5px;">
    <div style="width:7px;height:10px;border-radius:50% 50% 0 0;background:#9B7BB8;opacity:.6;"></div>
    <div style="width:7px;height:12px;border-radius:50% 50% 0 0;background:#B08FCC;opacity:.6;"></div>
    <div style="width:7px;height:9px;border-radius:50% 50% 0 0;background:#9B7BB8;opacity:.6;"></div>
    <div style="width:7px;height:11px;border-radius:50% 50% 0 0;background:#B08FCC;opacity:.6;"></div>
    <div style="width:7px;height:10px;border-radius:50% 50% 0 0;background:#9B7BB8;opacity:.6;"></div>
  </div>

  <!-- Text overlay -->
  <div class="textbox">
    <p class="label">TRAVEL PLAN 2026</p>
    <h1 class="title">東京・富士山</h1>
    <p class="sub">七天六夜小旅行</p>
    <p class="people">Jack &nbsp;×&nbsp; Mike &nbsp;×&nbsp; Apple</p>
    <p class="dates">2026.07.03 → 07.09</p>
  </div>
</div>
</body>
</html>
"""

components.html(HERO_HTML, height=316, scrolling=False)


# ──────────────────────────────────────────────────────────────────────────────
# OVERVIEW STATS
# ──────────────────────────────────────────────────────────────────────────────

stats = [
    ("🗓", "7天6夜", "旅行天數"),
    ("🗺", "3 個地點", "東京・河口湖・富士山"),
    ("👥", "3 人同行", "Jack・Mike・Apple"),
]
cols = st.columns(3, gap="medium")
for col, (icon, num, label) in zip(cols, stats):
    with col:
        st.markdown(f"""
<div class="stat-card">
  <div class="stat-icon">{icon}</div>
  <div class="stat-num">{num}</div>
  <div class="stat-label">{label}</div>
</div>""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# ROUTE VISUALIZATION
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<p class="sec-title">旅行路線</p>
<p class="sec-sub">ROUTE OVERVIEW</p>

<div class="route-strip">
  <div class="rstop">
    <div class="rdot rdot-tokyo">🗼</div>
    <div class="rname">東京</div>
    <div class="rnights">3 晚</div>
  </div>

  <div class="rarrow">
    <div class="rline"></div>
    <div class="rtrans">🚃 富士回遊號<br>1h 53m</div>
  </div>

  <div class="rstop">
    <div class="rdot rdot-lake">🏞</div>
    <div class="rname">河口湖</div>
    <div class="rnights">2 晚</div>
  </div>

  <div class="rarrow">
    <div class="rline"></div>
    <div class="rtrans">🚌 巴士<br>50 min</div>
  </div>

  <div class="rstop">
    <div class="rdot rdot-fuji">🗻</div>
    <div class="rname">富士山</div>
    <div class="rnights">1 晚 ⛺</div>
  </div>
</div>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# DAILY ITINERARY
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<p class="sec-title">每日行程</p>
<p class="sec-sub">DAILY ITINERARY — 點擊可展開</p>
""", unsafe_allow_html=True)

for d in ITINERARY:
    st.markdown(day_card_html(d), unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# KEY EXPERIENCES
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<p class="sec-title">重點體驗</p>
<p class="sec-sub">HIGHLIGHTS</p>
""", unsafe_allow_html=True)

for row_start in range(0, len(EXPERIENCES), 3):
    row = EXPERIENCES[row_start:row_start + 3]
    cols = st.columns(len(row), gap="medium")
    for col, exp in zip(cols, row):
        with col:
            st.markdown(f"""
<div class="exp-card">
  <div class="exp-icon">{exp['icon']}</div>
  <div class="exp-title">{exp['title']}</div>
  <div class="exp-desc">{exp['desc']}</div>
</div>""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# WEATHER
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<p class="sec-title">天氣與溫度參考</p>
<p class="sec-sub">WEATHER REFERENCE</p>
""", unsafe_allow_html=True)

st.markdown(weather_table_html(), unsafe_allow_html=True)

st.markdown("""
<div class="warn-box">
  ⚠️ <strong>重要：</strong>山腳至山頂溫差可達 20–30°C，請採洋蔥式穿搭。
  攻頂前務必查詢 <strong>tenkura 富士山天氣預報</strong>，確認當日風速與能見度。
</div>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# FUJI ROUTE
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<p class="sec-title">富士山登山資訊</p>
<p class="sec-sub">吉田路線（YOSHIDA TRAIL）</p>
""", unsafe_allow_html=True)

st.markdown(fuji_chart_html(), unsafe_allow_html=True)

st.markdown("""
<div style="margin-top:16px;">
<div class="info-box">
  📋 <strong>關鍵規定</strong><br>
  ・登山閘門：14:00 關閉（03:00 重開）｜住山屋者另開放<br>
  ・每日入山上限：<strong>4,000 人</strong>，需提前線上預約<br>
  ・通行費：<strong>每人 ¥4,000</strong>（線上付款）<br>
  ・山屋預約：簾岩館，越早越好！
</div>
<div class="warn-box">
  ⚠️ <strong>高山症提醒：</strong>五合目抵達後先休息 30 分鐘再出發。
  如有不適（頭痛、噁心、呼吸急促），請立即下山，不要強行攻頂。
</div>
</div>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# CHECKLISTS
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<p class="sec-title">行前準備清單</p>
<p class="sec-sub">PRE-TRIP CHECKLIST</p>
""", unsafe_allow_html=True)

checklist_colors = {
    "🏨 住宿預訂": "#3C828F",
    "🎫 票券交通": "#DD792E",
    "💊 醫藥準備": "#BD513A",
    "🥾 登山裝備": "#438B48",
}

for title, items in CHECKLISTS.items():
    color = checklist_colors.get(title, "#438B48")
    st.markdown(
        f'<div class="cl-header" style="background:{color};">{title}</div>'
        f'<div class="cl-box">',
        unsafe_allow_html=True,
    )

    if title == "🥾 登山裝備":
        left_items = items[: len(items) // 2 + len(items) % 2]
        right_items = items[len(items) // 2 + len(items) % 2 :]
        c1, c2 = st.columns(2)
        with c1:
            for i, item in enumerate(left_items):
                st.checkbox(item, key=f"check_{title}_{i}")
        with c2:
            for i, item in enumerate(right_items):
                st.checkbox(item, key=f"check_{title}_r{i}")
    else:
        for i, item in enumerate(items):
            st.checkbox(item, key=f"check_{title}_{i}")

    st.markdown("</div>", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# FOOTER
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<div class="page-footer">
  🗻 東京・富士山 2026 ｜ Jack × Mike × Apple<br>
  <span style="opacity:.6;">祝一路順風，御來光見！</span>
</div>
""", unsafe_allow_html=True)
