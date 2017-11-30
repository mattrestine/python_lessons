# Prints a sentence in a centered "box" of correct width

sentence = input("Sentence: ")

# Preset variables

screen_width = 80
text_width   = len(sentence)
box_width    = text_width + 6
left_margin  = (screen_width - box_width) // 2 # non-floating number

# Display and Print

print()
print(' ' * left_margin + '+'   + '-' * (box_width - 2) +   '+')
print(' ' * left_margin + '|  ' + ' ' * text_width      + '  |')
print(' ' * left_margin + '|  ' +       sentence        + '  |')
print(' ' * left_margin + '|  ' + ' ' * text_width      + '  |')
print(' ' * left_margin + '+'   + '-' * (box_width - 2) +   '+')
print()

# Prompt user to exit program
input("Press 'Enter' to end program...")
