from pathlib import Path
from datetime import datetime

PHONE = "010-4720-3895"
BASE_URL = "https://gyeonggi-gajogae-waste.vercel.app"

SEOUL_WASTE_URL = "#"
GYEONGGI_YUPUM_URL = "#"
SEOUL_YUPUM_URL = "#"

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

SERVICE_TYPES = [
    ("가정폐기물처리", "생활가구, 오래된 짐, 생활폐기물 정리"),
    ("이사폐기물처리", "이사 후 남은 가구와 잔짐 정리"),
    ("쓰레기집청소", "혼자 정리하기 어려운 생활폐기물 정리"),
    ("빈집정리", "오래 비어 있던 공간의 잔여 물품 정리"),
    ("폐업폐기물처리", "매장, 사무실, 창고 집기와 폐기물 정리"),
]

def img_num(i, max_num):
    return (i % max_num) + 1

def region_links(current_slug):
    links = []
    for slug, name in REGIONS:
        if slug != current_slug:
            links.append(f'<a href="/regions/{slug}/">{name} 폐기물처리</a>')
    return "\n".join(links)

def layout(title, desc, body, canonical):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{canonical}" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" href="/images/main/favicon.png" />

  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="/images/main/og-image.png" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canonical}" />

  <link rel="stylesheet" href="/css/style.css" />

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "경기 가족애 폐기물처리",
    "telephone": "{PHONE}",
    "areaServed": "경기도",
    "url": "{BASE_URL}",
    "image": "{BASE_URL}/images/main/og-image.png",
    "description": "{desc}"
  }}
  </script>
</head>

<body>
<header class="top-bar">
  <div class="top-inner">
    <span>경기 전지역 폐기물처리 · 가정폐기물 · 이사폐기물 · 쓰레기집청소</span>
    <strong>상담전화 {PHONE}</strong>
  </div>
</header>

<header class="site-header">
  <a href="/" class="logo">
    <strong>가족애폐기물처리</strong>
    <span>경기 폐기물처리 전문 상담</span>
  </a>

  <nav>
    <a href="/">메인</a>
    <a href="/#service">서비스</a>
    <a href="/#price">비용</a>
    <a href="/reviews/">작업후기</a>
    <a href="/#regions">지역별 안내</a>
    <a href="/#contact">상담접수</a>
  </nav>

  <a class="header-call" href="tel:{PHONE}">{PHONE}</a>
</header>

{body}

<footer class="site-footer">
  <div>
    <strong>가족애폐기물처리</strong>
    <p>경기 전지역 폐기물처리 상담 · 대표번호 {PHONE}</p>
    <p>
      <a href="{SEOUL_WASTE_URL}">서울 가족애폐기물처리</a>
      <a href="{GYEONGGI_YUPUM_URL}">경기 가족애유품정리</a>
      <a href="{SEOUL_YUPUM_URL}">서울 가족애유품정리</a>
    </p>
  </div>
</footer>

<a class="floating-call" href="tel:{PHONE}">전화상담 {PHONE}</a>
<script src="/js/contact.js"></script>
</body>
</html>"""

contact_form = f"""
<section id="contact" class="section contact-wrap">
  <div class="contact-info">
    <h2>경기 폐기물처리 상담 접수</h2>
    <p>사진, 주소, 폐기물 양을 남겨주시면 확인 후 연락드립니다.</p>
    <strong>{PHONE}</strong>
    <ul>
      <li>✓ 가정폐기물 · 이사폐기물</li>
      <li>✓ 쓰레기집청소 · 빈집정리</li>
      <li>✓ 폐업폐기물 · 사무실 집기정리</li>
    </ul>
  </div>

  <form id="contactForm" class="contact-form">
    <label>성함 <input type="text" name="name" placeholder="예: 홍길동" required /></label>
    <label>연락처 <input type="tel" name="phone" placeholder="예: 010-0000-0000" required /></label>
    <label>현장 주소 <input type="text" name="region" placeholder="예: 수원시 영통구" required /></label>

    <label>필요 서비스
      <select name="service" required>
        <option value="가정폐기물처리">가정폐기물처리</option>
        <option value="이사폐기물처리">이사폐기물처리</option>
        <option value="쓰레기집청소">쓰레기집청소</option>
        <option value="빈집정리">빈집정리</option>
        <option value="폐업폐기물처리">폐업폐기물처리</option>
      </select>
    </label>

    <label>문의 내용
      <textarea name="message" placeholder="폐기물 양, 엘리베이터 여부, 방문 희망일 등을 남겨주세요."></textarea>
    </label>

    <label class="agree"><input type="checkbox" required /> 상담 접수를 위한 개인정보 수집 및 이용에 동의합니다.</label>
    <button type="submit">상담 접수하기</button>
    <p id="formMessage" class="form-message"></p>
  </form>
