import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class FinanceAgent:
    def __init__(self):
        # Küçük hata: API key kontrolünü bazen unutabiliyoruz
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def analyze_spending(self, data_summary):
        prompt = f"""
        Sen bir finans asistanısın. Aşağıdaki harcama verilerimi analiz et:
        {data_summary}
        
        Bana 3 cümlelik kısa bir tavsiye ver. 
        Hangi kategoride çok harcama yapmışım? Gelecek ay neyi kısmalıyım?
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except:
            return "AI şu an analiz yapamıyor, cüzdanına sahip çık!" 