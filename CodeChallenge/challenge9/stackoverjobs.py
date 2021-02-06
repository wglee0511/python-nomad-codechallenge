import requests
from bs4 import BeautifulSoup


def get_job(last_number, STACK_OVER_URL):
  job_list_stack = []
  for page in range(last_number):
   EACH_URL = f"{STACK_OVER_URL}&pg={page}"
   requests_for_stack = requests.get(EACH_URL).text
   soup_for_stack = BeautifulSoup(requests_for_stack, "html.parser")
   find_lists = soup_for_stack.find(class_="listResults").find_all(class_="fl1")
   for each_list in find_lists:
     title = each_list.a.string
     try:
      company = each_list.find(class_="fc-black-700").span.string.strip()
     except:
      company = "None"
     href = f"https://stackoverflow.com{each_list.a['href']}"

     job_dict = {
       "title" : title,
       "company" : company,
       "href" : href
     }
     job_list_stack.append(job_dict)
  print("Stack Over Flow - Complete")
  return job_list_stack





def stack_over_init(keyword):
  STACK_OVER_URL = f"https://stackoverflow.com/jobs?r=true&q={keyword}"
  requests_for_stack = requests.get(STACK_OVER_URL).text
  soup_for_stack = BeautifulSoup(requests_for_stack, "html.parser")
  find_pagination = soup_for_stack.find(class_="s-pagination").find_all("span")
  last_number = find_pagination[-2].string
  convert_to_int = int(last_number)
  get_job(convert_to_int,STACK_OVER_URL)

 