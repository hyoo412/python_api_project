from location import Location
from weather import Weather

def main():

  ask = input("Type in IP: ")
  check = ask.split(".")
  
  if len(check) != 4:
    print("Incorrect IP type.")
    return

  for num in check:
    if not isinstance(int(num), int):
      print("Wrong value.")
      return
    if int(num) < 0 or int(num) > 255:
      print("IP out of range.")
      return
    
  ip = Location(ask)

  weather = Weather(ip.longitude, ip.latitude, ip.timez)

  print("\nLOCATION INFORMATION\n====================")
  print(f"Country: {ip.country}\nRegion: {ip.region}\nCity: {ip.city}\nTimezone: {ip.timez}\nLongitude: {ip.longitude}\nLatitude: {ip.latitude}\n")
  print("WEATHER INFORMATION\n====================")

  weather_info = [
      weather.daily_time, 
      weather.temperature_max, 
      weather.temperature_min, 
      weather.precipitation
  ]

  for info in weather_info:
    print("{: <30} {: <30} {: <30} {: <30}".format(*info))


main()
