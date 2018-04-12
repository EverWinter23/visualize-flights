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
        sym_tab_IATA = {}
        sym_tab_ICAO = {}
        air_dat = []

        with open(fname) as file:
            line = file.readline()       # the header
            line = file.readline()
            index = 0
            while line != None:
                # unpack values
                air_id, name, city, country, iata, icao, lat, lng, alt =  line[0:9]
                name, city, country, iata, icao = name.strip("\""),  city.strip("\""), country.strip("\""), iata.strip("\""), icao.strip("\"")
                air_id, lat, lng, alt = int(air_id), int(lat), int(lng), int(alt)

                airport = Airport(name, country, lat, lng, alt, iata, icao)
                if iata is not '\\N' and iata not in sym_tab_IATA.keys() and icao is not '\\N' and icao not in sym_tab_ICAO.keys():
                    sym_tab_IATA[iata] = index
                    sym_tab_ICAO[icao] = index
                    air_dat.append(airport)
                    index += 1                
                elif if iata is not '\\N' and iata not in sym_tab_IATA.keys():
                    sym_tab_IATA[iata] = index
                    air_dat.append(airport)
                    index += 1 
                else if icao is not '\\N' and icao not in sym_tab_ICAO.keys():
                    sym_tab_ICAO[icao] = index
                    air_dat.append(airport)
                    index += 1
                # don't add if both IATA and ICAO are None
            
        # construct inverted index for IATA code
        key_iata = [0 for index in range(len(sym_tab_IATA))]
        for iata in sym_tab_IATA.keys():
            key_iata[sym_tab[iata]] = iata

        # construct inverted index for ICAO code
        key_icao = [0 for index in range(len(sym_tab_ICAO))]
        for icao in sym_tab_ICAO.keys()
            key_icao[sym_tab_ICAO[icao]] = icao

        graph = Graph(len(sym_tab))
        with open(fname as )

        
        

                       