</section>
"""

Path("regions").mkdir(exist_ok=True)

# regions/index.html 생성
overview_links = "\n".join([f'<a href="/regions/{slug}/">{name} 폐기물처리</a>' for slug, name in REGIONS])
overview_body = f"""
<main>
<section class="sub-hero">
  <div class="sub-hero-inner">
    <p class="hero-badge">경기 31개 시·군</p>
    <h1>경기도 지역별 폐기물처리 안내</h1>
    <p>수원, 성남, 고양, 용인, 화성, 남양주 등 경기도 각 지역별 폐기물처리 안내 페이지입니다.</p>
  </div>
</section>

<section class="section">
  <p class="section-label">처리 가능 지역</p>
  <h2>경기도 전지역 폐기물처리</h2>
  <div class="region-grid">
    {overview_links}
  </div>
</section>

{contact_form}
</main>
"""
Path("regions/index.html").write_text(
    layout(
        "경기도 폐기물처리 지역별 안내 | 가족애폐기물처리",
        "경기도 31개 시군 폐기물처리 지역별 안내. 가정폐기물, 이사폐기물, 쓰레기집청소, 빈집정리 상담.",
        overview_body,
        f"{BASE_URL}/regions/"
    ),
    encoding="utf-8"
)

for idx, (slug, name) in enumerate(REGIONS, start=1):
    service_name, service_desc = SERVICE_TYPES[idx % len(SERVICE_TYPES)]
    b = img_num(idx, 30)
    p = img_num(idx * 3, 25)
    a = b

    title = f"{name} 폐기물처리 | 가족애폐기물처리 경기"
    desc = f"{name} 폐기물처리, 가정폐기물, 이사폐기물, 쓰레기집청소, 빈집정리 상담. 경기 가족애폐기물처리 {PHONE}"

    body = f"""
<main>
<section class="sub-hero">
  <div class="sub-hero-inner">
    <p class="hero-badge">{name} 폐기물처리 상담</p>
    <h1>{name} 폐기물처리</h1>
    <p>
      {name} 지역의 가정폐기물, 이사폐기물, 쓰레기집청소, 빈집정리,
      폐업폐기물까지 현장 상황에 맞춰 상담합니다.
    </p>
    <div class="hero-actions">
      <a href="tel:{PHONE}">전화 상담하기</a>
      <a href="#contact">상담 접수하기</a>
    </div>
  </div>
</section>

<section class="section text-section">
  <p class="section-label">지역 안내</p>
  <h2>{name} 폐기물처리, 현장 구조를 먼저 확인합니다</h2>
  <p>
    {name} 폐기물처리는 폐기물의 양만 보고 결정하기 어렵습니다.
    아파트, 빌라, 단독주택, 상가, 사무실처럼 현장 구조가 다르고
    차량 진입 가능 여부와 엘리베이터 사용 여부에 따라 작업 방식이 달라질 수 있습니다.
  </p>
  <p>
    가족애폐기물처리는 {name} 현장의 폐기물 종류, 반출 동선, 층수,
    작업 인원을 함께 확인한 뒤 필요한 범위만 안내합니다.
    {service_name}처럼 현장마다 정리해야 할 물품이 다를 수 있어
    상담 단계에서 사진과 주소를 함께 확인하는 것이 좋습니다.
  </p>
</section>

<section class="section">
  <p class="section-label">주요 업무</p>
  <h2>{name} 폐기물처리 주요 서비스</h2>
  <div class="card-grid service-grid">
    <article><h3>가정폐기물처리</h3><p>생활가구, 생활용품, 잡동사니, 오래된 짐을 정리합니다.</p></article>
    <article><h3>이사폐기물처리</h3><p>이사 후 남은 대형가구와 잔짐을 분류하고 반출합니다.</p></article>
    <article><h3>쓰레기집청소</h3><p>혼자 정리하기 어려운 생활폐기물 현장을 단계적으로 정리합니다.</p></article>
    <article><h3>빈집정리</h3><p>오래 비어 있던 공간의 잔여 물품과 폐기물을 정리합니다.</p></article>
    <article><h3>폐업폐기물처리</h3><p>매장, 창고, 사무실 정리 후 남은 집기를 처리합니다.</p></article>
  </div>
</section>

