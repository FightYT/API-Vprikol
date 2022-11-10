import requests


class VprikolAPI:
    def __init__(self, token: str) -> None:
        session = requests.sessions.Session()
        session.params = {"token":token} # Полученый токен

        self.baseUrl = "https://api.vprikol.dev" # А то у веселого прикола постоянно меняется домен и/или ссылка
        self.session = session 


    def getMembers(self, fraction_id:int, server):
        """GET | Данная функция возвращает полный список игроков, состоящих во фракции"""
        return self.session.get(f"{self.baseUrl}/members/", params={"server":server, "fraction_id":fraction_id}).json()    

    def getTaskResult(self, request_id:int):
        """GET | Получение статистики игрока по идентификатору из созданного задания"""
        return requests.get(f"{self.baseUrl}/find/getTaskResult/", params={"request_id":request_id}).json()

    def getRating(self, type:int, server):
        """GET | Топ игроков/семей на сервере по параметрам"""
        return self.session.get(f"{self.baseUrl}/rating/", params={"type":type, "server":server}).json()

    def getStatus(self):
        """GET | Доступность серверов Аризоны"""
        return self.session.get(f"{self.baseUrl}/status/").json()
        
    def getEstate(self, estate_type:str, server):
        """GET | Возвращает дома или бизнесы, у которых нет владельца"""
        return self.session.get(f"{self.baseUrl}/get_estate/", params={"estate_type":estate_type, "server":server}).json()

    def getCheckRP(self, nick:str):
        """GET | Проверка ника на РПшность"""
        return self.session.get(f"{self.baseUrl}/checkrp/", params={"nick":nick}).json()

    def getRPNick(self, gender:str, nation:str):
        """GET | Генерация РП ника по параметрам"""
        return self.session.get(f"{self.baseUrl}/rpnick/", params={"gender":gender, "nation":nation}).json()

    def getIP(self):
        """GET | IP-адрес запроса. Поддерживается IPv6"""
        return requests.get(f"{self.baseUrl}/ip/").json()

    def createTask(self, nick:str, server):
        """POST | Создание задания на получение статистики игрока"""
        return self.session.post(f"{self.baseUrl}/find/createTask/", params={"nick":nick, "server":server}).json()

    def generateSS(self, commands:str):
        """POST | API генератора скриншот-ситуаций из ВК-бота"""
        return self.session.get(f"{self.baseUrl}/rpnick/", params={"commands":commands}).json()