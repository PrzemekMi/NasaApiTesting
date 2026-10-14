import requests

def make_request(api_key):
    #base_url = "https://api.nasa.gov/neo/rest/v1/feed/"
    base_url = "https://technology.nasa.gov/api/api/software/visualization"
    #base_url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
    response = requests.get(f'{base_url}?api_key={api_key}')
    return response


