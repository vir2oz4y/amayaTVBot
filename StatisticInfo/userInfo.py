class Stats:
    """class to store statistic user"""
    def __init__(self, json_object):
        self.lifetime_info = self.set_type_info(json_object['Stats']['lifetime'])  # stats for lifetime
        self.warzone_info = self.set_type_info(json_object['Stats']['warzone'])   # stats for warzone


    def set_type_info(self, type_stats):
        """return class StatsElement"""
        return StatsElement(type_stats)


class StatsElement:
    """class elements of statistics"""
    def __init__(self, type_stats):
        self.kills = type_stats['kills']
        self.deaths = type_stats['deaths']
        self.downs = type_stats['downs']
        self.kda = type_stats['kda']
        self.wins = type_stats['wins']
        self.top5 = type_stats['top5']
        self.top10 = type_stats['top10']
        self.top25 = type_stats['top25']
        self.wr = type_stats['winrate']
        self.avgLife = type_stats['avgLife']
        self.contracts = type_stats['contracts']
        self.gamesPlayed = type_stats['gamesPlayed']
        self.scorePerGame = type_stats['scorePerGame']
        self.scorePerMinute = type_stats['scorePerMinute']
        self.timePlayed = type_stats['timePlayed']
        self.weeklyDamagePerMatch = type_stats['weeklyDamagePerMatch']





