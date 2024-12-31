import json
# Sort the following JSON keys and wrrite them into a file 
student = {"name":"Sourav","rollNo":115,"id":430,"age":21}
f = open("Introduction/demo.json","w")
data = json.dumps(student, indent=4, sort_keys=True)
f.write(data)


print("data has been added to the file.")