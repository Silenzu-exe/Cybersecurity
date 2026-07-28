
months = open('/home/silenzu/Documents/Myvault/Cyber_Security/2. Python/1. Python Basic/10. Reand and write/months.txt', "r")

print(months)

# print(months.readlines())

print(months.readable())

for month in months:
    print(month.strip())
    
months.close()

