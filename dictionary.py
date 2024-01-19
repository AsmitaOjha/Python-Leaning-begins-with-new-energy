vehicles = {
    'dream': 'Honda 250T',
    'roadster':'BNW R1100',
    'virago':'Yamaha XV250',
    'jimny': 'suzuki jimny 1.5',
}
#iterating over the vehicles
my_car= vehicles['roadster']
print(my_car)
my_dream= vehicles.get("dream")
print(my_dream)
#adding items to dictionary
vehicles['toy']="Glider"
vehicles['starfigher']="Lockhead F-104"
#upgrading the value 
vehicles['toy']="Truck"
for key in vehicles:
    print(key, vehicles[key], sep=":")
print("*"*60)
#deleting items from dictionary
del vehicles["toy"]
vehicles.pop("dream")
for key in vehicles:
    print(key, vehicles[key], sep=":")