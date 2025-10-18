from google import genai
import os
import json

# Создаём клиента Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_candidate(vacancy: dict, resume: dict) -> dict:
    """
    Анализирует совпадения и несоответствия между вакансией и резюме.
    Возвращает JSON с комментариями.
    """

    prompt = f"""
    Ты — помощник HR. Сравни данные вакансии и резюме кандидата.
    Найди совпадения и несоответствия по критериям:
    город, опыт, образование, языки, формат работы, зарплата, описание.

    Верни JSON в виде:
    {{
        "совпадения": [список полей],
        "несоответствия": [список полей],
        "комментарии": {{
            "город": "...",
            "опыт": "...",
            ...
        }}
    }}

    Вакансия: {json.dumps(vacancy, ensure_ascii=False)}
    Резюме: {json.dumps(resume, ensure_ascii=False)}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Gemini может вернуть текст, нужно преобразовать в dict
    try:
        result = response.candidates[0].content.parts[0].text
        result = result.strip("```json").strip("```").strip()
        result = json.loads(result)
    except json.JSONDecodeError:
        print("Parsing error")
        print(response.text)
        result = {"raw_output": response.text}

    return result