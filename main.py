from flask import Flask,render_template,request
import requests

app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url=blog_url)
posts = response.json()
for x in posts:
    print(x["title"])
@app.route("/")

def home():
    return render_template("index.html", posts = posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods = ["GET","POST"])
def contact():
    if request.method == "POST":
        first_name = request.form["fname"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        return f"<h1>{first_name},{email},{phone},{message}</h1>"
    else:
        return render_template("contact.html")

@app.route("/<int:num>")
def post(num):
    return render_template("post.html", posts=posts, index=num)

@app.route("/form-entry", methods=["GET","POST"])
def receive_data():
    if request.method == "POST":
        first_name = request.form["fname"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        return f"<h1>{first_name},{email},{phone},{message}</h1>"







if __name__== "__main__":
    app.run(debug=True)