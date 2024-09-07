import requests
base_url="http://localhost:8000"
data_path="/calculate/{num1}/{num2}"
x=12
y=14
response=requests.get(f"{base_url}/calculate/{x}/{y}")
print(response.text) #convert json to sum
print(response.json()["sum"])

#time info:
timer=requests.get(f"{base_url}/time-info")
print(timer.text)
print(f"year is:{timer.json()['year']}")


