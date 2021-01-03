import phonenumbers
from test import number
from phonenumbers import geocoder, carrier

country_num = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(country_num, "en"))

service_num = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_num, "en"))
