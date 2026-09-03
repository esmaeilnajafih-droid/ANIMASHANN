from flask import Flask, render_template, request
import os

app = Flask(__name__)

def create_templates():
    """ایجاد پوشه templates و فایل‌های HTML"""
    
    if not os.path.exists('templates'):
        os.makedirs('templates')
        print("✅ پوشه templates ایجاد شد")

    # ===== فایل base.html =====
    with open('templates/base.html', 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}🎬 سینمای انیمیشن{% endblock %}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;600;700;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #0a0a1a;
            --text-primary: #ffffff;
            --text-secondary: rgba(255,255,255,0.7);
            --accent-1: #ff6b6b;
            --accent-2: #4ecdc4;
            --gradient-main: linear-gradient(135deg, #6c5ce7, #a29bfe, #4ecdc4, #ff6b6b);
            --shadow-main: 0 30px 80px rgba(0,0,0,0.7);
            --radius-main: 24px;
            --glass-main: rgba(255,255,255,0.05);
            --glass-border: rgba(255,255,255,0.1);
        }
        * { margin:0; padding:0; box-sizing:border-box; }
        body {
            font-family: 'Vazirmatn', 'Segoe UI', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            overflow-x: hidden;
        }
        .cinema-bg {
            position: fixed;
            top:0; left:0; right:0; bottom:0;
            z-index:0;
            background: radial-gradient(ellipse at 10% 30%, rgba(108,92,231,0.4) 0%, transparent 50%),
                        radial-gradient(ellipse at 90% 70%, rgba(78,205,196,0.3) 0%, transparent 50%),
                        #0a0a1a;
            animation: cinemaPulse 10s ease-in-out infinite alternate;
        }
        @keyframes cinemaPulse {
            0% { opacity:0.7; }
            100% { opacity:1; }
        }
        .light-rays {
            position: fixed;
            top:-50%; left:-50%;
            width:200%; height:200%;
            z-index:1;
            pointer-events:none;
            background: repeating-linear-gradient(45deg, transparent 0px, rgba(255,255,255,0.02) 50px, transparent 100px);
            animation: lightRays 20s linear infinite;
        }
        @keyframes lightRays {
            0% { transform:rotate(0deg); }
            100% { transform:rotate(360deg); }
        }
        .particles-3d {
            position: fixed;
            top:0; left:0; right:0; bottom:0;
            z-index:1;
            pointer-events:none;
            overflow:hidden;
        }
        .particle-3d {
            position:absolute;
            border-radius:50%;
            background:rgba(255,255,255,0.1);
            border:1px solid rgba(255,255,255,0.05);
            animation:float3d linear infinite;
        }
        .particle-3d:nth-child(1) { width:40px; height:40px; left:10%; animation-duration:25s; }
        .particle-3d:nth-child(2) { width:60px; height:60px; left:25%; animation-duration:30s; animation-delay:2s; }
        .particle-3d:nth-child(3) { width:30px; height:30px; left:40%; animation-duration:20s; animation-delay:4s; }
        .particle-3d:nth-child(4) { width:50px; height:50px; left:55%; animation-duration:28s; animation-delay:1s; }
        .particle-3d:nth-child(5) { width:35px; height:35px; left:70%; animation-duration:22s; animation-delay:3s; }
        .particle-3d:nth-child(6) { width:45px; height:45px; left:85%; animation-duration:26s; animation-delay:5s; }
        @keyframes float3d {
            0% { transform:translateY(100vh) rotate(0deg) scale(0); opacity:0; }
            10% { opacity:0.5; }
            90% { opacity:0.5; }
            100% { transform:translateY(-10vh) rotate(720deg) scale(1); opacity:0; }
        }
        .container {
            position:relative;
            z-index:2;
            max-width:1100px;
            margin:0 auto;
            padding:20px;
        }
        .theme-toggle {
            position:fixed;
            top:25px; left:25px;
            z-index:1000;
            background:var(--glass-main);
            backdrop-filter:blur(25px);
            color:var(--text-primary);
            border:1px solid var(--glass-border);
            padding:18px 24px;
            border-radius:50px;
            cursor:pointer;
            font-size:1.5rem;
            transition:all 0.8s;
            box-shadow:var(--shadow-main);
        }
        .theme-toggle:hover {
            transform:scale(1.2) rotate(90deg);
            border-color:var(--accent-2);
        }
        .op-4 { opacity:0.4; }
        .mt-3 { margin-top:30px; }
        .fs-small { font-size:0.7rem; }
        @media (max-width:768px) {
            .theme-toggle { top:15px; left:15px; padding:12px 16px; font-size:1.1rem; }
        }
    </style>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <div class="cinema-bg"></div>
    <div class="light-rays"></div>
    <div class="particles-3d">
        <div class="particle-3d"></div>
        <div class="particle-3d"></div>
        <div class="particle-3d"></div>
        <div class="particle-3d"></div>
        <div class="particle-3d"></div>
        <div class="particle-3d"></div>
    </div>
    <button class="theme-toggle" onclick="toggleTheme()">
        <i class="fas fa-moon"></i>
    </button>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    <script>
        function toggleTheme() {
            const html = document.documentElement;
            const current = html.getAttribute('data-theme');
            const newTheme = current === 'light' ? 'dark' : 'light';
            html.setAttribute('data-theme', newTheme);
            const btn = document.querySelector('.theme-toggle');
            btn.innerHTML = newTheme === 'light' ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
            localStorage.setItem('theme', newTheme);
        }
        document.addEventListener('DOMContentLoaded', function() {
            const saved = localStorage.getItem('theme') || 'dark';
            document.documentElement.setAttribute('data-theme', saved);
            const btn = document.querySelector('.theme-toggle');
            btn.innerHTML = saved === 'light' ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
        });
        function cardGlow(e, card) {
            const rect = card.getBoundingClientRect();
            card.style.setProperty('--mouse-x', ((e.clientX - rect.left) / rect.width * 100) + '%');
            card.style.setProperty('--mouse-y', ((e.clientY - rect.top) / rect.height * 100) + '%');
        }
        function cardReset(card) {
            card.style.setProperty('--mouse-x', '50%');
            card.style.setProperty('--mouse-y', '50%');
        }
        {% block extra_js %}{% endblock %}
    </script>
