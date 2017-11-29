# Sydney New Zealand Japan Alaska Amazon River
places = ["Australia", "New Zealand", "Japan", "Alaska", "Amazon River"]
print("\n\t### Places List ###")
print("Python Raw List: " + str(places))
# sorted()
print("\t### Sorted List - sorted(arg) ###")
print("Sorted List: " + str(sorted(places)))
# sorted(reverse=True)
print("\t### Sorted Reverse List - sorted(arg, reverse=True) ###")
print("Sorted Reverse: " + str(sorted(places, reverse=True)))
# reverse()
print("\t### Reverse List - .reverse() ###")
places.reverse()
print("Reverse List (1/2): " + str(places))
places.reverse()
print("Reverse List (2/2): " + str(places))
# sort()
print("\t### Sort List - .sort() ###")
places.sort()
print("Sort List: " + str(places))
# sort(reverse=True)
print("\t### Sort Reverse List - .sort(reverse=True) ###")
places.sort(reverse=True)
print("Sort Reverse List: " + str(places))