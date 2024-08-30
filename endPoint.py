from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sort-string', methods=['POST'])
def sort_string():
    data = request.json.get('data', '')
    array_of_characters = list(data)
    array_of_characters.sort()
    return jsonify({'word': array_of_characters})

if __name__ == '__main__':
    app.run(debug=True)