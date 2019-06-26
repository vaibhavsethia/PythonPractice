import requests

my_data={"name":"Vaibhav","email":"vaibhavsethia@gmail.com"}
r=requests.post("https://www.w3schools.com/php/welcome.php",data=my_data)

f=open("My_file.html","w+")
f.write(r.text)