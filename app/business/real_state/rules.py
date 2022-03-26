from app.business.real_state.ineligible_property import Ineligible
from app.data_source.real_state_wrapper import PropertyWrapper


class PropertyForAllPortalRules:
    def __init__(self, property_data: PropertyWrapper):
        self.property_data = property_data
        self.ineligible = Ineligible(self.property_data)

