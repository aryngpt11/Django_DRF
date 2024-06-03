import requests
URL="http://127.0.0.1:8000/student_detail/1"
r=requests.get(url=URL) #response
data=r.json() #extracting data
print(data)


#third party application