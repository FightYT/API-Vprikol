from api import VprikolAPI

api = VprikolAPI("token полученый у Веселого прикола")

# Пример использование API
ip = api.getIP()

print(api) # Тип ответа: dict (словарь) | Пример ответа: {'real_ip': '123.123.123.123', 'proxied_ip': '172.123.123.123', 'country': 'BY'}