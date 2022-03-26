from app.business.real_state.rules import PropertyForAllPortalRules
from app.data_source.real_state_wrapper import PropertyWrapper
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def get_eligible_real_state():
    try:
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        url = "http://grupozap-code-challenge.s3-website-us-east-1.amazonaws.com/sources/source-2.json"
        real_state_response = session.get(url).json()

        eligible_properties = [property_is_eligible(PropertyWrapper(immobile)).property_data for immobile in
                               real_state_response if property_is_eligible(PropertyWrapper(immobile))]
        return eligible_properties
    except:
        raise "Erro ao pegar e tratar os dados"


def property_is_eligible(immobile):
    check_rules = PropertyForAllPortalRules(immobile)
    if check_rules.ineligible.if_lat_long_equals_zero():
        return False
    else:
        return immobile
