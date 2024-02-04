def liters_100km_to_miles_gallon(liters):
    return (100000 / 1609.344)/(liters / 3.785411784)


def miles_gallon_to_liters_100km(miles):
    return 3.785411784 / (miles * 0.01609344)


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
