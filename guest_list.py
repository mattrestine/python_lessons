guest_list = ["Jesus", "Albert Einstein", "Biological Mother"]
inviation = ", You have been invited to enjoy outdoors bbq feast with Matthew."
print(guest_list[0] + inviation)
print(guest_list[1] + inviation)
print(guest_list[2] + inviation)
print("\n")
print(guest_list[1] + ", could not make it to the feast.")
guest_list[1] = "Neil DeGrasse Tyson"
print(guest_list[0] + inviation)
print(guest_list[1] + inviation)
print(guest_list[2] + inviation)
print("\n")
guest_list.insert(0, "Abraham Lincoln")
guest_list.insert(2, "Martin Luther King Jr.")
guest_list.append("Thomas Hopkins Gallaudet")
print("\n")
print(guest_list[0] + inviation)
print(guest_list[1] + inviation)
print(guest_list[2] + inviation)
print(guest_list[3] + inviation)
print(guest_list[4] + inviation)
print(guest_list[5] + inviation)
print("\n")
print("I was recently informated that I could only invite 2 people.")
print("Kinda douchy I know...")
print(guest_list.pop(0) + ", Sorry for the inconvence.")
print(guest_list.pop(1) + ", Sorry for the inconvence.")
print(guest_list.pop(1) + ", Sorry for the inconvence.")
print(guest_list.pop(2) + ", Sorry for the inconvence.")
print("\n")
print(guest_list[0] + inviation)
print(guest_list[1] + inviation)
print("\n")
del guest_list[0]
del guest_list[0]
print(guest_list)
print("\n\t### Number of Guests Invited: " + str(len(guest_list)) + " ###")