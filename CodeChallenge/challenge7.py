import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {
  "popular": [],
  "new" : []
}

app = Flask("DayNine")



@app.route("/<id>")
def detail(id):
  db_for_comments = []
  requests_for_article = requests.get(make_detail_url(id)).json()
  article_title = requests_for_article["title"]
  article_author = requests_for_article["author"]
  article_url = requests_for_article["url"]
  article_points = requests_for_article["points"]
  dict_for_article = {
    "title" : article_title,
    "author" : article_author,
    "url" : article_url,
    "points" : article_points
  }
  
  list_for_comments = requests_for_article.get("children")
  for list_comment in list_for_comments:
   if list_comment["text"] != None:
     dict_for_comments = {
      "author": list_comment["author"],
      "text": list_comment["text"].replace("<p>", "").replace("</p>", "").replace("&lt;", "").replace("&gt;", "").replace("&quot;", "").replace("&#x27;", "")
     }
     db_for_comments.append(dict_for_comments)
   elif list_comment["text"] == None:
     dict_for_comments = {
      "author": list_comment["author"],
      "text": list_comment["text"]
      }
     db_for_comments.append(dict_for_comments)
  
  
  return render_template("detail.html", article_info = dict_for_article, comments_info=db_for_comments)
  
  

@app.route("/")
@app.route("/popular")
def index():
  index_requests = requests.get(popular).json()
  hits_lists = index_requests["hits"]

  for hit in hits_lists:
    object_titile = hit.get("title")
    object_url = hit.get("url")
    object_points = hit.get("points")
    object_id = hit.get("objectID")
    object_author = hit.get("author")
    object_comments = hit.get("num_comments")
    dict_for_popular = {
     "title" : object_titile,
     "url" : object_url,
     "points" : object_points,
     "id" : object_id,
     "author" : object_author,
     "comments" : object_comments
    }
    db["popular"].append(dict_for_popular)
  return render_template("index.html", popular_lists = db["popular"])


@app.route("/new")
def index_new():
  index_requests = requests.get(new).json()
  hits_lists = index_requests["hits"]

  for hit in hits_lists:
    object_titile = hit.get("title")
    object_url = hit.get("url")
    object_points = hit.get("points")
    object_id = hit.get("objectID")
    object_author = hit.get("author")
    object_comments = hit.get("num_comments")
    dict_for_new = {
     "title" : object_titile,
     "url" : object_url,
     "points" : object_points,
     "id" : object_id,
     "author" : object_author,
     "comments" : object_comments
    }
    db["new"].append(dict_for_new)

  return render_template("new.html", new_lists = db["new"])

app.run(host='0.0.0.0', port=5000, debug=True)