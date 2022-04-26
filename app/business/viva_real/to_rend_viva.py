from app.data_source.real_state_wrapper import PropertyWrapper


class IneligibleToRend:
    def __init__(self, property_data: PropertyWrapper):
        self.property_data = property_data

    def if_usable_areas_is_less_than_3500(self):
        usable_areas = self.property_data.usable_areas

        if usable_areas <= 3500:
            return "O Imóvel possui usable areas menos que 3500, portanto não é elegível em nenhum portal"
        else:
            return False