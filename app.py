from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def portfolio():
    data = None
    if request.method == "POST":
        data = {
            "profile_url": request.form.get("profile_url"),
            "banner_url": request.form.get("banner_url"),
            "name": request.form.get("name"),
            "headline": request.form.get("headline"),
            "email": request.form.get("email"),
            "location": request.form.get("location"),
            # Splits comma-separated skills into a list for iteration in Jinja2
            "skills": request.form.get("skills", "").split(","),
            "experience_level": request.form.get("experience_level"),
            "short_bio": request.form.get("short_bio"),
            "date_of_joining": request.form.get("date_of_joining"),
        }
    return render_template("base.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)