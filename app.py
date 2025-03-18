from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Your full name
    full_name = "Your Full Name"  # Replace with your actual name

    # System username
    username = os.getlogin()

    # Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Top output
    top_output = subprocess.getoutput("top -n 1 -b")

    # Displaying the output
    response = f"""
    <h1>Name: {full_name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {server_time}</h3>
    <pre>TOP output:<br>{top_output}</pre>
    """
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
