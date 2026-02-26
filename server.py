from flask import Flask, render_template
import random
import datetime
import requests



app=Flask(__name__)

# @app.route("/")
# def home():
#     random_number = random.randint(1, 10)
#     current_year=datetime.datetime.now().year
#     return  render_template("index.html", num=random_number, current_year=current_year)

@app.route("/guess/<name>")
def guess_age(name):
    response_age=requests.get(f"https://api.agify.io?name={name}")
    response_gender=requests.get(f"https://api.genderize.io?name={name}")

    age=response_age.json()['age']
    gender=response_gender.json()['gender']

    return  render_template("index.html", age=age, gender=gender, name=name)
@app.route("/blog")
def blog():
    blog_url="https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts=response.json()
    return render_template("blog.html", posts=all_posts)



if __name__=="__main__":
    app.run(debug=True)