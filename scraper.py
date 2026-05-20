import json
import requests
from bs4 import BeautifulSoup
from groq import Groq
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class AIScraperAgent:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.sources = [
            {
                "name": "Hacker News",
                "url": "https://news.ycombinator.com/",
                "selector": ("span", "titleline")
            },
            {
                "name": "TechCrunch",
                "url": "https://techcrunch.com/",
                "selector": ("h2", "wp-block-post-title")
            }
        ]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

    def get_ai_analysis(self, title, source):
        try:
            prompt = f"حلل هذا العنوان التقني من {source}: '{title}'\nأعطني:\n1. ترجمة عربية\n2. التصنيف (AI/Security/Startup/Other)\n3. الأهمية (High/Medium/Low)"
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": "أنت محلل تقني محترف. ردك يجب أن يكون JSON يحتوي على: 'translation' و 'category' و 'importance' فقط."},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response.choices[0].message.content.strip()
            return json.loads(result)
        except Exception as e:
            print(f"⚠️ خطأ في التحليل: {e}")
            return {"translation": "فشل التحليل", "category": "Other", "importance": "Low"}

    def scrape_source(self, source):
        results = []
        try:
            res = requests.get(source["url"], headers=self.headers, timeout=10)
            soup = BeautifulSoup(res.text, "html.parser")
            tag, cls = source["selector"]
            articles = soup.find_all(tag, class_=cls, limit=5)
            for item in articles:
                link_tag = item.find("a")
                if link_tag:
                    title = link_tag.text.strip()
                    link = link_tag.get("href", "")
                    print(f"🤖 تحليل: {title[:50]}...")
                    analysis = self.get_ai_analysis(title, source["name"])
                    results.append({
                        "title": title,
                        "link": link,
                        "source": source["name"],
                        "translation": analysis.get("translation", ""),
                        "category": analysis.get("category", "Other"),
                        "importance": analysis.get("importance", "Low"),
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
                    })
        except Exception as e:
            print(f"⚠️ خطأ في {source['name']}: {e}")
        return results

    def run(self, file_lock=None):
        print("🚀 بدء سحب الأخبار...")
        all_news = []
        for source in self.sources:
            print(f"\n📡 جاري سحب {source['name']}...")
            news = self.scrape_source(source)
            all_news.extend(news)

        if file_lock:
            with file_lock:
                with open("news_data.json", "w", encoding="utf-8") as f:
                    json.dump(all_news, f, ensure_ascii=False, indent=2)
        else:
            with open("news_data.json", "w", encoding="utf-8") as f:
                json.dump(all_news, f, ensure_ascii=False, indent=2)

        print(f"\n✅ تم حفظ {len(all_news)} خبر")
        return all_news