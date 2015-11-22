import numpy
import math

from math import radians, cos, sin, asin, sqrt

def distance(loc1, loc2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [loc1[0], loc1[1], loc2[0], loc2[1]])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    meters = 1000 * 6367 * c
    return meters

Range=10 #distance in meter


Buses = [1]
BusStops = [("Cherry", 33.772342, -84.395699), ("North Ave", 33.770062, -84.391629), ("Smith Dorm", 33.771664, -84.391992), ("Techwood and Bobby Dodd", 33.774098, -84.391979), ("Techwood and Fourth", 33.775346, -84.391958),("Techwood and Fifth", 33.776797, -84.392062), ("Ferst and Fowler", 33.776942, -84.394135), ("Klaus", 33.777560, -84.395679), ("Ferst and Atlantic", 33.778277, -84.397974), ("GTPD", 33.778439, -84.400019), ("Burger Bowl", 33.778075, -84.401855), ("Fitten Hall",33.778242, -84.404198), ("McMillan and Eigth", 33.779630, -84.404136), ("Hemphill and Eigth", 33.779699, -84.402557), ("CRC", 33.775352, -84.402599), ("Student Center", 33.773387, -84.399217), ("The Hub",33.773000, -84.397493)]
Data = numpy.recfromcsv('../data/data.csv')
print('About to print data:\n')

#times keeps track of the last time we went by a bus stop.
#times=[["Cherry",0], ["North Ave", 0], ["Smith Dorm", 0], ["Techwood and Bobby Dodd", 0], ["Techwood and Fourth", 0], ["Techwood and Fifth", 0], ["Ferst and Fowler", 0], ["Klaus", 0], ["Ferst and Atlantic",0], ["GTPD", 0], ["Burger Bowl", 0], ["Fitten Hall", 0], ["McMillan and Eigth", 0], ["Hemphill and Eigth", 0], ["CRC",0], ["Student Center",0], ["The Hub",0]]
for row in Data:
	busPosition=(row[0], row[1])
	time=row[2]
	for stop in BusStops:
		stopPosition=(stop[1],stop[2])
		#distance((lat,long),(buslat,buslong))
		if distance(busPosition,stopPosition) < Range:
			row[4]=stop[0]


print (Data[0])
numpy.savetxt("updatedData.csv",Data,fmt='%0.8f,%0.8f,%4d,%s,%s')

