from pathlib import Path
from datetime import datetime

PHONE = "010-4720-3895"
BASE_URL = "https://www.gyeonggi.gajogae-waste.com"

SEOUL_WASTE_URL = "https://www.seoul.gajogae-waste.com/"
GYEONGGI_YUPUM_URL = "https://www.gyeonggi.gajogae-yupum.com/"
SEOUL_YUPUM_URL = "https://www.seoul.gajogae-yupum.com/"

REVIEWS = [
    ("suwon-review-01", "수원시", "원룸 이사폐기물 처리", "이사폐기물처리", "이사 후 남은 가구와 생활폐기물을 정리한 현장"),
    ("seongnam-review-01", "성남시", "아파트 가정폐기물 처리", "가정폐기물처리", "오래 보관된 생활용품과 대형가구를 정리한 현장"),
    ("goyang-review-01", "고양시", "주거공간 쓰레기집청소", "쓰레기집청소", "생활폐기물이 쌓인 공간을 단계적으로 정리한 현장"),
    ("yongin-review-01", "용인시", "가정폐기물 정리", "가정폐기물처리", "가정 내 잔짐과 생활폐기물을 분류해 반출한 현장"),
    ("hwaseong-review-01", "화성시", "상가 폐업폐기물 처리", "폐업폐기물처리", "매장 정리 후 남은 집기와 폐기물을 처리한 현장"),
    ("namyangju-review-01", "남양주시", "빈집정리 폐기물 처리", "빈집정리", "오래 비어 있던 공간의 잔여 물품을 정리한 현장"),
    ("bucheon-review-01", "부천시", "이사 후 폐기물 처리", "이사폐기물처리", "이사 후 남은 대형가구와 잔짐을 정리한 현장"),
    ("ansan-review-01", "안산시", "생활폐기물 정리", "가정폐기물처리", "생활용품과 잔짐을 분류한 뒤 반출한 현장"),
    ("anyang-review-01", "안양시", "주택 폐기물처리", "가정폐기물처리", "주택 내부 정리 후 남은 폐기물을 처리한 현장"),
    ("pyeongtaek-review-01", "평택시", "창고 폐기물처리", "빈집정리", "창고에 쌓여 있던 물품과 폐기물을 정리한 현장"),
    ("gimpo-review-01", "김포시", "이사폐기물 처리", "이사폐기물처리", "이사 후 남은 가구와 생활폐기물을 정리한 현장"),
    ("hanam-review-01", "하남시", "사무실 폐기물처리", "폐업폐기물처리", "사무실 정리 후 남은 집기와 폐기물을 처리한 현장"),
    ("uijeongbu-review-01", "의정부시", "아파트 폐기물처리", "가정폐기물처리", "아파트 내부 잔짐과 대형가구를 정리한 현장"),
    ("siheung-review-01", "시흥시", "빈집 폐기물처리", "빈집정리", "빈집에 남아 있던 생활폐기물과 가구를 정리한 현장"),
    ("paju-review-01", "파주시", "주택 이사폐기물 처리", "이사폐기물처리", "이사 전후 남은 물품을 정리한 현장"),
    ("gwangmyeong-review-01", "광명시", "가정폐기물 처리", "가정폐기물처리", "생활가구와 잔짐을 함께 정리한 현장"),
    ("gwangju-review-01", "광주시", "단독주택 폐기물처리", "가정폐기물처리", "단독주택 내부와 창고 잔짐을 정리한 현장"),
    ("gunpo-review-01", "군포시", "생활폐기물 정리", "가정폐기물처리", "생활폐기물과 오래된 물품을 분류한 현장"),
    ("osan-review-01", "오산시", "이사폐기물 처리", "이사폐기물처리", "이사 후 남은 가구와 박스류를 정리한 현장"),
    ("icheon-review-01", "이천시", "창고 정리 폐기물처리", "빈집정리", "창고와 주거공간에 남은 물품을 정리한 현장"),
    ("anseong-review-01", "안성시", "가정폐기물 처리", "가정폐기물처리", "가구와 생활폐기물을 함께 반출한 현장"),
    ("uiwang-review-01", "의왕시", "아파트 잔짐 정리", "가정폐기물처리", "아파트 내 잔짐과 생활폐기물을 정리한 현장"),
    ("yangju-review-01", "양주시", "빈집정리 폐기물처리", "빈집정리", "비어 있던 공간의 가구와 폐기물을 정리한 현장"),
    ("guri-review-01", "구리시", "이사폐기물 처리", "이사폐기물처리", "이사 후 남은 대형가구와 생활용품을 정리한 현장"),
    ("pocheon-review-01", "포천시", "주택 폐기물처리", "가정폐기물처리", "주택 내부와 외부 잔짐을 정리한 현장"),
    ("yeoju-review-01", "여주시", "창고 폐기물처리", "빈집정리", "창고에 오래 보관된 물품을 정리한 현장"),
    ("dongducheon-review-01", "동두천시", "가정폐기물 정리", "가정폐기물처리", "생활폐기물과 가구를 함께 정리한 현장"),
    ("gwacheon-review-01", "과천시", "아파트 폐기물처리", "가정폐기물처리", "아파트 정리 후 남은 물품을 반출한 현장"),
    ("gapyeong-review-01", "가평군", "주택 빈집정리", "빈집정리", "주택 내 오래된 물품과 생활폐기물을 정리한 현장"),
    ("yangpyeong-review-01", "양평군", "단독주택 폐기물처리", "가정폐기물처리", "단독주택 내 생활폐기물과 가구를 정리한 현장"),
    ("yeoncheon-review-01", "연천군", "창고 및 주택 폐기물처리", "빈집정리", "창고와 주택에 남은 물품을 정리한 현장"),
    ("suwon-review-02", "수원시", "아파트 가정폐기물 처리", "가정폐기물처리", "아파트에 쌓여 있던 생활가구와 잔짐을 정리한 현장"),
    ("seongnam-review-02", "성남시", "원룸 이사폐기물 처리", "이사폐기물처리", "이사 후 남은 가구와 박스류를 정리한 현장"),
    ("goyang-review-02", "고양시", "단독주택 가정폐기물 처리", "가정폐기물처리", "단독주택 내부 생활폐기물과 대형가구를 정리한 현장"),
    ("yongin-review-02", "용인시", "원룸 쓰레기집청소", "쓰레기집청소", "생활폐기물이 쌓인 원룸을 단계적으로 정리한 현장"),
    ("hwaseong-review-02", "화성시", "아파트 이사폐기물 처리", "이사폐기물처리", "이사 전후 남은 가구와 생활폐기물을 정리한 현장"),
    ("bucheon-review-02", "부천시", "사무실 폐업폐기물 처리", "폐업폐기물처리", "사무실 정리 후 남은 집기와 폐기물을 처리한 현장"),
]

