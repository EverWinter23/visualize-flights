'''
12th april 2018 thursday
lorde - you're the only friend i need...
'''
from airport import Airport
from graph import DirGraph

class SymbolGraph:
    """
    sym_tab         dictionary with airport_name as key and index as value
    air_dat         array of airport objects, accessed using index
    key             inverted index, index->airport_name          
    """
    def __init__(self, airports_dat_file, routes_dat_file, delim):
        # construct index = dictionary> airport_name:index
        self.sym_tab_IATA = {}
        self.sym_tab_ICAO = {}
        self.air_dat = []
        
        with open(airports_dat_file) as file:
            line = file.readline()       # the header
            line = file.readline().split(delim)
            index = 0
            print("processing vertices...")
            while len(line) != 1:
                # unpack values
                air_id, name, city, country, iata, icao, lat, lng, alt, res =  line[0:10]

                name, city, country, iata, icao = name.strip("\""),  city.strip("\""), country.strip("\""), iata.strip("\""), icao.strip("\"")
                #print(air_id, "|", name, "|",city, "|", country, "|", iata, "|", icao, "|", lat,  "|",lng,  "|",alt,  "|",res)                
                
                try:
                    air_id, lat, lng, alt = int(air_id), float(lat), float(lng), float(alt)
                except Exception as ex:
                #if isinstance(lat, str):
                    lat, lng, alt = lng, alt, float(res)
                
                airport = Airport(name, country, lat, lng, alt, iata, icao)
                if iata is not '\\N' and iata not in self.sym_tab_IATA.keys() and icao is not '\\N' and icao not in self.sym_tab_ICAO.keys():
                    self.sym_tab_IATA[iata] = index
                    self.sym_tab_ICAO[icao] = index
                    self.air_dat.append(airport)
                    index += 1                
                elif iata is not '\\N' and iata not in self.sym_tab_IATA.keys():
                    self.sym_tab_IATA[iata] = index
                    self.air_dat.append(airport)
                    index += 1 
                elif icao is not '\\N' and icao not in self.sym_tab_ICAO.keys():
                    self.sym_tab_ICAO[icao] = index
                    self.air_dat.append(airport)
                    index += 1
                # don't add if both IATA and ICAO are None
                line = file.readline().split(',')

        # count of vertices in the symbol graph
        self.v = len(self.air_dat)    
        
        # construct inverted index for IATA code
        self.key_iata = {}
        for index in self.sym_tab_IATA.keys():
            self.key_iata[self.sym_tab_IATA[index]] = index
        print("iata",self.key_iata)

        # construct inverted index for ICAO code
        self.key_icao = {}
        for index in self.sym_tab_ICAO.keys():
            self.key_icao[self.sym_tab_ICAO[index]] = index

        graph = DirGraph(self.v)
        with open(routes_dat_file) as file:
            line = file.readline()      # the header
            line = file.readline().split(delim)
            print("processing edges...")
            while len(line) != 1:
                # unpack values
                src, src_id, dst, dst_id = line[2:6]
                #print(src, src_id, dst, dst_id)
                # both IATA
                src, dst = self.get_index(src), self.get_index(dst)
                if src != -1 and dst != -1:
                    graph.add_route(src, dst)
                line = file.readline().split(',')
        print(self.get_code(6477))
        #print(graph)
        print("preprocessing done...")
    
    def get_index(self, air_code):
        if air_code in self.sym_tab_IATA.keys():
            return self.sym_tab_IATA[air_code]
        elif air_code in self.sym_tab_ICAO.keys():
            return self.sym_tab_ICAO[air_code]
        else:
            return -1
    
    def get_code(self, index):
        # try IATA if exists
        if index in self.key_iata.keys():
            return self.key_iata[index]
        else:
            return self.key_icao[index]
            
            

def test():
    sg = SymbolGraph("../data/airports.dat", "../data/routes.dat", ",")

if __name__ == "__main__":
    test()
        
        

                       