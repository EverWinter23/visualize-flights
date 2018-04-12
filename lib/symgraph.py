'''
12th april 2018 thursday
lorde - you're the only friend i need...
'''
from airport import Airport
class SymbolGraph:
    def __init__(fname, delim):
        # construct index = dictionary> airport:index
        with open(fname) as file:
            line = file.readline()       # the header
            line = file.readline()
            while line != None:
                # unpack values
                air_id, name, city, country, iata, icao, lat, lng, alt =  line[0:9]
                airport = Airport(air_id, name, country, lat, lng, alt, iata, icao)
                



