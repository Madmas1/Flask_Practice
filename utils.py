# Подключаем модуль по обработке JSON
import json


def get_candidates_list(filename):
    """Метод загружающий список кандидатов из JSON файла"""
    with open(filename, 'r', encoding='utf-8') as candidates:
        candidates_list = json.load(candidates)
    return candidates_list


def format_candidates_list(candidates_list):
    """Метод формирующий страничку со списком всех кандидатов"""
    page = '<pre>'
    for candidate in candidates_list:
        page += (
            '<pre>'
            f"Имя кандидата - {candidate['name']} " 
            f"Позиция кандидата - {candidate['position']} "
            f"Навыки - {candidate['skills']}"
        )
    page += '</pre>'
    return page


def get_candidate_page(candidate_id, candidates_list):
    """Метод формирующий страничку кандидата по указанию его ID"""
    page = ""
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            page += (
                f"<img src='{candidate['picture']}'>"
                "<pre>"
                f""
                f"Имя кандидата - {candidate['name']} "
                f"Позиция кандидата - {candidate['position']} "
                f"Навыки - {candidate['skills']}"
                "<pre>"
            )
    return page


def get_candidate_skills_page(skill, candidates_list):
    """Метод формирующий страничку кандидата по указанию его навыка"""
    page = "<pre>"
    for candidate in candidates_list:
        if skill.lower() in candidate['skills'].lower():
            page += (
                "<pre>"
                f"Имя кандидата - {candidate['name']} "
                f"Позиция кандидата - {candidate['position']} "
                f"Навыки - {candidate['skills']}"
            )
    page += "</pre>"
    return page