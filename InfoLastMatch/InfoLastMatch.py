from functools import reduce

class InfoLastMatch:
    def __init__(self, json):
        self.duration = json['duration']
        self.nickName = self.getNickName(json)
        self.assists = json['segments'][0]['statistics']['assists']
        self.kills = json['segments'][0]['statistics']['kills']
        self.deaths = json['segments'][0]['statistics']['deaths']
        self.placement = json['segments'][0]['statistics']['placement']
        self.kd = json['segments'][0]['statistics']['kdRatio']
        self.damageDone = json['segments'][0]['statistics']['damageDone']
        self.gulagWin = self.getGulagWin(json)


    def getNickName(self, json):
        userName = json['segments'][0]['userName']
        clanTag = json['segments'][0]['clanTag']

        if clanTag is not None:
            return f'[{clanTag}] {userName}'

        return f'{userName}'

    def getGulagWin(self, json):
        return json['segments'][0]['statistics']['gulagKills'] > 0


class CommandStats:
    def __init__(self, dict):
        self.avgKDPerMatch = round(reduce(lambda x, y: x + y['statistics']['kdRatio'], dict, 0) / len(dict),2)
        self.kills = reduce(lambda x, y: x + y['statistics']['kills'], dict, 0)
        self.placement = dict[0]['placement']['displayValue']