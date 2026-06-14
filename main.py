from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import hashlib

app = Flask(__name__)
bootstrap = Bootstrap5(app)

profile = {
    "name": "Kaden Biondich",
    "title": "Software Developer",
    "email": "kbiondich7@gmail.com",
    "socials": [
        {"name": "GitHub", "url": "https://github.com/Widdershins-bash", "icon": "bi-github"},
        {"name": "LinkedIn", "url": "https://linkedin.com/in/kaden-biondich-274677364/", "icon": "bi-linkedin"},
    ],
}


@app.template_filter("gravatar")
def gravatar(email, size=200):
    digest = hashlib.md5(email.strip().lower().encode()).hexdigest()
    return f"https://www.gravatar.com/avatar/{digest}?s={size}&d=identicon"


games = [
    {
        "title": "Looping the Rooms",
        "url": "https://widdershins-bash.itch.io/looping-the-rooms",
        "tagline": "Can the knight escape his procedural prison?",
        "tech": "Built with pygame · No AI code used",
        "image": "https://img.itch.zone/aW1nLzI2MTU5MzYwLnBuZw==/105x83%23/QwqBSd.png",
    },
]


@app.route("/")
def home():
    return render_template("index.html", profile=profile, games=games)


if __name__ == "__main__":
    app.run(debug=True)
