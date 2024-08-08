import json

# Пример JSON-объекта
json_data = {'success': True, 'message': 'Успешно', 'meta': {'total': 1, 'page': 1, 'pages': 1, 'perPage': 20}, 'data': [{'ownerId': 778913, 'card': None, 'fio': 'Петр I', 'chatId': -4165367083, 'limitOut': 1000000, 'status': {'id': 0, 'name': 'Заблокирован'}, 'mainPhone': None, 'secondaryPhone': None, 'isDeposit': False, 'tgNick': '@Mike_Taran', 'incommingTransactionsIsAllowed': True, 'outcommingTransactionsIsAllowed': True, 'agentId': 89, 'amount': None, 'pingInterval': 60, 'imei': '12345678008913', 'pingStatus': True, 'disputesLimit': 5, 'priority': 1, 'outcomingOrdersPriority': 1, 'ping': False, 'trustLimit': 1000000, 'isAutoAssigmentEnabled': False, 'goip': '27G3201', 'channelId': None, 'isSbpEnabled': False, 'limitMinIn': 0, 'trusted': False}]}


data = json_data

def find_all_keys(d, key):
    values = []
    if key in d:
        values.append(d[key])
    for k, v in d.items():
        if isinstance(v, dict):
            values.extend(find_all_keys(v, key))
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    values.extend(find_all_keys(item, key))
    return values

# Пример использования функции
key_to_find = "name"
values = find_all_keys(data, key_to_find)
print(f"Значения ключа '{key_to_find}': {values}")
