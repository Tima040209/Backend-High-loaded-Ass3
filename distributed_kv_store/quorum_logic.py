import requests

INSTANCES = ['http://localhost:8000', 'http://localhost:8001', 'http://localhost:8002']

def write_with_quorum(key, value):
    success_count = 0
    for instance in INSTANCES:
        try:
            response = requests.post(f'{instance}/api/store/', json={'key': key, 'value': value})
            if response.status_code == 201:
                success_count += 1
        except requests.exceptions.RequestException:
            continue
    return success_count >= 2

def read_with_quorum(key):
    responses = []
    for instance in INSTANCES:
        try:
            response = requests.get(f'{instance}/api/retrieve/{key}/')
            if response.status_code == 200:
                responses.append(response.json()['value'])
        except requests.exceptions.RequestException:
            continue
    # Проверка на совпадение двух значений
    for value in set(responses):
        if responses.count(value) >= 2:
            return value
    return None  # Если кворум не достигнут
