import http.client
import json

url = "http://127.0.0.1"
port = 8081
endpoint = "/get_form"

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json; charset=utf-8',
}

base_info_full = {
    "id": 1,
    "username": "wul3x",
    "age": 25,
    "cellphone": "80123456789"
}

base_info_test = {
    "id": 1,
    "username": "Иван",
    "age": 30,
    "cellphone": "+71234567890",
    "addition_field1": 1234,
    "data_order": "10-10-2010"
}

base_info_test_mix = {
    "id": 1,
    "username": "Иван",
    "age": 30,
    "cellphone": "+71234567890",
    "email": "IvanovIvan@example.com",
    "password": "Qwerty123456",
    "addition_field1": "dsa",
    "addition_field2": "sdas"
}

base_email_info = {
    "email": "IvanovIvan@example.com",
    "username": "Ivan4eg",
    "password": "Qwerty123456",
    "register_date": "10-10-2010"
}

base_user_test = {
    "username": "PDestroyer228",
    "usersurname": "1337MLGPROGAMER",
    "bdate": "07-07-2007",
    "password": "Qwerty",
    "email": "vanechkaivanov@example.com",
    "quantity": 4
}

base_order_test = {
    "order_id": 321567,
    "email": "vanechkaivanov@example.com",
    "cellphone": "+71234567890",
    "age": 14,
    "product_id": 1245,
    "product_name": "Мышка игровая для киберкотлет",
    "quantity": 4
}

base_error = {
    "Text": "Текстовое сообщение",
    "data": "01-02-2003",
    "HasHomework": True,
    "bimbim": "bambom",
    "email": "EMAIL@example.com",
    "What_else": "SMTH",
    "number": "1234567890"
}

test_list = [base_info_full, base_info_test, base_info_test_mix, base_email_info, base_user_test, base_order_test,
             base_error]


def send_post_request(url, port, headers, endpoint, test):
    # Не нужно повторно присваивать переменную headers, можно сразу использовать параметр
    conn = http.client.HTTPConnection(url, port)
    json_data = json.dumps(test)

    try:
        # Отправка POST запроса
        conn.request("POST", endpoint, body=json_data, headers=headers)
        response = conn.getresponse()  # Получение ответа
        response_data = response.read().decode("utf-8")
        return response.status, response_data  # Возвращаем статус и данные ответа
    except Exception as e:
        print(f"Ошибка: {e}")
        return None, None
    finally:
        conn.close()  # Закрытие соединения после завершения

for i, test in enumerate(test_list, 1):
    print(f"Тест {i}")
    status, response = send_post_request(url, port, headers, endpoint, test)
    print(f"Статус запроса: {status}")
    print(f"Ответ: {response}")
