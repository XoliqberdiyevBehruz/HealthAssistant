from google import genai

def text_to_ai(text):
    client = genai.Client(api_key="AIzaSyC4o2Mvs8JEzkBKs2hf0hoGRiwtiOg80UA")

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"{text}, I don't need advice, I just need to know which doctor type to look at and why."
    )
    return response.text