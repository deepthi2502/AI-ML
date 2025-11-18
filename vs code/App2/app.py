from flask import Flask, render_template, request

app = Flask(_name_)

@app.route("/", methods=["GET", "POST"])
def classify():
    result = ""
    if request.method == "POST":
        email = request.form["email"].lower()
        spam_words= ["win", "offer", "free", "lottery", "click", "money", "urgent"]
        if any(word in email for word in spam_words):
            result = "🚨 Spam Email Detected!"
        else:
            result = "✅ Not Spam (Safe Email)"
    return render_template("index.html", result=result)

if _name_ == "_main_":
    app.run(debug=True)