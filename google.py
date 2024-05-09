import requests
import webbrowser


def location(search, apikey):
    base_url = "https://us1.locationiq.com/v1/search?format=json"
    params = {
        "key": apikey,
        "q": search,
    }

    response = requests.get(base_url, params=params)

    data = response.json()

    if response.status_code == 200 and data:
        result = {
            "place_id": data[0].get("place_id", ""),
            "lat": data[0].get("lat", ""),
            "lon": data[0].get("lon", ""),
            "display_name": data[0].get("display_name", ""),
        }
        print(result)
        return result
    else:
        print("error")
        return None


def open_map(lat, lon):
    map_url = f"https://maps.google.com/?q={lat},{lon}"
    webbrowser.open(map_url)


apikey = "pk.4acb4753cf501e3cae5aadd923149fff"
search = input("Enter location: ")

location_data = location(search, apikey)
if location_data:
    open_map(location_data['lat'], location_data['lon'])
