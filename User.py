class User:
    def __init__(self, discord_id, name, cod_id):
        self._name_warzone = name
        self._cod_id = cod_id
        self._discord_id = discord_id

    # nickname from battle net
    @property
    def wz_name(self):
        return self._name_warzone

    @wz_name.setter
    def wz_name(self, value):
        self._name_warzone = value

    # id from battle net
    @property
    def id(self):
        return self._cod_id

    @id.setter
    def id(self, value):
        self.id = value

    # discord nickname
    @property
    def dis_id(self):
        return self._discord_id

    @dis_id.setter
    def dis_id(self, value):
        self._discord_id = value
