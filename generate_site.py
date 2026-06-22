from pathlib import Path
from datetime import datetime

SITE_NAME = "경기 가족애 폐기물처리"
PHONE = "010-4720-3895"
BASE_URL = "https://gyeonggi-gajogae-waste.vercel.app"

REGIONS = [
    ("suwon", "수원시"), ("seongnam", "성남시"), ("goyang", "고양시"),
    ("yongin", "용인시"), ("bucheon", "부천시"), ("ansan", "안산시"),
    ("anyang", "안양시"), ("namyangju", "남양주시"), ("hwaseong", "화성시"),
    ("pyeongtaek", "평택시"), ("uijeongbu", "의정부시"), ("siheung", "시흥시"),
    ("paju", "파주시"), ("gimpo", "김포시"), ("gwangmyeong", "광명시"),
    ("gwangju", "광주시"), ("gunpo", "군포시"), ("hanam", "하남시"),
    ("osan", "오산시"), ("icheon", "이천시"), ("anseong", "안성시"),
    ("uiwang", "의왕시"), ("yangju", "양주시"), ("guri", "구리시"),
    ("pocheon", "포천시"), ("yeoju", "여주시"), ("dongducheon", "동두천시"),
    ("gwacheon", "과천시"), ("gapyeong", "가평군"), ("yangpyeong", "양평군"),
    ("yeoncheon", "연천군")
]

REVIEWS = [
    ("suwon-review-01", "수원시 원룸 폐기물처리 작업후기", "수원시"),
    ("seongnam-review-01", "성남시 아파트 폐기물처리 작업후기", "성남시"),
    ("goyang-review-01", "고양시 빈집정리 폐기물처리 작업후기", "고양시"),
    ("yongin-review-01", "용인시 가정폐기물 처리 작업후기", "용인시"),
    ("bucheon-review-01", "부천시 이사폐기물 처리 작업후기", "부천시"),
    ("ansan-review-01", "안산시 쓰레기집청소 작업후기", "안산시"),
    ("namyangju-review-01", "남양주시 폐기물처리 작업후기", "남양주시"),
    ("hwaseong-review-01", "화성시 폐업폐기물 처리 작업후기", "화성시"),
]

Path("css").mkdir(exist_ok=True)
Path("js").mkdir(exist_ok=True)
Path("regions").mkdir(exist_ok=True)
Path("reviews").mkdir(exist_ok=True)
Path("images/main").mkdir(parents=True, exist_ok=True)
Path("images/cases").mkdir(parents=True, exist_ok=True)


def layout(title, description, body, canonical):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/png" href="/images/main/favicon.png">

<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="/images/main/og-image.png">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="/images/main/og-image.png">

<link rel="stylesheet" href="/css/style.css">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "{SITE_NAME}",
  "telephone": "{PHONE}",
  "areaServed": "경기도",
  "url": "{BASE_URL}",
  "image": "{BASE_URL}/images/main/og-image.png",
  "description": "{description}"
}}
</script>
</head>
<body>
<header class="site-header">
  <a href="/" class="logo">가족애 폐기물처리</a>
  <nav>
    <a href="/#service">서비스</a>
    <a href="/#regions">지역</a>
    <a href="/#reviews">작업후기</a>
    <a href="/#contact">상담접수</a>
  </nav>
  <a class="phone" href="tel:{PHONE}">{PHONE}</a>
</header>

{body}

<footer class="site-footer">
  <p><strong>경기 가족애 폐기물처리</strong> | 상담전화 <a href="tel:{PHONE}">{PHONE}</a></p>
  <p class="links">
    <a href="/">경기 가족애 폐기물처리</a>
    <a href="https://seoul-gajogae-waste.vercel.app">서울 가족애폐기물처리</a>
    <a href="https://gajogae-waste.vercel.app">가족애폐기물처리</a>
  </p>
</footer>

