import requests


def request_for_weather(geo_point):
    url = 'https://wttr.in/'
    http_params = {"mMnqT": "", "lang": "ru"}
    try:
        response = requests.get(f"{url} {geo_point}", timeout=5, params=http_params)
        response.raise_for_status()
        return response.text
    except requests.ConnectionError:
        print('Connection Error')
    except requests.HTTPError:
        print('HTTP error')
    except requests.Timeout:
        print('Timeout occurred')


def main():
    geo_points = ['London', 'svo', 'Череповец']
    for geo_point in geo_points:
        print(request_for_weather(geo_point))


if __name__ == '__main__':
    main()
