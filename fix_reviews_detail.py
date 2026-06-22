from pathlib import Path
import re

for path in Path("reviews").glob("*-review-01.html"):
    html = path.read_text(encoding="utf-8")

    html = html.replace(
        '<section class="sub-hero">',
        '<section class="sub-hero review-detail-hero">',
        1
    )

    # 기존 상담 영역이 너무 넓게 나오면 감싸서 정리
    html = html.replace(
        '<section class="section contact-mini">',
        '<section class="review-contact-box"><div class="contact-mini">',
        1
    )

    html = html.replace(
        '</section>\n</main>',
        '</div></section>\n</main>',
        1
    )

    path.write_text(html, encoding="utf-8")
    print(f"수정 완료: {path}")

print("작업후기 상세페이지 레이아웃 수정 완료")