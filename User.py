class User:
    def __init__(self, userArr):
        self.id = userArr[0]
        self.battleNetName = userArr[1]
        self.tracker = userArr[2]

    @staticmethod
    def userFromMessage(message):
        discordId = message.author.id
        battleNet = message.content.split(' ')[1].split('#')
        battleNetName = battleNet[0]
        tracker = battleNet[1]
        return User([discordId, battleNetName, tracker])
