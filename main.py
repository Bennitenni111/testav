from flask import Flask, jsonify, request

app = Flask(__name__)

# Hardcoded country code for demonstration purposes
HARDCODED_COUNTRY_CODE = "PK"

@app.route('/get_ip_info', methods=['GET'])
def get_ip_info():
    # Get the client's IP address
    client_ip = request.remote_addr

    # Create the JSON response
    ip_info = {"ip": client_ip, "country": HARDCODED_COUNTRY_CODE}

    return jsonify(ip_info)

if __name__ == '__main__':
    app.run(debug=True)
