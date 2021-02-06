import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]


app = Flask("DayEleven")

@app.route("/")
def init_home():
  
  return render_template("home.html")

@app.route("/read")
def init_read():
  keyword_lists = []
  check_lists = request.args.getlist("checkbox")
  reading_word = " ".join(check_lists)
  for each_keyword in check_lists:
    url = f"https://www.reddit.com/r/{each_keyword}/top/?t=month"

    keyword_for_requests = requests.get(url, headers = headers).text
    keyword_for_soup = BeautifulSoup(keyword_for_requests, 'html.parser')
    

    big_divs = keyword_for_soup.find(class_="rpBJOHq2PR60pnwJlUyP0").find_all(class_="_1oQyIsiPHYt6nx7VOmd1sz")

    for list_html in big_divs:
      title = list_html.find(class_="_eYtD2XCVieq6emjKBH3m").string
      url = list_html.a.get("href")
      try:
        upvotes = int(list_html.find(class_="_1rZYMD_4xY3gRcSS3p8ODO").string)
      except:
        upvotes = 0
      keyword = keyword_for_soup.find(class_="_2yYPPW47QxD4lFQTKpfpLQ").string


      keyword_dict = {
        "title" : title,
        "url" : url,
        "upvotes" : upvotes,
        "keyword" : keyword
      }
      keyword_lists.append(keyword_dict)
  sorted_lists = sorted(keyword_lists, key=lambda x:x["upvotes"], reverse=True)
  return render_template("read.html", keyword = reading_word, keyword_lists = sorted_lists)

app.run(host="0.0.0.0")