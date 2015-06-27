from xml.etree import ElementTree
import requests
from .config import BUS_STOPS, BUSTRACKER_API_KEY, PREDICTIONS_URL


def arrival_time(prediction):
    prdtm = prediction.find('prdtm')
    return prdtm.text.split()[1]


def bus_info():
    output = {}
    for bus_route, bus_stop_id in BUS_STOPS.iteritems():
        params = {
            'key': BUSTRACKER_API_KEY,
            'stpid': bus_stop_id
        }
        r = requests.get(PREDICTIONS_URL, params=params)
        xml_doc = ElementTree.fromstring(r.content)
        error = xml_doc.findall('error')
        predictions = xml_doc.findall('prd')
        output[bus_route] = [] if error else [arrival_time(p) for p in predictions]
    return output
