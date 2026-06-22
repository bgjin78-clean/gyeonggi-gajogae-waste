from pathlib import Path
import re

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

REGION_TRAITS = [
    "아파트와 오피스텔이 많은 지역이라 엘리베이터 사용 가능 여부가 중요합니다.",
    "빌라와 단독주택 현장이 섞여 있어 차량 진입 동선을 먼저 확인하는 것이 좋습니다.",
    "신도시와 오래된 주거지가 함께 있어 폐기물 종류가 현장마다 다를 수 있습니다.",
    "상가와 주거공간이 함께 있는 지역이라 가정폐기물과 사업장 집기가 같이 나오는 경우가 있습니다.",
    "이사 전후 정리 문의가 많은 지역으로 대형가구와 생활폐기물을 함께 확인하는 것이 좋습니다.",
]

def num(n, max_n):
    return ((n - 1) % max_n) + 1

for idx, (slug, name) in enumerate(REGIONS, start=1):
    path = Path("regions") / slug / "index.html"
    if not path.exists():
        print(f"없음: {path}")
        continue

    html = path.read_text(encoding="utf-8")

    b1 = num(idx, 30)
    b2 = num(idx + 1, 30)
    p1 = num(idx * 3, 25)
    a1 = b1
    a2 = b2

    trait = REGION_TRAITS[idx % len(REGION_TRAITS)]

    seo_block = f"""
<section class="section text-section region-seo">
  <p class="section-label">지역별 폐기물처리 안내</p>
  <h2>{name} 폐기물처리, 직접 하기 어려운 이유</h2>

  <p>
    {name} 폐기물처리는 단순히 물건을 밖으로 빼는 작업만으로 끝나지 않습니다.
    폐기물의 양, 반출 동선, 차량 진입 가능 여부, 층수와 엘리베이터 사용 여부에 따라
    작업 시간과 필요한 인원이 달라질 수 있습니다.
  </p>

  <p>
    {trait}
    특히 침대, 장롱, 소파, 책상처럼 부피가 큰 물품은 분해와 이동 과정이 필요할 수 있고,
    생활폐기물과 잔짐이 함께 있는 경우에는 종류별 분리 정리가 먼저 진행되어야 합니다.
  </p>

  <div class="notice-box">
    <h3>{name} 폐기물처리 전 확인하면 좋은 사항</h3>
    <ul>
      <li>폐기물의 대략적인 양과 종류</li>
      <li>엘리베이터 사용 가능 여부</li>
      <li>차량 진입 및 건물 앞 정차 가능 여부</li>
      <li>대형가구 분해 필요 여부</li>
      <li>사진 상담 가능 여부</li>
    </ul>
  </div>

  <h3>{name} 폐기물처리 비용이 달라지는 이유</h3>
  <p>
    같은 1톤 차량 기준이라도 현장 상황에 따라 비용은 달라질 수 있습니다.
    계단 작업이 필요한 경우, 차량을 멀리 세워야 하는 경우,
    대형가구가 많거나 분류해야 할 생활폐기물이 많은 경우에는 작업 시간이 길어질 수 있습니다.
  </p>
</section>
"""

    # 기존 지역 안내 섹션 뒤, 주요 업무 섹션 앞에 SEO 블록 삽입
    marker = '<section class="section">\n  <p class="section-label">주요 업무</p>'
    if "region-seo" not in html and marker in html:
        html = html.replace(marker, seo_block + "\n" + marker)

    new_photo = f"""
<section class="section photo-section">
  <p class="section-label">현장사진</p>
  <h2>{name} 폐기물처리 전·중·후 사진</h2>
  <p class="section-desc">
    전·후 사진은 같은 번호를 사용하고, 작업 중 사진은 현장 흐름에 맞게 배치했습니다.
  </p>

  <h3>작업 전</h3>
  <div class="photo-grid">
    <img src="/images/main/before-{b1:02d}.jpg" alt="{name} 폐기물처리 작업 전 1" />
    <img src="/images/main/before-{b2:02d}.jpg" alt="{name} 폐기물처리 작업 전 2" />
  </div>

  <h3>작업 중</h3>
  <div class="photo-grid single-photo">
    <img src="/images/main/process-{p1:02d}.jpg" alt="{name} 폐기물처리 작업 중" />
  </div>

  <h3>작업 후</h3>
  <div class="photo-grid">
    <img src="/images/main/after-{a1:02d}.jpg" alt="{name} 폐기물처리 작업 후 1" />
    <img src="/images/main/after-{a2:02d}.jpg" alt="{name} 폐기물처리 작업 후 2" />
  </div>
</section>
"""

    html = re.sub(
        r'<section class="section photo-section">.*?</section>',
        new_photo,
        html,
        count=1,
        flags=re.S
    )

    html = html.replace(
        '<a href="/reviews/">지역별 작업후기 전체보기</a>',
        f'<a href="/reviews/{slug}-review-01.html">{name} 작업후기 보기</a>'
    )

    path.write_text(html, encoding="utf-8")
    print(f"업그레이드 완료: {name}")

print("31개 지역페이지 SEO/사진 업그레이드 완료")