#http://zanaca.com

### Enviar um post

Para escrever um post, basta criar um post no Medium.com, o cron <code>fetchMediumPosts.py</code> vai cuidar de trazer ele para o site

### Deployment

* Praparar um crontab para rodar o fetchMediumPosts.py e fetchBackgroundImg.py
* Rodar `./app.py &`

### Desenvolvimento

Para começar a servir:
`./app.py`

Para pegar os posts:
`./_grabber/fetchMediumPosts.py`

Para alterar a imagem de fundo:
`./_grabber/fetchBackgroundImg.py`
