# Define your functions
def coffee_bot():
  print('Welcome to the cafe! ')
  size = get_size()
  drink_type = get_drink_type()
  print('Alright, that\'s a {} {}!'.format(size, drink_type))
  name = input('Can I get your name please? \n')
  print('Thanks, {}! Your drink will be ready shortly.'.format(name))

def print_message():
  print("I'm sorry. I did not understand your selection. Please enter the corresponding letter for  your response.")

def get_size():
  res = input('What size drink can I get for you? \n[A] Small \n [B] Medium \n [C] Large \n')
  if res == 'A':
    return 'Small'
  elif res == 'B':
    return 'Medium'
  elif res == 'C':
    return 'Large'
  else:
    print_message()
    return get_size()

def get_drink_type():
  res = input('What type of drink would you like? \n[A] Brewed Coffee \n [B] Mocha \n [C] Latte \n')
  if res == 'A':
    return 'Brewed Coffee'
  elif res == 'B':
    return 'Mocha'
  elif res == 'C':
    return ordered_latte()
  else:
    print_message()
    return get_drink_type()

def ordered_latte():
  res = input('What kind of milk for your latte? \n[A] 2% Milk \n [B] Non-fat Milk \n [C] Soy Milk \n')
  if res == 'A':
    return 'Latte with 2% milk'
  elif res == 'B':
    return 'non-fat Latte'
  elif res == 'C':
    return 'Soy Latte'
  else:
    print_message()
    return ordered_latte()


# Call coffee_bot()!
coffee_bot()
