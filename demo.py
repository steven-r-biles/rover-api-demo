"""
Our rover has just landed on Mars and we need to send it instructions on how to move around.
The rover has limited power and each instruction will consume power.
The rover service will estimate the power level after completing each instruction.
If the power level will fall below 0, the mission will be rejected.
We can send subsequent requests to update our mission with new instructions.


"""

import requests

API_URL = "http://localhost:8000"
session = requests.session()

# Create a new valid mission

mission = {
    "name": "Mars rover",
    "description": "Test 1",
    "commands": [
        "forward 10",
        "right 90",
        "forward 5",
        "left 45",
        "wait 10",
        "picture",
        "forward 15",
        "picture",
    ]
}

print('Sending mission to rover service with instructions:', mission)

response = session.post(f"{API_URL}/mission/", json=mission)

print("The mission was accepted. ")
print(response.json())
print("Press Enter to continue...")
input()

# Create a mission that would use too much power

mission = {
    "name": "Mars rover",
    "description": "Test 2",
    "commands": [
        "forward 10",
        "right 90",
        "forward 5",
        "left 45",
        "wait 10",
        "picture",
        "forward 150",
        "picture",
    ]
}

print('Sending mission to rover service with instructions:', mission)

response = session.post(f"{API_URL}/mission/", json=mission)

print("The mission was rejected. ")
response_data = response.json()
print(response_data)
mission_id = response_data['data']['id']
print("Press Enter to continue...")
input()

# Update the mission with new instructions

mission['commands'][6] = 'forward 8'
print('Sending updated mission to rover service with instructions:', mission)
response = session.post(f"{API_URL}/mission/{mission_id}/", json=mission)

print("The mission was accepted. ")
print(response.json())
print("Press Enter to continue...")
input()

# Get the mission data in JSON format
print('Getting mission data JSON')
response = session.get(f"{API_URL}/mission/{mission_id}/", headers={'Accept': 'application/json'})
print(response.json())
print("Press Enter to continue...")
input()

# Get the mission data in CSV format
print('Getting mission data CSV')
response = session.get(f"{API_URL}/mission/{mission_id}/", headers={'Accept': 'text/csv'})
filename = response.headers['Content-Disposition'].split('=')[1]
print('filename:', filename)
print('file contents:')
print(response.text)
print("Press Enter to continue...")
input()

# Delete the mission
print('Deleting mission')
response = session.delete(f"{API_URL}/mission/{mission_id}/")
print(response.json())
