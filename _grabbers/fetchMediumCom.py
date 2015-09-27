#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
import urllib2
import sys
import datetime
import time
import json
import codecs

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


req = urllib2.Request('https://medium.com/@zanaca/latest', json.dumps({'count':10}), {'accept': 'application/json', 'x-xsrf-token': 2})
response = urllib2.urlopen(req).read().split('</x>')[1]
mediumPosts =  json.loads(response)['payload']['posts']


for mediumPost in mediumPosts:
    title = mediumPost['title']
    link = 'https://medium.com/@zanaca/%s' % mediumPost['uniqueSlug']

    postBody = ''
    for p in mediumPost['previewContent']['bodyModel']['paragraphs']:
        if p['type'] is 1:
            postBody+= "<p>%s</p>\n" % p['text']

        elif p['type'] is 7:
            postBody+= "<p><pre>%s</pre></p>\n" % p['text']

    body = """<h3>%(title)s</h3>
%(body)s

<span class="footnote">[ <time>%(time)s</time> - <a href="%(link)s" rel="no-follow">Medium</a> ]</span>""" % {'title' : title, 'body' : postBody, 'time': mediumPost['virtuals']['latestPublishedAtAbbreviated'], 'link' : link}
    codecs.open("../posts/%s-%s.html" % (mediumPost['createdAt'], mediumPost['uniqueSlug']) , 'w', 'utf-8').write(body)


posts = [ f for f in listdir('../posts') if isfile(join('../posts',f)) ]
posts.reverse()
container = ''
for postFile in posts:
    if postFile == 'index.html':
        continue

    post = open('../posts/%s' % postFile,'r').read()
    title = post.split('</h3>')[0][4:]
    time = post.split('time>')[1][:-2]


    container+= """
    <div class="post-summary">
        <div class="row-fluid">
                <a href='#%s'><h3>%s</h3></a><time  class="footnote">%s</time>
        </div>
    </div>
""" % (postFile,title,time)

html = open("../index.html",'r').read()
html = html.replace('<!-- containerBody -->', '<div class="posts">%s</div>' % container.encode('utf-8'))
codecs.open('../posts/index.html','w').write(html)
