import requests
from requests.exceptions import ConnectionError

class Location:
  def __init__(self, ask):
    self.ask = ask
    self.l_url = f"https://get.geojs.io/v1/ip/geo/{ask}.json"
    self.getLocation()

  def __str__(self):
    pass

  def getLocation(self):
    try:
      self.response = requests.get(self.l_url).json()
      self.longitude = self.response['longitude']
      self.latitude = self.response['latitude']
      self.timez = self.response['timezone']
      self.country = self.response['country']
      self.region = self.response['region']
      self.city = self.response['city']
    except ConnectionError:
      print("Connection Error")
