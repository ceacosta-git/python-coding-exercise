import requests
import logging
import logging.config
from datetime import datetime
from pathlib import Path

logging.config.fileConfig(str(Path('../logging.conf').resolve()))

# create logger
logger = logging.getLogger('test_nasa_picture_api')

def test_get_picture_of_the_day():
    today = datetime.today().strftime('%Y-%m-%d')
    api_url = 'https://api.nasa.gov/planetary/apod'
    query_params = {"date": today, "api_key": 'PTMCb8NPvJak1bsyJ5DK4cAMRegCufHXxUIzNLil'}
    todays_pic_response = requests.get(api_url, query_params)
    logger.debug(f"response: {str(todays_pic_response)}")
    todays_pic_json = todays_pic_response.json()
    logger.debug(f"response (json): {str(todays_pic_json)}")
    assert todays_pic_json["date"] == today
    assert todays_pic_json["media_type"] == "image"
