# import requests
# city = input("Insert city")
# for i in city:
#     if i == ' ':
#         city.replace(i, '+')
#
# api_weather = "api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=953a4a4cddff1086a1171621db392044"
# details = requests.get(api_weather).json()
# print(details["weather"]["main"])
