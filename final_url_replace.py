from pathlib import Path

OLD_SITE = "https://gyeonggi-gajogae-waste.vercel.app"
NEW_SITE = "https://www.gyeonggi.gajogae-waste.com"

SEOUL_WASTE = "https://www.seoul.gajogae-waste.com/"
GYEONGGI_YUPUM = "https://www.gyeonggi.gajogae-yupum.com/"
SEOUL_YUPUM = "https://www.seoul.gajogae-yupum.com/"

for path in list(Path(".").glob("*.html")) + list(Path("regions").glob("**/*.html")) + list(Path("reviews").glob("**/*.html")):
    html = path.read_text(encoding="utf-8")
    html = html.replace(OLD_SITE, NEW_SITE)

    html = html.replace('href="#">서울 가족애폐기물처리</a>', f'href="{SEOUL_WASTE}">서울 가족애폐기물처리</a>')
    html = html.replace('href="#">경기 가족애유품정리</a>', f'href="{GYEONGGI_YUPUM}">경기 가족애유품정리</a>')
    html = html.replace('href="#">서울 가족애유품정리</a>', f'href="{SEOUL_YUPUM}">서울 가족애유품정리</a>')

    html = html.replace('href="https://seoul-gajogae-waste.vercel.app"', f'href="{SEOUL_WASTE}"')
    html = html.replace('href="https://gyeonggi-gajogae-yupum.vercel.app"', f'href="{GYEONGGI_YUPUM}"')
    html = html.replace('href="https://seoul-gajogae-yupum.vercel.app"', f'href="{SEOUL_YUPUM}"')

    path.write_text(html, encoding="utf-8")
    print("수정:", path)

for file in ["sitemap.xml", "rss.xml", "robots.txt"]:
    p = Path(file)
    if p.exists():
        text = p.read_text(encoding="utf-8")
        text = text.replace(OLD_SITE, NEW_SITE)
        p.write_text(text, encoding="utf-8")
        print("URL 수정:", file)

print("최종 도메인/백링크 교체 완료")