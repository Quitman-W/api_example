import requests
from dataclasses import asdict
from models import ApiResponse

# hardcoded base url always rick and morty kinda weird but its just an example
base_url = "https://rickandmortyapi.com/api"


# function for getting endpoint
def get_endpoint(endpoint, params):
    # dyanmic request based on endpoint
    response = requests.get(f"{base_url}/{endpoint}", params=asdict(params))
    # throw error on not 200
    response.raise_for_status()
    # unpack it into the dataclass model of api response
    response = ApiResponse(**response.json())
    # return that unpacked version
    return response
