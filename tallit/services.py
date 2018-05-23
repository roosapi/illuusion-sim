import requests

def get_vrl_info(vh):
    url = 'http://www.virtuaalihevoset.net/?rajapinta/ominaisuudet.html?' 
    params = {'vh': vh}
    r = requests.get(url, params=params)
    print(r.url)
    return r.json()