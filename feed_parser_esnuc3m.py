#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

#for post in d.entries:
#    print post.title + ": " + post.link + "\n"
#    print post.description

print d.entries[0].title
print d.entries[0].link
#print d.entries[0].description


dparser = pq(d.entries[0].description)



#Selection of data_events
date_data=dparser('div[class="field-item even"]')
date_data=date_data.append("**")
date_data=date_data.text()
date_data=date_data.split("**")

print date_data[0]

#for x in date_data:
#	print x

#<div class="field-item even">
