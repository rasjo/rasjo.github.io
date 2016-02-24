'''
joyce rasing 
gus 8066 / final project
'''

import csv
import collections
from itertools import izip
import pylab
import pandas as pd
import folium
import matplotlib.pyplot as plt

ds = r'C:\data'

#========================
#counting sulu occurances of terrorism by asg
from pandas import read_csv

occurrences = collections.Counter()
with open (r'C:\data\sulu.csv', 'r') as z:
    reader = csv.reader(z)
    for row in reader: 
        occurrences[row[29]] +=1
print (occurrences.most_common())

with open (r'C:\data\sulu2.csv', 'w') as y:
    fieldnames = ['attacktype1_txt', 'Armed Assault', 'Assassination', 
    'Bombing/Explosion', 'Hostage Taking (Kidnapping)', 
    'Facility/Infrastructure Attack']
    writer = csv.DictWriter(y, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(occurrences)

a = izip(*csv.reader(open("c:\data\sulu2.csv", "rb")))
csv.writer(open("c:\data\sulu3.csv", "wb")).writerows(a)

appendme = read_csv('c:\data\sulu3.csv')
appendme.columns = ['Type', 'Count']
appendme.to_csv('c:\data\sulu3-1.csv')

#========================
#plotting sulu3-1.csv values mpl

#sulu31 = r'c:\data\sulu3-1.csv'

def graph():
    
    attacktype = [0, 1, 2, 3]
    counts = ['24', '1', '34', '44', '2']
    
    plt.figure(figsize=(20, 15))
    pylab.title("Terrorist Campaigns in Sulu, Philippines")
    pylab.xlabel("Attack Type")
    pylab.ylabel("Count")
    
    LABELS = ['Armed Assault', 'Assassination', \
    'Bombing/Explosion', 'Kidnapping', \
    'Infrastructure']
    
    pylab.xticks(attacktype, LABELS, fontsize=10)
    pylab.plot(counts, marker='o', color='black', markersize=10)
    
    pylab.show()

graph()
    
#========================
#visulization of sulu attacks using folium
    
sulu = (6.05519, 121.001323) #this is sulu town hall/city hall

tileset = r'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png'
map = folium.Map(location=sulu, tiles=tileset, \
        attr='Map tiles by CartoDB, under CC BY 3.0. Data by OpenStreetMap, under ODbL.' ,\
        zoom_start=12)
                 
terror = pd.read_csv('c:\data\sulu.csv')
max = 100 #caps display at 100 events

#add a marker for terrorist campaign
for each in terror[0:max].iterrows():  
    map.polygon_marker(location = [each[1]['latitude'],each[1]['longitude']], \
    popup=each[1]['attacktype1_txt'], fill_color='#94bad6', num_sides=4, radius=5)
    
    map.circle_marker(location=[6.054391, 121.002195], radius=1609.34, \
        popup='Jolo Town Hall', line_color='#000', fill_color='none', \
        fill_opacity=0.6)
    
map.create_map(path='c:\data\sulu.html')