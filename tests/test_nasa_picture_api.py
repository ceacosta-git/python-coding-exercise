import requests
from datetime import datetime


def test_get_picture_of_the_day():
    today = datetime.today().strftime('%Y-%m-%d')
    api_url = 'https://api.nasa.gov/planetary/apod'
    query_params = {"date": today, "api_key": 'PTMCb8NPvJak1bsyJ5DK4cAMRegCufHXxUIzNLil'}
    todays_pic_response = requests.get(api_url, query_params)
    todays_pic_json = todays_pic_response.json()
    assert todays_pic_json["date"] == today
    assert todays_pic_json["media_type"] == "image"
