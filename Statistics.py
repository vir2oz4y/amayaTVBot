import requests
from User import User


class CodStatistic:
    userURL = "http://warzoneapi.ru/warzone/api/v1.0/stats/{name}={tracker}"
    userMatchesURL = "http://warzoneapi.ru/warzone/api/v1.0/stats/{name}={tracker}/matches"
    userWeaponURL = "http://warzoneapi.ru/warzone/api/v1.0/stats/{name}={tracker}/weapons"
    matchURL = "http://warzoneapi.ru/warzone/api/v1.0/stats/matches/{matchID}"

    def getUserStatistics(self, user):
        URL = self.userURL.format(name=user.battleNetName, tracker=user.tracker)
        response = requests.get(URL)
        try:
            return response.json()
        except:
            return 404


if __name__ == '__main__':
    cs = CodStatistic()
    user = User([1, 'vir2oz', 21182])
    print(cs.getUserStatistics(user))
