from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

def compress(html=None): 
    pass 

@app.route("/")
def index(): 
    return "<pre>Use /api/ as the API endpoint for POST requests.</pre>"

@app.route("/api/", methods=['GET', 'POST']) 
def api():
    data = {} 
    if request.method == "GET": 
        return redirect("/", code=302) 
    else:
        try:
            data = request.values.to_dict()
            data["status"] = "up"
        except:
            data["status"] = "down"

        return jsonify(data)
        # return jsonify(data)

if __name__ == "__main__": 
    app.run(port=8000, debug=True)