from ramapi import get_endpoint
from models import ApiParameters, CharacterSchema

# hardoded weirdge
endpoint = "character"


# just paginates till hits page limit using extend instead of unpacking tho
def get_all_results(endpoint, pages, params):
    results = []
    # from page 1 to last page
    for page in range(1, pages + 1):
        # increment the page in your params dataclass
        params.page = page
        print(f"current page = {page}")
        # do a request
        response = get_endpoint(endpoint, params)
        # e x t e n d
        results.extend(response.results)
    return results


if __name__ == "__main__":
    # dataclass model
    params = ApiParameters()
    # one request to grab the inital page count for for loop
    response = get_endpoint(endpoint, params)
    # start calling all pages
    results = get_all_results(endpoint, response.info.pages, params)
    print(f"total records: {len(results)}")
