carBrand = input("Insert car brand: ")
carModel = input("Insert car model: ")

#print(f'Car brand is "{carBrand}" and the model is \'{carModel}\'')

print("Car", "brand", "is", '"'+carBrand+'"', sep=' ', end=' ')
print("and", "the", "model", "is", "'"+carModel+"'.", sep=' ')
print(f"Program ending.")