

class PropertyWrapper:
    def __init__(self, property_data):
        self.property_data = property_data
        self.address = self.property_data['address']
        self.city = self.property_data['address']['city']
        self.address_longitude = self.property_data['address']['geoLocation']['location']['lon']
        self.address_latitude = self.property_data['address']['geoLocation']['location']['lat']
        self.usable_areas = "teste"
