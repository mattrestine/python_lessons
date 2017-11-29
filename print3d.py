unprinted_designs = ['iPhone Case', 'Robot Pendant', 'Dodecahedron']
completed_models = []

while unprinted_designs:
    current_print = unprinted_designs.pop()
    print("Currently printing: " + current_print)
    completed_models.append(current_print)
print("\nThe following designs has been printed into a model:")
for model in completed_models:
    print(model)
