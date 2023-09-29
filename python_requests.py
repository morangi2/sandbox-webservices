#!/usr/bin/env python3

#for programs that send and receive HTTP
import requests

response = requests.get("https://www.google.com")
print(response) #OUTPUT is <Response [200]>
print(response.text[:300]) #output below
"""
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-CA"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="SQ5PNL1uhaVda
"""

response2 = requests.get("https://www.google.com", stream = True)
print(response2.raw.read()[:100]) #reads the raw response

print(response.ok) #returns TRUE ==> checks if we got a successful response
print(response2.ok) #returns TRUE

print(response.status_code) #returns 200, the response code, to show you got the response you needed

#raise exceptions if the status code isn't what you expected
#response_bad = requests.get("https://www.mathogsz.com")
#if not response_bad.ok:
    #raise Exception("GET failed with status code {}".format(response_bad.status_code))
    #or
    #print(response_bad.raise_for_status()) #will raise an HTTPError exception only if the response wasn’t successful.

# example of a GET request
# https://example.com/path/to/api/cat_pictures?search=grey+kitten&max_results=15
# has parameters, seperated by the ?

p = {"search": "grey kitten", "max_results": 15}
response_querystring = requests.get("https://www.google.com", params = p)
print(response_querystring.request.url) # returns ==> https://www.google.com/?search=grey+kitten&max_results=15 ... look at .url, that's where you'll find the params

# example of a POST request
p2 = {"description": "white_kitten", "name": "Snowball", "age_months": 6}
response_poststring = requests.post("https://www.google.com", data = p2)
print(response_poststring.request.body) # returns description=white_kitten&name=Snowball&age_months=6 ... look at .request.body

# another POST example using a json file
"""
>>> response = requests.post("https://example.com/path/to/api", json=p)
>>> response.request.url
'https://example.com/path/to/api'
>>> response.request.body
b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 
"""


{'title': 'Good deal for a 2015 RAV4', 'username': 'Anonymous', 'date': '2018-04-17', 'feedback': 'Called them to look for a second-hand RAV4 and they are very nice and patience to help me find me a few matches then scheduled an appointmet with me. Came in and they had everything ready for me. I was surprised how professional those sales are and they explained and answered all my questions. Ended up buying the car and been using it for more than a month now. Everything looks good!'}