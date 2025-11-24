print("-------Fuel Cost Estimator----------")
#distance travelled in trip
distance=(float(input("enter the distance(km) travelled by the vehicle:")))
print("the distance travelled is",distance)
#mileage of the vehicle
mileage=(float(input("enter the mileage of the vehicle(km/l):")))
print("the mileage is ",mileage)
#fuel type of the vehicle
fuel=input("enter the fuel needed of the vehicle=")
#fuel price of the vehicle
fuel_price=(float(input("enter the feul price of ",fuel,":")))
print(f"the feul price of",fuel,fuel_price)
fuel_needed=distance/mileage
print("the fuel needed for the trip is",fuel_needed)
total_cost=fuel_needed*fuel_price
print("the fuel cost is",total_cost)
print("Save Earth Save Fuel!")
