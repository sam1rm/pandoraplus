from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/downloads/', methods=('GET', 'POST'))
def get_link():
    results = {}
    if request.method == "POST":
        client_json = request.json
        results['url'] = get_download_url
    return jsonify(dict=results)

def get_download_url(song_info_dict):
    return ""