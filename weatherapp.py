import requests 

apikey = 'your api key'
print("                   ____      /\      _____     |      |       ____   _____            ")
print("\      /\      /  |         /  \       |       |      |      |       |    |        ")
print(" \    /  \    /   |____    /    \      |       |______|      |____   |____|       ")
print("  \  /    \  /    |       /______\     |       |      |      |       | \            ")
print("   \/      \/     |____  /        \    |       |      |      |____   |  \           ")


location = input("enter loaction :")
weatherdata = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&APPID={apikey}")

if weatherdata.json()['cod'] =='404':
    print("City not found")
else:
    weather = weatherdata.json()['weather'][0]['main']
    temp = round(weatherdata.json()['main']['temp'])
    print("weather of" ,location, "is" ,weather )
    print("Temperature of",location, "is", temp ,"degrees")
