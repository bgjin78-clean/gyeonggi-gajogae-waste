# -*- coding: utf-8 -*-
"""이사폐기물처리·생활폐기물처리 키워드 후기 10개 추가 (비용·FAQ·스키마 포함)"""
from pathlib import Path
from datetime import date
import re

ROOT = Path(__file__).resolve().parent
PHONE = "010-4720-3895"
BASE_URL = "https://www.gyeonggi.gajogae-waste.com"
TODAY = date.today().isoformat()

SEOUL_WASTE_URL = "https://www.seoul.gajogae-waste.com/"
GYEONGGI_YUPUM_URL = "https://www.gyeonggi.gajogae-yupum.com/"
SEOUL_YUPUM_URL = "https://www.seoul.gajogae-yupum.com/"

REGION_SLUG = {
    "수원시": "suwon", "성남시": "seongnam", "고양시": "goyang", "용인시": "yongin",
    "화성시": "hwaseong", "남양주시": "namyangju", "부천시": "bucheon", "안산시": "ansan",
    "안양시": "anyang", "평택시": "pyeongtaek", "김포시": "gimpo", "하남시": "hanam",
    "의정부시": "uijeongbu", "시흥시": "siheung", "파주시": "paju", "광명시": "gwangmyeong",
    "광주시": "gwangju", "군포시": "gunpo", "오산시": "osan", "이천시": "icheon",
    "안성시": "anseong", "의왕시": "uiwang", "양주시": "yangju", "구리시": "guri",
    "포천시": "pocheon", "여주시": "yeoju", "동두천시": "dongducheon", "과천시": "gwacheon",
    "가평군": "gapyeong", "양평군": "yangpyeong", "연천군": "yeoncheon",
}

# idx는 기존 42개 이후 이미지 충돌 방지용 (85~)
NEW_REVIEWS = [
    {
        "slug": "goyang-review-03",
        "region": "고양시",
        "case_title": "아파트 이사폐기물처리",
        "service": "이사폐기물처리",
        "housing": "아파트",
        "summary": "이사 당일 남은 대형가구와 생활잡화를 엘리베이터 동선에 맞춰 반출한 현장",
        "cost_note": "1톤 차량 기준 상담 후 약 28만~35만 원대",
        "amount": "1톤 차량 1대 분량",
        "img_base": 85,
    },
    {
        "slug": "yongin-review-03",
        "region": "용인시",
        "case_title": "빌라 이사폐기물처리",
        "service": "이사폐기물처리",
        "housing": "빌라",
        "summary": "엘리베이터 없는 빌라에서 이사 후 남은 가구와 박스류를 계단 반출한 현장",
        "cost_note": "계단 반출·인원 추가로 약 32만~40만 원대",
        "amount": "대형가구 포함 중형 규모",
        "img_base": 87,
    },
    {
        "slug": "namyangju-review-03",
        "region": "남양주시",
        "case_title": "주택 이사폐기물처리",
        "service": "이사폐기물처리",
        "housing": "단독주택",
        "summary": "주택 이사 전후 남은 장롱·침대·생활폐기물을 마당 동선으로 정리한 현장",
        "cost_note": "폐기물 양 기준으로 약 30만~38만 원대",
        "amount": "1톤 차량 1~1.5대 분량",
        "img_base": 89,
    },
    {
        "slug": "uijeongbu-review-02",
        "region": "의정부시",
        "case_title": "원룸 이사폐기물처리",
        "service": "이사폐기물처리",
        "housing": "원룸",
        "summary": "원룸 이사 후 매트리스·책상·생활잡화를 빠르게 반출한 현장",
        "cost_note": "소형 원룸 기준으로 약 25만~30만 원대",
        "amount": "소형(원룸) 1회 분량",
        "img_base": 91,
    },
    {
        "slug": "siheung-review-02",
        "region": "시흥시",
        "case_title": "아파트 이사폐기물처리",
        "service": "이사폐기물처리",
        "housing": "아파트",
        "summary": "아파트 이사 후 남은 소파·가전·잔짐을 지하 주차장 동선으로 반출한 현장",
        "cost_note": "엘리베이터 사용 가능 현장으로 약 27만~34만 원대",
        "amount": "1톤 차량 1대 분량",
        "img_base": 93,
    },
    {
        "slug": "hanam-review-02",
        "region": "하남시",
        "case_title": "아파트 생활폐기물처리",
        "service": "생활폐기물처리",
        "housing": "아파트",
        "summary": "베란다·창고에 쌓인 생활폐기물과 쓰지 않는 가구를 분리 반출한 현장",
        "cost_note": "생활폐기물 위주 정리로 약 25만~32만 원대",
        "amount": "중형(방 1~2칸) 분량",
        "img_base": 95,
    },
    {
        "slug": "gwangmyeong-review-02",
        "region": "광명시",
        "case_title": "주택 생활폐기물처리",
        "service": "생활폐기물처리",
        "housing": "주택",
        "summary": "주택 내부 생활잡화·낡은 가전·잔짐을 종류별로 나눠 반출한 현장",
        "cost_note": "양과 차량 진입에 따라 약 28만~36만 원대",
        "amount": "중형~대형 혼합 분량",
        "img_base": 97,
    },
    {
        "slug": "uiwang-review-02",
        "region": "의왕시",
        "case_title": "아파트 생활폐기물처리",
        "service": "생활폐기물처리",
        "housing": "아파트",
        "summary": "이사 없이 집 정리 중 나온 생활폐기물과 잔짐을 정리한 현장",
        "cost_note": "잔짐 위주 정리로 약 25만~31만 원대",
        "amount": "소형~중형 분량",
        "img_base": 99,
    },
    {
        "slug": "gwacheon-review-02",
        "region": "과천시",
        "case_title": "원룸 생활폐기물처리",
        "service": "생활폐기물처리",
        "housing": "원룸",
        "summary": "원룸에 쌓인 생활용품·박스·소형가구를 분리해 반출한 현장",
        "cost_note": "원룸 소량 기준으로 약 25만~29만 원대",
        "amount": "소형(원룸) 분량",
        "img_base": 71,
    },
    {
        "slug": "yangju-review-02",
        "region": "양주시",
        "case_title": "단독주택 생활폐기물처리",
        "service": "생활폐기물처리",
        "housing": "단독주택",
        "summary": "단독주택 창고·마당에 쌓인 생활폐기물과 오래된 물품을 정리한 현장",
        "cost_note": "야외·창고 포함으로 약 30만~39만 원대",
        "amount": "1톤 차량 1대 이상",
        "img_base": 73,
    },
]


