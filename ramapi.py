import requests
from dataclasses import asdict
from models import ApiResponse


base_url = "https://rickandmortyapi.com/api"


def get_endpoint(endpoint, params):
    response = requests.get(f"{base_url}/{endpoint}", params=asdict(params))
    response.raise_for_status()
    response = ApiResponse(**response.json())

    return response
