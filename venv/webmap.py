import folium # generates maps for python
print(dir(folium)) # prints directory of folium lib
# create a map object
# input latitude & longitude
# zoom_start is the magnification seeting of the map, higher num zooms more, lower num zooms out
map = folium.Map(location=[43.886478, -79.010799], zoom_start= 7)
print(map)
# need html file out of this object - to create a map

print(dir(folium.Map))
print(map.save('test.html')) # rt click on html file and open in browser

#change zoom to 15 and add tiles = 'Stamen Terrain' and recreate html file
map2 = folium.Map(location=[43.886478, -79.010799], zoom_start= 15, tiles= 'Stamen Terrain')
print(map2)
print(map2.save('test2.html'))

#create 3rd map file
map3= folium.Map(location=[43.886478, -79.010799], zoom_start= 15, tiles= 'Stamen Terrain')
# Add some markers to our map
folium.Marker(location=[43.886478, -79.010799], popup= 'I am so lost', icon= folium.Icon(icon='cloud')).add_to(map3)
folium.Marker(location=[43.993521, -79.124561], popup= 'But I can see you', icon= folium.Icon(color='green')).add_to(map3)
print(map3.save('test3.html'))

import pandas as pd # to read .csv file
# keep map3 objects
map4= folium.Map(location=[43.886478, -79.010799], zoom_start= 15, tiles= 'Stamen Terrain')
# read csv file into python and store it in a variable
df= pd.read_csv('volcano.txt') # df= data frame

# create for loop to use file data to create markers
# we have 2 iterators in this loop, put them in zip function
# read as iterator, then where is df to "grab" that iterators value
for lat,lon,name in zip(df['LAT'], df['LON'], df['NAME']):
    folium.Marker(location=[lat,lon], popup= name, icon= folium.Icon(icon='cloud')).add_to(map4)
print(map4.save('test4.html'))
#if html file doesn't load in browser, go to txt file and in line 30 remove the apostrophe in the name: Hell's Half Acre

# we can integrate some if statements to make the cloud color change based on elevation
# we need to assign elev to our for loop as an iterator
for lat,lon,name,elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    # we want to say: if elev is at x elevation make color y
    # our expression (color) is inside a method, so we can use an inline statement
    folium.Marker(location=[lat,lon], popup= name, icon= folium.Icon(color='green' if elev in range (0,1000) else 'orange' if elev in range (1001,1999) else 'blue' if elev in range (2000,2999) else 'red', icon= 'cloud')).add_to(map4)
print(map4.save('test5.html'))

# Now lets organize the code
map4= folium.Map(location=[43.886478, -79.010799], zoom_start= 15, tiles= 'Stamen Terrain')
df= pd.read_csv('volcano.txt')

def color(elev):
    if elev in range (0,1000):
        col= 'green'
    elif elev in range (1001,1999):
        col= 'orange'
    elif elev in range (2000,2999):
        col= 'blue'
    else:
        col= 'red'
    return col

for lat,lon,name,elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color= color(elev), icon= 'cloud')).add_to(map4)
print(map4.save('test6.html'))

# Now we want to have the map centred around the data
# take the average
latmean= df['LAT'].mean()
lonmean= df['LON'].mean()

map4= folium.Map(location=[latmean, lonmean], zoom_start= 6, tiles= 'Stamen Terrain')

def color(elev):
    if elev in range (0,1000):
        col= 'green'
    elif elev in range (1001,1999):
        col= 'orange'
    elif elev in range (2000,2999):
        col= 'blue'
    else:
        col= 'red'
    return col

for lat,lon,name,elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color= color(elev), icon_color= 'yellow', icon= 'cloud')).add_to(map4)
print(map4.save('test7.html'))