def process_path(n):
    n = ((n - 1) % 25) + 1
    ext = ".jpeg" if n == 1 else ".jpg"
    return f"/images/main/process-{n:02d}{ext}"


def imgs_for(base):
    p1 = ((base - 1) % 100) + 1
    p2 = (base % 100) + 1
    return {
        "before1": f"/images/cases/waste-before-{p1:03d}.jpg",
        "after1": f"/images/cases/waste-after-{p1:03d}.jpg",
        "before2": f"/images/cases/waste-before-{p2:03d}.jpg",
        "after2": f"/images/cases/waste-after-{p2:03d}.jpg",
        "mid1": process_path(base),
        "mid2": process_path(base + 3),
    }


def faq_json(region, service, cost_note):
    qas = [
        (
            f"{region} {service} 비용은 얼마인가요?",
            f"{region} {service} 비용은 기본 25만원부터이며, 이번 현장은 {cost_note} 안내 범위였습니다. "
            f"정확한 금액은 폐기물 양, 차량 대수, 층수, 엘리베이터 여부, 작업 인원에 따라 달라집니다.",
        ),
        (
            f"{region}에서 사진으로 {service} 견적이 가능한가요?",
            f"가능합니다. 현장 사진과 주소, 엘리베이터·주차 가능 여부를 알려주시면 "
            f"{region} {service} 대략 비용을 먼저 안내할 수 있습니다.",
        ),
        (
            f"{region} {service}는 당일 작업이 가능한가요?",
            f"일정과 차량 상황에 따라 당일 또는 빠른 일정 배정이 가능합니다. "
            f"상담전화 {PHONE}로 남겨주시면 가능 여부를 바로 확인합니다.",
        ),
    ]
    entities = []
    for q, a in qas:
        entities.append(
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
        )
    import json

    return json.dumps(
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities},
        ensure_ascii=False,
        indent=2,
    )


