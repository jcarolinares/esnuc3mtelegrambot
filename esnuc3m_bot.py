from pyquery import PyQuery as pq
from lxml import etree
import urllib


#Acceso al html
#d = pq("<html></html>")
#d = pq(etree.fromstring("<html></html>"))
d = pq(url='http://www.esnuc3m.org/events')
#d.make_links_absolute(base_url="http://www.esnuc3m.org")
#d = pq(url='http://google.com/', opener=lambda url, **kw: urllib.urlopen(url).read())
#d = pq(filename='table.html')

#print d

#href_d=str(d)

#href_d=href_d.find("/events")
#print href_d

#<span class="tabla_titulo_fecha">2016-01-24 09:00:00.0</span>


#Selection of events
date_data=d('div[class="field-item even"]')
date_data=date_data.append("**")
date_data=date_data.text()
date_data=date_data.split("**")

for x in date_data:
	print (x)

#Selection of links events
event_link=d('h2') #We take the headers where are the links
#event_link=event_link.append("**")
#event_link=event_link
#event_link=event_link.find("href")
#print (event_link('a').find('href'))
#print event_link
event_link=str(event_link)
event_link=event_link.split("**")

del event_link[-1]#We erase the last header

#Lo siguiente es sacar el href del primer link, reconstruirlo a absoluto y continuar con el resto
#event_link[0]=event_link[0]

for x in event_link:
	print "\n\n"
	print x

#for x in event_link:
#	print (x)
#<a href="/events/

'''
<div class="node node-event node-promoted view-mode-list clearfix">

	<!-- Needed to activate contextual links -->

	<div class="group-image">
		<div class="field field-name-field-image field-type-image field-label-hidden"><div class="field-items"><div class="field-item even"><a href="/events/viaje-barcelona"><img src="http://www.esnuc3m.org/sites/default/files/styles/list/public/events/images/Imagen%20Barcelona.jpg?itok=1Ohdsgc6" alt=""></a></div></div></div>	</div>

	<div class="group-content">
		<div class="field field-name-field-date field-type-datetime field-label-hidden"><div class="field-items"><div class="field-item even"><div class="date-display-range"><span class="date-display-start">05/02/2016</span> to <span class="date-display-end">07/02/2016</span></div></div></div></div><div class="field field-name-title field-type-ds field-label-hidden"><div class="field-items"><div class="field-item even"><h2><a href="/events/viaje-barcelona">Viaje a Barcelona</a></h2></div></div></div>	</div>

</div>
#<a href="/events/welcome-days">Welcome Days </a>
'''
'''
#Selection of station name
station_name=d('td[class="primertd"]')
station_name=station_name.append("**")
station_name=station_name.text()
station_name=station_name.split("**")
#print(station_name)

del station_name[0] #Delete the first empty element of  the list

#for x in station_name:
#	print(x)


#Selection of all the N02 data
no2rawdata=d('td[headers="NO2"]')
no2data=no2rawdata.text()
no2data=no2data.replace("-","0")#Replaces no data with a 0
no2data=no2data.split(" ")
no2data = map(int, no2data) #int conversion



#Info output
print("\n\nContaminacion de NO2 en Madrid-Fecha: "+date_data)
for x in no2data:
	if x<20:
		print(str(x)+"-ALERTA POR POLUCION")
	else:
		print(x)


#Info output
print("\n\nContaminacion de NO2 en Madrid-Fecha: "+date_data)
for x in range(len(no2data)):
	if no2data[x]>400:
		print("\n")
		print(station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico"+"-POSIBLE ALERTA POR POLUCION")
	elif no2data[x]>250:
		print("\n")
		print(station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico"+"-POSIBLE AVISO POR POLUCION")
	elif no2data[x]>200:
		print("\n")
		print(station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico"+"-POSIBLE PREAVISO POR POLUCION")
	else:
		print("\n")
		print(station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico")
'''
