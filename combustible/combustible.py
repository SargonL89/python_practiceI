def liters_100km_to_miles_gallon(liters):
    gallon = liters * 1.609344
    miles = 3.785411784 * 100
    miles_gallon = miles / gallon
    return miles_gallon

def miles_gallon_to_liters_100km(miles):
    miles_gallon = (3.785411784 * 100) / 1.609344
    liters_100km = miles_gallon / miles
    return liters_100km


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))




