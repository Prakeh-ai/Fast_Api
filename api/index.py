import json

# from flask import Flask, request, jsonify
# app = Flask(__name__)

#Load data once at startup

# with open('data.json', 'r') as f:
#     data = json.load(f) 

# marks_map = {item['name']: item['marks'] for item in data}

# @app.route('/api', methods=['GET'])
# def get_marks():
#     names = request.args.getlist('name')
#     marks = [marks_map.get(name, None) for name in names]
#     data = {
#         "marks": marks
#     }
#     print(marks)
#     # data = {
#     #     "marks": jsonify(marks)
#     # }
#     #return jsonify(marks)
#     return jsonify(data)

#for Vercel, ex[pose as 'handler' function]
def handler(request, response):
    # Load the data file (or cache it)
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    # Build name -> marks map
    marks_map = {item['name']: item['marks'] for item in data}
    
    # Extract 'name' query params
    query_params = request.query
    names = query_params.getlist('name')
    
    # Prepare response
    marks = [marks_map.get(name, None) for name in names]
    data = {
        "marks": marks
    }
    return response.json(data)

# if __name__ == "__main__":
#     app.run(debug=True)