def article_json(title, desc, canonical, region, service):
    import json

    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "mainEntityOfPage": canonical,
        "author": {"@type": "Organization", "name": "경기 가족애폐기물처리"},
        "publisher": {
            "@type": "Organization",
            "name": "경기 가족애폐기물처리",
            "telephone": PHONE,
        },
        "about": [service, f"{region} 폐기물처리", "폐기물처리 비용"],
        "inLanguage": "ko-KR",
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def layout(title, desc, body, canonical, extra_head=""):
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
{extra_head}
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


def build_body(r, imgs):
    region = r["region"]
    service = r["service"]
    case = r["case_title"]
    region_slug = REGION_SLUG[region]
    cost = r["cost_note"]
    amount = r["amount"]
    housing = r["housing"]
    summary = r["summary"]

    if service == "이사폐기물처리":
        why = (
            f"이사 일정에 맞춰 빠르게 반출해야 하는 현장이었습니다. "
            f"{housing} 특성상 엘리베이터·계단·주차 가능 여부가 비용과 작업 시간에 직접 영향을 줍니다."
        )
        tip = (
            "이사폐기물처리는 대형가구 포함 여부, 엘리베이터 사용, 차량 진입 가능 여부를 "
            "미리 알려주시면 비용 안내가 더 정확해집니다."
        )
    else:
        why = (
            f"이사와 무관하게 집에 쌓인 생활폐기물을 정리한 현장이었습니다. "
            f"{housing} 내부와 창고·베란다에 섞여 있던 물품을 먼저 분류한 뒤 반출했습니다."
        )
        tip = (
            "생활폐기물처리는 버리는 양과 대형가구 포함 여부에 따라 비용이 달라집니다. "
            "사진으로 먼저 상담하시면 기본 25만원부터의 범위를 안내받을 수 있습니다."
        )

    return f"""
<main>
<section class="sub-hero review-detail-hero">
  <div class="sub-hero-inner">
    <p class="hero-badge">{region} {service} 작업후기</p>
    <h1>{region} {case} 작업후기</h1>
    <p>{summary}입니다. 작업 전·후 비교와 함께 {region} {service} 비용 기준도 정리했습니다.</p>
    <div class="hero-actions">
      <a href="tel:{PHONE}">전화 상담하기</a>
      <a href="/#contact">상담 접수하기</a>
    </div>
  </div>
</section>

<section class="section">
  <p class="section-label">작업개요</p>
  <h2>{region} {service} 한눈에 보기</h2>
  <div class="factor-grid">
    <article><span>01</span><h3>작업지역</h3><p>{region}</p></article>
    <article><span>02</span><h3>작업유형</h3><p>{service}</p></article>
    <article><span>03</span><h3>주거형태</h3><p>{housing}</p></article>
    <article><span>04</span><h3>폐기물 양</h3><p>{amount}</p></article>
  </div>
</section>

<section class="section text-section">
  <p class="section-label">현장 설명</p>
  <h2>{region} {service}, 이렇게 진행했습니다</h2>
  <p>
    이번 {region} 작업후기는 {summary}을 기준으로 작성했습니다.
    {why}
  </p>
  <p>
    작업 순서는 ① 현장 확인 및 폐기물 분류 → ② 대형가구·생활잡화 분리 →
    ③ 엘리베이터·계단 동선에 맞춘 반출 → ④ 수거 후 마무리 정리 순으로 진행했습니다.
    {region} {service}를 알아볼 때는 사진과 주소를 함께 보내주시면
    차량·인원·비용을 더 빠르게 안내할 수 있습니다.
  </p>
</section>

<section class="section">
  <p class="section-label">비용 안내</p>
  <h2>{region} {service} 비용은 어떻게 산정했나요?</h2>
  <p class="section-desc">
    경기 폐기물처리 기본 비용은 25만원부터이며, 같은 지역이라도 현장 조건에 따라 달라집니다.
  </p>
  <div class="factor-grid">
    <article>
      <h3>이번 현장 안내 범위</h3>
      <p><strong>{cost}</strong>로 상담했습니다. 확정 금액은 당일 폐기물 양 확인 후 안내합니다.</p>
    </article>
    <article>
      <h3>비용에 영향 큰 요소</h3>
      <p>폐기물 양(차량 대수), 대형가구 포함, 층수·엘리베이터, 주차·진입 동선, 작업 인원입니다.</p>
    </article>
    <article>
      <h3>사진 상담이 유리한 이유</h3>
      <p>사진을 보면 양과 동선을 먼저 가늠할 수 있어 {region} {service} 대략 비용을 빠르게 안내합니다.</p>
    </article>
    <article>
      <h3>추가 비용이 생기는 경우</h3>
      <p>예상보다 양이 많거나, 계단 반출·특수 가구 분해가 필요하면 인원·시간이 늘어날 수 있습니다.</p>
    </article>
  </div>
  <p style="margin-top:18px;color:#5f4630">
    <strong>참고:</strong> {tip}
  </p>
</section>

<section class="section review-photo-section">
  <p class="section-label">작업사진</p>
  <h2>{region} {service} 작업 전·중·후 사진</h2>
  <p class="section-desc">같은 현장의 전·후를 짝으로 비교하고, 분류·반출 과정도 함께 확인할 수 있습니다.</p>

  <div class="before-after-grid">
    <figure>
      <img src="{imgs['before1']}" alt="{region} {service} 작업 전 1" loading="lazy" />
      <figcaption>작업 전 현장 상태</figcaption>
    </figure>
    <figure>
      <img src="{imgs['after1']}" alt="{region} {service} 작업 후 1" loading="lazy" />
      <figcaption>작업 후 정리 완료</figcaption>
    </figure>
    <figure>
      <img src="{imgs['before2']}" alt="{region} {service} 작업 전 2" loading="lazy" />
      <figcaption>다른 각도 작업 전</figcaption>
    </figure>
    <figure>
      <img src="{imgs['after2']}" alt="{region} {service} 작업 후 2" loading="lazy" />
      <figcaption>다른 각도 작업 후</figcaption>
    </figure>
    <figure>
      <img src="{imgs['mid1']}" alt="{region} {service} 분류 과정" loading="lazy" />
      <figcaption>폐기물 분류 과정</figcaption>
    </figure>
    <figure>
      <img src="{imgs['mid2']}" alt="{region} {service} 반출 과정" loading="lazy" />
      <figcaption>반출 및 정리 과정</figcaption>
    </figure>
  </div>
</section>

<section class="section text-section">
  <p class="section-label">작업 후기</p>
  <h2>{region} {service}를 마치며</h2>
  <p>
    {region} 현장은 폐기물 양뿐 아니라 반출 동선 확인이 중요했습니다.
    상담 단계에서 비용 기준을 먼저 공유한 뒤 작업을 진행해,
    현장에서 범위가 갑자기 커지지 않도록 맞춰 나갔습니다.
  </p>
  <p>
    {region} {service} 비용이 궁금하시다면 사진과 주소를 남겨주세요.
    기본 25만원부터의 범위와 함께, 차량·인원 기준을 안내드립니다. 상담전화 {PHONE}.
  </p>
</section>

<section class="section">
  <p class="section-label">자주 묻는 질문</p>
  <h2>{region} {service} FAQ</h2>
  <div class="faq-list">
    <article class="faq-item">
      <h3>{region} {service} 비용은 얼마인가요?</h3>
      <p>기본 25만원부터이며, 이번 현장은 {cost} 안내 범위였습니다. 양·차량·층수·엘리베이터에 따라 달라집니다.</p>
    </article>
    <article class="faq-item">
      <h3>사진으로 견적이 가능한가요?</h3>
      <p>가능합니다. 사진·주소·엘리베이터·주차 여부를 알려주시면 {region} {service} 대략 비용을 먼저 안내합니다.</p>
    </article>
    <article class="faq-item">
      <h3>당일 작업이 가능한가요?</h3>
      <p>일정과 차량 여유에 따라 가능합니다. {PHONE}로 문의해 주시면 바로 확인해 드립니다.</p>
    </article>
  </div>
</section>

<section class="section">
  <p class="section-label">관련 안내</p>
  <h2>{region} 폐기물처리 더 보기</h2>
  <div class="region-grid">
    <a href="/regions/{region_slug}/">{region} 폐기물처리</a>
    <a href="/reviews/">전체 작업후기 보기</a>
    <a href="/#price">폐기물처리 비용 안내</a>
  </div>
</section>

<section class="review-contact-box">
  <div class="contact-mini">
    <h2>{region} {service} 상담이 필요하신가요?</h2>
    <p>사진과 주소를 남겨주시면 폐기물 양과 비용을 확인한 뒤 연락드립니다. 기본 25만원부터.</p>
    <div class="hero-actions mini-actions">
      <a href="tel:{PHONE}">전화상담 {PHONE}</a>
      <a href="/#contact">상담접수하기</a>
    </div>
  </div>
</section>
</main>
"""


