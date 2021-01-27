import datetime
member = [
  {
    "name":"Tray",
    "handle":"BigT",
    "favorite food":"donuts",
    "age":2,
    "intro": "The hardest thing in the world is to get up from bed."
  },
  {
    "name":"Jippy",
    "handle":"Jip",
    "favorite food":"Apple",
    "age":6,
    "intro": "An apple a day keep the dogtor away."
  },
  {
    "name":"Cloud",
    "handle":"CC",
    "favorite food":"Cake",
    "age":3,
    "intro": "I can always eat."
  },
  {
    "name":"Haha",
    "handle":"HHHH",
    "favorite food":"Lime",
    "age":5,
    "intro": "You are a bore."
  },
  {
    "name":"Juice",
    "handle":"Juice",
    "favorite food":"Chicken",
    "age":2,
    "intro": "Don't mess with me."
  }
]

posts=[
  {
    "name":"Tray",
    "post":["Today was a nice day.", "I ate an apple today."],
    "likes":[2,3]
  },
  {
    "name":"Jippy",
    "post":["I ate my dad's ceral today.","Is he mad at me?"],
    "likes":[1,4],
  },
  {
    "name":"Juice",
    "post":["Can't live without juice!", "Hey where did my juice go?"],
    "likes":[3,2],
  },
  {
    "name":"Haha",
    "post":["Imagine a dog with an unbrella on his head!", "Can someone laugh at my joke please?"],
    "likes":[2,3],
  },
  {
    "name":"Cloud",
    "post":["Time to get some sleep!","What y'all doing?"],
    "likes":[5,0],
  }
]

post=[
  {
    "author":"Tray",
    "post":"Today was a nice day.",
    "reply":["Yep.","Agree."],
    "responder":["Cloud","Juice"],
    "time": "09 21 2020"
  },
  {
    "author":"Tray",
    "post":"I ate an apple today.",
    "reply":["Good","Awesome","Great"],
    "responder":["Cloud","Haha","Jippy"],
    "time":"04 02 2020"
  },
  {
    "author":"Jippy",
    "post": "I ate my dad's ceral today.",
    "reply": ["Yep","Agree","So what?","ok","Hmm"],
    "responder": ["Juice","Jippy","Cloud","Tray","Tray"],
    "time":"08 22 2020"
  },
  {
    "author":"Jippy",
    "post": "Is he mad at me?",
    "reply": ["He is."],
    "responder": ["Tray"],
    "time":"09 12 2020"
  },
  {
    "author":"Juice",
    "post": "Can't live without juice!",
    "reply": ["Yep","Agree","So what?","ok"],
    "responder": ["Juice","Tray","Jippy","Cloud"],
    "time":"04 29 2020"
  },
  {
    "author":"Juice",
    "post": "Hey where did my juice go?",
    "reply": ["Hmm","Jesus","What?","Are you kidding me?"],
    "responder": ["Cloud","Jippy","juice","Tray","Cloud"],
    "time":"07 02 2020"
  },
  {
    "author":"Haha",
    "post": "Imagine a dog with an unbrella on his head!",
    "reply": ["Yep","Agree","So what?","ok"],
    "responder": ["Tray","Jippy","Cloud","Juice"],
    "time":"02 04 2020"
  },
  {
    "author":"Haha",
    "post": "Can someone laugh at my joke please?",
    "reply": ["Hmm","Jesus","Are you ok?"],
    "responder": ["Haha","Tray","Cloud"],
    "time":"08 30 2020"
  },
  {
    "author":"Cloud",
    "post": "Time to get some sleep!",
    "reply": ["Yep","Agree","So what?","ok","Hmm"],
    "responder": ["Tray","Tray","Juice","Jippy","Cloud"],
    "time":"11 21 2020"
  },
  {
    "author":"Cloud",
    "post": "What y'all doing?",
    "reply": ["Nothing"],
    "responder": ["Tray"],
    "time":"11 22 2020"
  }
]

# my_dates = ['11 21 2020', '11 22 2020', '02 04 2020', '04 29 2020']
# my_dates.sort(key=lambda date: datetime.datetime.strptime(date, '%m %d %Y'),reverse=True)
# print(my_dates)

# obtain likes
def get_stats(post):
  for section in posts:
    ind=0
    for item in section["post"]:
      if item==post:
        return section["likes"][ind]
      ind+=1

# for displaying date
def date_format(value, format='medium'):
  date_obj = datetime.datetime.strptime(value, '%m %d %Y')
  if format == 'full':
    return date_obj.strftime("%m/%d/%Y")
  elif format == 'medium':
    return date_obj.strftime("%b %d %Y")      

# uses a name to return a cat's info
def get_cat(input):
  for cat in member:
    if cat['name'] == input:
      return cat
  return None

# obtains all posts from a specific user
def get_post(name): 
  list = []
  sorted_posts=[]
  for section in post:
    if section["author"]==name:
      list.append(section['time'])
  list.sort(key=lambda date: datetime.datetime.strptime(date, '%m %d %Y'),reverse=True)
  for item in list:
    for part in post:
      if part['time']==item:
        sorted_posts.append(part)
  return sorted_posts

# sort all posts by date
def sort_posts():
  list=[]
  sorted_posts=[]
  for section in post:
    list.append(section["time"])
  list.sort(key=lambda date: datetime.datetime.strptime(date, '%m %d %Y'),reverse=True)
  for item in list:
    for part in post:
      if part['time']==item:
        sorted_posts.append(part)
  return sorted_posts


# rtr=sort_posts()
# for item in rtr:
#   print(item)

# obtains replies and responders from each post
def get_replies(item):
  for section in post:
    if section['post']==item:
      return section['reply'],section['responder'],section['time']


#member_replies= [
#   {
#     "name":"Tray",
#     "post":[["I ate my dad's cereal today."],["Can't live without juice!"]],
#     "reply":[["Agree"],["Yep"]]
#   },
#   {
#     "name":"Haha",
#     "post":[["Time to get some sleep!"],["Can someone laugh at my joke please?"]],
#     "reply":[["Jesus"],["ok"]]
#   },
#   {
#     "name":"Jippy",
#     "post":[["Imagine a dog with an unbrella on his head!"],["Hey where did my juice go?"]],
#     "reply":[["So what?"],["Hmm"]]
#   },
#   {
#     "name":"Juice",
#     "post":[["Imagine a dog with an unbrella on his head!"],["I ate an apple today."]],
#     "reply":[["Are you ok?"],["Wow."]]
#   },
#   {
#     "name":"Cloud",
#     "post":[["Can't live without juice!"],["I ate my dad's ceral today."]],
#     "reply":[["Hmm"],["Jesus"]]
#   }

# ]