REGION_SLUG = {
    "수원시": "suwon", "성남시": "seongnam", "고양시": "goyang", "용인시": "yongin",
    "화성시": "hwaseong", "남양주시": "namyangju", "부천시": "bucheon", "안산시": "ansan",
    "안양시": "anyang", "평택시": "pyeongtaek", "김포시": "gimpo", "하남시": "hanam",
    "의정부시": "uijeongbu", "시흥시": "siheung", "파주시": "paju", "광명시": "gwangmyeong",
    "광주시": "gwangju", "군포시": "gunpo", "오산시": "osan", "이천시": "icheon",
    "안성시": "anseong", "의왕시": "uiwang", "양주시": "yangju", "구리시": "guri",
    "포천시": "pocheon", "여주시": "yeoju", "동두천시": "dongducheon", "과천시": "gwacheon",
    "가평군": "gapyeong", "양평군": "yangpyeong", "연천군": "yeoncheon"
}

def safe_num(n, total=100):
    return ((n - 1) % total) + 1

PROCESS_EXT = {1: ".jpeg"}  # process-01 only

def process_path(n):
    n = safe_num(n, 25)
    ext = PROCESS_EXT.get(n, ".jpg")
    return f"/images/main/process-{n:02d}{ext}"

def image_set(idx):
    """전·후는 같은 번호끼리 짝, 중은 process 이미지."""
    p1 = safe_num((idx - 1) * 2 + 1)
    p2 = safe_num((idx - 1) * 2 + 2)
    mid1 = process_path((idx - 1) % 25 + 1)
    mid2 = process_path(idx % 25 + 1)
    return {
        "p1": p1,
        "p2": p2,
        "before1": f"/images/cases/waste-before-{p1:03d}.jpg",
        "after1": f"/images/cases/waste-after-{p1:03d}.jpg",
        "before2": f"/images/cases/waste-before-{p2:03d}.jpg",
        "after2": f"/images/cases/waste-after-{p2:03d}.jpg",
        "mid1": mid1,
        "mid2": mid2,
    }

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
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{canonical}" />

  <link rel="stylesheet" href="/css/style.css" />
