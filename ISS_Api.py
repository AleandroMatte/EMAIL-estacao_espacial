import datetime
import smtplib
import time

import requests

#
minha_lat = -17.863520
minha_long = -41.507118
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

latitude = response.json()["iss_position"]['latitude']
longitude = response.json()['iss_position']['longitude']
iss_position = (longitude, latitude)

parametros = {
    'lat': minha_lat,
    'lng': minha_long,
    'formatted': 0
}


def is_night():
    resposta = requests.get(url='https://api.sunrise-sunset.org/json', params=parametros)
    resposta.raise_for_status()
    dados = resposta.json()
    sunrise = dados['results']['sunrise']
    sundown = dados['results']['sunset']
    sunrise = sunrise.split('T')
    sunrise = sunrise[1].split(':')[0]
    sundown = sundown.split('T')
    sundown = sundown[1].split(':')[0]
    print(sunrise + '\n' + sundown)

    horas = datetime.datetime.now().hour
    if int(sundown) < horas < int(sunrise):
        return True

    # If the ISS is close to my current position
from tkinter import *
email=''
senha=''
def pegar_senha_e_email():
    global email,senha
    email=entrada_email.get()
    senha=entrada_senha.get()
window=Tk()
window.title('Inserir email')
window.config(pady=5)
entrada_email=Entry(width=30)
entrada_email.insert(0,"Digite seu email aqui")
entrada_email.focus()
entrada_email.grid(column=2,row=1,pady=5,padx=20)
entrada_senha=Entry(width=30)
entrada_senha.grid(column=2,row=2)
entrada_senha.insert(0,'Digite sua senha aqui')
botao=Button(text='Inserir',command=pegar_senha_e_email)
botao.grid(column=1,row=1)
window.mainloop()
while True:
    time.sleep(60)
    if minha_lat - 5 < int(latitude) < minha_lat + 5 and minha_long - 5 < int(latitude) < minha_long + 5 and is_night():
        connection = smtplib.SMTP("insira o '@' e tudo o que vem DEPOIS dele no seu endereço de email aqui")
        connection.starttls()
        connection.login(user=email, password=senha)
        # Then send me an email to tell me to look up.
        connection.sendmail(from_addr=email, to_addrs="email que receebra a localização",
                            msg='Subject:look up to the sky \n\n the ISS is above you')
