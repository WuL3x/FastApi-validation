import re
from typing import List, Type, Dict

from fastapi import APIRouter, Body
from pydantic import BaseModel

from db import add_data_to_db, remove_from_db
from models import BaseInfo, EmailInfo, User, Order

router = APIRouter()

re_date = re.compile(
    r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$|^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$")
re_phone = re.compile(r"^(\+7|8)[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}$")
re_email = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
re_number = re.compile(r"^\d+(\.\d+)?$")


def validate_template(templates: List[Type[BaseModel]], data: dict) -> str:
    for template in templates:
        try:
            # data_for_validation = {k: v for k, v in data.items()}
            template(**data)
            return template.get_template_name()
        except ValueError:
            continue
    return None

def is_valid_date(value: str) -> bool:
    return bool(re.match(re_date, value))


def is_valid_cell_numbers(value: str) -> bool:
    return bool(re.match(re_phone, value))


def is_valid_email(value: str) -> bool:
    return bool(re.match(re_email, value))


def is_valid_number(value: str) -> int:
    try:
        int(value)
        return True
    except ValueError:
        return False


def match_error_field(value: str) -> str:
    if is_valid_date(value):
        return 'Дата'
    elif is_valid_cell_numbers(value):
        return 'Номер телефона'
    elif is_valid_email(value):
        return 'Эмейл'
    elif is_valid_number(value):
        return 'Число'
    else:
        return 'Текст'


def find_coincidence(data: Dict[str, any]) -> Dict[str, str]:

    potencial_types = {}
    for key, value in data.items():
        potencial_types[key] = match_error_field(str(value))
    return potencial_types


def find_similar(templates: List[Type[BaseModel]], data: Dict[str, any]) -> str:
    best_choice = None
    max_match = 0
    match_try = 3  # Минимальное количество совпадающих полей для поиска

    for template in templates:
        matches = 0
        non_similar_fields = 0

        # Перебираем поля шаблона и сравниваем их с данными
        for field_name, field_type in template.__annotations__.items():
            if field_name in data:  # Если поле есть в данных
                field_value = data[field_name]
                try:
                    # Проверяем тип поля в данных
                    if isinstance(field_value, field_type):
                        matches += 1  # Если тип совпадает, увеличиваем счетчик совпадений
                    else:
                        non_similar_fields += 1  # Если тип не совпадает, увеличиваем счетчик несовпадений
                except (ValueError, TypeError):
                    non_similar_fields += 1  # Если ошибка, считаем это несовпадением
                    continue

        # Для похожего шаблона: максимум 2 несовпадающих поля
        if matches >= match_try and non_similar_fields <= 1:
            # Если количество совпавших полей больше текущего максимума, обновляем best_choice
            if matches > max_match:
                max_match = matches
                best_choice = template

    # Возвращаем имя шаблона, если похожий найден
    return best_choice.get_template_name() if best_choice else None


@router.post("/get_form")
async def get_form(data: dict = Body(...)):
    add_data_to_db(data)
    templates = [BaseInfo, EmailInfo, User, Order]
    match_template = validate_template(templates, data)
    try:
        if match_template:
            return {"Шаблон": match_template}

        similar_template = find_similar(templates, data)
        if similar_template:
            return {"Похожий шаблон": similar_template}

        potencial_types = find_coincidence(data)
        return potencial_types
    finally:
        remove_from_db()