</head>

<body>
<header class="top-bar">
  <div class="top-inner">
    <span>경기 전지역 폐기물처리 작업후기</span>
    <strong>상담전화 {PHONE}</strong>
  </div>
</header>

<header class="site-header">
  <a href="/" class="logo">
    <strong>가족애폐기물처리</strong>
    <span>경기 폐기물처리 작업후기</span>
  </a>

  <nav>
    <a href="/">메인</a>
    <a href="/#service">서비스</a>
    <a href="/#price">비용</a>
    <a href="/reviews/">작업후기</a>
    <a href="/regions/">지역별 안내</a>
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
</body>
</html>"""

Path("reviews").mkdir(exist_ok=True)

cards = []

for idx, (slug, region, case_title, service, summary) in enumerate(REVIEWS, start=1):
    region_slug = REGION_SLUG[region]
    imgs = image_set(idx)

    title = f"{region} {case_title} 작업후기 | 경기 가족애폐기물처리"
    desc = f"{region} {case_title} 작업후기. {summary}. 경기 폐기물처리 상담 {PHONE}"

    body = f"""
<main>
<section class="sub-hero review-detail-hero">
  <div class="sub-hero-inner">
    <p class="hero-badge">{region} 작업후기</p>
    <h1>{region} {case_title} 작업후기</h1>
    <p>{summary}입니다. 작업 전·후 비교와 분류·반출 과정까지 확인할 수 있습니다.</p>
    <div class="hero-actions">
      <a href="tel:{PHONE}">전화 상담하기</a>
      <a href="/#contact">상담 접수하기</a>
    </div>
  </div>
</section>

<section class="section">
  <p class="section-label">작업개요</p>
  <h2>{region} 폐기물처리 작업 내용</h2>
  <div class="factor-grid">
    <article><span>01</span><h3>작업지역</h3><p>{region}</p></article>
    <article><span>02</span><h3>작업유형</h3><p>{service}</p></article>
    <article><span>03</span><h3>작업범위</h3><p>분류, 반출, 수거 후 정리</p></article>
    <article><span>04</span><h3>상담기준</h3><p>폐기물 양과 현장 동선 확인</p></article>
  </div>
</section>

<section class="section text-section">
  <p class="section-label">현장 설명</p>
  <h2>{region} {service}, 현장 상황에 맞춰 진행했습니다</h2>
  <p>
    이번 {region} 작업후기는 {summary}을 기준으로 진행되었습니다.
    현장에는 생활폐기물과 정리 대상 물품이 함께 남아 있어 먼저 종류를 나누고,
    반출이 필요한 물품과 정리 후 남길 물품을 구분하는 과정이 필요했습니다.
  </p>
  <p>
    폐기물처리는 단순히 물건을 옮기는 작업처럼 보일 수 있지만,
    실제 현장에서는 층수, 엘리베이터 사용 여부, 차량 진입 가능 여부,
    대형가구 포함 여부에 따라 작업 순서가 달라집니다.
    그래서 상담 단계에서 사진과 주소를 함께 확인하면 더 정확한 안내가 가능합니다.
  </p>
</section>

<section class="section review-photo-section">
  <p class="section-label">작업사진</p>
  <h2>{region} 폐기물처리 작업 전·중·후 사진</h2>
  <p class="section-desc">같은 현장의 작업 전·후를 짝으로 비교하고, 분류·반출 과정도 함께 확인할 수 있도록 구성했습니다.</p>

  <div class="before-after-grid">
    <figure>
      <img src="{imgs['before1']}" alt="{region} 폐기물처리 작업 전 1" loading="lazy" />
      <figcaption>작업 전 현장 상태</figcaption>
    </figure>
    <figure>
      <img src="{imgs['after1']}" alt="{region} 폐기물처리 작업 후 1" loading="lazy" />
      <figcaption>작업 후 정리 완료</figcaption>
    </figure>
    <figure>
      <img src="{imgs['before2']}" alt="{region} 폐기물처리 작업 전 2" loading="lazy" />
      <figcaption>다른 각도 작업 전</figcaption>
    </figure>
    <figure>
      <img src="{imgs['after2']}" alt="{region} 폐기물처리 작업 후 2" loading="lazy" />
      <figcaption>다른 각도 작업 후</figcaption>
    </figure>
    <figure>
      <img src="{imgs['mid1']}" alt="{region} 폐기물 분류 과정" loading="lazy" />
      <figcaption>폐기물 분류 과정</figcaption>
    </figure>
    <figure>
      <img src="{imgs['mid2']}" alt="{region} 폐기물 반출 과정" loading="lazy" />
      <figcaption>반출 및 정리 과정</figcaption>
    </figure>
  </div>
