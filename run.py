from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    return "No illegal activity will occur on this site."

@app.route('/downloads/', methods=('GET', 'POST'))
def get_link():
    results = {}
    if request.method == "GET":
        client_json = request.json
        results['url'] = get_download_url(client_json)
    return jsonify(dict=results)

def get_download_url(song_info_dict):
    return ""

if __name__ == '__main__':
    app.run()