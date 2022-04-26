from app.business.real_state.rules import PropertyForAllPortalRules
from app.business.viva_real.to_rend_viva import IneligibleToRend
from app.data_source.real_state_wrapper import PropertyWrapper
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def get_all_properties():
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    url = "http://grupozap-code-challenge.s3-website-us-east-1.amazonaws.com/sources/source-2.json"
    real_state_response = session.get(url).json()
    return real_state_response

def get_eligible_real_state():
    try:
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        url = "http://grupozap-code-challenge.s3-website-us-east-1.amazonaws.com/sources/source-2.json"
        real_state_response = session.get(url).json()
        properties_zap_to_sale = []
        properties_zap_to_rent = []
        properties_viva_real_to_sale = []
        properties_viva_real_to_rent = []
        eligible_properties = [property_is_eligible(PropertyWrapper(immobile)).property_data for immobile in
                               real_state_response if property_is_eligible(PropertyWrapper(immobile))]
        properties = {"viva_real": {"to_rend": properties_viva_real_to_rent, "to_sale": properties_viva_real_to_sale},
                      "zap": {"to_rend": properties_zap_to_rent, "to_sale": properties_zap_to_sale}}
        return properties
    except:
        raise "Erro ao pegar e tratar os dados"


def eligible_to_rent_viva_real(immobile):
    check_rules = IneligibleToRend(immobile)
    if check_rules.if_usable_areas_is_less_than_3500():
        return False

    else:
        return immobile


def eligible_to_sale_viva_real():
    pass


def eligible_to_rent_zap():
    pass


def eligible_to_sale_zap():
    pass


def property_is_eligible(immobile):
    check_rules = PropertyForAllPortalRules(immobile)
    if check_rules.ineligible.if_lat_long_equals_zero():
        return False
    else:
        return immobile
