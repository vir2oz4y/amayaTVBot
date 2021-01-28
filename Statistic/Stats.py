from  Statistic.StatsElement import StatsElement

class Stats:
    def __init__(self, json_object):
        self.json = json_object
        lifetime_stats = self.json['data']['segments'][0]['stats']
        self.lifetime_info = self.set_type(lifetime_stats)  # stats for lifetime

        warzone_stats = self.json['data']['segments'][1]['stats']
        self.warzone_info = self.set_type(warzone_stats)  # stats for warzone

        # plunder_stats = self.json['data']['segments'][2]['stats']
        # self.plunder_info = self.set_type(plunder_stats)  # stats for plunder


    def set_type(self, type_stats):
        kills=type_stats['kills']['value']
        deaths=type_stats['deaths']['value']
        downs=type_stats['downs']['value']
        kda=type_stats['kdRatio']['value']
        wins=type_stats['wins']['value']
        top5=type_stats['top5']['value']
        top10=type_stats['top10']['value']
        top25=type_stats['top25']['value']
        wr=type_stats['wlRatio']['displayValue']
        avgLife=type_stats['averageLife']['displayValue']
        return StatsElement(kills, deaths, downs, kda, wins, top5, top10, top25, wr, avgLife)


    def __str__(self):
        return "lifetime - " + str(self.lifetime_info) + '\nwarzone - ' + str(self.warzone_info)
