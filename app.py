from flask import Flask, render_template
from data import get_cat,date_format,get_members,find_post,sort_find,organized_ten
# from jinja2 import Environment, PackageLoader, select_autoescape
import datetime

app = Flask(__name__, template_folder="templates", static_url_path="/static")

# env = Environment(
#   loader=PackageLoader('app', 'templates'),
#   autoescape=select_autoescape(['html', 'xml'])
# )


@app.route('/')
def feed(): # shows only ten recent posts
  render_template("feed_box.html")
  return render_template('feed.html', get_cat=get_cat,posts=organized_ten,date_format=date_format)

@app.route('/<string:name>')
def profile(name):
  cat=get_cat(name)
  posts=find_post(name)
  return render_template('profile.html',bio=cat,posts=posts,date_format=date_format,get_cat=get_cat)


@app.route('/member')
def member():
  members=get_members()
  return render_template('member.html',get_cat=get_cat,members=members)

if __name__ == "__main__":
    app.run(debug=True)