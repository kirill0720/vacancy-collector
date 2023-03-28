"""
The "collector" module stores classes to connect and get vacancies
from HH, SJ, LinkedIn and other job platforms.
"""

from abc import ABC, abstractmethod
import requests


class Collector(ABC):
    @abstractmethod
    def get_request(self, keyword):
        ...


class HHCollector(Collector):
    """HeadHunter vacancy collector"""

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_request(self, keyword, page=0):
        params = {
            "text": keyword,
            "page": page
        }
        return requests.get(self.url, params=params)


class SJCollector(Collector):
    """SuperJob vacancy collector"""

    def __init__(self, api_key):
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.api_key = api_key

    def get_request(self, keyword, page=1):
        params = {
            "keywords": keyword,
            "page": page
        }
        headers = {"X-Api-App-Id": self.api_key}
        return requests.get(self.url, headers=headers, params=params)
