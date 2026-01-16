'''
Using the Positionstack API, retrieve the full address for the coordinates: Latitude: 6.6778, Longitude: 3.1654. 
Write a function to call the API, and extract the first address in the array. Paste the full address below.
'''


import requests

def get_full_address(latitude, longitude, api_key):
    url = "http://api.positionstack.com/v1/reverse"
    params = {
        "access_key": api_key,
        "query": f"{latitude},{longitude}",
        "limit": 1
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    # Get the first address label
    if data.get("data"):
        return data["data"][0].get("label")

    return None


# Example usage
API_KEY = "ec34b0edf01da3a86979ec93520108c8"
latitude = 6.6778
longitude = 3.1654

address = get_full_address(latitude, longitude, API_KEY)
print(address)

# output: Faith Tabarnacle, Agege, OG, Nigeria
