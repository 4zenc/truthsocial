import os
import google.generativeai as genai
from supabase import create_client

# Setup
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"])

def process_news():
    # Use 'gemini-1.5-flash' (without v1beta) - this is the standard model name
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Updated Prompt for cleaner JSON output
    prompt = "Find 1 major global news event today. Return ONLY valid JSON with keys: 'headline', 'impact' (for a citizen), and 'source_url'. No markdown, no extra text."
    
    response = model.generate_content(prompt)
    
    # Clean string to ensure it is just JSON
    text = response.text.replace("```json", "").replace("```", "").strip()
    
    # Import json library to parse safely
    import json
    data = json.loads(text)
    
    # Push to Supabase
    supabase.table("news_items").insert(data).execute()
    print("Success: News posted.")

if __name__ == "__main__":
    process_news()