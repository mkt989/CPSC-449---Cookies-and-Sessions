from flask import Flask, request, make_response
app = Flask(__name__)
@app.route('/')
def index():
    # Check if the client has a 'unique_id' cookie
    unique_id = request.cookies.get('unique_id')   
    if unique_id:
        id = int(request.cookies.get('id')) + 1   
        response = make_response(f"Hello! Your unique ID is: {unique_id} and counter is {id}")
        response.set_cookie('id',str(id))
        return response
    else:
        # Generate a new unique ID
        new_unique_id = str(uuid.uuid4())  
        # Create a response and set a 'unique_id' cookie
        response = make_response(f"Hello! Your unique ID is: {new_unique_id}")
        response.set_cookie('unique_id', new_unique_id)
        id = 1
        response.set_cookie('id',str(id))
        return response

if __name__ == '__main__':
    import uuid
    app.run()
