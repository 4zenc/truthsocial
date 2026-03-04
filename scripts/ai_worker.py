import os
import json
import google.generativeai as genai
from supabase import create_client

def process_news():
    # 1. Configure
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"])
    
    # 2. Use 'gemini-pro' (more stable across different API accounts)
    model = genai.GenerativeModel('gemini-pro')
    
    # 3. Simple prompt
    prompt = "Give me one global news headline, a one-sentence impact for a normal person, and a source URL. Return ONLY raw JSON like: {'headline': '...', 'impact': '...', 'source_url': '...'}"
    
    response = model.generate_content(prompt)
    
    # 4. Clean text
    text = response.text.replace("```json", "").replace("```", "").strip()
    data = json.loads(text)
    
    # 5. Insert
    supabase.table("news_items").insert(data).execute()
    print("Success")

if __name__ == "__main__":
    process_news()