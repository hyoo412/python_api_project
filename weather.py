import requests
from requests.exceptions import ConnectionError

class Weather:
  def __init__(self, longitude, latitude, timez):
    
    self.url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&timezone={timez}&daily=temperature_2m_max&daily=temperature_2m_min&daily=precipitation_sum"
    self.getWeather()

  def __str__(self):
    pass

  def getWeather(self):
    try:
      self.response = requests.get(self.url).json()
      self.temperature_max = self.response['daily']['temperature_2m_max']
      self.temperature_max.insert(0, "Maximum Temperature")
      self.temperature_min = self.response['daily']['temperature_2m_min']
      self.temperature_min.insert(0, "Minimum Temperature")
      self.precipitation = self.response['daily']['precipitation_sum']
      self.precipitation.insert(0, "Precipitation")
      self.daily_time = self.response['daily']['time']
      self.daily_time.insert(0, "Day")
    except ConnectionError:
      print("Connection Error")