<a class="floating-call" href="tel:{PHONE}">전화상담 {PHONE}</a>
<script src="/js/contact.js"></script>
</body>
</html>"""


contact_form = f"""
<section id="contact" class="contact-section">
  <h2>경기 폐기물처리 상담접수</h2>
  <p>상담 접수 후 담당자가 확인하여 순차적으로 연락드립니다.</p>

  <form id="contactForm" class="contact-form">
    <input type="text" name="name" placeholder="성함" required>
    <input type="tel" name="phone" placeholder="연락처" required>
    <input type="text" name="region" placeholder="작업지역 예: 수원시, 성남시" required>
    <select name="service" required>
      <option value="">서비스 선택</option>
      <option>가정폐기물처리</option>
      <option>쓰레기집청소</option>
      <option>빈집정리</option>
      <option>이사폐기물</option>
      <option>폐업폐기물</option>
    </select>
    <textarea name="message" placeholder="현장 상황을 간단히 적어주세요."></textarea>
    <label class="agree">
      <input type="checkbox" required>
      개인정보 수집 및 상담 목적 이용에 동의합니다.
    </label>
    <button type="submit">상담접수하기</button>
    <p id="formMessage" class="form-message"></p>
  </form>
</section>
"""


def region_links(current=None):
    html = '<div class="region-grid">'
    for slug, name in REGIONS:
        if slug != current:
            html += f'<a href="/regions/{slug}/">{name} 폐기물처리</a>'
    html += '</div>'
    return html


def review_cards():
    html = '<div class="review-grid">'
    for slug, title, region in REVIEWS:
        html += f"""
        <article class="card">
          <img src="/images/cases/waste-after-001.jpg" alt="{title}">
          <h3>{title}</h3>
          <p>{region} 현장의 폐기물 분류, 수거, 마무리 정리까지 진행한 작업후기입니다.</p>
          <a href="/reviews/{slug}.html">작업후기 보기</a>
        </article>
        """
    html += '</div>'
    return html


main_body = f"""
<section class="hero">
  <div class="hero-inner">
    <p class="eyebrow">경기도 전지역 폐기물처리</p>
    <h1>경기 가족애 폐기물처리</h1>
    <p>가정폐기물, 쓰레기집청소, 빈집정리, 이사폐기물, 폐업폐기물까지 현장 상황에 맞게 정리합니다.</p>
    <div class="hero-buttons">
      <a href="tel:{PHONE}">전화상담 {PHONE}</a>
      <a href="#contact">상담접수</a>
    </div>
  </div>
</section>

<section id="service" class="section">
  <h2>경기 폐기물처리 주요 서비스</h2>
  <div class="service-grid">
    <div><h3>가정폐기물처리</h3><p>생활가구, 생활폐기물, 정리 후 남은 물품을 수거합니다.</p></div>
    <div><h3>쓰레기집청소</h3><p>혼자 정리하기 어려운 현장을 분류와 수거 중심으로 정돈합니다.</p></div>
    <div><h3>빈집정리</h3><p>장기간 방치된 공간의 폐기물과 잔여 물품을 정리합니다.</p></div>
    <div><h3>폐업폐기물</h3><p>매장, 사무실, 창고 정리 후 발생하는 폐기물을 처리합니다.</p></div>
  </div>
</section>

<section class="section image-flow">
  <h2>작업 전·중·후 흐름</h2>
  <div class="photo-grid">
    <img src="/images/main/before-01.jpg" alt="경기 폐기물처리 작업 전">
    <img src="/images/main/process-01.jpg" alt="경기 폐기물처리 분류 작업">
    <img src="/images/main/process-02.jpg" alt="경기 폐기물 수거 작업">
    <img src="/images/main/after-01.jpg" alt="경기 폐기물처리 작업 후">
  </div>
</section>

<section id="regions" class="section">
  <h2>경기도 지역별 폐기물처리</h2>
  <p>경기 31개 시·군 지역페이지가 서로 연결되도록 구성했습니다.</p>
  {region_links()}
</section>

<section id="reviews" class="section">
  <h2>작업후기</h2>
  <p>작업후기는 전/후 2장 비교가 아니라 가족애 유품정리 스타일처럼 4~5장 흐름으로 구성합니다.</p>
  {review_cards()}
</section>

