from pyquery import PyQuery as pq
from lxml import etree
import urllib
import re

import feedparser

#combinando feedparser para obtener el html de cada entrada, junto con pyquery para filtrar la informacion del html se puede sacar cada dato importante

d = feedparser.parse('http://www.esnuc3m.org/rss.xml')

'''
print d['feed']['title']
print d['feed']['link']
print d['feed']['description']#no hay descripcion en el rss
print d.keys()
print d.updated
print d.updated_parsed #informacion separada
print d.headers
print d.href
print len(d.entries)
print d.entries[0].title #titulo de la primera entrada
print d.entries[0].link #link de la primera entrada
print d.entries[0].published #fecha de publicacion del ultimo articulo
'''

for post in d.entries:
    print post.title + ": " + post.link + "\n"
