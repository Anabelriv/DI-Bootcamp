# import modules (requests, time?)
# HTTP get request, check with if statement if it loads
# if it loads, check the time it took to get a response, use attr elapsed from requests? --- elapsed: The amount of time elapsed between sending the request and the arrival of the response (as a timedelta). This property specifically measures the time taken between sending the first byte of the request and finishing parsing the headers. It is therefore unaffected by consuming the response content or the value of the stream keyword argument.


import requests

def measure_load_time(url):
    response = requests.get(url)
    if response.status_code == 200:
        load_time = response.elapsed.total_seconds()
        return f"The webpage {url} took {load_time:.2f} seconds to load."
    
    else:
        return "Error: Failed to load the webpage."

# Test the function with multiple websites.
urls = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]
for url in urls:
    print(measure_load_time(url))



# Second Option with import time measuring before the connection and after:

# import requests
# import time



# def get_webpage_load_time(url):
#     try:
#         start_time = time.time()
#         response = requests.get(url)
#         end_time = time.time()
#         load_time = end_time - start_time
#         return load_time
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
#         return None
    
# if __name__ == "__main__":
#     websites = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]
#     for website in websites: 
#         load_time = get_webpage_load_time(website)
#         if load_time is not None:
#             print(f"load time for {website}: {load_time:.2f} seconds")


