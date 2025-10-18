import json
from .analyze import analyze_candidate
from .question_generator import generate_questions
from .relevance_calculator import calculate_relevance


def process_candidate(vacancy: dict, resume: dict) -> dict:
    """
    Полный цикл анализа кандидата:
    1. Анализирует совпадения и несоответствия
    2. Генерирует уточняющие вопросы
    3. Считает релевантность
    4. Возвращает сводку для работодателя
    """

    # 1️⃣ Анализ
    analysis = analyze_candidate(vacancy, resume)

    # 2️⃣ Генерация уточняющих вопросов
    questions = generate_questions(analysis)

    # 3️⃣ Подсчёт релевантности
    relevance_info = calculate_relevance(analysis)

    # 4️⃣ Объединяем всё в итоговый ответ
    result = {
        "relevance": relevance_info["relevance"],
        "summary": relevance_info["summary"],
        "matches": analysis.get("совпадения", []),
        "mismatches": analysis.get("несоответствия", []),
        "questions": questions,
        "comments": analysis.get("комментарии", {})
    }

    return result


