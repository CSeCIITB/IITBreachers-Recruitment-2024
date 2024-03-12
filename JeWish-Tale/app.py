from flask import Flask, render_template, make_response, request, jsonify
import jwt

app = Flask(__name__)

# Secret key to sign the JWT token
SECRET_KEY = 'SECRET_KEY'
FLAG = "flag{Fake_Flag}"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        # Create the payload for the JWT token
        payload = {'username': 'guest', 'isAdmin': 0}
        
        # Encode the payload into a JWT token
        jwt_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        
        # Set the JWT token as a cookie
        response = make_response(render_template('index.html', message="Guest user logged in!"))
        response.set_cookie('auth', jwt_token)
        
        return response
    elif request.method == 'POST':
        # Get the JWT token from the POST request
        jwt_cookie = request.cookies.get('auth')
        
        if jwt_cookie:
            try:
                # Decode and verify the JWT token
                payload = jwt.decode(jwt_cookie, SECRET_KEY, algorithms=['HS256'])
                if(payload['isAdmin'] == 1):
                    response = make_response(render_template('index.html', message=FLAG))
                else:
                    response = make_response(render_template('index.html', message="Guest user logged in!"))
                response.set_cookie(jwt_cookie)
                return response
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Authentication Expired!'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid Auth Token!'}), 401
        else:
            return jsonify({'message': 'Authentication details missing!'}), 401

if __name__ == '__main__':
    app.run(debug=False, port=8000, host="0.0.0.0")
