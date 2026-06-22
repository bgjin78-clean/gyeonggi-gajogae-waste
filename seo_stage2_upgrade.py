from pathlib import Path

CITY_CONTENT = {
    "suwon": {
        "title": "수원시는 아파트 단지와 오피스텔 비중이 높은 지역입니다.",
        "cost": "엘리베이터 사용 여부와 주차 가능 여부가 비용에 영향을 줄 수 있습니다."
    },
    "seongnam": {
        "title": "성남시는 상가와 주거시설이 혼재된 지역입니다.",
        "cost": "상가 정리와 사무실 집기 반출 문의가 비교적 많은 편입니다."
    },
    "goyang": {
        "title": "고양시는 신도시와 기존 주거지역이 함께 형성되어 있습니다.",
        "cost": "이사폐기물과 생활폐기물 문의가 꾸준히 발생하는 지역입니다."
    },
    "yongin": {
        "title": "용인시는 단독주택과 창고형 공간 비중이 높은 편입니다.",
        "cost": "대형가구와 창고 정리 작업이 자주 접수됩니다."
    },
    "hwaseong": {
        "title": "화성시는 산업단지와 주거지역이 함께 발달했습니다.",
        "cost": "주거공간과 사업장 폐기물 문의가 모두 발생합니다."
    }
}

DEFAULT_TEXT = {
    "title": "생활폐기물과 가정폐기물 문의가 꾸준히 발생하는 지역입니다.",
    "cost": "현장 구조와 폐기물 양에 따라 작업 범위가 달라질 수 있습니다."
}

for file in Path("regions").glob("*/index.html"):

    slug = file.parent.name

    data = CITY_CONTENT.get(slug, DEFAULT_TEXT)

    html = file.read_text(encoding="utf-8")

    seo_block = f"""
<section class="section text-section seo-stage2">

<h2>왜 지역마다 폐기물처리 비용이 달라질까요?</h2>

<p>
{data['title']}
</p>

<p>
{data['cost']}
</p>

<p>
폐기물의 양뿐 아니라 차량 진입 가능 여부,
건물 구조, 엘리베이터 사용 여부,
대형가구 포함 여부에 따라 필요한 작업 인원이 달라질 수 있습니다.
</p>

<h3>상담 전 준비하면 좋은 내용</h3>

<ul>
<li>현장 사진 3~5장</li>
<li>작업 주소</li>
<li>엘리베이터 유무</li>
<li>폐기물 종류</li>
<li>희망 작업일</li>
</ul>

<h3>사진 상담이 빠른 이유</h3>

<p>
현장 사진을 보내주시면 폐기물 양을 보다 빠르게 파악할 수 있어
상담 시간이 줄어들고 방문 일정 조율도 수월합니다.
</p>

</section>
"""

    marker = '<section class="section faq-section">'

    if "seo-stage2" not in html:
        html = html.replace(
            marker,
            seo_block + "\n" + marker
        )

    file.write_text(html, encoding="utf-8")

    print("완료:", slug)

print("SEO 2단계 완료")