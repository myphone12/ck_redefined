import requests,json

class Net:

    def __init__(self):
        self.server = 'http://api.smb-studio.cn'
    
    def shop(self):
        a = requests.get(self.server + '/shop.json')
        a = json.loads(a.text())