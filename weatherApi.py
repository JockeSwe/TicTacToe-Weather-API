import requests, json  # API import

class weatherApiProgram:
  def __init__(self):
    self.api_key = "6b8f5cd2cf91800133c5e5a612457a04"
    self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
    self.city_name = input("Enter city name:\n")
    self.complete_url = self.base_url + "appid=" + self.api_key + "&q=" + self.city_name  #Adds everything together to send a request to the url
    self.response = requests.get(self.complete_url)  #sends request
    self.x = self.response.json()  # Converts to json

  
  def cityFinder(self):
    if self.x["cod"] != "404":  #If it finds a city
      current_temperature = self.x["main"]["temp"]
      print(round(current_temperature - 273.15, 2))
# Converts from Kelvin to Celsius and rounds the number to the nearest hundredth decimal
    else:  # If 404 is not returned something went wrong/ no city was found
      print("City not found")

  def weatherNumber(self):
    global first_digit, weather_list
    #weather_name_condition = "null"
    weather_id_condition = self.x["weather"][0]["id"] # Saves a weather ID which will later match the id to a list
    weather_string = str(weather_id_condition) # Convert weather_id_condition to string
    first_digit = int(weather_string[0]) # First digit of weather_id_condition
    weather_list = ["0", "1", "thunderImage.png", "drizzleImage.png", "cloudyImage.png", "rainyImage.jpg", "snowyImage.png", "atmosphericImage.png", "clearskyImage.png"] # List to match the weather condition with images in pygameCode.py line 10

    if weather_id_condition in (801, 802, 803, 804): # WORKAROUND: if condition of weather is cloudy, make first digit = 4
      first_digit = 4 # number "4" in weather_list is cloud image, 4 was not in use
    
weatherG = weatherApiProgram()
weatherG.cityFinder()
weatherG.weatherNumber()


""" ---------------------------------------------------
https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2

Weather conditions code:
2xx: thunderstorm
3xx: Drizzle (dugga)
5xx: rain
6xx: snow
7xx: Atmosphere (mist, fog, smoke)
800: clear
80x: cloudy
-------------------------------------------------- """


  