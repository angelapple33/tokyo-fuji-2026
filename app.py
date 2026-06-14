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
            {"time": "抵達", "icon": "✈️", "name": "成田機場落地", "detail": "方案A：N'EX→新宿→JR総武線→錦糸町（約75分，¥3,070）｜方案B：京成本線→押上→錦糸町（約80分，¥1,050）"},
            {"time": "傍晚", "icon": "🏨", "name": "入住錦糸町飯店", "detail": "KINSHICHO Tokyo Holiday Hotel，整理行李，熟悉環境"},
            {"time": "晚上", "icon": "🍣", "name": "錦糸町周邊晚餐", "detail": "車站周邊有超市、居酒屋，輕鬆覓食"},
            {"time": "夜", "icon": "😴", "name": "早睡調時差", "detail": "明天一早就搭富士回遊號出發！"},
        ],
    },
    {
        "day": 2, "date": "07/04（六）", "title": "錦糸町 → 富士吉田",
        "location": "kawaguchiko",
        "activities": [
            {"time": "上午", "icon": "🚆", "name": "富士回遊號直達出發", "detail": "從錦糸町站直搭富士回遊號 → 富士急高原樂園站（約2小時15分），完全不需先去新宿！"},
            {"time": "抵達", "icon": "🏨", "name": "Mystays 放行李", "detail": "步行5分鐘抵達 Hotel Mystays，寄放行李"},
            {"time": "上午", "icon": "⛩", "name": "新倉山淺間公園（忠靈塔）", "detail": "五重塔＋富士山經典構圖，需爬約400階，上午雲少最美"},
            {"time": "13:00", "icon": "🍜", "name": "吉田烏龍麵午餐", "detail": "富士吉田本町通，名物「吉田烏龍麵」，湯頭偏甜辣，麵條超粗"},
            {"time": "14:00", "icon": "🌸", "name": "大石公園", "detail": "湖邊漫步，遠眺富士山，7月薰衣草季盛開"},
            {"time": "15:30", "icon": "🚡", "name": "富士山全景纜車（天上山公園）", "detail": "俯瞰河口湖＋富士山全景，來回約20分鐘"},
            {"time": "16:30", "icon": "🍪", "name": "Fujiyama Cookie", "detail": "纜車站旁，富士山造型餅乾，¥180起（週二休）"},
            {"time": "晚上", "icon": "♨️", "name": "Hotel Mystays 頂樓溫泉", "detail": "邊泡湯邊看富士山，登山前最佳放鬆！早睡"},
        ],
    },
    {
        "day": 3, "date": "07/05（日）", "title": "登富士山 ↑",
        "location": "fuji",
        "activities": [
            {"time": "早上", "icon": "🚌", "name": "巴士前往五合目", "detail": "步行5分→富士急高原樂園站，搭1站至河口湖站，再轉巴士約50分（吉田口五合目，海拔2,390m）"},
            {"time": "14:00前", "icon": "🔒", "name": "通過登山閘門", "detail": "⚠️ 閘門 14:00 關閉，務必提前抵達！住山屋者另有安排"},
            {"time": "下午", "icon": "⛰️", "name": "吉田路線上山", "detail": "目標八合目，預計 5–7 小時（含休息）"},
            {"time": "傍晚", "icon": "🛖", "name": "入住簾岩館", "detail": "海拔 3,100m 山屋。充分休息，備戰凌晨攻頂"},
        ],
    },
    {
        "day": 4, "date": "07/06（一）", "title": "御來光攻頂 → 回富士吉田",
        "location": "fuji",
        "activities": [
            {"time": "凌晨", "icon": "🌅", "name": "攻頂・御來光", "detail": "從山屋出發，登頂日出（海拔 3,776m）——此生難忘"},
            {"time": "早上", "icon": "🌋", "name": "火山口環繞", "detail": "頂峰環走，四周壯麗雲海"},
            {"time": "上午", "icon": "⬇️", "name": "下山返回五合目", "detail": "約 3–4 小時，搭巴士回河口湖站，再回 Mystays 放行李"},
            {"time": "13:00", "icon": "🍵", "name": "忍野八海", "detail": "富士山融雪形成的八個清澈湧泉，世界遺產，傳統村落，食蕎麥麵"},
            {"time": "17:00", "icon": "🗻", "name": "富士吉田本町通", "detail": "直街盡頭就是富士山，黃昏光線最美，逆富士拍攝聖地"},
            {"time": "晚上", "icon": "♨️", "name": "旅館頂樓溫泉", "detail": "犒勞辛苦的雙腳，登山後最需要的就是這個！"},
        ],
    },
    {
        "day": 5, "date": "07/07（二）", "title": "回東京 × 下北澤",
        "location": "tokyo",
        "activities": [
            {"time": "上午", "icon": "🚆", "name": "富士回遊號返錦糸町", "detail": "富士急高原樂園站直搭，約2小時，下車步行3分入住飯店，放行李休息"},
            {"time": "14:00", "icon": "🛍️", "name": "Bonus Track（下北澤）", "detail": "獨立商店街，咖啡館、發酵食品店、藝廊，有戶外座位"},
            {"time": "15:30", "icon": "📖", "name": "B&B（Book & Beer）", "detail": "Bonus Track 2F，邊喝啤酒邊看書，超放鬆"},
            {"time": "16:30", "icon": "🎸", "name": "Village Vanguard", "detail": "亞文化雜貨聖地，奇奇怪怪的東西都有"},
            {"time": "17:30", "icon": "📚", "name": "TSUTAYA 下北澤", "detail": "有品味的選書蔦屋書店，附設咖啡"},
            {"time": "晚上", "icon": "🍶", "name": "下北澤居酒屋晚餐", "detail": "享受下北澤獨特文青氛圍"},
        ],
    },
    {
        "day": 6, "date": "07/08（三）", "title": "清澄白河咖啡聚落",
        "location": "tokyo",
        "activities": [
            {"time": "10:00", "icon": "☕", "name": "ARiSE Coffee Roasters", "detail": "在地烘豆師，手沖依當日豆單推薦，東南亞氛圍（週一公休，今天週三OK）"},
            {"time": "11:00", "icon": "☕", "name": "Blue Bottle Coffee 旗艦店", "detail": "日本第一家，老倉庫改建，挑高空間，必朝聖"},
            {"time": "13:00", "icon": "🎨", "name": "東京都現代美術館（MOT）", "detail": "步行約 10 分鐘，展覽品質高（週一休，今天週三OK）"},
            {"time": "15:00+", "icon": "🚶", "name": "清澄白河周邊漫步", "detail": "倉庫改造咖啡館一間接一間，慢慢探索"},
            {"time": "晚上", "icon": "🍽️", "name": "自由行程", "detail": "可前往上野、秋葉原或銀座晚餐，從清澄白河搭地鐵均可達"},
        ],
    },
    {
        "day": 7, "date": "07/09（四）", "title": "返台",
        "location": "tokyo",
        "activities": [
            {"time": "上午", "icon": "🛍️", "name": "退房 + 最後購物", "detail": "別忘了伴手禮！錦糸町周邊有藥妝、超市"},
            {"time": "出發", "icon": "🚃", "name": "前往成田機場", "detail": "方案A：総武線→新宿→N'EX（約75分，¥3,070）｜方案B：錦糸町→押上→京成本線（約80分，¥1,050）"},
            {"time": "✈️", "icon": "🛫", "name": "成田 → 台北桃園", "detail": "建議提前 2.5 小時到機場，一路平安！"},
        ],
    },
]

