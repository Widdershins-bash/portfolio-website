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


@app.route("/")
def home():
    return render_template("index.html", profile=profile)


if __name__ == "__main__":
    app.run(debug=True)
