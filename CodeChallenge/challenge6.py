import requests
from bs4 import BeautifulSoup
import csv

ALBA_FIRST_URL = "http://www.alba.co.kr/"
alba_main_requests = requests.get(f"{ALBA_FIRST_URL}").text

alba_main_soup = BeautifulSoup(alba_main_requests, 'html.parser')
alba_find_ul = alba_main_soup.find("div", id="MainSuperBrand")
alba_company_href_lists = alba_find_ul.find_all("a", class_="goodsBox-info")


def save_to_csv(company_name ,get_list):
  create_csv_file = open(f"{company_name}.csv", mode="w")
  write_csv = csv.writer(create_csv_file)
  write_csv.writerow(["place","title","time","pay","date"])
  for each_dict in get_list:
    write_csv.writerow(each_dict.values())

def extract_job(href):
  href_equests = requests.get(f"{href}").text
  href_soup = BeautifulSoup(href_equests, 'html.parser')

  company_name = href_soup.title.string.replace("채용정보 - 알바자리천국 알바천국(alba.co.kr)", "")
  try:
    get_tr_lists = href_soup.find("tbody").find_all("tr")

    get_list = []


    for get_tr_list in get_tr_lists[0::2]:
      get_place = get_tr_list.find("td", class_="local").get_text().replace("\xa0", " ")
      get_title = get_tr_list.find("span", class_="title").get_text()
      get_time = get_tr_list.find("td", class_="data").get_text()
      get_pay = get_tr_list.find("td", class_="pay").get_text()
      get_date = get_tr_list.find("td", class_="regDate last").get_text()

      get_each_dict = {
       "place" : get_place,
       "title" : get_title,
       "time" : get_time,
       "pay" : get_pay,
       "date" : get_date
      }
      get_list.append(get_each_dict)
    save_to_csv(company_name ,get_list)
  except:
    print(company_name)





for alba_href_list in alba_company_href_lists:
  alba_href = alba_href_list["href"]
  extract_job(alba_href)