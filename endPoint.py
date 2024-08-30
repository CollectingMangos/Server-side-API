from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/sort-string', methods=['POST'])
def sort_string():
    data = request.json.get('data', '')
    array_of_characters = list(data)
    array_of_characters.sort()
    return jsonify({'word': array_of_characters})

if _name_ == '_main_':
    app.run(debug=True)