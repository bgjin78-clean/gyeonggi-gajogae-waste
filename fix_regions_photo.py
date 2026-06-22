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

def num(n, max_n):
    return ((n - 1) % max_n) + 1

for idx, (slug, name) in enumerate(REGIONS, start=1):
    path = Path("regions") / slug / "index.html"

    if not path.exists():
        print(f"없음: {path}")
        continue

    html = path.read_text(encoding="utf-8")

    b = num(idx, 30)
    p = num(idx * 3, 25)
    a = b

    new_photo = f"""
<section class="section photo-section">
  <p class="section-label">현장사진</p>
  <h2>{name} 폐기물처리 전·중·후 사진</h2>
  <p class="section-desc">
    지역페이지는 전·중·후 흐름을 간단히 확인할 수 있도록 3장으로 구성했습니다.
    상세 작업후기는 작업 전 2장, 작업 중 1장, 작업 후 2장 구성으로 확인할 수 있습니다.
  </p>

  <div class="photo-grid region-photo-grid">
    <article>
      <h3>작업 전</h3>
      <img src="/images/main/before-{b:02d}.jpg" alt="{name} 폐기물처리 작업 전" />
    </article>

    <article>
      <h3>작업 중</h3>
      <img src="/images/main/process-{p:02d}.jpg" alt="{name} 폐기물처리 작업 중" />
    </article>

    <article>
      <h3>작업 후</h3>
      <img src="/images/main/after-{a:02d}.jpg" alt="{name} 폐기물처리 작업 후" />
    </article>
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

    path.write_text(html, encoding="utf-8")
    print(f"사진 3장 구조 수정 완료: {name}")

print("지역페이지 전·중·후 3장 구조 수정 완료")