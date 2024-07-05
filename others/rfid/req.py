import requests
import threading
import time

'''
# check process
ps aux | more | grep python
# kill a process
sudo kill -9 <ID>

'''

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
    # print(post_response_json)

    # Print status code from original response (not JSON)
    # print("status_code="+str(post_response.status_code))

    return post_response_json, str(post_response.status_code)

def get_all_data():
    r = requests.get('https://mern-stack-website.onrender.com/api/workouts')
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.text)
        pass

def test_loop():
    index = 0
    while True:
        index = index + 1
        print("loop_"+str(index))
        time.sleep(1)

if __name__ == '__main__':

    try:
        #json_data, res_code = post_data("0001", "test data 123")
        #print(json_data)
        #print(res_code)

        t1 = threading.Thread(target = test_loop)
        t1.start()

        #get_all_data()

        #test_loop()
        print("let go")

    except requests.Timeout:
        # back off and retry
        print("requests.Timeout")
        pass
    except requests.ConnectionError:
        print("requests.ConnectionError")
        pass
