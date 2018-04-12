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
    alt 	    In kilometers. 0 if not assigned
    IATA 	    3-letter IATA code. Null if not assigned/unknown.
    ICAO 	    4-letter ICAO code. Null if not assigned.
    """
    def __init__(self, name, city, country, lat, lng, alt=0, IATA=None, ICAO=None):
        self.name = name
        self.city = city
        self.country = country
        self.lat = lat
        self.lng = lng
        self.alt = alt
        self.IATA = IATA
        self.ICAO = ICAO

    def __repr__(self):        
        print("Name             {}".format(self.name))
        print("City             {}".format(self.city))
        print("Country          {}".format(self.country))
        print("Latitude         {} degrees North".format(self.lat))
        print("Longitude        {} degrees East".format(self.lng))
        print("Altitude         {}km".format(self.alt))
        print("IATA             {}".format(self.IATA))
        print("ICAO             {}".format(self.ICAO))
        return ""
    
    def cal_dist_from(self, loc):
        """
        Calculates the distance from this airport to the other airport in kilometers.
        """
        AVG_EARTH_RADIUS = 6.371E3
        
        lat1 = self.get_lat()
        lat2 = loc.get_lat()

        lng1 = self.get_lng()
        lng2 = loc.get_lng()
        if lat1 is None or lng1 is None or lat2 is None or lng2 is None:
            return inf

         # convert all latitudes/longitudes from decimal degrees to radians
        lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

        # calculate haversine
        lat = lat2 - lat1
        lng = lng2 - lng1
        d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
        h = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))
        return
