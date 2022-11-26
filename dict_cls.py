#dictionaries:sequence of key:value pair which are separated with comma,declared inside {}

dict1={"name":"Praveen","email":"praveen123@gmail.com","mobile":98653008634,"compainies":["tcs","infosys","wipro"]}

print(dict1)


#dict_name[key_name]

print(dict1["email"])

#print(dict1["companies"])

print(dict1["mobile"])

dict1["address"]="12-2-78,mettuguda,hyderabad"
print(dict1)


#dictionary Methods

print(dir(dict))


#Nested dictionary: dictionary inside the dictionary called as nested...


dict2={"teams":{
                "cks":3,
                "MI":4,
                "KKR":2,
                "RR":1,
                "DD":1
                },

      "captains":{
                  "chennai":"Dhoni",
                  "Mumbai":"Sachin",
                  "Kolkata":"Gambhir",
                  "Rajasthan":"Warne",
                  "Hyderabad":"Gilchrist"
      }
      }

print(dict2["captains"]["Hyderabad"])

print(dict2["teams"]["DD"])


#dict methods---update():this is for adding a dictionary into the dict

dict1={"name":"Praveen","email":"praveen123@gmail.com","mobile":98653008634,"compainies":["tcs","infosys","wipro"]}

dict3={"city":"hyderabad","position":"software engineer"}

dict1.update(dict3)
print(dict1)

#get(): its used for accessing the key:values inside the dictionary

print(dict1.get("email"))

print(dict1.get("name"))


#key():it will return all the keys inside the dictionary..

print(dict1.keys())

#values: it will return all the values inside the dictionary..

print(dict1.values())

#items(): it will return all key:value pairs as tuple inside the list

data=list(dict1.items())

print(data[1])

print(data[1][1])


#fromkeys(): its for creating a dict from list of elements

a=[1,"name","email","mobile"]


print({}.fromkeys(a,"sample"))


#set default(): it will set the default value,it will be constant
#giving the default key:value to the dict..

dict={}
dict.setdefault("city","Delhi")
print(dict)


print(dict.setdefault("city"))

#dictionary comprehension:


dict4={}

for ele in range(1,7):
    dict4[ele]=ele**3
print(dict4)

#1st syntax:
print({ele:ele**3 for ele in range(1,7)})


#i want only even numbers performance square

for ele in range(1,7):
    if ele%2==0:
        dict4[ele]=ele**2
print(dict4)

#2nd syntax:

print({ele:ele**2 for ele in range(1,7) if ele%2==0})

#3rd syntax:
for ele in range(1,7):
    if ele%2==0:
        dict4[ele]=ele**2
    else:
        dict4[ele]=ele**3
print(dict4)



print({ele:ele**2 if ele%2==0 else ele**3 for ele in range(1,7)})













