</body>
</html>''')
    print("✅ base.html ایجاد شد")

    # ===== فایل header.html =====
    with open('templates/header.html', 'w', encoding='utf-8') as f:
        f.write('''<div class="header">
    <div class="header-content">
        <div class="header-badge"><i class="fas fa-crown"></i> برترین انیمیشن‌ها</div>
        <h1><i class="fas fa-film"></i> سینمای انیمیشن</h1>
        <p class="subtitle"><i class="fas fa-play-circle"></i> بیش از {{ total_count }} انیمیشن دوبله فارسی از آپارات</p>
        {% include 'stats.html' %}
    </div>
</div>
<style>
.header {
    text-align:center;
    padding:70px 30px 50px;
    background:var(--glass-main);
    backdrop-filter:blur(40px);
    border-radius:var(--radius-main);
    margin-bottom:35px;
    border:1px solid var(--glass-border);
    box-shadow:var(--shadow-main);
    position:relative;
    overflow:hidden;
}
.header::before {
    content:'';
    position:absolute;
    inset:-2px;
    background:conic-gradient(from 0deg, transparent, rgba(255,107,107,0.4), rgba(78,205,196,0.4), transparent);
    border-radius:var(--radius-main);
    z-index:-1;
    animation:rotateBorder 8s linear infinite;
    filter:blur(30px);
}
@keyframes rotateBorder {
    0% { transform:rotate(0deg); }
    100% { transform:rotate(360deg); }
}
.header-content { position:relative; z-index:1; }
.header-badge {
    display:inline-block;
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(10px);
    padding:8px 24px;
    border-radius:50px;
    font-size:0.85rem;
    color:var(--accent-2);
    border:1px solid rgba(78,205,196,0.25);
    margin-bottom:20px;
    letter-spacing:3px;
    animation:badgePulse 2s infinite;
}
@keyframes badgePulse {
    0%,100% { box-shadow:0 0 20px rgba(78,205,196,0); }
    50% { box-shadow:0 0 60px rgba(78,205,196,0.15); }
}
.header h1 {
    font-size:5rem;
    font-weight:900;
    background:var(--gradient-main);
    background-size:300% 300%;
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    animation:gradientMove 5s ease-in-out infinite;
    letter-spacing:5px;
}
@keyframes gradientMove {
    0% { background-position:0% 50%; }
    50% { background-position:100% 50%; }
    100% { background-position:0% 50%; }
}
.header h1 i {
    -webkit-text-fill-color:initial;
    color:#fff;
    margin-left:25px;
    filter:drop-shadow(0 0 40px rgba(108,92,231,0.5));
    animation:iconFloat 4s ease-in-out infinite;
}
@keyframes iconFloat {
    0%,100% { transform:translateY(0); }
    50% { transform:translateY(-15px); }
}
.header .subtitle {
    font-size:1.4rem;
    color:var(--text-secondary);
    margin-top:15px;
    font-weight:300;
}
.header .subtitle i {
    color:var(--accent-2);
    margin-left:12px;
}
@media (max-width:768px) {
    .header h1 { font-size:3rem; }
    .header { padding:40px 20px 30px; }
    .header .subtitle { font-size:1rem; }
}
@media (max-width:480px) {
    .header h1 { font-size:2rem; }
    .header { padding:25px 15px 20px; }
}
</style>''')
    print("✅ header.html ایجاد شد")

    # ===== فایل stats.html =====
    with open('templates/stats.html', 'w', encoding='utf-8') as f:
        f.write('''<div class="header-stats">
    <div class="header-stat"><i class="fas fa-video"></i> <strong>{{ total_count }}</strong> انیمیشن</div>
    <div class="header-stat"><i class="fas fa-check-circle"></i> <strong>{{ result_count }}</strong> نمایش داده شده</div>
    <div class="header-stat"><i class="fas fa-eye"></i> <strong>۵۰,۰۰۰+</strong> بازدید کل</div>
