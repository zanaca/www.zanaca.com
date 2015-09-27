#!/usr/bin/python

import urllib2
import sys

def processHashtag(hash):
    url = 'http://iconosquare.com/tag/%s' % hash
    response = urllib2.urlopen(url)

    body = response.read()
    if body.split('<img src="https://scontent.cdni') is False or body.split('<img src="https://scontent.cdni')[1].split('"') is False:
        return False

    img = body.split('<img src="https://scontent.cdni')[1].split('"')[0]
    user = body.split('<img src="https://scontent.cdni')[0].split('title="@')[-1].split('"')[1].split('<')[0][1:]
    img = 'https://scontent.cdni%s' % img.replace('150x150','640x640')

    css = """HTML:before {
        background: url('%s')  no-repeat;
        width: 100%%;
        height: 100%%;
        background-size: 100%%;
        -webkit-filter: blur(26px);
        -moz-filter: blur(26px);
        -o-filter: blur(26px);
        -ms-filter: blur(26px);
        filter: blur(26px);
        position:fixed;
        z-index: -1;
        content:"";
        background-color: #efefef;
    }

    BODY{background-color: transparent;}
    """ % img
    open('../css/background.css', 'w').write(css)

    instagram='<a href="https://instagram.com/%s" target=_blank><img src="%s" width="150px" height="150px"><br>@%s</a>' % (user, img, user)
    open('../__instagramPhoto.html','w').write(instagram)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        hash = sys.argv[1]
    else:
        hash = 'landscape'

    processHashtag(hash)
