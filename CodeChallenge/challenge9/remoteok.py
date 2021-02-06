import requests
from bs4 import BeautifulSoup

def remoteok_init(keyword):
  job_list = []
  REMOTEOK_URL = f"https://remoteok.io/remote-dev+{keyword}-jobs"
  requests_for_remo = requests.get(REMOTEOK_URL, headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}).text
  soup_for_remo = BeautifulSoup(requests_for_remo, "html.parser")
  tr_list = soup_for_remo.find_all(class_="company_and_position_mobile")
  for each_info in tr_list:
    try:
      title = each_info.a.h2.get_text()
      company = each_info.h3.get_text()
      href = f'https://remoteok.io{each_info.a["href"]}'
    except:
      title = "None"
      company = "None"
      href = "None"

    job_dict = {
       "title" : title,
       "company" : company,
       "href" : href
    }
    job_list.append(job_dict) 
  print("Remote OK - Complete")
  return job_list