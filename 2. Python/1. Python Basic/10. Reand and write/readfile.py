
months = open('/home/silenzu/Documents/Myvault/Cyber Security/Python/10. Reand and write/months.txt')

print(months)

# print(months.readlines())

print(months.readable())

for month in months:
    print(month.strip())
    
months.close()

