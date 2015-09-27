#!/usr/bin/python

from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import urllib2
import sys
import datetime
import time

def string_to_datetime(string_delta):
    if string_delta.find('ago') > 1:
        value, unit, _ = string_delta.split()
        diff =  time.time()/datetime.timedelta(**{unit: float(value)}).total_seconds()
        diff-= int(diff)
        print diff*time.time()

        print time.time()-diff*time.time()
        sys.exit(1)
        timestamp =  time.time()-datetime.timedelta(**{unit: float(value)}).total_seconds()
        output = datetime.datetime.fromtimestamp(timestamp)

    else:
        output = datetime.datetime.strptime(string_delta, '%b %d')

    return output


response = urllib2.urlopen('https://medium.com/@zanaca/latest').read()
soup = BeautifulSoup(response, 'html.parser')


mediumPostsDate = [div.find('a') for div in soup.findAll('span',{'class':'postMetaInline--supplemental'})]
mediumPosts = soup.findAll('div',{'class':'block-streamText'})

i=0
for mediumPost in mediumPosts:
    title = mediumPost.find('h3').text
    link = mediumPost.find('a',href=True)
    link = link['href'].split('?')[0]
    postDate = mediumPostsDate[i].text.replace('hrs','hours')
    date = string_to_datetime(postDate)
    date = date.strftime('%Y-%m-%dT%H:%M:%S')

    postBody = mediumPost.find('div',{'class':'section-inner layoutSingleColumn'})
    [x.extract() for x in postBody.findAll('h3')]

    postBody = postBody.decode_contents(formatter="html")

    body = """<h2>%(title)s</h2>
%(body)s

<time>%(time)s</time> [<a href="%(link)s" rel="no-follow" class="canonical-link">Medium</a>]""" % {'title' : title, 'body' : postBody, 'time': time, 'link' : link}

    open("../posts/%s-%s.html" % (date, link.split('/')[-1]) , 'w').write(body)
    i+= 1


posts = [ f for f in listdir('../posts') if isfile(join('../posts',f)) ]
container = ''
for postFile in posts:
    if postFile == 'index.html':
        continue

    post = open('../posts/%s' % postFile,'r').read()
    title = post.split('</h2>')[0][4:]
    time = post.split('time>')[1][:-2]


    container+= """
    <div class="post-summary">
        <div class="row-fluid">
                <a href='#%s'><h3>%s</h3><time>%s</time></a>
        </div>
    </div>
""" % (postFile,title,time)

html = open("../index.html",'r').read()
html = html.replace('<!-- containerBody -->', '<div class="posts">%s</div>' % container)
open('../posts/index.html','w').write(html)
