'''
12th april 2018 thursday
lorde - you're the only friend i need...
'''
from airport import Airport
class SymbolGraph:
    """
    sym_tab         dictionary with airport_name as key and index as value
    air_dat         array of airport objects, accessed using index
    key             inverted index, index->airport_name          
    """
    def __init__(fname, delim):
        # construct index = dictionary> airport_name:index
        sym_tab = {}
        air_dat = []
        key = []
        with open(fname) as file:
            line = file.readline()       # the header
            line = file.readline()
            index = 0
            while line != None:
                # unpack values
                air_id, name, city, country, iata, icao, lat, lng, alt =  line[0:9]
                airport = Airport(name, country, lat, lng, alt, iata, icao)
                if name not in sym_tab.keys():
                    sym_tab[name] = index
                    air_dat.append(airport)
                    index += 1
            
        # construct inverted index
        for name in sym_tab.keys():
            key[sym_tab[name]] = name

        graph = Graph(len(sym_tab))
        with open(fname as )

        
        

                       