def write_pages():
    cards = []
    for r in NEW_REVIEWS:
        imgs = imgs_for(r["img_base"])
        region = r["region"]
        case = r["case_title"]
        service = r["service"]
        title = f"{region} {case} 작업후기 | 경기 가족애폐기물처리"
        desc = (
            f"{region} {case} 작업후기. {r['summary']}. "
            f"비용 {r['cost_note']}. 기본 25만원부터. 상담 {PHONE}"
        )
        canonical = f"{BASE_URL}/reviews/{r['slug']}.html"
        body = build_body(r, imgs)
        extra = f"""
  <script type="application/ld+json">
{article_json(title, desc, canonical, region, service)}
  </script>
  <script type="application/ld+json">
{faq_json(region, service, r['cost_note'])}
  </script>
"""
        path = ROOT / "reviews" / f"{r['slug']}.html"
        path.write_text(layout(title, desc, body, canonical, extra), encoding="utf-8")
        print(f"생성: {path.name}")

        cards.append(
            f"""
    <article>
      <img src="{imgs['after1']}" alt="{region} {case} 작업후기" />
      <span>{service}</span>
      <h3>{region} {case} 작업후기</h3>
      <p>{r['summary']}입니다. 안내 비용은 {r['cost_note']}입니다.</p>
      <a href="/reviews/{r['slug']}.html">자세히 보기</a>
    </article>
"""
        )
    return cards