</section>

<section class="section text-section">
  <p class="section-label">작업후기</p>
  <h2>{region} 폐기물처리 작업을 마치며</h2>
  <p>
    {region} 현장은 폐기물의 양뿐 아니라 반출 동선 확인이 중요한 작업이었습니다.
    정리 전에는 물품이 섞여 있어 작업 범위를 바로 판단하기 어려웠지만,
    종류별로 나눈 뒤 필요한 순서대로 반출을 진행하면서 현장을 정돈할 수 있었습니다.
  </p>
  <p>
    비슷한 현장이라도 비용은 폐기물 양, 대형가구 포함 여부, 작업 인원,
    차량 진입 가능 여부에 따라 달라집니다.
    {region} 폐기물처리 상담이 필요하다면 현장 사진과 주소를 함께 남겨주시면
    보다 빠르게 확인해드릴 수 있습니다.
  </p>
</section>

<section class="section">
  <p class="section-label">관련 지역</p>
  <h2>{region} 폐기물처리 지역 안내</h2>
  <div class="region-grid">
    <a href="/regions/{region_slug}/">{region} 폐기물처리</a>
    <a href="/reviews/">전체 작업후기 보기</a>
    <a href="/regions/">경기도 지역별 안내</a>
  </div>
</section>

<section class="review-contact-box">
  <div class="contact-mini">
    <h2>비슷한 현장 상담이 필요하신가요?</h2>
    <p>사진과 주소를 남겨주시면 폐기물 양과 작업 조건을 확인한 뒤 연락드립니다.</p>
    <div class="hero-actions mini-actions">
      <a href="tel:{PHONE}">전화상담 {PHONE}</a>
      <a href="/#contact">상담접수하기</a>
    </div>
  </div>
</section>
</main>
"""

    file_path = Path("reviews") / f"{slug}.html"
    file_path.write_text(
        layout(title, desc, body, f"{BASE_URL}/reviews/{slug}.html"),
        encoding="utf-8"
    )
    print(f"생성: {file_path}")

    cards.append(f"""
    <article>
      <img src="{imgs['after1']}" alt="{region} {case_title} 작업후기" />
      <span>{service}</span>
      <h3>{region} {case_title} 작업후기</h3>
      <p>{summary}입니다.</p>
      <a href="/reviews/{slug}.html">자세히 보기</a>
    </article>
    """)

index_body = f"""
<main>
<section class="sub-hero review-hero">
  <div class="sub-hero-inner">
    <p class="hero-badge">경기 폐기물처리 작업후기</p>
    <h1>지역별 폐기물처리 작업후기</h1>
    <p>경기도 현장에서 진행한 가정폐기물, 이사폐기물, 빈집정리, 쓰레기집청소 작업후기를 지역별로 정리했습니다.</p>
  </div>
</section>

<section class="section">
  <p class="section-label">작업후기 모음</p>
  <h2>경기 폐기물처리 실제 작업후기</h2>
  <p class="section-desc">
    작업후기는 같은 현장의 전·후 사진을 짝으로 비교하고,
    분류·반출 과정까지 자연스럽게 보이도록 구성했습니다.
  </p>

  <div class="review-list-grid">
    {''.join(cards)}
  </div>
</section>

<section class="section contact-mini">
  <h2>비슷한 현장 상담이 필요하신가요?</h2>
  <p>사진과 주소를 남겨주시면 폐기물 양과 작업 조건을 확인한 뒤 연락드립니다.</p>
  <div class="hero-actions mini-actions">
    <a href="tel:{PHONE}">전화상담 {PHONE}</a>
    <a href="/#contact">상담접수하기</a>
  </div>
</section>
</main>
"""

Path("reviews/index.html").write_text(
    layout(
        "경기 폐기물처리 작업후기 | 가족애폐기물처리",
        "경기 가족애폐기물처리 작업후기 모음. 수원, 성남, 고양, 용인, 화성 등 경기도 폐기물처리 실제 작업후기 안내.",
        index_body,
        f"{BASE_URL}/reviews/"
    ),
    encoding="utf-8"
)

print("작업후기 생성 완료")
print("개별 후기 html과 reviews/index.html을 세트 이미지 기준으로 갱신했습니다.")