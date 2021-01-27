"""
Again, the code is broken, you need to create 4 functions.
  - add_to_dict: Add a word to a dict.
  - get_from_dict: Get a word from inside a dict.
  - update_word: Update a word inside of the dict.
  - delete_from_dict: Delete a word from the dict.

All this functions should check for errors, follow the comments to see all cases you need to cover.

There should be NO ERRORS from Python in the console.
"""

def add_to_dict(add_dict, add_key, add_value="none"):
  if type(add_dict) is str:
    print(f"You need to send a dictionary. You sent : {type(add_dict)}")
  elif add_value == "none":
    print(f"You need to send a word and a definiton.")
  elif add_value != "none":
    if (add_key in add_dict) == False:
      add_dict[add_key]=add_value
      print(f"{add_key} has been added.")
    elif (add_key in add_dict) == True:
      print(f"{add_key} is already on the dictionary. Won't add.")

def get_from_dict(get_dict, get_key="none"):
  if type(get_dict) is str:
    print(f"You need to send a dictionary. You sent : {type(get_dict)}")
  elif get_key == "none":
    print("You need to send ad word to search for.")
  elif (get_key in get_dict) == False:
    print(f"{get_key} was not found in this dict.")
  elif (get_key in get_dict) == True:
    print(f"{get_key} : {get_dict[get_key]}")

def update_word(update_dict, update_key, update_value="none"):
  if type(update_dict) is str:
    print(f"You need to send a dictionary. You sent : {type(update_dict)}")
  elif update_value == "none":
    print(f"You need to send a word and a definiton.")
  elif update_value != "none":
    if (update_key in update_dict) == True:
      update_dict[update_key] = update_value
      print(f"{update_key} has been updated to : {update_value}")
    elif (update_key in update_dict) == False:
      print(f"{update_key} is not on the dict. Can't update non-existing word.")

def delete_from_dict(delete_dict, delete_key="none"):
  if type(delete_dict) is str:
    print(f"You need to send a dictionary. You sent : {type(delete_dict)}")
  elif delete_key == "none":
    print(f"You need to specify a word to delete")
  elif delete_key != "none":
    if (delete_key in delete_dict) == True:
      del delete_dict[delete_key]
      print(f"{delete_key} has been deleted.")
    elif (delete_key in delete_dict) == False:
      print(f"{delete_key} is not in this dict. Won't delete")
  

# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\