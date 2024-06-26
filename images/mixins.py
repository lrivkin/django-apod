from django.conf import settings
import requests


class APODImageAPIMixin:
    def fetch_apod_from_api(self, params):
        api_url = "https://api.nasa.gov/planetary/apod/"
        params["api_key"] = settings.API_KEY

        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.HTTPError:
            return None
