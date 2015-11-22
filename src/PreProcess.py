import numpy

Buses = [1]
BusStops = [("Cherry", 33.772342, -84.395699), ("North Ave", 33.770062, -84.391629), ("Smith Dorm", 33.771664, -84.391992), ("Techwood and Bobby Dodd", 33.774098, -84.391979), ("Techwood and Fourth", 33.775346, -84.391958),("Techwood and Fifth", 33.776797, -84.392062), ("Ferst and Fowler", 33.776942, -84.394135), ("Klaus", 33.777560, -84.395679), ("Ferst and Atlantic", 33.778277, -84.397974), ("GTPD", 33.778439, -84.400019), ("Burger Bowl", 33.778075, -84.401855), ("Fitten Hall",33.778242, -84.404198), ("McMillan and Eigth", 33.779630, -84.404136), ("Hemphill and Eigth", 33.779699, -84.402557), ("CRC", 33.775352, -84.402599), ("Student Center", 33.773387, -84.399217), ("The Hub",33.773000, -84.397493)]
Data = recfromcsv('../data/data.csv')
print('About to print data:\n')
Data