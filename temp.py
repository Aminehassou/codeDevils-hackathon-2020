import pycountry
import json
cc={}
t = list(pycountry.countries)   
for country in t:
    cc[country.name]=country.alpha_2

print(cc)