def patch_reviews_index(cards_html):
    path = ROOT / "reviews" / "index.html"
    html = path.read_text(encoding="utf-8")
    # insert before closing of review-list-grid
    marker = '  <div class="review-list-grid">'
    if marker not in html:
        raise SystemExit("reviews/index.html grid marker not found")
    # append cards before </div> that closes review-list-grid - find last occurrence before contact
    insert_at = html.find("</div>\n</section>\n\n<section class=\"section contact-mini\">")
    if insert_at == -1:
        insert_at = html.find('</div>\n</section>\n\n<section class="section contact-mini">')
    if insert_at == -1:
        # fallback: before contact-mini
        insert_at = html.find('<section class="section contact-mini">')
        if insert_at == -1:
            raise SystemExit("cannot find insert point in reviews/index.html")
        # find previous </div>
        insert_at = html.rfind("</div>", 0, insert_at)
    html = html[:insert_at] + "".join(cards_html) + "\n  " + html[insert_at:]
    path.write_text(html, encoding="utf-8")
    print("갱신: reviews/index.html")


def patch_region_pages():
    for r in NEW_REVIEWS:
        slug = REGION_SLUG[r["region"]]
        path = ROOT / "regions" / slug / "index.html"
        html = path.read_text(encoding="utf-8")
        article = f"""
    <article>
      <span>{r['service']}</span>
      <h3>{r['region']} {r['case_title']} 작업후기</h3>
      <p>{r['summary']}입니다. 안내 비용은 {r['cost_note']}입니다.</p>
      <a href="/reviews/{r['slug']}.html">{r['region']} 작업후기 보기</a>
    </article>
"""
        if f"/reviews/{r['slug']}.html" in html:
            print(f"유지: regions/{slug}/ (이미 링크 있음)")
            continue
        # insert before closing </div> of case-grid
        m = re.search(r'(<div class="case-grid">)(.*?)(</div>\s*</section>)', html, re.S)
        if not m:
            print(f"경고: regions/{slug}/ case-grid 없음")
            continue
        new_grid = m.group(1) + m.group(2) + article + m.group(3)
        html = html[: m.start()] + new_grid + html[m.end() :]
        path.write_text(html, encoding="utf-8")
        print(f"갱신: regions/{slug}/index.html")