</div>
<style>
.header-stats {
    display:flex;
    justify-content:center;
    gap:40px;
    margin-top:30px;
    flex-wrap:wrap;
}
.header-stat {
    background:var(--glass-main);
    backdrop-filter:blur(15px);
    padding:12px 30px;
    border-radius:50px;
    border:1px solid var(--glass-border);
    font-size:0.95rem;
    color:var(--text-secondary);
    transition:all 0.8s;
    cursor:default;
}
.header-stat:hover {
    transform:translateY(-5px) scale(1.05);
    border-color:var(--accent-2);
}
.header-stat strong {
    color:#fff;
    font-size:1.2rem;
}
.header-stat i {
    color:var(--accent-2);
    margin-left:10px;
}
@media (max-width:768px) {
    .header-stats { gap:15px; }
    .header-stat { padding:8px 18px; font-size:0.8rem; }
}
@media (max-width:480px) {
    .header-stats { gap:10px; }
    .header-stat { padding:6px 14px; font-size:0.7rem; }
    .header-stat strong { font-size:0.9rem; }
}
</style>''')
    print("✅ stats.html ایجاد شد")

    # ===== فایل search.html =====
    with open('templates/search.html', 'w', encoding='utf-8') as f:
        f.write('''<form class="search-box" method="GET" action="/">
    <input type="text" name="search" placeholder="🔍 جستجوی انیمیشن..." value="{{ search_query }}">
    <button type="submit"><i class="fas fa-search"></i> جستجو</button>
    {% if search_query %}<a href="/" class="reset-btn"><i class="fas fa-times"></i> پاک کردن</a>{% endif %}
