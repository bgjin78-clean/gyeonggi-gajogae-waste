from pathlib import Path
from datetime import datetime

BASE_URL = "https://gyeonggi-gajogae-waste.vercel.app"
SITE_NAME = "경기 가족애 폐기물처리"

today = datetime.now().strftime("%Y-%m-%d")

urls = [BASE_URL + "/"]

for p in sorted(Path("regions").glob("*/index.html")):
    slug = p.parent.name
    urls.append(f"{BASE_URL}/regions/{slug}/")

urls.append(f"{BASE_URL}/regions/")

for p in sorted(Path("reviews").glob("*.html")):
    if p.name == "index.html":
        urls.append(f"{BASE_URL}/reviews/")
    else:
        urls.append(f"{BASE_URL}/reviews/{p.name}")

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for url in urls:
    priority = "1.0" if url == BASE_URL + "/" else "0.8"
    sitemap += f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>
"""

sitemap += "</urlset>\n"
Path("sitemap.xml").write_text(sitemap, encoding="utf-8")

rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>{SITE_NAME}</title>
<link>{BASE_URL}</link>
<description>경기 가족애 폐기물처리 지역별 안내와 작업후기</description>
<language>ko</language>
"""

for p in sorted(Path("reviews").glob("*-review-01.html"))[:30]:
    title = p.stem.replace("-", " ")
    rss += f"""
<item>
<title>{title}</title>
<link>{BASE_URL}/reviews/{p.name}</link>
<description>경기 폐기물처리 작업후기</description>
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

print("sitemap.xml / rss.xml / robots.txt 생성 완료")
print("총 URL 수:", len(urls))