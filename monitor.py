import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11',
           }
url1 = "https://www.laundryview.com/api/currentRoomData?school_desc_key=8861&location=415890057"  # smith b
url2 = "https://www.laundryview.com/api/currentRoomData?school_desc_key=8861&location=415890003"  # smith a

response_a = requests.get(url2, headers=headers)
response_b = requests.get(url1, headers=headers)

if not response_a:  # failed
    time.sleep(30)
    response_a = requests.get(url2, headers=headers)
    if not response_a:  # really failed
        print("Failed to get status for Smith A")
        raise requests.exceptions.ConnectionError

if not response_b:  # failed
    time.sleep(30)
    response_b = requests.get(url1, headers=headers)
    if not response_b:  # really failed
        print("Failed to get status for Smith B")
        raise requests.exceptions.ConnectionError

objects_a = response_a.json()['objects']
objects_b = response_b.json()['objects']

a_washers = {}
a_dryers = {}
for i in objects_a:
    if i['type'] == "washFL":
        a_washers.update(i)
    elif i['type'] == "dry":
        a_dryers.update(i)

b_washers = {}
b_dryers = {}
for i in objects_b:
    if i['type'] == "washFL":
        b_washers.update(i)
    elif i['type'] == "dry":
        b_dryers.update(i)



