from flask import Flask
from flask import render_template
from flask import request
import os
from gptOutput import gpt_output

app = Flask(__name__)

@app.route('/', methods=['POST'])
# @app.route('/')
def index():
    # if (request.method ==  "POST"):
    #     pass
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template("result.html", text = gpt_output())


if __name__ == "__main__":
    app.run(host='localhost', port=int(os.getenv("PORT", "8080")), debug=True)