</form>
<style>
.search-box {
    display:flex;
    gap:15px;
    margin-bottom:35px;
    justify-content:center;
    flex-wrap:wrap;
}
.search-box input {
    flex:1;
    max-width:520px;
    padding:20px 35px;
    background:var(--glass-main);
    backdrop-filter:blur(25px);
    color:var(--text-primary);
    border:1px solid var(--glass-border);
    border-radius:60px;
    font-size:1.1rem;
    transition:all 0.8s;
    font-family:inherit;
    box-shadow:var(--shadow-main);
}
.search-box input:focus {
    outline:none;
    border-color:var(--accent-2);
    transform:scale(1.03);
}
.search-box input::placeholder {
    color:var(--text-secondary);
    opacity:0.4;
}
.search-box button {
    padding:20px 50px;
    background:var(--gradient-main);
    background-size:300% 300%;
    animation:gradientMove 4s ease-in-out infinite;
    color:white;
    border:none;
    border-radius:60px;
    font-size:1.1rem;
    cursor:pointer;
    transition:all 0.8s;
    font-family:inherit;
    font-weight:700;
    box-shadow:0 15px 60px rgba(108,92,231,0.3);
    display:flex;
    align-items:center;
    gap:12px;
}
.search-box button:hover {
    transform:translateY(-8px) scale(1.05);
    box-shadow:0 25px 80px rgba(108,92,231,0.5);
}
.reset-btn {
    padding:20px 35px;
    background:rgba(255,107,107,0.12);
    backdrop-filter:blur(25px);
    color:var(--accent-1);
    border:1px solid rgba(255,107,107,0.15);
    border-radius:60px;
    font-size:1.1rem;
    cursor:pointer;
    transition:all 0.8s;
    font-family:inherit;
    text-decoration:none;
    display:inline-flex;
    align-items:center;
    gap:10px;
    box-shadow:var(--shadow-main);
}
.reset-btn:hover {
    transform:translateY(-8px) scale(1.05);
    background:rgba(255,107,107,0.2);
}
@media (max-width:768px) {
    .search-box input { max-width:100%; width:100%; padding:14px 22px; font-size:0.95rem; }
    .search-box button { width:100%; justify-content:center; padding:14px; font-size:0.95rem; }
    .reset-btn { width:100%; justify-content:center; padding:14px; font-size:0.95rem; }
}
@media (max-width:480px) {
    .search-box input { padding:12px 18px; font-size:0.85rem; height:44px; }
    .search-box button { padding:12px 18px; font-size:0.85rem; height:44px; }
    .reset-btn { padding:12px 18px; font-size:0.85rem; height:44px; }
}
</style>''')
    print("✅ search.html ایجاد شد")

    # ===== فایل card.html (بدون loop) =====
    with open('templates/card.html', 'w', encoding='utf-8') as f:
        f.write('''<div class="card" onmousemove="cardGlow(event, this)" onmouseleave="cardReset(this)">
    <div class="card-avatar"><i class="fas {{ icons[anim_index % icons|length] }}"></i></div>
    <div class="card-info">
        <div class="card-title">
            <span class="card-number">#{{ anim_index + 1 }}</span>
            {{ anim.title }}
            {% if anim_index < 3 %}<span class="badge-new">جدید</span>{% endif %}
        </div>
        <div class="card-description"><i class="fas fa-circle"></i> {{ anim.description }}</div>
    </div>
    <a href="{{ anim.url }}" target="_blank" class="btn-watch"><i class="fas fa-play"></i> تماشا</a>
