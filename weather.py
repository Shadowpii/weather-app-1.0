import requests

city = input('The City Name = ')


print("Displaying "+city+" Weather Report")

url = 'https://wttr.in/{}'.format(city)

res = requests.get(url)

print (res.text)