# d = {"name":"Sourav","rollNo":115,"id":430}
# print(type(d))

# Convert the dict into JSON format 
import json
# d = {"name":"Sourav","rollNo":115,"id":430}
# data = json.dumps(d)
# print(type(data))



# access the value of age from the given data 
# student = '{"name":"Sourav","rollNo":115,"id":430,"age":21}'
# data_st = json.loads(student)
# print(data_st["name"])



# Pretty Print following JSON 
# student = {"name":"Sourav","rollNo":115,"id":430,"age":21}
# data = json.dumps(student, indent=2, separators=(",","="))
# print(data)

# Also know as pretty printing 



# # Sort the following JSON keys and wrrite them into a file 
# student = {"name":"Sourav","rollNo":115,"id":430,"age":21}
# f = open("Introduction/demo.json","w")
# data = json.dumps(student, indent=4, sort_keys=True)
# f.write(data)


# print("data has been added to the file.")