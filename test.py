import socket
from ip2geotools.databases.noncommercial import DbIpCity

url = input("Incert a URL: ")
ip = socket.gethostbyname(url)
response = DbIpCity.get(ip, api_key="free")

print(f"IP: {ip}")
print(f"City: {response.city}")
print(f"Region: {response.region}")
print(f"Country: {response.country}")
print(f"Longitude: {response.longitude}")
print(f"Latitude: {response.latitude}")

def get_google_maps_link(latitude, longitude):
    base_url = "https://www.google.com/maps/place/{},{}"
    return base_url.format(latitude, longitude)

google_maps_link = get_google_maps_link(response.latitude, response.longitude)
print("Google Maps link:", google_maps_link)
