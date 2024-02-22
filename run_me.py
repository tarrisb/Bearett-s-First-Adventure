import requests

##

class City:

  # unit_match_dict = {
  #   'metric': "C",
  #   'imperial': "F"
  # }
  
  def __init__(self, name, lat, lon, units="metric"):
    self.name = name
    self.lat = lat
    self.lon = lon
    self.units = units
    self.get_weather()
  
  def get_weather(self):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=f5c9e238f5930c78654afd1f5c9d863c")
    self.response = response.json()
    self.temp = self.response["main"]["temp"]
    self.temp_min = self.response["main"]["temp_min"]
    self.temp_max = self.response["main"]["temp_max"]

  def temp_print(self):
      if self.units == "metric":
         label = "C"
      else:
         label = "F"
      print(f"In {self.name}, the current temperature is {self.temp} {label}")
      print(f"Today's high is: {self.temp_max} °")
      print(f"Today's low is: {self.temp_min} °")
    

my_city = City("Whistler", 50.1162, -122.9535)
my_city.temp_print()
new_city = City("Fairplay", 39.2247, -106.0020, "imperial")
new_city.response
new_city.temp_print()
#print(new_city.response)
