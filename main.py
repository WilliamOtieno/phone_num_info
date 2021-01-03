import phonenumbers
from test import number
from phonenumbers import geocoder, carrier, timezone

country_num = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(country_num, "en"))

service_num = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_num, "en"))

gb_num = phonenumbers.parse(number, "GB")
print(timezone.time_zones_for_number(gb_num))
