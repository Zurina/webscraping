import re

names_reg = re.compile(r'.*Møller')
numbers_reg = re.compile(r'\d{2} \d{2} \d{2} \d{2}')
zip_codes_reg = re.compile(r'\A\d{4}\n')

with open('adresses.txt', encoding='utf8') as file:
    content = file.readlines()

[print(line) for line in content if names_reg.search(line) != None] # finding Møllers
[print(line) for line in content if numbers_reg.search(line) != None] # finding numbers
[print(line) for line in content if zip_codes_reg.search(line) != None] # finding zip codes




