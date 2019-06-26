import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size!=0 :
    Old_File=open("./ages.json","r+")
    #Data=Old_File.read()
    Data=json.load(Old_File.read())
    print("Current Age is : "+str(Data["Age"])+"---Adding a year")
    Data["Age"]+=1
    print("New Age is : "+str(Data["Age"]))

else :
    Old_File=open("./ages.json","w+")
    Data={"Name" : "Nick","Age":27}
    Old_File.write(json.dumps(Data))
