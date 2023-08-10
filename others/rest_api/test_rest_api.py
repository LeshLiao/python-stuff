import requests

# The API endpoint
url = "http://localhost:4000/api/workouts/1"

# A GET request to the API
response = requests.get(url)

# Print the response
response_json = response.json()
print(response_json)

# Print status code from original response (not JSON)
print(response.status_code)

"""
{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
"""

# =============== POST

# Define new data to create
new_data = {
    "title": "Situps_python_01",
    "load": 2,
    "reps": 3
}
# The API endpoint to communicate with
url_post = "http://localhost:4000/api/workouts"

# A POST request to tthe API
post_response = requests.post(url_post, json=new_data)

# Print the response
post_response_json = post_response.json()
print(post_response_json)

# Print status code from original response (not JSON)
print("status_code="+str(post_response.status_code))
"""
{'userID': 1, 'id': 101, 'title': 'Making a POST request', 'body': 'This is the data we created.'}
"""
