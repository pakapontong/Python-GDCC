import datetime 

now = datetime.datetime.now()
nowwithformat = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(now)
print(nowwithformat)