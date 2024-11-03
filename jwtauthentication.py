from flask import Flask, jsonify, request
import jwt
import datetime

app = Flask(__name__)

# Install the JWT library before running the script.
# pip3 install Flask PyJWT


# Secret key for encoding and decoding JWT
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Endpoint to generate JWT token
@app.route('/generate-token', methods=['POST'])
def generate_token():
    # Example data for JWT payload
    data = request.get_json()
    username = data.get('username')
    
    if not username:
        return jsonify({"message": "Username is required"}), 400

    # Set expiration time for the token (e.g., 30 minutes from now)
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)

    # Create payload with user info and expiration time
    payload = {
        'username': username,
        'exp': expiration_time
    }

    # Generate the JWT token
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    
    return jsonify({'token': token}), 200

# Endpoint to validate JWT token
@app.route('/validate-token', methods=['GET'])
def validate_token():
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({"message": "Token is missing"}), 400
    
    # Extract token from 'Bearer <token>' format if present
    try:
        token = token.split(" ")[1]
    except IndexError:
        return jsonify({"message": "Invalid token format"}), 400

    try:
        # Decode the JWT token
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({"message": "Token is valid", "user": decoded['username']}), 200

    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401

if __name__ == '__main__':
    app.run(debug=True)