<section class="section price-wrap">
  <div class="price-main">
    <p class="section-label">비용 안내</p>
    <h2>{name} 폐기물처리 비용은<br />기본 25만원부터입니다</h2>
    <strong>25만원부터</strong>
    <p>
      실제 비용은 폐기물 양, 차량 대수, 층수, 엘리베이터 여부,
      차량 진입 가능 여부에 따라 달라질 수 있습니다.
    </p>
  </div>

  <div class="price-points">
    <p>✓ 현장 사진을 보내주시면 대략적인 비용 안내가 쉽습니다.</p>
    <p>✓ {name} 지역의 건물 구조와 반출 동선을 함께 확인합니다.</p>
    <p>✓ 대형가구, 생활폐기물, 잔짐을 함께 상담할 수 있습니다.</p>
    <p>✓ 작업 전 비용 기준과 진행 순서를 안내합니다.</p>
  </div>
</section>

<section class="section">
  <p class="section-label">진행 과정</p>
  <h2>{name} 폐기물처리 진행 과정</h2>
  <div class="process-grid">
    <article><span>01</span><h3>상담 접수</h3><p>주소, 폐기물 종류, 대략적인 양을 확인합니다.</p></article>
    <article><span>02</span><h3>현장 확인</h3><p>차량 진입, 층수, 엘리베이터 여부를 확인합니다.</p></article>
    <article><span>03</span><h3>분리 정리</h3><p>가구, 생활폐기물, 잔짐을 작업 순서에 맞게 정리합니다.</p></article>
    <article><span>04</span><h3>반출 마무리</h3><p>폐기물 반출 후 현장을 정돈합니다.</p></article>
  </div>
</section>

<section class="section photo-section">
  <p class="section-label">현장사진</p>
  <h2>{name} 폐기물처리 전·중·후 사진</h2>
  <p class="section-desc">전·후 사진은 같은 번호를 사용하고, 작업 중 사진은 현장 흐름에 맞게 배치했습니다.</p>

  <div class="photo-grid">
    <img src="/images/main/before-{b:02d}.jpg" alt="{name} 폐기물처리 작업 전" />
    <img src="/images/main/process-{p:02d}.jpg" alt="{name} 폐기물처리 작업 중" />
    <img src="/images/main/after-{a:02d}.jpg" alt="{name} 폐기물처리 작업 후" />
  </div>
</section>

<section class="section">
  <p class="section-label">작업후기</p>
  <h2>{name} 관련 작업후기</h2>
  <div class="case-grid">
    <article>
      <span>{service_name}</span>
      <h3>{name} {service_name} 작업후기</h3>
      <p>{service_desc} 현장을 기준으로 정리 전, 작업 중, 수거 후 흐름을 확인할 수 있습니다.</p>
      <a href="/reviews/">지역별 작업후기 전체보기</a>
    </article>
  </div>
</section>

<section class="section">
  <p class="section-label">인근 지역</p>
  <h2>{name} 주변 폐기물처리 가능 지역</h2>
  <div class="region-grid">
    {region_links(slug)}
  </div>
</section>

{contact_form}

<section class="section faq-section">
  <p class="section-label">자주 묻는 질문</p>
  <h2>{name} 폐기물처리 FAQ</h2>

  <article>
    <h3>{name} 폐기물처리 비용은 얼마부터인가요?</h3>
    <p>기본 비용은 25만원부터이며 폐기물 양, 차량 대수, 층수, 작업 인원에 따라 달라질 수 있습니다.</p>
  </article>
  <article>
    <h3>{name} 지역도 사진 상담이 가능한가요?</h3>
    <p>가능합니다. 현장 사진, 주소, 엘리베이터 여부, 폐기물 양을 알려주시면 상담이 더 정확해집니다.</p>
  </article>
  <article>
    <h3>가구와 생활폐기물을 함께 정리할 수 있나요?</h3>
    <p>대형가구, 생활용품, 이사 후 남은 짐, 빈집 잔여 물품까지 현장 상황에 맞춰 상담 가능합니다.</p>
  </article>
</section>

<section class="section family-links">
  <p class="section-label">가족애 관련 서비스</p>
  <h2>서울·경기 가족애 서비스 바로가기</h2>
  <div class="family-grid">
    <a href="{SEOUL_WASTE_URL}">서울 가족애폐기물처리</a>
    <a href="{GYEONGGI_YUPUM_URL}">경기 가족애유품정리</a>
    <a href="{SEOUL_YUPUM_URL}">서울 가족애유품정리</a>
  </div>
</section>
</main>
"""
    folder = Path("regions") / slug
    folder.mkdir(exist_ok=True)
    (folder / "index.html").write_text(
        layout(title, desc, body, f"{BASE_URL}/regions/{slug}/"),
        encoding="utf-8"
    )

print("지역페이지 생성 완료: regions/index.html + 31개 지역페이지")