def patch_main_index():
    path = ROOT / "index.html"
    html = path.read_text(encoding="utf-8")
    # replace case-grid inside #reviews with newest 6 from NEW_REVIEWS (last 6 reversed? show all 10? main has 6)
    latest = list(reversed(NEW_REVIEWS[-6:]))
    articles = []
    for r in latest:
        tag = "이사폐기물" if r["service"] == "이사폐기물처리" else "생활폐기물"
        articles.append(
            f"""      <article>
        <span>{tag}</span>
        <h3>{r['region']} {r['case_title']} 작업후기</h3>
        <p>{r['summary']}입니다. 안내 비용은 {r['cost_note']}입니다.</p>
        <a href="/reviews/{r['slug']}.html">작업후기 보기</a>
      </article>"""
        )
    new_grid = '    <div class="case-grid">\n' + "\n".join(articles) + "\n    </div>"
    html2, n = re.subn(
        r'(<section id="reviews" class="section">.*?<div class="case-grid">).*?(</div>\s*<div class="more-link">)',
        r"\1PLACEHOLDER\2",
        html,
        count=1,
        flags=re.S,
    )
    if n != 1:
        print("경고: 메인 reviews 섹션 교체 실패")
        return
    html2 = html2.replace(
        '<div class="case-grid">PLACEHOLDER</div>',
        new_grid,
        1,
    )
    # also update section-desc to mention cost keywords
    html2 = html2.replace(
        "작업후기는 전·후 2장 비교가 아니라 전 2장, 중간 흐름, 후 2장 방식으로 구성합니다.",
        "이사폐기물처리·생활폐기물처리 후기에 비용 기준(기본 25만원부터)과 전·중·후 사진을 함께 담았습니다.",
        1,
    )
    path.write_text(html2, encoding="utf-8")
    print("갱신: index.html")


def patch_sitemap_rss():
    sm_path = ROOT / "sitemap.xml"
    sm = sm_path.read_text(encoding="utf-8")
    for r in NEW_REVIEWS:
        url = f"{BASE_URL}/reviews/{r['slug']}.html"
        if url not in sm:
            block = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
"""
            sm = sm.replace("</urlset>", block + "</urlset>")
    sm_path.write_text(sm, encoding="utf-8")

    rss_path = ROOT / "rss.xml"
    rss = rss_path.read_text(encoding="utf-8")
    for r in NEW_REVIEWS:
        url = f"{BASE_URL}/reviews/{r['slug']}.html"
        if url not in rss:
            item = f"""
<item>
<title>{r['region']} {r['case_title']} 작업후기</title>
<link>{url}</link>
<guid>{url}</guid>
<description>{r['summary']}. 비용 {r['cost_note']}. 기본 25만원부터.</description>
</item>
"""
            rss = rss.replace("</channel>", item + "</channel>")
    rss_path.write_text(rss, encoding="utf-8")
    print("갱신: sitemap.xml, rss.xml")


def patch_generate_reviews_list():
    path = ROOT / "generate_reviews.py"
    text = path.read_text(encoding="utf-8")
    if "goyang-review-03" in text:
        print("유지: generate_reviews.py REVIEWS")
        return
    lines = []
    for r in NEW_REVIEWS:
        lines.append(
            f'    ("{r["slug"]}", "{r["region"]}", "{r["case_title"]}", "{r["service"]}", "{r["summary"]}"),'
        )
    block = "\n".join(lines) + "\n"
    text = text.replace(
        '    ("gimpo-review-02", "김포시", "상가 폐업폐기물 처리", "폐업폐기물처리", "상가 폐업 후 남은 집기와 폐기물을 처리한 현장"),\n]',
        '    ("gimpo-review-02", "김포시", "상가 폐업폐기물 처리", "폐업폐기물처리", "상가 폐업 후 남은 집기와 폐기물을 처리한 현장"),\n'
        + block
        + "]",
    )
    path.write_text(text, encoding="utf-8")
    print("갱신: generate_reviews.py")


def ensure_faq_css():
    css_path = ROOT / "css" / "style.css"
    css = css_path.read_text(encoding="utf-8")
    if ".faq-list" in css:
        return
    css += """

.faq-list{
    display:grid;
    gap:16px;
    margin-top:24px;
}
.faq-item{
    background:#fff;
    border:1px solid #ead8c4;
    border-radius:16px;
    padding:22px 24px;
    box-shadow:0 5px 15px rgba(0,0,0,.04);
}
.faq-item h3{
    margin:0 0 10px;
    font-size:18px;
    color:#5c3c20;
}
.faq-item p{
    margin:0;
    color:#5f4630;
    line-height:1.7;
}
"""
    css_path.write_text(css, encoding="utf-8")
    print("갱신: css/style.css (faq)")


if __name__ == "__main__":
    ensure_faq_css()
    cards = write_pages()
    patch_reviews_index(cards)
    patch_region_pages()
    patch_main_index()
    patch_sitemap_rss()
    patch_generate_reviews_list()
    print(f"완료: {len(NEW_REVIEWS)}개 후기 추가")