<section class="section faq">
  <h2>자주 묻는 질문</h2>
  <details><summary>경기도 전지역 출장이 가능한가요?</summary><p>수원, 성남, 고양, 용인, 남양주 등 경기 전지역 상담 가능합니다.</p></details>
  <details><summary>비용은 어떻게 정해지나요?</summary><p>폐기물 양, 층수, 엘리베이터, 차량 진입, 작업 인원에 따라 달라집니다.</p></details>
  <details><summary>사진으로 견적 상담이 가능한가요?</summary><p>현장 사진을 보내주시면 대략적인 상담이 가능합니다.</p></details>
</section>

{contact_form}
"""

Path("index.html").write_text(
    layout(
        "경기 가족애 폐기물처리 | 경기도 쓰레기집청소 빈집정리",
        "경기 가족애 폐기물처리. 경기도 전지역 가정폐기물, 쓰레기집청소, 빈집정리, 이사폐기물, 폐업폐기물 상담.",
        main_body,
        BASE_URL + "/"
    ),
    encoding="utf-8"
)


for i, (slug, name) in enumerate(REGIONS, start=1):
    nearby = region_links(slug)
    review = REVIEWS[i % len(REVIEWS)]
    body = f"""
<section class="sub-hero">
  <h1>{name} 폐기물처리</h1>
  <p>{name} 지역의 가정폐기물, 쓰레기집청소, 빈집정리, 이사폐기물 상담을 진행합니다.</p>
  <a href="tel:{PHONE}" class="main-btn">전화상담 {PHONE}</a>
</section>

<section class="section">
  <h2>{name} 폐기물처리 안내</h2>
  <p>{name} 현장은 아파트, 빌라, 단독주택, 상가, 사무실 등 공간 구조가 다르기 때문에 폐기물 양과 반출 동선을 함께 확인하는 것이 중요합니다.</p>
  <p>가족애 폐기물처리는 현장 상황에 맞춰 분류, 반출, 수거, 마무리 정리 순서로 진행합니다.</p>
</section>

<section class="section image-flow">
  <h2>{name} 작업 사진</h2>
  <div class="photo-grid">
    <img src="/images/main/before-{(i%30)+1:02d}.jpg" alt="{name} 폐기물처리 작업 전">
    <img src="/images/main/process-{(i%25)+1:02d}.jpg" alt="{name} 폐기물처리 작업 중">
    <img src="/images/main/process-{((i+5)%25)+1:02d}.jpg" alt="{name} 폐기물 분류 수거">
    <img src="/images/main/after-{(i%30)+1:02d}.jpg" alt="{name} 폐기물처리 작업 후">
  </div>
</section>

<section class="section">
  <h2>{name} 관련 작업후기</h2>
  <div class="review-grid">
    <article class="card">
      <img src="/images/cases/waste-after-{(i%100)+1:03d}.jpg" alt="{name} 폐기물처리 작업후기">
      <h3>{review[1]}</h3>
      <p>사진 4~5장 구성으로 작업 흐름이 자연스럽게 보이도록 정리했습니다.</p>
      <a href="/reviews/{review[0]}.html">작업후기 보기</a>
    </article>
  </div>
</section>

<section class="section">
  <h2>인근 지역 폐기물처리</h2>
  {nearby}
</section>

{contact_form}
"""
    Path(f"regions/{slug}").mkdir(exist_ok=True)
    Path(f"regions/{slug}/index.html").write_text(
        layout(
            f"{name} 폐기물처리 | 가족애 폐기물처리 경기",
            f"{name} 폐기물처리, 쓰레기집청소, 빈집정리, 가정폐기물, 이사폐기물 상담. 경기 가족애 폐기물처리.",
            body,
            f"{BASE_URL}/regions/{slug}/"
        ),
        encoding="utf-8"
    )


for idx, (slug, title, region) in enumerate(REVIEWS, start=1):
    body = f"""
<section class="sub-hero">
  <h1>{title}</h1>
  <p>{region} 현장에서 진행한 폐기물처리 작업후기입니다.</p>
  <a href="tel:{PHONE}" class="main-btn">전화상담 {PHONE}</a>
</section>

<section class="section">
  <h2>현장 상황</h2>
  <p>{region} 현장은 생활폐기물과 정리 대상 물품이 함께 남아 있어 먼저 종류별로 분류한 뒤 반출 동선을 확인했습니다.</p>
  <p>작업후기는 단순 전/후 비교가 아니라 작업 전, 분류 중, 반출 후, 마무리 상태가 자연스럽게 이어지도록 구성했습니다.</p>
