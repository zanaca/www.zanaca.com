#http://zanaca.com

### Enviar um post

Para escrever um post, basta criar um post no Medium.com, o cron <code>fetchMediumPosts.py</code> vai cuidar de trazer ele para o site

### Deployment

* Praparar um crontab para rodar o fetchMediumPosts.py e fetchBackgroundImg.py
* Servir a raiz com o servidor web que preferir

Setup with just the `gh-pages` branch so anything you do in this branch will be displayed on the site on push. (It can take up to 10 minutes to be reflected)

### Desenvolvimento

Para começar a servir:
`python -m SimpleHTTPServer 8080 &`

Para pegar os posts:
`./_grabber/fetchMediumPosts.py`

Para alterar a imagem de fundo:
`./_grabber/fetchBackgroundImg.py`
