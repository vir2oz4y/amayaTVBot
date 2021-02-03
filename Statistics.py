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
            return response
        except:
            return 404

    def getUserStatJson(self, user):
        return self.getUserStatistics(user).json()

    def getLastMatchStats(self, user):
        URL = self.userMatchesURL.format(name=user.battleNetName, tracker=user.tracker)
        response = requests.get(URL)
        try:
            return response
        except:
            return 404

    def getLastMatchJson(self, user):
        return self.getLastMatchStats(user).json()['matches'][0]

    def getMatchByID(self, matchId):
        URL = self.matchURL.format(matchID=matchId)
        response = requests.get(URL)
        return response

    def getMatchByIDJson(self, matchId):
        return self.getMatchByID(matchId).json()





if __name__ == '__main__':
    cs = CodStatistic()
    myUser = User([1, 'vir2oz4y', 2249])


