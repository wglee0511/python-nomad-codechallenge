import os
import requests

def clear():
  os.system('clear')

def restart_for_online():
  yes_no_input = input("Do you want to start over? y/n  ")
  to_lower = yes_no_input.lower()
  if yes_no_input == "y":
    init()
  elif yes_no_input == "n":
    print("Okay, bye")
  else:
    print("That is not a valid response")
    restart_for_online()

def check_for_request(site):
  try:
    request_site = requests.get(f"{site}")
    request_number = request_site.status_code
    if request_number == 200:
      print(f"{site} is up")
    elif request_number != 200:
      print(f"{site} is down")
     
  except requests.ConnectionError:
    print(f"{site.replace('http://','')} is not URL.")


def check_online():
  site = input()
  site_list = site.split(",")
  for site_data in site_list:
    remove_space = site_data.strip()
    to_lower_data = remove_space.lower()
    find_for_http = "http://"
    is_exist = to_lower_data.find(find_for_http)
    if is_exist == -1:
      full_site = find_for_http + to_lower_data
      check_for_request(full_site)
    if is_exist != -1:
      check_for_request(to_lower_data)
  restart_for_online()
    
 

def welcome_print():
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs yon want to check. (separated by comma)")

def init():
  clear()
  welcome_print()
  check_online()

init()