class StatsElement:
    def __init__(self, kills, deaths, downs, kda, wins, top5, top10, top25, wr, avgLife):
        self.kills = kills
        self.deaths = deaths
        self.downs = downs
        self.kda = kda
        self.wins = wins
        self.top5 = top5
        self.top10 = top10
        self.top25 = top25
        self.wr = wr
        self.avgLife = avgLife

    def __str__(self):
        elements = [str(self.kills),
                    str(self.deaths),
                    str(self.downs),
                    str(self.kda),
                    str(self.wins),
                    str(self.top5),
                    str(self.top10),
                    str(self.top25),
                    str(self.wr),
                    str(self.avgLife)
                    ]
        string = ' ,'.join(elements)
        return string
