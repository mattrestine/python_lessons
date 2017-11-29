poll_responses = {}

poll_is_active = True

while poll_is_active:
    name = input("\nWhat is your name?")
    response = input("\nWhat car model do you prefer?")

    poll_responses[name] = response

    next_response = input("Would you like to let another person response? (yes/no)")
    if next_response == 'no':
        poll_is_active = False
print("\n ###### Poll Result ######")
for name, response in poll_responses.items():
    print("\t" + name + " voted: " + response + ".\n")