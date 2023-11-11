from ramapi import get_endpoint
from models import ApiParameters, CharacterSchema

endpoint = "character"


def get_all_results(endpoint, pages, params):
    results = []
    for page in range(1, pages + 1):
        params.page = page
        print(f"current page = {page}")
        response = get_endpoint(endpoint, params)
        results.extend(response.results)
    return results


if __name__ == "__main__":
    params = ApiParameters()
    response = get_endpoint(endpoint, params)
    results = get_all_results(endpoint, response.info.pages, params)
    print(f"total records: {len(results)}")
