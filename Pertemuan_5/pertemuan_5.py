# import datetime
# import math
import json
# import os

# # x = datetime.datetime(2023,1,1)
# # print (x.strftime("%d/%m/%Y"))

# # #
# # arr_1 = [5,78,2,0]

# # assert(min(arr_1)) == 0
# # assert(max(arr_1)) == 78

# # assert pow (5,5) == 3125

# # #
# # #try:
# #   #f = open("demofile.txt")
# #   #try:
# #     #f.write("Lorum Ipsum")
# #   #except:
# #     #print("Something went wrong when writing to the file")
# #   #finally:
# #     #f.close()
# # #except:
# #   #print("Something went wrong when opening the file")

# # try:
# #   print(x)
# # except:
# #   print("Something went wrong")
# # finally:
# #   print("The 'try except' is finished")

# # # dari luar ke dalam
# # # some JSON:
# # x =  '{ "name":"John", "age":30, "city":"New York"}'

# # # parse x:
# # y = json.loads(x)

# # # the result is a Python dictionary:
# # print(y["age"])

# # #dari dalam ke luar
# # # a Python object (dict):
# # x = {
# #   "name": "John",
# #   "age": 30,
# #   "city": "New York"
# # }

# # # convert into JSON:
# # y = json.dumps(x)

# # # the result is a JSON string:
# # print(y)


# # f = open("demofile.txt", "r")

# # print(f.readline())
# # print(f.close())

# f = open("demofile2.txt", "w")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())

# os.remove("demofile.txt")

f = open('json_read.txt','w')
json_string = f.write(json_stringg)

print(json_string)
users = [
 {
    
    'email':'mdzikrifathul@gmail.com',
    'password':'231'
 }
]

json_dict = json.loads(json_string)
print(json_dict)
print(type(json_dict))
print(json_dict['name'])

