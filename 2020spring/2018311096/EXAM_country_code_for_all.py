import pygal 
from pygal_maps_world.i18n import COUNTRIES

for code in COUNTRIES.keys():
	print(code,COUNTRIES[code])

def get_code(country_name):
	for code,name in COUNTRIES.items():
		if name==country_name:
			return code
	return None
	
	

