from app.data_source.real_state_wrapper import PropertyWrapper


class Ineligible:
    def __init__(self, property_data: PropertyWrapper):
        self.property_data = property_data

    def if_lat_long_equals_zero(self):
        longitude = self.property_data.address_longitude
        latitude = self.property_data.address_latitude

        if longitude == 0 and latitude == 0:
            return "O Imóvel possui lat e lon iguais a zero, portanto não é elegível em nenhum portal"
        else:
            return False
