'''
12th april 2018 thursday
set fire to the rain...
'''

class Airport:
    """
    id	        Unique OpenFlights identifier for this airport
    name 	    Name of airport. May or may not contain the City name.
    city 	    Main city served by airport. May be spelled differently from Name.
    country 	Country or territory where airport is located. See countries.dat to cross-reference to ISO 3166-1 codes.
    lat  	    Decimal degrees, usually to six significant digits. Negative is South, positive is North.
    lng      	Decimal degrees, usually to six significant digits. Negative is West, positive is East.
    alt 	    In kilometer. 0 if not assigned
    IATA 	    3-letter IATA code. Null if not assigned/unknown.
    ICAO 	    4-letter ICAO code. Null if not assigned.
    """
    def __init__(self, id, name, city, country, lat, lng, alt=0, IATA=None, ICAO=None):
        self.id = id
        self.name = name
        self.city = city
        self.country = country
        self.lat = lat
        self.lng = lng
        self.alt = alt
        self.IATA = IATA
        self.ICAO = ICAO

    def __repr__(self):        
        print("Airport ID       {}".format(self.id))
        print("Name             {}".format(self.name))
        print("City             {}".format(self.city))
        print("Country          {}".format(self.country))
        print("Latitude         {} degrees North".format(self.lat))
        print("Longitude        {} degrees East".format(self.lng))
        print("Altitude         {}km".format(self.alt))
        print("IATA             {}".format(self.IATA))
        print("ICAO             {}".format(self.ICAO))
        return ""
