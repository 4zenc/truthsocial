import os
import google.generativeai as genai
from supabase import create_client

# Setup
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"])

def process_news():
    # You can swap this URL with any high-trust RSS feed
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Simple prompt logic for the AI Factory
    prompt = "Read current top world news. Return ONLY a JSON object with 'headline', 'impact' (for a citizen), and 'source_url'."
    
    response = model.generate_content(prompt)
    data = eval(response.text.replace("```json", "").replace("```", ""))
    
    # Push to Supabase
    supabase.table("news_items").insert(data).execute()

if __name__ == "__main__":
    process_news()