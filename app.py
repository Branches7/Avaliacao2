import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():  # put application's code here
    return render_template('login.html')

@app.route('/home', methods=['post','get'])
def home():
    bd = {'Dani': ['QQ', 'dan123'],
          'Thiago': ['QQ', 'th123']}
    user = request.form.get('user')
    senha = request.form.get('pass')
    validar = bd.get(user, ['erro', 'ex'])

    if validar[1] == senha:
        listaJogos = ['FIFA 21', 'CS GO', 'CALL OF DUTY MODERN WARFARE', 'RAINBOW SIX', 'GTA V', 'BATTLEFIELD V', 'VALORANT',
                      'LEAGUE OF LEGENDS', 'DOTA 2', 'ROCKET LEAGUE', 'FORZA 7', 'WATCH DOGS']
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
    querystring = {"q": 'logo do jogo ' + game, "count": "2"}

    headers = {
        'x-rapidapi-host': "bing-image-search1.p.rapidapi.com",
        'x-rapidapi-key': "ab9d73959fmsheb09c71ab215fe0p16199bjsndbe36a9cd935"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    value = data['value']
    imagem = value[0]['contentUrl'], value[1]['contentUrl']


@app.route('/biblioteca', methods=['post','get'])
def biblioteca():
    game = request.form.get('nome')
    imagem = request.form.get('img')
    #TODO adicao de jogos
    return render_template('biblioteca.html', game=game, imagem=imagem)


if __name__ == '__main__':
    app.run()
