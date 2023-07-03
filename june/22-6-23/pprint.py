# A python code with pprint
import requests
import pprint


def geocode(address):
    url = "https://www.w3schools.com/python/gloss_python_function_recursion.asp"
    resp = requests.get(url, params={'address': address})
    return resp.json()


# calling geocode function
data = geocode('India gate')

# pretty-printing json response
pprint(data)
