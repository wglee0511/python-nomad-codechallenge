import requests
from bs4 import BeautifulSoup

URL = "https://www.iban.com/currency-codes"

requests_for_url = requests.get(f"{URL}")
soup_for_url = BeautifulSoup(requests_for_url.text, 'html.parser')
find_to_tr = soup_for_url.table
find_to_tds = find_to_tr.find_all("td")
list_for_every_words = []
list_for_country = []
n = 4

def select_number(full_list):
  first_query = input("#: ")
  transfer_to_int = int(first_query)
  try:
    if transfer_to_int > 264:
      print("Choose a number from list.")
      select_number(full_list)
    else:
      print(f"You chose {full_list[transfer_to_int][0]}")
      print(f"The currency code is {full_list[transfer_to_int][2]}")
      select_number(full_list)
  except:
    print("That wasn't a number.")
    select_number(full_list)

def shoot_the_list(full_list):
  for index, value in enumerate(full_list):
    print(f"# {index} {value[0]}")
  select_number(full_list)


def setting_country_list():
  for find_to_td in find_to_tds:
    each_table = find_to_td.string
    list_for_every_words.append(each_table)
  each_lists = [list_for_every_words[i * n:(i + 1) * n] for i in range((len(list_for_every_words) - 1 + n) // n )]
  
  for country_list in each_lists:
    if country_list[1] != "No universal currency":
      list_for_country.append(country_list)
  shoot_the_list(list_for_country)


def init():
  print("Hello Please choose select a country by number:")
  setting_country_list()

init()
