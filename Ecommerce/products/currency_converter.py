import requests
from django.conf import settings

class CurrencyConverter:
    def __init__(self):
        self.api_key = settings.OXR_API_KEY
        self.base_url = settings.OXR_BASE_URL

    def get_conversion_rate(self, from_currency: str, to_currency: str):
        endpoint = f"{self.base_url}/latest.json"
        params = {
            'app_id': self.api_key,
            'base': from_currency,
            'symbols': to_currency
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            data = response.json()
            return data['rates'].get(to_currency, 1.0)
        return None
