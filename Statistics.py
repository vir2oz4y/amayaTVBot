import requests
from User import User

class CodStatistic:
    userURL = "http://warzoneapi.ru/warzone/api/v1.0/stats/{name}={tracker}"
    userMatchesURL = "http://warzoneapi.ru/warzone/api/v1.0/stats/{name}={tracker}/matches"
    userWeaponURL = "http://warzoneapi.ru/warzone/api/v1.0/stats/{name}={tracker}/weapons"
    matchURL = "http://warzoneapi.ru/warzone/api/v1.0/stats/matches/{matchID}"

    def getUserStatistics(self, user):
        URL = self.userURL.format(name=user.name, tracker=user.tracker)
        response = requests.get(URL)
        print(response.json())

if __name__ == '__main__':
    cs = CodStatistic()

    cs.getUserStatistics()