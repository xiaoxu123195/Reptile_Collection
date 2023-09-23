import requests
import urllib.request


url = "https://www.bilibili.com/"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
# response = urllib.request.urlopen(url)
# print(response.getheader('Server'))
response = requests.get(url, headers=headers)
return_headers = response.headers
types = return_headers['Content-Type']
print(types)
