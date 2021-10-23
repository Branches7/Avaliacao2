import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():  # put application's code here
    return render_template('login.html')


@app.route('/home', methods=['post'])
def home():
    bd = {'Dani': ['QQ', 'dan123'],
          'Thiago': ['QQ', 'th123']}
    user = request.form.get('user')
    senha = request.form.get('pass')
    validar = bd.get(user, ['erro', 'ex'])

    if validar[1] == senha:
        listaJogos = ['FIFA 22', 'CS GO', 'CALL OF DUTY WARZONE', 'RAINBOW SIX', 'GTA V', 'BATTLEFIELD V', 'VALORANT', 'LEAGUE OF LEGENDS', 'DOTA 2', 'ROCKET LEAGUE']
        jogos = {}
        cont = 1
        for jogo in listaJogos:
            img(jogo)
            jogos[cont] = [jogo, imagem[0], imagem[1]]
            cont += 1

        return render_template('home.html', dados=[user, validar[0]], jogos=jogos)
    else:
        return render_template('login.html', erro=True)

def img(game):
    url = "https://bing-image-search1.p.rapidapi.com/images/search"
    global imagem
    querystring = {"q": 'capa pequena jogo pc ' + game, "count": "2"}

    headers = {
        'x-rapidapi-host': "bing-image-search1.p.rapidapi.com",
        'x-rapidapi-key': "00e1cc2352mshd18db3cd042accdp135e2ejsnf272b01b1e3e"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    value = data['value']
    imagem = value[0]['contentUrl'], value[1]['contentUrl']


@app.route('/biblioteca')
def biblioteca():
    return render_template('biblioteca.html')


if __name__ == '__main__':
    app.run()
