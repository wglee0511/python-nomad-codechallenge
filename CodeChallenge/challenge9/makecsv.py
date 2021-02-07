import csv

def csv_init(jobs):
  file = open("jobs.csv", mode = "w")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "link"])
  for job in jobs:
   writer.writerow(list(job.values())) 

  return