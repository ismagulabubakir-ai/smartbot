from google import genai
import os
import json

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_questions(analysis_result: dict) -> list[str]:
    """
    Принимает результат из analyze_candidate() и создаёт уточняющие вопросы.
    Возвращает список строк.
    """

    mismatches = analysis_result.get("несоответствия", [])
    comments = analysis_result.get("комментарии", {})

    prompt = f"""
    Ты — вежливый и дружелюбный HR-бот.
    На основе комментариев ниже задай короткие уточняющие вопросы кандидату.
    Избегай шаблонных фраз и давления.
    Формат ответа — JSON-список строк.

    Пример:
    ["Вакансия в Алматы, вы готовы рассмотреть переезд?",
     "У вас немного меньше опыта, готовы рассматривать обучение?"]

    Комментарии по несоответствиям:
    {json.dumps(comments, ensure_ascii=False, indent=2)}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.candidates[0].content.parts[0].text
    text = text.strip("```json").strip("```").strip()

    try:
        questions = json.loads(text)
    except json.JSONDecodeError:
        questions = [text]

    return questions



