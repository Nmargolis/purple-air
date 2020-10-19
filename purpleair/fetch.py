from typing import List
import requests


def get_all_sensor_data(purple_air_url) -> List:
    """
    Gets all purple air json data, and returns the json response.
    """
    response = requests.get(purple_air_url)
    if response:
        json = response.json()
        return json['results']
    else:
        print(f'Error [{response.status_code}]:', response.json())
        # TODO: throw error or otherwise trigger retry
