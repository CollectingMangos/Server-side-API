from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def sort():
    string_data = request.json.get('data', '')
    
    if not string_data:
        return jsonify({'error':'if you see this, your string cannot be empty'}), 400
    
    array_of_characters = list(string_data)
    array_of_characters.sort()
    
    return jsonify({'word': array_of_characters})


# Uncomment the below if you want to run tests locally 
if __name__ == '__main__':
    app.run(debug=True)
