import requests
from bs4 import BeautifulSoup

def wework_init(keyword):
  job_lists = []
  WEWORK_URL = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"
  requests_for_wework = requests.get(WEWORK_URL).text
  soup_for_wework = BeautifulSoup(requests_for_wework, "html.parser")
  find_list = soup_for_wework.find(class_="jobs-container").find_all("li", class_="feature")
  for each_info in find_list:
    title = each_info.find(class_="title").string
    company = each_info.find(class_="company").string
    href_lists = each_info.find_all(["a", "href"])[1::2]

    for href_ready in href_lists:
      href_extracted = href_ready["href"]

    href = f"https://weworkremotely.com/{href_extracted}"

    job_dict = {
       "title" : title,
       "company" : company,
       "href" : href
     }
    job_lists.append(job_dict)

  print("Wework Remotely - Complete")
  return job_lists