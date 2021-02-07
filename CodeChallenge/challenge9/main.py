"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
from stackoverjobs import stack_over_init
from weworkremotely import wework_init
from remoteok import remoteok_init
from flask import Flask, render_template, request, redirect, send_file
from makecsv import csv_init



"""

"""

app = Flask("Job Scrapping")

db = {}

@app.route("/export")
def export_csv():
  try:
    word = request.args.get("word")
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    csv_init(jobs)
    return send_file("jobs.csv")
  except:
    return redirect("/")

@app.route("/page")
def page():
  try:
    keyword_for_getting_jobs = request.args.get("keyword").lower()
    find_exist_job = db.get(keyword_for_getting_jobs)
    if find_exist_job:
      jobs = find_exist_job
    else:
    
      stack_jobs = stack_over_init(keyword_for_getting_jobs)
      wework_jobs = wework_init(keyword_for_getting_jobs)
      remote_jobs = remoteok_init(keyword_for_getting_jobs)
      jobs = stack_jobs + wework_jobs + remote_jobs
      
      db[keyword_for_getting_jobs] = jobs

    total_job = len(jobs)

  except:
    print("Error")
  
  return render_template("page.html", total_job = total_job, keyword=keyword_for_getting_jobs, job_list = jobs)


@app.route("/")
def page_init():
  return render_template("home.html")




app.run(host='0.0.0.0', port=5000, debug=True)


