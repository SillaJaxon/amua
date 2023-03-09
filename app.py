# Define a function to get user input
def get_input(prompt):
    return input(prompt + '\n> ')

# Get the decision from the user
decision = get_input('What decision do you need to make?')

# Get a list of options from the user
options = []
while True:
    option = get_input('Enter an option (or enter nothing to stop):')
    if option == '':
        break
    options.append(option)

# Get a list of reasons for each option from the user
option_reasons = {}
for option in options:
    reasons = []
    while True:
        reason = get_input(f'Enter a reason for "{option}" (or enter nothing to stop):')
        if reason == '':
            break
        reasons.append(reason)
    option_reasons[option] = reasons

# Count the number of reasons for each option
option_counts = {option: len(reasons) for option, reasons in option_reasons.items()}

# Print the option with the most reasons
max_option = max(option_counts, key=option_counts.get)
print(f'The recommended option is "{max_option}" with {option_counts[max_option]} reasons.')