EXPERIENCES = [
    {"icon": "🌄", "title": "御來光", "desc": "凌晨攻頂，在海拔 3,776m 親眼見證日出"},
    {"icon": "🌸", "title": "薰衣草海", "desc": "大石公園 7 月盛開，富士山為背景"},
    {"icon": "🌊", "title": "富士溫泉", "desc": "Mystays 頂樓溫泉，泡湯遠眺富士山影"},
    {"icon": "🍵", "title": "精品咖啡", "desc": "清澄白河，Tokyo 精品咖啡聖地"},
    {"icon": "📚", "title": "下北澤文化", "desc": "古著、書店、音樂、居酒屋，文青天堂"},
    {"icon": "💧", "title": "忍野八海", "desc": "世界遺產湧泉群，傳統村落風情"},
]

WEATHER = [
    {"loc": "東京市區", "alt": "0 m", "temp": "25–33°C", "note": "梅雨尾聲，午後陣雨，體感炎熱"},
    {"loc": "河口湖・富士吉田", "alt": "900 m", "temp": "17–28°C", "note": "比東京涼 5–8°C，早晚需薄外套"},
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
        "KINSHICHO Tokyo Holiday Hotel（7/3 入住）",
        "KINSHICHO Tokyo Holiday Hotel（7/7、7/8 入住）",
        "Hotel Mystays Fuji Onsen Resort（7/4、7/6）—— 選 Fuji View 房型！",
        "富士山山屋：簾岩館（7/5）—— 越早越好！",
    ],
    "🎫 票券交通": [
        "富士山吉田路線線上通行預約（每人 ¥4,000）",
        "富士回遊號特急券（錦糸町↔富士急高原樂園，去程＋回程，提前在えきねっと購買）",
        "成田機場交通（N'EX 或京成本線）",
        "日本 SIM 卡或 Wi-Fi 分享器",
        "Mt. Fuji Pass 2–3日券（7/4、7/6 玩多景點時划算）",
    ],
    "💊 醫藥準備": [
        "高山症藥（乙醯唑胺，請先諮詢醫師，出發前 2 天服用）",
        "止痛藥、腸胃藥",
        "暈車藥（富士山巴士山路蜿蜒）",
        "肌肉痠痛貼布（下山後必用）",
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

HOTELS = [
    {
        "name": "KINSHICHO Tokyo Holiday Hotel",
        "location": "東京・錦糸町",
        "nights": "7/3・7/7・7/8（三晚）",
        "station": "錦糸町站 步行 3 分",
        "color": "tokyo",
        "highlight": "🚆 富士回遊號直接從這裡出發，出門步行3分即上車，完全不需先去新宿！",
    },
    {
        "name": "Hotel Mystays Fuji Onsen Resort",
        "location": "富士吉田市・新倉山下",
        "nights": "7/4・7/6（兩晚）",
        "station": "富士急高原樂園站 步行 5 分",
        "color": "kawaguchiko",
        "highlight": "♨️ 頂樓溫泉可遠眺富士山！建議選 Fuji View 房型",
    },
    {
        "name": "簾岩館（山屋）",
        "location": "富士山八合目 3,100m",
        "nights": "7/5（一晚）",
        "station": "步行登山 5–7 小時方能抵達",
        "color": "fuji",
        "highlight": "⛰️ 凌晨從這裡出發攻頂御來光，越早預訂越好，非常搶手！",
    },
]

TRANSPORT_ROWS = [
    {
        "seg": "成田 → 錦糸町",
        "mode": "🚃",
        "options": [
            {"label": "N'EX + JR 総武線快速（省時）", "time": "約 75 分", "cost": "¥3,070", "tag": None},
            {"label": "京成本線（快特）→ 押上 → 錦糸町", "time": "約 80 分", "cost": "¥1,050", "tag": "省錢"},
        ],
    },
    {
        "seg": "錦糸町 → 富士急高原樂園",
        "mode": "🚆",
        "options": [
            {"label": "富士回遊號（直達，不需去新宿）", "time": "約 2h 15m", "cost": "¥4,400", "tag": "直達"},
        ],
    },
    {
        "seg": "河口湖 → 五合目",
        "mode": "🚌",
        "options": [
            {"label": "富士山巴士（吉田口五合目）", "time": "約 50 分", "cost": "¥1,800", "tag": None},
        ],
    },
    {
        "seg": "錦糸町 → 清澄白河",
        "mode": "🚇",
        "options": [
            {"label": "東京地鐵半蔵門線（直達）", "time": "約 3 分", "cost": "¥180", "tag": "超近"},
        ],
    },
    {
        "seg": "錦糸町 → 下北澤",
        "mode": "🚇",
        "options": [
            {"label": "JR 総武線 → 山手線 → 小田急線", "time": "約 35 分", "cost": "¥320", "tag": None},
        ],
    },
    {
        "seg": "錦糸町 → 成田",
        "mode": "🚃",
        "options": [
            {"label": "JR 総武線快速 → 新宿 → N'EX（省時）", "time": "約 75 分", "cost": "¥3,070", "tag": None},
            {"label": "錦糸町 → 押上 → 京成本線", "time": "約 80 分", "cost": "¥1,050", "tag": "省錢"},
        ],
    },
]

# ──────────────────────────────────────────────────────────────────────────────
# CSS
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Kiwi+Maru:wght@300;400;500&family=Noto+Sans+TC:wght@300;400;500;700&family=Noto+Serif+TC:wght@400;600&display=swap');

*, *::before, *::after { box-sizing: border-box; }

/* ── Page background — cream + subtle green dot texture ── */
.stApp {
    background-color: #F7F3EA !important;
    background-image: radial-gradient(circle, rgba(100,170,100,0.13) 1.4px, transparent 1.4px) !important;
    background-size: 26px 26px !important;
}
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
    font-size: 1.65rem;
    color: #1e2e1e;
    text-align: center;
    margin: 56px 0 6px;
    letter-spacing: 0.06em;
}
.sec-title::after {
    content: '';
    display: block;
    width: 64px;
    height: 5px;
    background: linear-gradient(90deg, #438B48 0%, #FFDF76 50%, #DD792E 100%);
    margin: 10px auto 0;
    border-radius: 3px;
}
.sec-sub {
    text-align: center;
    color: #78A95B;
    font-size: 0.80rem;
    letter-spacing: 0.14em;
    margin: 0 0 26px;
    font-family: 'Noto Sans TC', sans-serif;
}

/* ── Nature divider ─────────────────────────── */
.nature-div {
    text-align: center;
    font-size: 1rem;
    letter-spacing: 0.6rem;
    margin: 2px 0 10px;
    color: #A8C89A;
    user-select: none;
}

/* ── Stat cards ─────────────────────────────── */
.stat-card {
    background: linear-gradient(160deg, #ffffff 0%, #F5FBF5 100%);
    border-radius: 20px;
    padding: 28px 16px 22px;
    text-align: center;
    box-shadow: 0 6px 28px rgba(67,139,72,.12), 0 1px 4px rgba(67,139,72,.06);
    border-top: 5px solid #438B48;
    transition: transform .25s, box-shadow .25s;
    height: 100%;
}
.stat-card:hover { transform: translateY(-6px); box-shadow: 0 12px 36px rgba(67,139,72,.18); }
.stat-icon  { font-size: 2.4rem; margin-bottom: 10px; }
.stat-num   { font-family: 'Noto Serif TC', serif; font-size: 2rem; font-weight: 700; color: #1e2e1e; line-height: 1; }
.stat-label { font-size: .82rem; color: #78A95B; margin-top: 6px; font-family: 'Noto Sans TC', sans-serif; }

/* ── Day accordion ──────────────────────────── */
.day-wrap { margin-bottom: 10px; }
details.day-card {
    background: white;
    border-radius: 18px;
    box-shadow: 0 3px 18px rgba(67,139,72,.09), 0 1px 4px rgba(0,0,0,.04);
    overflow: hidden;
    transition: box-shadow .2s;
}
details.day-card:hover { box-shadow: 0 6px 24px rgba(67,139,72,.14); }
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
details.day-card summary:hover { background: #FAFDF8; }
details.day-card summary::-webkit-details-marker { display: none; }
details.day-card[open] > summary { border-bottom: 1px dashed #E8E2DA; }

.day-badge {
    font-family: 'Kiwi Maru', serif;
    font-size: .82rem;
    color: white;
    padding: 4px 14px;
    border-radius: 20px;
    white-space: nowrap;
    font-weight: 500;
    letter-spacing: .04em;
    box-shadow: 0 2px 8px rgba(0,0,0,.15);
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
    border-radius: 18px;
    padding: 28px 18px 22px;
    text-align: center;
    box-shadow: 0 5px 22px rgba(67,139,72,.10);
    border-bottom: 4px solid #FFDF76;
    transition: transform .25s, box-shadow .25s;
    height: 100%;
}
.exp-card:hover { transform: translateY(-6px); box-shadow: 0 12px 32px rgba(67,139,72,.16); }
.exp-icon  {
    font-size: 2.1rem;
    width: 76px; height: 76px;
    background: linear-gradient(135deg, #EBF8EB 0%, #C8E6C8 55%, #A8D4A8 100%);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    margin: 0 auto 14px;
    box-shadow: 0 4px 16px rgba(67,139,72,.20);
    border: 3px solid rgba(255,255,255,.8);
}
.exp-title { font-family: 'Noto Serif TC', serif; font-size: 1rem; font-weight: 600; color: #1e2e1e; margin-bottom: 7px; }
.exp-desc  { font-size: .80rem; color: #5E7960; line-height: 1.6; font-family: 'Noto Sans TC', sans-serif; }

/* ── Weather table ──────────────────────────── */
.wtable {
    width: 100%; border-collapse: collapse;
    border-radius: 18px; overflow: hidden;
    box-shadow: 0 5px 24px rgba(67,139,72,.09);
    font-family: 'Noto Sans TC', sans-serif; font-size: .88rem;
}
.wtable thead tr { background: linear-gradient(90deg, #438B48, #3C8A50); color: white; }
.wtable th { padding: 14px 16px; text-align: left; letter-spacing: .05em; }
.wtable tbody tr:nth-child(odd)  { background: white; }
.wtable tbody tr:nth-child(even) { background: #F5FAF5; }
.wtable td { padding: 12px 16px; border-bottom: 1px solid #EDF2ED; color: #2a3a2a; }
.wtable td:first-child { font-weight: 700; color: #438B48; }
.tbadge {
    background: linear-gradient(135deg, #3C828F, #2E6E7A);
    color: white;
    padding: 5px 16px;
    border-radius: 20px;
    font-size: .90rem;
    font-weight: 700;
    letter-spacing: .03em;
    display: inline-block;
    white-space: nowrap;
    box-shadow: 0 2px 8px rgba(60,130,143,.25);
}

/* ── Fuji elevation chart ───────────────────── */
.fuji-chart { background: white; border-radius: 18px; padding: 28px 24px; box-shadow: 0 5px 24px rgba(67,139,72,.09); }
.frow { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
.fstation { font-size: .85rem; font-weight: 600; color: #1e2e1e; min-width: 150px; text-align: right; font-family: 'Noto Sans TC', sans-serif; }
.fbar-bg { flex: 1; background: #EDF0ED; border-radius: 8px; height: 34px; overflow: hidden; }
.fbar {
    height: 100%; border-radius: 8px;
    background: linear-gradient(90deg, #9ABE74, #78A95B, #438B48);
    display: flex; align-items: center; padding-left: 10px;
}
.fbar.summit { background: linear-gradient(90deg, #E7A93B, #DD792E, #C96820); }
.fbar-label { font-size: .78rem; color: white; font-weight: 700; white-space: nowrap; font-family: 'Noto Sans TC', sans-serif; text-shadow: 0 1px 3px rgba(0,0,0,.2); }
.fnote { font-size: .76rem; color: #78A95B; min-width: 150px; font-family: 'Noto Sans TC', sans-serif; }

/* ── Info / warning boxes ───────────────────── */
.info-box {
    background: linear-gradient(135deg, #EAF5EA, #E0F0E0);
    border-left: 4px solid #438B48;
    border-radius: 0 14px 14px 0; padding: 14px 20px;
    margin: 14px 0; font-size: .86rem; color: #1a3a1a;
    font-family: 'Noto Sans TC', sans-serif;
    box-shadow: 0 2px 10px rgba(67,139,72,.08);
}
.warn-box {
    background: linear-gradient(135deg, #FFF8ED, #FFF0DC);
    border-left: 4px solid #DD792E;
    border-radius: 0 14px 14px 0; padding: 14px 20px;
    margin: 14px 0; font-size: .86rem; color: #5E3A10;
    font-family: 'Noto Sans TC', sans-serif;
    box-shadow: 0 2px 10px rgba(221,121,46,.08);
}
.warn-box strong, .info-box strong { font-weight: 700; }

/* ── Checklist section ──────────────────────── */
.cl-header {
    font-family: 'Noto Serif TC', serif;
    font-size: 1rem; color: white;
    padding: 11px 22px;
    border-radius: 14px 14px 0 0;
    margin-bottom: 0; font-weight: 600;
    letter-spacing: 0.04em;
}
.cl-box {
    background: white;
    border-radius: 0 0 14px 14px;
    padding: 16px 20px 12px;
    box-shadow: 0 5px 20px rgba(67,139,72,.09);
    margin-bottom: 20px;
}

[data-testid="stCheckbox"] label,
[data-testid="stCheckbox"] label p,
[data-testid="stCheckbox"] label span,
[data-testid="stCheckbox"] p,
[data-testid="stCheckbox"] span,
[data-testid="stCheckbox"] div {
    font-family: 'Noto Sans TC', sans-serif !important;
    font-size: .88rem !important;
    color: #000000 !important;
}

/* ── Route strip ────────────────────────────── */
.route-strip {
    background: white; border-radius: 22px;
    box-shadow: 0 5px 24px rgba(67,139,72,.10);
    padding: 26px 32px; margin-bottom: 12px;
    display: flex; align-items: center; justify-content: center; gap: 0;
}
.rstop { text-align: center; }
.rdot {
    width: 72px; height: 72px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.9rem; margin: 0 auto 8px;
    box-shadow: 0 5px 18px rgba(0,0,0,.15);
    border: 3px solid rgba(255,255,255,.6);
}
.rdot-tokyo  { background: linear-gradient(135deg,#DD792E,#E8974A); }
.rdot-lake   { background: linear-gradient(135deg,#3C828F,#5BA5B0); }
.rdot-fuji   { background: linear-gradient(135deg,#438B48,#5A9E5A); }
.rname   { font-weight: 700; color: #1e2e1e; font-size: .95rem; margin-bottom: 2px; font-family: 'Noto Sans TC', sans-serif; }
.rsub    { font-size: .70rem; color: #aaa; margin-bottom: 4px; font-family: 'Noto Sans TC', sans-serif; }
.rnights { font-size: .72rem; color: #78A95B; background: #EAF5EA; padding: 2px 10px; border-radius: 10px; display: inline-block; font-family: 'Noto Sans TC', sans-serif; }
.rarrow {
    flex: 1; min-width: 80px;
    display: flex; flex-direction: column; align-items: center; padding: 0 8px;
}
.rline {
    width: 100%; height: 2px;
    background: repeating-linear-gradient(90deg,#78A95B 0,#78A95B 7px,transparent 7px,transparent 13px);
    position: relative; margin-bottom: 5px;
}
.rline::after { content:'▶'; position:absolute; right:-7px; top:-9px; color:#78A95B; font-size:.75rem; }
.rtrans { font-size: .68rem; color: #5E7960; text-align: center; white-space: nowrap; font-family: 'Noto Sans TC', sans-serif; }

/* ── Route highlight callout ────────────────── */
.route-callout {
    background: linear-gradient(135deg, #FFF4EE, #FFE8D5);
    border: 2px solid #DD792E;
    border-radius: 16px;
    padding: 14px 22px;
    margin-bottom: 28px;
    display: flex;
    align-items: center;
    gap: 14px;
    font-family: 'Noto Sans TC', sans-serif;
    box-shadow: 0 3px 14px rgba(221,121,46,.12);
}
.rc-icon { font-size: 1.9rem; flex-shrink: 0; }
.rc-text { font-size: .88rem; color: #5E3A10; line-height: 1.65; }
.rc-text strong { color: #DD792E; }

/* ── Hotel cards ────────────────────────────── */
.hotel-card {
    border-radius: 16px;
    padding: 20px 18px;
    height: 100%;
    box-shadow: 0 4px 18px rgba(0,0,0,.08);
    transition: transform .2s;
}
.hotel-card:hover { transform: translateY(-4px); }
.hc-name { font-family: 'Noto Serif TC', serif; font-size: .92rem; font-weight: 700; margin-bottom: 10px; line-height: 1.4; }
.hc-meta { font-size: .78rem; color: #666; margin-bottom: 4px; font-family: 'Noto Sans TC', sans-serif; }
.hc-nights { font-size: .82rem; font-weight: 700; margin-bottom: 4px; font-family: 'Noto Sans TC', sans-serif; }
.hc-highlight { font-size: .78rem; border-radius: 10px; padding: 9px 13px; line-height: 1.65; margin-top: 10px; font-family: 'Noto Sans TC', sans-serif; }

/* ── Transport block ────────────────────────── */
.transport-block { background: white; border-radius: 18px; box-shadow: 0 5px 24px rgba(67,139,72,.09); overflow: hidden; }
.trow { padding: 14px 20px; border-bottom: 1px solid #F0EDE8; display: flex; align-items: flex-start; gap: 16px; }
.trow:last-child { border-bottom: none; }
.tr-seg { font-family: 'Noto Sans TC', sans-serif; font-size: .88rem; font-weight: 700; color: #1e2e1e; min-width: 190px; padding-top: 2px; flex-shrink: 0; }
.tr-opts { flex: 1; display: flex; flex-direction: column; gap: 6px; }
.tr-opt { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.tr-opt-b .tr-name { color: #888; }
.tr-name { font-size: .82rem; color: #3a3a3a; flex: 1; font-family: 'Noto Sans TC', sans-serif; min-width: 160px; }
.tr-time { font-size: .78rem; color: #777; white-space: nowrap; font-family: 'Noto Sans TC', sans-serif; }
.tr-cost { font-size: .80rem; font-weight: 700; padding: 2px 11px; border-radius: 12px; white-space: nowrap; background: #EDF7EE; color: #438B48; font-family: 'Noto Sans TC', sans-serif; }
.tr-tag { font-size: .70rem; padding: 2px 9px; border-radius: 10px; background: #FFF4EE; color: #DD792E; font-weight: 700; white-space: nowrap; font-family: 'Noto Sans TC', sans-serif; }
.tr-tag-blue { background: #EEF8FA; color: #3C828F; }

/* ── Footer ─────────────────────────────────── */
.page-footer {
    text-align: center; padding: 40px 20px;
    color: #78A95B; font-size: .82rem;
    border-top: 2px dashed #C8DCC8; margin-top: 60px;
    font-family: 'Noto Sans TC', sans-serif;
    letter-spacing: 0.04em;
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


def hotel_card_html(h):
    c = LOC_COLORS[h["color"]]
    return (
        f'<div class="hotel-card" style="border-left:5px solid {c["badge"]};background:{c["light"]}">'
        f'<div class="hc-name" style="color:{c["badge"]}">{h["name"]}</div>'
        f'<div class="hc-meta">📍 {h["location"]}</div>'
        f'<div class="hc-nights" style="color:{c["badge"]}">🗓 {h["nights"]}</div>'
        f'<div class="hc-meta">🚉 {h["station"]}</div>'
        f'<div class="hc-highlight" style="background:{c["badge"]}22;border-left:3px solid {c["badge"]}">{h["highlight"]}</div>'
        f'</div>'
    )


def transport_html():
    rows = ""
    for r in TRANSPORT_ROWS:
        opts_html = ""
        for i, opt in enumerate(r["options"]):
            tag_html = ""
            if opt["tag"]:
                tag_cls = "tr-tag tr-tag-blue" if opt["tag"] in ("直達", "超近") else "tr-tag"
                tag_html = f'<span class="{tag_cls}">{opt["tag"]}</span>'
            opts_html += (
                f'<div class="tr-opt{"" if i == 0 else " tr-opt-b"}">'
                f'<span class="tr-name">{opt["label"]}</span>'
                f'<span class="tr-time">{opt["time"]}</span>'
                f'<span class="tr-cost">{opt["cost"]}</span>'
                f'{tag_html}'
                f'</div>'
            )
        rows += (
            f'<div class="trow">'
            f'<div class="tr-seg">{r["mode"]} {r["seg"]}</div>'
            f'<div class="tr-opts">{opts_html}</div>'
            f'</div>'
        )
    return f'<div class="transport-block">{rows}</div>'


def nature_divider():
    st.markdown('<div class="nature-div">🌿 · 🌸 · 🌿</div>', unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# HERO  — enhanced with animations, torii gate, three hikers
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

@keyframes twinkle {
  0%,100% { opacity:.25; transform:scale(.8); }
  50%      { opacity:1;   transform:scale(1.3); }
}
@keyframes cloudDrift {
  0%,100% { transform:translateX(0); }
  50%      { transform:translateX(14px); }
}
@keyframes cloudDriftR {
  0%,100% { transform:translateX(0); }
  50%      { transform:translateX(-10px); }
}
@keyframes sunRise {
  0%   { opacity:0; transform:translateY(8px); }
  100% { opacity:1; transform:translateY(0); }
}

.ta { animation:twinkle 2.4s ease-in-out infinite; }
.tb { animation:twinkle 3.6s ease-in-out infinite .7s; }
.tc { animation:twinkle 2.0s ease-in-out infinite 1.4s; }
.td { animation:twinkle 4.2s ease-in-out infinite .3s; }
.te { animation:twinkle 3.0s ease-in-out infinite 1.9s; }
.tf { animation:twinkle 2.7s ease-in-out infinite 1.1s; }
.cloud-l { animation:cloudDrift  9s ease-in-out infinite; }
.cloud-r { animation:cloudDriftR 7s ease-in-out infinite; }

.hero {
  position:relative; width:100%; height:300px;
  background:linear-gradient(180deg,#0D2035 0%,#1a4258 28%,#2E6E80 58%,#4A9BAA 80%,#3A8040 100%);
  border-radius:16px; overflow:hidden;
}
.star { position:absolute; border-radius:50%; background:white; }
.moon     { position:absolute; top:26px; right:108px; width:36px; height:36px; border-radius:50%; background:#FFFCE8; box-shadow:0 0 18px rgba(255,252,200,.5); }
.moon-cut { position:absolute; top:20px; right:94px;  width:32px; height:32px; border-radius:50%; background:#1f4e64; }
.cloud { position:absolute; border-radius:50%; background:white; }

/* Mt Fuji — slightly more detailed */
.fuji {
  position:absolute; bottom:55px; right:4%;
  width:530px; height:270px;
  background:linear-gradient(175deg,#EAE8E5 0%,#C8B8A8 18%,#A89080 50%,#80604E 78%,#684838 100%);
  clip-path:polygon(50% 0%,0% 100%,100% 100%);
}
/* Snow layers */
.snow {
  position:absolute; bottom:260px; right:calc(4% + 132px);
  width:266px; height:114px;
  background:linear-gradient(180deg,rgba(255,255,255,.98),rgba(230,230,230,.7));
  clip-path:polygon(50% 0%,4% 100%,96% 100%);
}
.snow-w1 { position:absolute; bottom:250px; right:calc(4%+108px); width:122px; height:62px; background:rgba(255,255,255,.42); clip-path:polygon(50% 0%,0% 100%,100% 100%); }
.snow-w2 { position:absolute; bottom:254px; right:calc(4%+238px); width:104px; height:58px; background:rgba(255,255,255,.36); clip-path:polygon(50% 0%,0% 100%,100% 100%); }

/* Green base */
.hill-base  { position:absolute; bottom:0; left:0; right:0; height:66px; background:#2D5E30; }
.hill-left  { position:absolute; bottom:24px; left:-55px;  width:490px; height:115px; background:linear-gradient(180deg,#4A9E55,#387040); border-radius:50% 50% 0 0; }
.hill-right { position:absolute; bottom:28px; right:-38px; width:370px; height:98px;  background:linear-gradient(180deg,#438B48,#2D5E30); border-radius:50% 50% 0 0; }

/* Trees */
.tree { position:absolute; width:0; height:0; border-left:11px solid transparent; border-right:11px solid transparent; }

/* Lake */
.lake { position:absolute; border-radius:50%; background:#3C8A9A; opacity:.28; }

/* ── Torii Gate (鳥居) ── */
.torii { position:absolute; bottom:65px; left:252px; }
.torii-top1 { position:absolute; top:-10px; left:-12px; width:64px; height:8px; background:#C0392B; border-radius:4px 4px 0 0; transform:perspective(80px) rotateX(-8deg); }
.torii-top2 { position:absolute; top:5px;  left:-4px;  width:48px; height:5px; background:#C0392B; }
.torii-leg  { position:absolute; top:9px;  width:7px;  height:50px; background:#C0392B; border-radius:0 0 4px 4px; }
.torii-ll   { left:0; }
.torii-rl   { left:33px; }

/* ── Three hikers: Jack(orange) Mike(teal) Apple(green) ── */
.hikers { position:absolute; bottom:66px; left:172px; display:flex; gap:7px; align-items:flex-end; }
.hiker  { position:relative; }
/* head */
.hk-head { width:11px; height:11px; border-radius:50%; background:#F5D5A0; border:1.5px solid #D4A060; position:absolute; top:0; left:3px; }
/* body */
.hk-body { position:absolute; top:9px; left:0; border-radius:4px 4px 2px 2px; }
/* legs */
.hk-leg  { position:absolute; bottom:0; width:5px; border-radius:0 0 3px 3px; }
/* backpack */
.hk-pack { position:absolute; top:12px; border-radius:3px; width:5px; }

/* Lavender field */
.lavender { position:absolute; bottom:67px; display:flex; gap:4px; }
.lv { border-radius:50% 50% 0 0; }

/* Text box */
.textbox {
  position:absolute; top:50%; left:5%;
  transform:translateY(-50%);
  background:rgba(247,243,234,.92);
  border-radius:18px; padding:20px 28px;
  border-left:5px solid #DD792E;
  max-width:340px;
  backdrop-filter:blur(10px);
  box-shadow:0 8px 32px rgba(0,0,0,.15);
}
.label  { font-family:'Noto Sans TC',sans-serif; font-size:.70rem; color:#78A95B; letter-spacing:.16em; margin-bottom:5px; }
.title  { font-family:'Kiwi Maru',serif; font-size:2.3rem; color:#1e2e1e; line-height:1.12; margin-bottom:5px; }
.sub    { font-family:'Noto Serif TC',serif; font-size:.90rem; color:#438B48; font-weight:600; letter-spacing:.07em; margin-bottom:11px; }
.people { font-family:'Noto Sans TC',sans-serif; font-size:.82rem; color:#5E7960; margin-bottom:7px; }
.dates  { font-family:'Noto Serif TC',serif; font-size:.96rem; color:#DD792E; font-weight:700; }

/* decorative dots corner (like 参考首頁) */
.dot-cluster { position:absolute; }
.dot-c { position:absolute; border-radius:50%; }
</style>
</head>
<body>
<div class="hero">

  <!-- Corner dot clusters (参考首頁 style) -->
  <div class="dot-cluster" style="top:-10px;left:-10px;">
    <div class="dot-c" style="width:80px;height:80px;background:rgba(196,226,196,.35);top:0;left:0;"></div>
    <div class="dot-c" style="width:50px;height:50px;background:rgba(255,223,118,.25);top:40px;left:50px;"></div>
    <div class="dot-c" style="width:30px;height:30px;background:rgba(196,226,196,.28);top:70px;left:18px;"></div>
  </div>

  <!-- Stars (more, with twinkle) -->
  <div class="star ta" style="top:20px;left:78px;width:4px;height:4px;"></div>
  <div class="star tb" style="top:10px;left:170px;width:3px;height:3px;"></div>
  <div class="star tc" style="top:35px;left:240px;width:3px;height:3px;"></div>
  <div class="star td" style="top:15px;right:195px;width:4px;height:4px;"></div>
  <div class="star te" style="top:48px;left:340px;width:2px;height:2px;"></div>
  <div class="star tf" style="top:26px;right:285px;width:3px;height:3px;"></div>
  <div class="star ta" style="top:8px;right:340px;width:2px;height:2px;"></div>
  <div class="star tc" style="top:55px;left:140px;width:2px;height:2px;"></div>

  <!-- Moon -->
  <div class="moon"></div>
  <div class="moon-cut"></div>

  <!-- Clouds left (animated) -->
  <div class="cloud-l">
    <div class="cloud" style="top:62px;left:48px;width:190px;height:54px;opacity:.72;"></div>
    <div class="cloud" style="top:50px;left:80px;width:152px;height:48px;opacity:.80;"></div>
    <div class="cloud" style="top:70px;left:32px;width:102px;height:40px;opacity:.68;"></div>
  </div>

  <!-- Clouds right (animated, opposite) -->
  <div class="cloud-r" style="position:absolute;top:0;right:0;">
    <div class="cloud" style="top:58px;right:335px;width:134px;height:42px;opacity:.50;position:absolute;"></div>
    <div class="cloud" style="top:47px;right:352px;width:104px;height:36px;opacity:.46;position:absolute;"></div>
  </div>

  <!-- Mt Fuji -->
  <div class="fuji"></div>
  <div class="snow"></div>
  <div class="snow-w1"></div>
  <div class="snow-w2"></div>

  <!-- Hills -->
  <div class="hill-left"></div>
  <div class="hill-right"></div>
  <div class="hill-base"></div>

  <!-- Trees left -->
  <div class="tree" style="bottom:64px;left:38px;border-bottom:30px solid #245828;"></div>
  <div class="tree" style="bottom:64px;left:60px;border-bottom:34px solid #245828;"></div>
  <div class="tree" style="bottom:64px;left:84px;border-bottom:28px solid #2D6830;"></div>
  <div class="tree" style="bottom:64px;left:106px;border-bottom:32px solid #245828;"></div>
  <div class="tree" style="bottom:64px;left:128px;border-bottom:26px solid #2D6830;"></div>

  <!-- Trees right -->
  <div class="tree" style="bottom:64px;right:44px;border-bottom:30px solid #245828;"></div>
  <div class="tree" style="bottom:64px;right:24px;border-bottom:34px solid #2D6830;"></div>
  <div class="tree" style="bottom:64px;right:66px;border-bottom:28px solid #245828;"></div>

  <!-- Lake -->
  <div class="lake" style="bottom:68px;left:200px;width:130px;height:16px;"></div>

  <!-- Lavender field (extended) -->
  <div class="lavender" style="left:148px;">
    <div class="lv" style="width:6px;height:11px;background:#9B7BB8;opacity:.65;"></div>
    <div class="lv" style="width:6px;height:13px;background:#B08FCC;opacity:.65;"></div>
    <div class="lv" style="width:6px;height:10px;background:#9B7BB8;opacity:.65;"></div>
    <div class="lv" style="width:6px;height:12px;background:#A882C2;opacity:.65;"></div>
    <div class="lv" style="width:6px;height:11px;background:#B08FCC;opacity:.65;"></div>
    <div class="lv" style="width:6px;height:9px;background:#9B7BB8;opacity:.65;"></div>
    <div class="lv" style="width:6px;height:13px;background:#A882C2;opacity:.65;"></div>
    <div class="lv" style="width:6px;height:10px;background:#B08FCC;opacity:.65;"></div>
  </div>

  <!-- ── Torii Gate 鳥居 ── -->
  <div class="torii">
    <div class="torii-top1"></div>
    <div class="torii-top2"></div>
    <div class="torii-leg torii-ll"></div>
    <div class="torii-leg torii-rl"></div>
  </div>

  <!-- ── Three hikers: Jack / Mike / Apple ── -->
  <div class="hikers">
    <!-- Jack — orange -->
    <div class="hiker" style="width:18px;height:42px;">
      <div class="hk-head"></div>
      <div class="hk-body" style="width:18px;height:20px;background:#DD792E;"></div>
      <div class="hk-pack" style="right:-4px;background:#C06020;height:12px;"></div>
      <div class="hk-leg" style="left:1px;height:15px;background:#DD792E;"></div>
      <div class="hk-leg" style="left:12px;height:15px;background:#DD792E;"></div>
    </div>
    <!-- Mike — teal -->
    <div class="hiker" style="width:18px;height:40px;">
      <div class="hk-head"></div>
      <div class="hk-body" style="width:18px;height:18px;background:#3C828F;"></div>
      <div class="hk-pack" style="right:-4px;background:#2A6870;height:11px;"></div>
      <div class="hk-leg" style="left:1px;height:14px;background:#3C828F;"></div>
      <div class="hk-leg" style="left:12px;height:14px;background:#3C828F;"></div>
    </div>
    <!-- Apple — green -->
    <div class="hiker" style="width:18px;height:38px;">
      <div class="hk-head"></div>
      <div class="hk-body" style="width:18px;height:17px;background:#438B48;"></div>
      <div class="hk-pack" style="right:-4px;background:#326836;height:10px;"></div>
      <div class="hk-leg" style="left:1px;height:13px;background:#438B48;"></div>
      <div class="hk-leg" style="left:12px;height:13px;background:#438B48;"></div>
    </div>
  </div>

  <!-- Text overlay -->
  <div class="textbox">
    <p class="label">✦ TRAVEL PLAN 2026 ✦</p>
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

nature_divider()

stats = [
    ("🗓", "7天6夜", "旅行天數"),
    ("🗺", "3 個地點", "東京・富士吉田・富士山"),
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
    <div class="rsub">錦糸町</div>
    <div class="rnights">3 晚</div>
  </div>
  <div class="rarrow">
    <div class="rline"></div>
    <div class="rtrans">🚆 富士回遊號<br>2h 15m</div>
  </div>
  <div class="rstop">
    <div class="rdot rdot-lake">🏞</div>
    <div class="rname">富士吉田</div>
    <div class="rsub">河口湖周邊</div>
    <div class="rnights">2 晚</div>
  </div>
  <div class="rarrow">
    <div class="rline"></div>
    <div class="rtrans">🚌 巴士<br>50 min</div>
  </div>
  <div class="rstop">
    <div class="rdot rdot-fuji">🗻</div>
    <div class="rname">富士山</div>
    <div class="rsub">八合目山屋</div>
    <div class="rnights">1 晚 ⛺</div>
  </div>
</div>

<div class="route-callout">
  <span class="rc-icon">🚆</span>
  <div class="rc-text">
    <strong>重大亮點：</strong>富士回遊號停靠「錦糸町」站！從飯店步行 3 分鐘直接上車，<strong>完全不需要先去新宿轉車</strong>，直達富士急高原樂園站，再步行 5 分鐘到 Hotel Mystays。
  </div>
</div>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────────────────────
# ACCOMMODATION
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<p class="sec-title">住宿安排</p>
<p class="sec-sub">ACCOMMODATION</p>
""", unsafe_allow_html=True)

cols = st.columns(3, gap="medium")
for col, h in zip(cols, HOTELS):
    with col:
        st.markdown(hotel_card_html(h), unsafe_allow_html=True)

nature_divider()


# ──────────────────────────────────────────────────────────────────────────────
# DAILY ITINERARY
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<p class="sec-title">每日行程</p>
<p class="sec-sub">DAILY ITINERARY — 點擊可展開</p>
""", unsafe_allow_html=True)

for d in ITINERARY:
    st.markdown(day_card_html(d), unsafe_allow_html=True)

nature_divider()


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

nature_divider()


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

nature_divider()


# ──────────────────────────────────────────────────────────────────────────────
# TRANSPORT SUMMARY
# ──────────────────────────────────────────────────────────────────────────────

st.markdown("""
<p class="sec-title">交通一覽</p>
<p class="sec-sub">TRANSPORT GUIDE</p>
""", unsafe_allow_html=True)

st.markdown(transport_html(), unsafe_allow_html=True)

st.markdown("""
<div class="info-box" style="margin-top:12px;">
  🎫 <strong>票券建議：</strong>7/4 和 7/6 玩多個富士山底景點（纜車、富士急、忍野八海）時，推薦購買 <strong>Mt. Fuji Pass 2–3日券</strong>，含周邊12個景點優惠，比單買划算很多。
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
  🌿 東京・富士山 2026 ｜ Jack × Mike × Apple 🌿<br>
  <span style="opacity:.55;font-size:.75rem;">祝一路順風，御來光見！</span>
</div>
""", unsafe_allow_html=True)
