import requests
from Statistic.Stats import Stats


class CodTracker:
    API = 'https://api.tracker.gg/api/v2/warzone/standard/profile/battlenet/{name}%23{cod}'

    # check account for exist
    def check_acc(self, user):
        link = self.API.format(name=user.wz_name, cod=user.id)  # create link
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en',
            'Referer': link + '/overview',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.60 Mobile Safari/537.36'
        }
        response = requests.get(link, headers=headers)
        if response.status_code == 404:  # if account not exists
            return False
        return True

    def get_stats(self, user):  # get stats from codTracker
        link = self.API.format(name=user.wz_name, cod=user.id)  # create link
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en',
            'Referer': link + '/overview',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.60 Mobile Safari/537.36'
        }
        response = requests.get(link, headers=headers)
        json_object = response.json()
        stats = Stats(json_object)
        return stats


