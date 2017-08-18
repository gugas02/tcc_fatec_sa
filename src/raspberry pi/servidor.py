import requests
from bs4 import BeautifulSoup



class Server(object):
    url = 'http://gugas02.pythonanywhere.com/apiUi'
    listona = ['user_id',
              'tempAgua',
              'pressaoTurbo',
              'pressaoColetor0',
              'tempAdm',
              'pontoIgn',
              'fluxoAr',
              'nvlCombustivel',
              'tempOleo',
              'relacaoEstequiometrica',
              'consumoInstantaneo',
              'dtc'
              ]
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
    config = False

    def login(self, user, senha):
        url = 'http://gugas02.pythonanywhere.com/loginapi'
        payload = {
            'user': user,
            'senha': senha
            }
        r = requests.post(url, data=payload)
        if r.status_code == requests.codes.ok:
            html_data = r.text
            soup = BeautifulSoup(html_data,"html.parser")
            status = soup.find(attrs={'name': 'status'}).get_text()
            if status == "success":
                user_id = soup.find(attrs={'name': 'expression'}).get('value')
                self.payload.update({'user_id': user_id})
                return user_id
            else:
                return True
        else:
            return False

    def setdata(self, data):
        for i in range(len(data)):
            if data[i] == 0:
                self.payload.pop(self.listona[i])

    def setvalue(self, data):
        aux = list(self.payload.keys())
        j=0
        for i in range(len(aux)):
            if i>=1:
                self.payload.update({aux[i]: str(data[j])})
                j+=1

    def send(self, mask, value):
        if not self.config:
            self.setdata(mask)
            self.config = True
        self.setvalue(value)
        r = requests.post(self.url, data=self.payload)
        if r.status_code == requests.codes.ok:
            return True
        else:
            return False
