import requests


def request_for_weather(geo_point, http_params):
    url = 'https://wttr.in/'
    response = requests.get(f"{url} {geo_point}", timeout=5, params=http_params)
    response.raise_for_status()
    return response.text


def main():
    geo_points = ['London', 'svo', 'Череповец']
    for geo_point in geo_points:
        try:
            print(request_for_weather(geo_point, {"mMnqT": "", "lang": "ru"}))
        except requests.HTTPError:
            print("HTTP Error")
        except requests.Timeout:
            print("Timeout occurred")
        except requests.ConnectionError:
            print("Connection Error")


if __name__ == '__main__':
    main()
