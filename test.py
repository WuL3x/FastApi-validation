# from typing import Type, List
#
# from pydantic import BaseModel
#
# from models import BaseInfo, EmailInfo, Order
#
# data = {
#     "id": 123,
#     "username": "john_doe",
#     "age": 30,
#     "cellphone": "+123456789",
#     "email": "john@example.com",
#     "password": "strongpassword",
#     "register_date": "2023-01-01T00:00:00"
# }
#
# base_info_full = {
#     "id": 1,
#     "username": "wul3x",
#     "age": 25,
#     "cellphone": "80123456789"
# }
#
# base_info_test = {
#     "id": 1,
#     "username": "Иван",
#     "age": 30,
#     "cellphone": "+71234567890",
#     "addition_field1": 1234,
#     "data_order": "10-10-2010"
# }
#
# base_info_test_mix = {
#
#     "cellphone": "+71234567890",
#     "email": "IvanovIvan@example.com",
#     "password": "Qwerty123456",
#     "addition_field1": "dsa",
#     "addition_field2": "sdas"
# }
#
# base_order_test = {
#     "order_id": 321567,
#     "email": "vanechkaivanov@example.com",
#     "product_name": "Мышка игровая для киберкотлет",
#     "quantity": 4
# }
#
#
# base_tests = [base_info_test_mix,base_info_test,base_info_test,data, base_order_test]
#
# def validate_template(templates: List[Type[BaseModel]], data: dict) -> bool:
#     for template in templates:
#         try:
#             template(**data)
#             return template.get_template_name()
#         except ValueError:
#             continue
#
#
# templates = [BaseInfo, EmailInfo, Order]
#
# # Проверяем данные
# for data in base_tests:
#     template_name = validate_template(templates, data)
#     if template_name:
#         print(f"Данные соответствуют шаблону: {template_name}")
#     else:
#         print("Нет подходящего шаблона.")
#
# if __name__ == "__main__":
#     validate_template(templates, data)