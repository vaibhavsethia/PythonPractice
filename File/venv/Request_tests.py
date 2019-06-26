import requests

params={"q":"Pizza"}
r=requests.get("https://www.bing.com/search",params=params)
print("Status :",r.status_code)
print(r.url)
#print(r.text)

File=open("./Page.html","w+")
File.write(r.text)