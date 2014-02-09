from flask import Flask, jsonify
app = Flask(__name__)
from download import scrap

@app.route('/', methods=('GET', 'POST'))
def index():
    return "No illegal activity will occur on this site."

@app.route('/downloads/', methods=('GET', 'POST'))
def get_link():
    results = {}
    print "test"
    print request.method
    print "test"
    if request.method == "POST":
        print request.json
        client_json = request.json
        results['url'] = scrap(client_json)
    return jsonify(dict=results)

if __name__ == '__main__':
    app.run()