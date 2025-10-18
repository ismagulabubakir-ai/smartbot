def calculate_relevance(analysis_result: dict) -> dict:
    """
    Принимает результат анализа (из analyzer.py)
    Возвращает процент релевантности и краткое объяснение.
    """

    # Веса критериев (можно менять в зависимости от важности)
    weights = {
        "город": 0.15,
        "опыт": 0.3,
        "образование": 0.1,
        "языки": 0.1,
        "формат": 0.15,
        "зарплата": 0.2
    }

    # Берём списки совпадений и несоответствий
    matches = set(analysis_result.get("совпадения", []))
    mismatches = set(analysis_result.get("несоответствия", []))

    # Общие критерии, которые можно оценить
    criteria = set(weights.keys())
    score = 0
    total_weight = sum(weights.values())

    for criterion, weight in weights.items():
        if criterion in matches:
            score += weight  # совпадение = полный балл
        elif criterion in mismatches:
            score += weight * 0.3  # частичное соответствие
        else:
            score += weight * 0.5  # неизвестно → среднее значение

    # Вычисляем процент релевантности
    relevance = round((score / total_weight) * 100, 1)

    # Генерируем краткое объяснение
    if relevance >= 85:
        summary = f"Подходит на {relevance}%, небольшие уточнения по деталям."
    elif relevance >= 60:
        summary = f"Подходит частично ({relevance}%), есть расхождения: {', '.join(list(mismatches)[:3])}."
    else:
        summary = f"Низкая релевантность ({relevance}%), основные несоответствия: {', '.join(list(mismatches)[:3])}."

    return {
        "relevance": relevance,
        "summary": summary
    }


