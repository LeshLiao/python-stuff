import requests

def post_data(id, data):
    # Define new data to create
    new_data = {
        "card_id": id,
        "card_data": data
    }
    # The API endpoint to communicate with
    url_post = "https://mern-stack-website.onrender.com/api/workouts"
    #url_post = "http://192.168.1.12:4000/api/workouts"

    # A POST request to tthe API
    post_response = requests.post(url_post, json=new_data)

    # Print the response
    post_response_json = post_response.json()
    print(post_response_json)

    # Print status code from original response (not JSON)
    print("status_code="+str(post_response.status_code))

if __name__ == '__main__':
    post_data("0001", "test data 123")
