from flask import Flask, render_template
from data import get_cat, get_post, posts,get_replies,get_stats,date_format,sort_posts
from jinja2 import Environment, PackageLoader, select_autoescape
import datetime
app = Flask(__name__, template_folder="templates", static_url_path="/static")

env = Environment(
  loader=PackageLoader('app', 'templates'),
  autoescape=select_autoescape(['html', 'xml'])

)

@app.route('/')
def feed():
  the_list=sort_posts()
  render_template("feed_box.html")
  return render_template('feed.html', get_cat=get_cat,posts=the_list,get_replies=get_replies,get_stats=get_stats,date_format=date_format)

@app.route('/<string:name>')
def profile(name):
  cat=get_cat(name)
  posts=get_post(name)
  return render_template('profile.html',bio=cat,posts=posts,get_stats=get_stats,get_replies=get_replies,date_format=date_format,get_cat=get_cat)

if __name__ == "__main__":
    app.run(debug=True)