</section>

<section class="section image-flow">
  <h2>작업후기 사진</h2>
  <div class="photo-grid five">
    <img src="/images/cases/waste-before-{idx:03d}.jpg" alt="{region} 폐기물처리 작업 전 1">
    <img src="/images/cases/waste-before-{idx+10:03d}.jpg" alt="{region} 폐기물처리 작업 전 2">
    <img src="/images/cases/waste-before-{idx+20:03d}.jpg" alt="{region} 폐기물 분류 전">
    <img src="/images/cases/waste-after-{idx:03d}.jpg" alt="{region} 폐기물처리 작업 후 1">
    <img src="/images/cases/waste-after-{idx+10:03d}.jpg" alt="{region} 폐기물처리 작업 후 2">
  </div>
</section>

<section class="section">
  <h2>{region} 폐기물처리 상담</h2>
  <p>비슷한 현장이라도 폐기물 양, 층수, 엘리베이터, 차량 진입 여부에 따라 작업 방식이 달라질 수 있습니다.</p>
  <a href="/regions/{[s for s,n in REGIONS if n == region][0]}/">지역페이지 보기</a>
</section>

{contact_form}
"""
    Path(f"reviews/{slug}.html").write_text(
        layout(
            f"{title} | 경기 가족애 폐기물처리",
            f"{title}. {region} 폐기물처리, 쓰레기집청소, 빈집정리 작업후기.",
            body,
            f"{BASE_URL}/reviews/{slug}.html"
        ),
        encoding="utf-8"
    )


css = """
*{box-sizing:border-box}
body{margin:0;font-family:Arial,'Noto Sans KR',sans-serif;color:#222;line-height:1.65;background:#faf8f4}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block;border-radius:18px}
.site-header{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid #eee;display:flex;align-items:center;justify-content:space-between;padding:14px 5%}
.logo{font-weight:800;font-size:20px;color:#5a3b22}
.site-header nav{display:flex;gap:18px;font-size:15px}
.phone{background:#6b4423;color:#fff;padding:10px 16px;border-radius:999px;font-weight:700}
.hero{min-height:560px;background:linear-gradient(rgba(0,0,0,.45),rgba(0,0,0,.4)),url('/images/main/main-banner.png') center/cover no-repeat;display:flex;align-items:center;color:#fff}
.hero-inner{width:min(1100px,90%);margin:auto}
.eyebrow{font-weight:700;color:#ffe3b5}
.hero h1{font-size:52px;margin:10px 0}
.hero p{font-size:20px;max-width:720px}
.hero-buttons{display:flex;gap:12px;margin-top:26px;flex-wrap:wrap}
.hero-buttons a,.main-btn,.contact-form button{background:#7a4b24;color:#fff;padding:14px 22px;border-radius:12px;font-weight:800;border:0}
.hero-buttons a:nth-child(2){background:#fff;color:#7a4b24}
.section{width:min(1120px,90%);margin:70px auto}
.section h2{font-size:34px;color:#3f2a18;margin-bottom:18px}
.service-grid,.review-grid,.region-grid,.photo-grid{display:grid;gap:18px}
.service-grid{grid-template-columns:repeat(4,1fr)}
.service-grid div,.card,.contact-section,.faq details{background:#fff;border:1px solid #eee;border-radius:20px;padding:22px;box-shadow:0 10px 25px rgba(0,0,0,.04)}
.photo-grid{grid-template-columns:repeat(4,1fr)}
.photo-grid.five{grid-template-columns:repeat(5,1fr)}
.review-grid{grid-template-columns:repeat(4,1fr)}
.region-grid{grid-template-columns:repeat(4,1fr)}
.region-grid a{background:#fff;border:1px solid #eadfce;border-radius:14px;padding:14px;text-align:center}
.sub-hero{background:#6b4423;color:#fff;text-align:center;padding:80px 5%}
.sub-hero h1{font-size:44px;margin:0 0 12px}
.contact-section{width:min(760px,90%);margin:80px auto}
.contact-form{display:grid;gap:12px}
.contact-form input,.contact-form select,.contact-form textarea{width:100%;padding:14px;border:1px solid #ddd;border-radius:10px;font-size:16px}
.contact-form textarea{min-height:120px}
.agree{font-size:14px}
.form-message{font-weight:700;color:#6b4423}
.site-footer{background:#302217;color:#fff;text-align:center;padding:36px 5%;margin-top:80px}
.site-footer .links{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.floating-call{position:fixed;right:18px;bottom:18px;background:#6b4423;color:#fff;padding:14px 18px;border-radius:999px;font-weight:800;box-shadow:0 8px 25px rgba(0,0,0,.25)}
@media(max-width:900px){
  .site-header{display:block;text-align:center}
  .site-header nav{justify-content:center;flex-wrap:wrap;margin:10px 0}
  .hero h1{font-size:38px}
  .service-grid,.review-grid,.region-grid,.photo-grid,.photo-grid.five{grid-template-columns:1fr 1fr}
}
@media(max-width:560px){
  .service-grid,.review-grid,.region-grid,.photo-grid,.photo-grid.five{grid-template-columns:1fr}
  .hero h1{font-size:32px}
}
"""
Path("css/style.css").write_text(css, encoding="utf-8")


contact_js = """
// EmailJS 설정값은 기존 가족애 폐기물처리 설정에 맞춰 교체하세요.
// service_id, template_id, public_key 3개만 바꾸면 됩니다.

const EMAILJS_SERVICE_ID = "YOUR_SERVICE_ID";
const EMAILJS_TEMPLATE_ID = "YOUR_TEMPLATE_ID";
const EMAILJS_PUBLIC_KEY = "YOUR_PUBLIC_KEY";

(function(){
  const script = document.createElement("script");
  script.src = "https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js";
  script.onload = function(){
    emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });
  };
  document.head.appendChild(script);
})();

document.addEventListener("DOMContentLoaded", function(){
  const form = document.getElementById("contactForm");
  const msg = document.getElementById("formMessage");
  if(!form) return;

  form.addEventListener("submit", function(e){
    e.preventDefault();
    msg.textContent = "접수 중입니다.";

    const data = {
      title: "[가족애폐기물처리 경기] 상담접수",
      name: form.name.value,
      phone: form.phone.value,
      region: form.region.value,
      service: form.service.value,
      message: form.message.value
    };

    emailjs.send(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, data)
      .then(function(){
        msg.textContent = "접수가 완료되었습니다. 담당자가 확인 후 연락드리겠습니다.";
        form.reset();
      })
      .catch(function(){
        msg.textContent = "접수 중 오류가 발생했습니다. 전화상담 010-4720-3895로 연락주세요.";
      });
  });
});
"""
Path("js/contact.js").write_text(contact_js, encoding="utf-8")


today = datetime.now().strftime("%Y-%m-%d")
urls = [BASE_URL + "/"]
urls += [f"{BASE_URL}/regions/{slug}/" for slug, _ in REGIONS]
urls += [f"{BASE_URL}/reviews/{slug}.html" for slug, _, _ in REVIEWS]

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in urls:
    sitemap += f"  <url><loc>{url}</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>\n"
sitemap += "</urlset>"
Path("sitemap.xml").write_text(sitemap, encoding="utf-8")

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>{SITE_NAME}</title>
<link>{BASE_URL}</link>
<description>경기 가족애 폐기물처리 작업후기와 지역별 폐기물처리 안내</description>
"""
for slug, title, region in REVIEWS:
    rss += f"""
<item>
<title>{title}</title>
<link>{BASE_URL}/reviews/{slug}.html</link>
<description>{region} 폐기물처리 작업후기</description>
<pubDate>{datetime.now().strftime("%a, %d %b %Y 00:00:00 +0900")}</pubDate>
</item>
"""
rss += """
</channel>
</rss>
"""
Path("rss.xml").write_text(rss, encoding="utf-8")

robots = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
Path("robots.txt").write_text(robots, encoding="utf-8")

vercel = """{
  "cleanUrls": true,
  "trailingSlash": true
}
"""
Path("vercel.json").write_text(vercel, encoding="utf-8")

print("경기 가족애 폐기물처리 사이트 생성 완료")
print("생성 파일: index.html, regions 31개, reviews, sitemap.xml, rss.xml, robots.txt")