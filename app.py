from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/home')
def show_home():
    """show the madlib form"""

    return render_template("home.html", words=story.prompts)

@app.route('/madlib', methods=['GET'])
def show_story():
    """show the story of the madlib"""

    text = story.generate(request.args)

    return render_template("madlib.html", text=text)