from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def sort_string():
    data = request.json.get('data', '')
    
    if not data:
        return jsonify({'error':'the string cannot be empty'})

    array_of_characters = list(data)
    array_of_characters.sort()
    return jsonify({'word': array_of_characters})

if __name__ == '__main__':
    app.run(debug=True)