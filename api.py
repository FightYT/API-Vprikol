import requests


class VprikolAPI:
    def __init__(self, token: str) -> None:
        session = requests.sessions.Session()
        session.params = {"token": token}  # Полученый токен

        self.base_url = "https://api.vprikol.dev"  # А то у веселого прикола постоянно меняется домен и/или ссылка
        self.session = session

    def get_members(self, fraction_id: int, server: int) -> dict:
        """GET | Данная функция возвращает полный список игроков, состоящих во фракции"""
        return self.session.get(f"{self.base_url}/members/",
                                params={"server": server, "fraction_id": fraction_id}).json()

    def get_task_result(self, request_id: int) -> dict:
        """GET | Получение статистики игрока по идентификатору из созданного задания"""
        return self.session.get(f"{self.base_url}/find/getTaskResult/", params={"request_id": request_id}).json()

    def get_rating(self, rating_type: int, server: int) -> dict:
        """GET | Топ игроков/семей на сервере по параметрам"""
        return self.session.get(f"{self.base_url}/rating/", params={"type": rating_type, "server": server}).json()

    def get_status(self) -> dict:
        """GET | Доступность серверов Аризоны"""
        return self.session.get(f"{self.base_url}/status/").json()

    def get_estate(self, estate_type: str, server: int) -> dict:
        """GET | Возвращает дома или бизнесы, у которых нет владельца"""
        return self.session.get(f"{self.base_url}/get_estate/",
                                params={"estate_type": estate_type, "server": server}).json()

    def getCheckRP(self, nick: str) -> dict:
        """GET | Проверка ника на РПшность"""
        return self.session.get(f"{self.base_url}/checkrp/", params={"nick": nick}).json()

    def get_rp_nick(self, gender: str, nation: str) -> dict:
        """GET | Генерация РП ника по параметрам"""
        return self.session.get(f"{self.base_url}/rpnick/", params={"gender": gender, "nation": nation}).json()

    def get_ip(self) -> dict:
        """GET | IP-адрес запроса. Поддерживается IPv6"""
        return requests.get(f"{self.base_url}/ip/").json()

    def create_task(self, nick: str, server: int) -> dict:
        """POST | Создание задания на получение статистики игрока"""
        return self.session.post(f"{self.base_url}/find/createTask/", params={"nick": nick, "server": server}).json()

    def generate_ss(self, commands: str) -> dict:
        """POST | API генератора скриншот-ситуаций из ВК-бота"""
        return self.session.post(f"{self.base_url}/rpnick/", params={"commands": commands}).json()