</div>
<style>
.card {
    background:var(--glass-main);
    backdrop-filter:blur(30px);
    border-radius:var(--radius-main);
    padding:18px 26px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    transition:all 0.8s;
    border:1px solid var(--glass-border);
    box-shadow:var(--shadow-main);
    position:relative;
    overflow:hidden;
    animation:cardSlide 0.7s ease forwards;
    opacity:0;
    gap:20px;
    height:120px;
    min-height:120px;
    max-height:120px;
    cursor:default;
}
.card::before {
    content:'';
    position:absolute;
    inset:0;
    background:radial-gradient(circle at var(--mouse-x,50%) var(--mouse-y,50%), rgba(255,255,255,0.1) 0%, transparent 60%);
    transition:0.3s;
    pointer-events:none;
    border-radius:var(--radius-main);
}
.card::after {
    content:'';
    position:absolute;
    inset:-1px;
    border-radius:var(--radius-main);
    padding:1px;
    background:conic-gradient(from var(--angle,0deg), #ff6b6b, #4ecdc4, #a29bfe, #fdcb6e, #ff6b6b);
    -webkit-mask:linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite:xor;
    mask-composite:exclude;
    opacity:0;
    transition:all 0.8s;
}
.card:hover::after {
    opacity:1;
    animation:spinBorder 2s linear infinite;
}
@keyframes spinBorder {
    from { --angle:0deg; }
    to { --angle:360deg; }
}
@property --angle {
    syntax:'<angle>';
    initial-value:0deg;
    inherits:false;
}
.card:hover {
    transform:translateY(-10px) scale(1.03);
    border-color:transparent;
}
@keyframes cardSlide {
    from { opacity:0; transform:translateY(60px) scale(0.85); }
    to { opacity:1; transform:translateY(0) scale(1); }
}
.card-avatar {
    width:55px;
    height:55px;
    min-width:55px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:1.6rem;
    color:white;
    background:var(--gradient-main);
    background-size:300% 300%;
    animation:gradientMove 4s ease-in-out infinite;
    box-shadow:0 15px 50px rgba(0,0,0,0.4);
    transition:all 0.8s;
}
.card:hover .card-avatar {
    transform:scale(1.2) rotate(-15deg);
}
.card-info {
    display:flex;
    flex-direction:column;
    gap:5px;
    flex:1;
    min-width:0;
    overflow:hidden;
}
.card-title {
    font-size:1.05rem;
    font-weight:700;
    color:var(--text-primary);
    display:flex;
    align-items:center;
    gap:12px;
    flex-wrap:wrap;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
}
.card-number {
    font-size:0.7rem;
    color:var(--text-secondary);
    background:var(--glass-main);
    padding:2px 16px;
    border-radius:20px;
    font-weight:700;
    min-width:38px;
    text-align:center;
    border:1px solid var(--glass-border);
    flex-shrink:0;
}
.card-description {
    font-size:0.85rem;
    color:var(--text-secondary);
    display:flex;
    align-items:center;
    gap:8px;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
}
.card-description i {
    color:var(--accent-2);
    font-size:0.4rem;
    flex-shrink:0;
}
.btn-watch {
    background:var(--gradient-main);
    background-size:300% 300%;
    animation:gradientMove 4s ease-in-out infinite;
    color:white;
    border:none;
    padding:12px 32px;
    border-radius:60px;
    font-size:0.9rem;
    cursor:pointer;
    text-decoration:none;
    transition:all 0.8s;
    font-family:inherit;
    font-weight:700;
    white-space:nowrap;
    display:flex;
    align-items:center;
    gap:10px;
    box-shadow:0 15px 50px rgba(108,92,231,0.3);
    flex-shrink:0;
    height:44px;
}
.btn-watch:hover {
    transform:scale(1.15) translateY(-5px);
    box-shadow:0 25px 70px rgba(108,92,231,0.5);
}
.badge-new {
    background:var(--gradient-main);
    background-size:300% 300%;
    animation:gradientMove 3s ease-in-out infinite;
    color:white;
    font-size:0.6rem;
    padding:2px 14px;
    border-radius:20px;
    font-weight:700;
    flex-shrink:0;
}
@media (max-width:768px) {
    .card { padding:12px 16px; gap:12px; height:100px; min-height:100px; max-height:100px; }
    .card-avatar { width:42px; height:42px; min-width:42px; font-size:1.2rem; }
    .card-title { font-size:0.85rem; white-space:normal; }
    .card-description { font-size:0.7rem; white-space:normal; }
    .btn-watch { padding:8px 20px; font-size:0.75rem; height:36px; }
}
@media (max-width:480px) {
    .card { padding:10px 14px; gap:10px; height:85px; min-height:85px; max-height:85px; }
    .card-avatar { width:34px; height:34px; min-width:34px; font-size:1rem; }
    .card-title { font-size:0.75rem; gap:6px; }
    .card-number { font-size:0.55rem; padding:1px 10px; min-width:28px; }
    .card-description { font-size:0.6rem; }
    .btn-watch { font-size:0.65rem; padding:6px 14px; height:30px; }
    .badge-new { font-size:0.5rem; padding:1px 8px; }
}
</style>''')
    print("✅ card.html ایجاد شد")

    # ===== فایل empty.html =====
    with open('templates/empty.html', 'w', encoding='utf-8') as f:
        f.write('''<div class="empty-message">
    <i class="fas fa-sad-tear"></i>
    <h3>😕 انیمیشنی پیدا نشد</h3>
    <p>کلمه دیگری جستجو کنید یا <a href="/">به صفحه اصلی</a> برگردید</p>
</div>
<style>
.empty-message {
    text-align:center;
    padding:80px 20px;
    color:var(--text-secondary);
}
.empty-message i {
    font-size:5rem;
    color:var(--accent-2);
    margin-bottom:25px;
    display:block;
}
.empty-message h3 {
    font-size:2rem;
    margin-bottom:12px;
    color:var(--text-primary);
}
.empty-message a {
    color:var(--accent-2);
    text-decoration:none;
    font-weight:600;
}
@media (max-width:480px) {
    .empty-message h3 { font-size:1.2rem; }
    .empty-message i { font-size:3rem; }
}
</style>''')
    print("✅ empty.html ایجاد شد")

    # ===== فایل footer.html =====
    with open('templates/footer.html', 'w', encoding='utf-8') as f:
        f.write('''<div class="footer">
    <div class="social">
        <a href="#"><i class="fab fa-telegram"></i></a>
        <a href="#"><i class="fab fa-instagram"></i></a>
        <a href="#"><i class="fab fa-youtube"></i></a>
        <a href="#"><i class="fab fa-github"></i></a>
    </div>
    <p>تمام ویدیوها از <a href="https://www.aparat.com" target="_blank">آپارات</a> | ساخته شده با <span class="heart">❤️</span> با Flask</p>
    <p class="mt-3 op-4 fs-small"><i class="fas fa-code"></i> نسخه ۵.۰ | ۱۴۰۴</p>
</div>
<style>
.footer {
    text-align:center;
    margin-top:50px;
    padding:40px 20px 30px;
    border-top:1px solid var(--glass-border);
    color:var(--text-secondary);
    font-size:0.95rem;
    position:relative;
}
.footer::before {
    content:'';
    position:absolute;
    top:-1px; left:0; right:0;
    height:2px;
    background:var(--gradient-main);
    background-size:300% 300%;
    animation:gradientMove 4s ease-in-out infinite;
}
.footer .social {
    display:flex;
    justify-content:center;
    gap:25px;
    margin-bottom:20px;
}
.footer .social a {
    color:var(--text-secondary);
    font-size:2rem;
    transition:all 0.8s;
}
.footer .social a:hover {
    color:var(--accent-2);
    transform:translateY(-8px) scale(1.2);
}
.footer a {
    color:var(--accent-2);
    text-decoration:none;
    font-weight:600;
}
.footer .heart {
    color:var(--accent-1);
    display:inline-block;
    animation:heartBeat 1.5s infinite;
}
@keyframes heartBeat {
    0%,100% { transform:scale(1); }
    50% { transform:scale(1.5); }
}
@media (max-width:480px) {
    .footer { font-size:0.75rem; padding:25px 10px 15px; }
    .footer .social a { font-size:1.4rem; }
}
</style>''')
    print("✅ footer.html ایجاد شد")

    # ===== فایل index.html (نسخه درست) =====
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write('''{% extends 'base.html' %}

{% block title %}🎬 سینمای انیمیشن{% endblock %}

{% block content %}

{% include 'header.html' %}
{% include 'search.html' %}

<div class="result-count">
    <i class="fas fa-list-ul"></i>
    <strong>{{ result_count }}</strong> انیمیشن پیدا شد
    {% if search_query %}
    <span class="op-4">(از {{ total_count }} انیمیشن)</span>
    {% endif %}
</div>

<div class="animations-list">
    {% if animations %}
        {% for anim in animations %}
            {% set anim_index = loop.index0 %}
            {% include 'card.html' %}
        {% endfor %}
    {% else %}
        {% include 'empty.html' %}
    {% endif %}
</div>

{% include 'footer.html' %}

{% endblock %}

<style>
.result-count {
    text-align:center;
    color:var(--text-secondary);
    margin-bottom:30px;
    font-size:1.05rem;
}
.result-count strong {
    color:#fff;
    font-size:1.3rem;
    font-weight:900;
}
.animations-list {
    display:flex;
    flex-direction:column;
    gap:18px;
    max-height:700px;
    overflow-y:auto;
    padding-right:5px;
}
.animations-list::-webkit-scrollbar {
    width:8px;
}
.animations-list::-webkit-scrollbar-track {
    background:var(--glass-main);
    border-radius:10px;
}
.animations-list::-webkit-scrollbar-thumb {
    background:var(--gradient-main);
    border-radius:10px;
}
@media (max-width:768px) {
    .animations-list { max-height:500px; gap:12px; }
}
@media (max-width:480px) {
    .animations-list { gap:10px; max-height:400px; }
}
</style>''')
    print("✅ index.html ایجاد شد")

    print("\n✅ همه فایل‌های HTML با موفقیت ساخته شدند!")

# ============================================
# دیتای انیمیشن‌ها
# ============================================

animations = [
    {"title": "شکارچیان شیطان کی پاپ (دوبله فارسی)", "url": "https://www.aparat.com/v/isc04sq", "description": "انیمیشن دوبله فارسی با ۳۱۲,۹۲۷ بازدید"},
    {"title": "بچهمرشد ۲ (ماجراهای نوید)", "url": "https://www.aparat.com/v/dhh5g3x", "description": "پویانمایی ایرانی جدید با ۱۹۸,۲۱۷ بازدید"},
    {"title": "گروه شب نقاب", "url": "https://www.aparat.com/v/kjmgeh5", "description": "انیمیشن با ۱۳۱,۱۸۷ بازدید"},
    {"title": "کارتون موزیکال ماشین ها", "url": "https://www.aparat.com/v/vlrw569", "description": "کارتون موزیکال با ۱۰۱,۲۰۸ بازدید"},
    {"title": "انیمیشن جدید دوست (دوبله فارسی ۲۰۲۵)", "url": "https://www.aparat.com/v/gvzgs3s", "description": "انیمیشن دوبله فارسی با ۸۷,۲۹۰ بازدید"},
    {"title": "لوراکس (دوبله فارسی)", "url": "https://www.aparat.com/v/o5713f0", "description": "انیمیشن سینمایی محبوب"},
    {"title": "شرک ۱ (دوبله فارسی)", "url": "https://www.aparat.com/v/kud96x1", "description": "انیمیشن سینمایی محبوب با ۸۵,۷۲۶ بازدید"},
    {"title": "توییت ها (دوبله فارسی ۲۰۲۶)", "url": "https://www.aparat.com/v/hnhbspi", "description": "انیمیشن کمدی با ۱۵,۵۲۵ بازدید"},
    {"title": "دهکده حیوانات (کارتون دهه شصت)", "url": "https://www.aparat.com/v/oR357", "description": "کارتون قدیمی با ۱۳,۹۰۹ بازدید"},
    {"title": "انیمیشن شیر", "url": "https://www.aparat.com/v/y58oi63", "description": "انیمیشن با ۹,۲۵۳ بازدید"},
    {"title": "ضرب اعداد اعشاری (انیمیشن آموزشی)", "url": "https://www.aparat.com/v/8IAZP", "description": "آموزشی ریاضی با ۶,۹۰۷ بازدید"},
    {"title": "کارتون موش کوهستان", "url": "https://www.aparat.com/v/s638w9i", "description": "کارتون دهه شصتی با ۳,۳۱۲ بازدید"},
    {"title": "آناستازیا (دوبله فارسی)", "url": "https://www.aparat.com/v/x629mjq", "description": "انیمیشن سینمایی کلاسیک"},
    {"title": "پینوکیو (دوبله فارسی)", "url": "https://www.aparat.com/v/a62gl9p", "description": "انیمیشن کلاسیک ۱۹۴۰"},
    {"title": "افسانه جومونگ (سریال) - قسمت ۶", "url": "https://www.aparat.com/v/q322453", "description": "سریال انیمیشنی دوبله فارسی با ۳۱۷,۲۸۵ بازدید"},
    {"title": "تام سخنگو", "url": "https://www.aparat.com/v/mnn72k1", "description": "کارتون گربه سخنگو با ۲۹,۲۴۹ بازدید"}
]

# ============================================
# اجرای برنامه
# ============================================

@app.route('/')
def index():
    search_query = request.args.get('search', '').strip()
    
    if search_query:
        filtered = [a for a in animations if search_query.lower() in a['title'].lower() or search_query.lower() in a.get('description', '').lower()]
    else:
        filtered = animations
    
    return render_template('index.html', 
                         animations=filtered,
                         total_count=len(animations),
                         result_count=len(filtered),
                         search_query=search_query,
                         icons=['fa-film', 'fa-video', 'fa-tv', 'fa-play', 'fa-star', 'fa-music', 'fa-crown', 'fa-rocket'])

# ============================================
# اجرای اصلی
# ============================================

if __name__ == '__main__':
    print("="*60)
    print("🎬 سینمای انیمیشن - راه‌اندازی خودکار")
    print("="*60)
    
    create_templates()
    
    print("\n" + "="*60)
    print("🚀 سرور در حال اجرا...")
    print("📍 آدرس: http://127.0.0.1:5000")
    print("="*60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)