# Testing heroku deployment
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Review</h1>
    <p>It is currently {time}.</p>
    <label for="service">Choose a service:</label>
        <select name="service" id="st">
            <option value="scraping">scraping</option>
            <option value="download">Download</option>
        </select>
    <label for="platform">Choose a service:</label>
        <select name="platform" id="pf">
            <option value="Amazon">Amazon</option>
            <option value="Flipkart">Flipkart</option>
        </select>

    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)