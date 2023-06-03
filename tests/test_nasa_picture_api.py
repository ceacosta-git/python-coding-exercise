import requests
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)


def test_get_picture_of_the_day():
    today = datetime.today().strftime('%Y-%m-%d')
    api_url = 'https://api.nasa.gov/planetary/apod'
    query_params = {"date": today, "api_key": 'PTMCb8NPvJak1bsyJ5DK4cAMRegCufHXxUIzNLil'}
    todays_pic_response = requests.get(api_url, query_params)
    logging.debug(f"response: {str(todays_pic_response)}")
    todays_pic_json = todays_pic_response.json()
    logging.debug(f"response (json): {str(todays_pic_json)}")
    assert todays_pic_json["date"] == today
    assert todays_pic_json["media_type"] == "image"
