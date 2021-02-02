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

select_convert_list = []

def convert_currency(code_list, full_list):
  print(f"How many {code_list[0]} do you want to convert to {code_list[1]}")
  amount = input(": ")
  amount_to_int = float(amount)
  
  site=f"https://transferwise.com/gb/currency-converter/{code_list[0]}-to-{code_list[1]}-rate?amount={amount_to_int}"
  
  requests_for_currency = requests.get(site).text
  soup_for_currency = BeautifulSoup(requests_for_currency, 'html.parser')
  currency = float(soup_for_currency.find("span", class_="text-success").string)

  convert_value = amount_to_int * currency

  print(f"{code_list[0]} {amount_to_int} equal to {code_list[1]} {convert_value}")

  select_convert_list = []
  print("Where are you from? Choose a country by number?")
  select_number(full_list)


def select_for_convert(full_list):
  print("Now choose another country.")
  second_query = input("#: ")
  transfer_to_int = int(second_query)
  convert_for_country = full_list[transfer_to_int][0]
  convert_for_code = full_list[transfer_to_int][2]
  print(convert_for_country)
  select_convert_list.append(convert_for_code)
  convert_currency(select_convert_list,full_list)

def select_number(full_list):
  first_query = input("#: ")
  try:
    transfer_to_int = int(first_query)
    if transfer_to_int > 264:
      print("Choose a number from list.")
      select_number(full_list)
    else:
      print(f"{full_list[transfer_to_int][0]}")
      select_convert_list.append(full_list[transfer_to_int][2])
      select_for_convert(full_list)
  except:
    print("That wasn't a number.")
    select_number(full_list)

def shoot_the_list(full_list):
  for index, value in enumerate(full_list):
    print(f"# {index} {value[0]}")
  print("Where are you from? Choose a country by number?")
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
  setting_country_list()

init()
