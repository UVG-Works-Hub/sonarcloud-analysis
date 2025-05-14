import os
import subprocess
import pickle
import base64
import hashlib
import random
import tempfile
import sqlite3
import re

# Error: Hardcoded credentials (Security Hotspot)
DATABASE_PASSWORD = "supersecretpassword123"
API_KEY = "sk_live_51HV7wXHJ8oKL6XpYs2d32s7TYSx"

# Error: Definite SQL Injection vulnerability (Security Issue)
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # CRITICAL: Direct SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

# Error: Definite Command Injection (Security Issue)
def execute_command(command):
    # CRITICAL: Direct command injection
    return os.system(command)

# Error: Insecure hash algorithm (Security Issue)
def hash_password(password):
    # Insecure hash algorithm (MD5)
    return hashlib.md5(password.encode()).hexdigest()

# Error: Insecure random (Security Issue)
def generate_token():
    # Using random instead of secure random for security token
    return str(random.randint(10000, 99999))

def read_file(file_path):
    try:
        # Error: Path traversal vulnerability (Security Issue)
        # Allows reading any file with ../ attacks
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None
    except Exception as e:
        # Error: Swallowing exception (Reliability Issue)
        pass

def save_user_data(user_id, data):
    # Error: Path traversal in file write (Security Issue)
    with open(f"user_{user_id}.dat", 'w') as file:
        file.write(data)

# Error: Definite deserialization vulnerability (Security Issue)
def load_user_preferences(data):
    # CRITICAL: Unsafe deserialization
    return pickle.loads(base64.b64decode(data))

def sanitize_html(user_input):
    # Error: Inadequate XSS protection (Security Issue)
    # Only removes <script> tags but leaves other XSS vectors
    return re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', user_input)

def get_user_input():
    user_input = input("Enter some text: ")
    
    # Error: SQL Injection (Security Issue)
    if user_input.startswith('user:'):
        username = user_input[5:]
        return get_user(username)
        
    # Error: Command Injection (Security Issue)
    elif user_input.startswith('run:'):
        command = user_input[4:]
        return execute_command(command)
        
    # Error: Code Injection (Security Issue)
    elif user_input.startswith('calc:'):
        result = eval(user_input[5:])  # CRITICAL: Code injection
        return str(result)
        
    return user_input

# Error: XSS vulnerability (Security Issue)
def generate_user_profile_html(user_data):
    # CRITICAL: Direct XSS vulnerability
    return f"<div class='profile'><h2>{user_data['name']}</h2><p>{user_data['bio']}</p></div>"

def process_data(data):
    if data is None:
        # Error: Null pointer dereference (Reliability Issue)
        return data.lower()  # Will cause exception when data is None
    
    processed_data = data.lower()
    return processed_data

# Error: Hard-coded IP address with commented password (Security Issue)
def connect_to_admin_panel():
    return subprocess.call("ssh admin@192.168.1.1", shell=True)  # password is admin123

# Error: LDAP Injection (Security Issue)
def ldap_search(username):
    # CRITICAL: LDAP injection vulnerability
    ldap_query = f"(uid={username})"
    # Simulate LDAP search
    return f"Searching with query: {ldap_query}"

def main():
    # Error: Command injection vulnerability (Security Issue)
    user_provided_path = input("Enter file path: ")
    os_command = f"ls {user_provided_path}"
    os.popen(os_command)
    
    # Error: XSS vulnerability (Security Issue)
    user_name = input("Enter your name: ")
    user_bio = input("Enter your bio: ")
    user_data = {"name": user_name, "bio": user_bio}
    html_output = generate_user_profile_html(user_data)
    
    # Error: Path traversal risk (Security Issue)
    data = read_file(user_provided_path)
    
    # Error: Storing unencrypted sensitive data (Security Issue)
    with open("credentials.txt", "w") as f:
        f.write(f"API_KEY={API_KEY}\nPASSWORD={DATABASE_PASSWORD}")
    
    # Error: CSRF vulnerability (Security Issue)
    def process_transfer(account_from, account_to, amount):
        # No CSRF token validation
        return f"Transferring {amount} from {account_from} to {account_to}"
    
    # Error: Insecure XML parsing (Security Issue)
    def parse_xml(xml_string):
        # Vulnerable to XXE attacks
        import xml.dom.minidom
        return xml.dom.minidom.parseString(xml_string)

# Error: Backdoor access (Security Issue)
def debug_backdoor(secret_code):
    if secret_code == "backdoor123":
        return os.system("sh -i")  # Give shell access
    return False

# Error: Hard-coded JWTs (Security Issue)
JWT_SECRET = "my_super_secret_jwt_key_do_not_share"

if __name__ == "__main__":
    main()