import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+919081200383")
phone_number2 = phonenumbers.parse("+918003338208")

print("\nphone numbers location\n")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
