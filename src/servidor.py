import requests
from bs4 import BeautifulSoup


class Server(object):
    url = 'http://gugas02.pythonanywhere.com/apiUi'

    payload = {
        'user_id': '0',
        "tempAgua": '0',
        "pressaoTurbo": '0',
        "pressaoColetor"'0': '0',
        "tempAdm": '0',
        "pontoIgn": '0',
        "fluxoAr": '0',
        "nvlCombustivel": '0',
        "tempOleo": '0',
        "relacaoEstequiometrica": '0',
        "consumoInstantaneo": '0',
        "dtc": '0'
         }

    @staticmethod
    def login(user, senha):
        url = 'http://gugas02.pythonanywhere.com/loginapi'
        payload = {
            'user': user,
            'senha': senha
            }
        r = requests.post(url, data=payload)
        if r.status_code == requests.codes.ok:
            html_data = r.text
            soup = BeautifulSoup.BeautifulSoup(html_data)
            status = soup.find(attrs={'name': 'status'}).get('value')
            if status == "success":
                user_id = soup.find(attrs={'name': 'expression'}).get('value')
                return user_id
            else:
                return True
        else:
            return False

    def setdata(self, data):
        for i in range(len(data)):
            if data[i] == 0:
                self.payload.pop(i)

    def setvalue(self, data):
        aux = list(self.payload.keys())
        for i in range(len(aux)):
            self.payload.update({aux[1]: str(data[i])})

    def send(self, mask, value):
        self.setdata(mask)
        self.setvalue(value)
        r = requests.post(self.url, data=self.payload)
        if r.status_code == requests.codes.ok:
            return True
        else:
            return False
