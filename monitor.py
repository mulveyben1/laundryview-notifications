import requests
import time

room1 = 415890003
room2 = 415890057


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11',
           }
url1 = "https://www.laundryview.com/api/currentRoomData?school_desc_key=8861&location=%s" % room1 # smith a
url2 = "https://www.laundryview.com/api/currentRoomData?school_desc_key=8861&location=%s" % room2  # smith b

response_a = requests.get(url1, headers=headers)
response_b = requests.get(url2, headers=headers)

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

a_washers = []
a_dryers = []
for i in objects_a:
    if i['type'] == "washFL":
        a_washers.append(i)
    elif i['type'] == "dry":
        a_dryers.append(i)

b_washers = []
b_dryers = []
for i in objects_b:
    if i['type'] == "washFL":
        b_washers.append(i)
    elif i['type'] == "dry":
        b_dryers.append(i)

available = []
unavailable = []

for washer in a_washers:
    if washer['time_left_lite'] == "Available":
        available.append({'ID': "%s" % washer["appliance_desc_key"], 'Location': "%s" % washer['appliance_desc'],
                          'Room': "A"})
    else:
        unavailable.append({'ID': "%s" % washer["appliance_desc_key"], 'Location': "%s" % washer['appliance_desc'],
                           'Room': "A"})

for dryer in a_dryers:
    if dryer['time_left_lite'] == "Available":
        available.append({'ID': "%s" % dryer["appliance_desc_key"], 'Location': "%s" % dryer['appliance_desc'],
                          'Room': "A"})
    else:
        unavailable.append({'ID': "%s" % dryer["appliance_desc_key"], 'Location': "%s" % dryer['appliance_desc'],
                           'Room': "A"})


for washer in b_washers:
    if washer['time_left_lite'] == "Available":
        available.append({'ID': "%s" % washer["appliance_desc_key"], 'Location': "%s" % washer['appliance_desc'],
                          'Room': "B"})
    else:
        unavailable.append({'ID': "%s" % washer["appliance_desc_key"], 'Location': "%s" % washer['appliance_desc'],
                           'Room': "B"})


for dryer in b_dryers:
    if dryer['time_left_lite'] == "Available":
        available.append({'ID': "%s" % dryer["appliance_desc_key"], 'Location': "%s" % dryer['appliance_desc'],
                          'Room': "B"})
    else:
        unavailable.append({'ID': "%s" % dryer["appliance_desc_key"], 'Location': "%s" % dryer['appliance_desc'],
                           'Room': "B"})

print("Available: " + str(available))
print("Unavailable: " + str(unavailable))
