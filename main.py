import os
import subprocess
import time
import pickle
import random
import tempfile
import base64
import hashlib

# Error: Hardcoded credentials (Security Hotspot)
DATABASE_PASSWORD = "supersecretpassword123"
API_KEY = "sk_live_51HV7wXHJ8oKL6XpYs2d32s7TYSx"
JWT_SECRET = "my-super-secret-jwt-token-that-is-very-long-and-should-never-be-in-code"

# Error: Insecure hash algorithm (Security Issue)
def hash_password(password):
    # Insecure hash algorithm (MD5)
    return hashlib.md5(password.encode()).hexdigest()

def read_file(file_path):
    try:
        # Error: Path traversal vulnerability (Security Issue)
        # Allows reading any file with ../ attacks
        with open(file_path, 'r') as file:
            data = file.read()
            line_count = len(data.split('\n'))
        return data
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")
        return None
    except Exception as e:
        # Error: Swallowing exception (Reliability Issue)
        pass

def write_file(file_path, data):
    # Error: Path traversal for writing files (Security Issue)
    with open(file_path, 'w') as file:
        file.write(data)

def unsafe_deserialization(serialized_data):
    # Error: Unsafe deserialization (Critical Security Issue)
    return pickle.loads(base64.b64decode(serialized_data))

def get_user_input():
    user_input = input("Enter some text: ")
    
    # Error: SQL Injection vulnerability (Critical Security Issue)
    if user_input.startswith('user:'):
        username = user_input[5:]
        query = "SELECT * FROM users WHERE username = '" + username + "'"
        # Execute raw query with user input
        
    # Error: Command Injection (Critical Security Issue)
    elif user_input.startswith('run:'):
        command = user_input[4:]
        os.system(command)
        
    # Error: Code Injection (Critical Security Issue)
    elif user_input.startswith('calc:'):
        result = eval(user_input[5:])
        return str(result)
        
    return user_input

def process_data(data):
    # Error: Null pointer dereference (Reliability Issue)
    if random.randint(1, 10) > 5:
        data = None
    
    # This will cause NullPointerException randomly
    processed_data = data.lower()
    
    # Error: Resource leak (Reliability Issue)
    temp_file = open("temp_processing.txt", "w")
    temp_file.write(processed_data)
    # Missing close
    
    return processed_data

def insecure_random():
    # Error: Insecure random number generation (Security Issue)
    return random.randint(1, 6)  # For security purposes like token generation

def main():
    # Error: Insecure temporary file creation (Security Issue)
    temp_dir = tempfile.mkdtemp()
    file_path = temp_dir + "/example.txt"
    
    # Error: Command injection vulnerability (Security Issue)
    user_provided_path = input("Enter file path: ")
    os_command = "ls " + user_provided_path
    os.popen(os_command)
    
    # Error: Potential file path injection
    data = read_file(user_provided_path)
    
    # Error: Unchecked error condition (Reliability Issue)
    if data is None:
        # should return but doesn't, continues execution with None
        print("Warning: No data found")
    
    # Error: Null pointer dereference risk (Reliability Issue)
    processed_data = process_data(data)
    print(f"Processed Data: {processed_data}")
    
    # Error: XSS vulnerability in a web context (Security Issue)
    html_output = "<div>" + get_user_input() + "</div>"
    
    # Error: Insecure cipher (Security Issue)
    def encrypt(text, key):
        # Extremely insecure XOR "encryption"
        return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
    
    # Error: Storing sensitive data (Security Issue)
    encrypted_password = encrypt(DATABASE_PASSWORD, "key")
    with open("secret.dat", "w") as f:
        f.write(encrypted_password)
    
    # Error: Unreleased resource (Reliability Issue)
    f = open("output.log", "w")
    f.write("Operation completed")
    # Missing f.close()
    
    # Error: Unvalidated redirect (Security Issue)
    redirect_url = get_user_input()
    # redirect_to(redirect_url)  # Commented to avoid syntax error
    
    # Error: Integer overflow risk (Reliability Issue)
    big_calculation = 10000000000 * 1000000000
    
    # Error: Race condition (Reliability Issue)
    global_counter = 0
    def increment_counter():
        global global_counter
        temp = global_counter
        # Simulated delay
        time.sleep(0.1)
        global_counter = temp + 1
    
    # Error: Hardcoded IP address (Security Issue)
    server_ip = "192.168.1.1"
    admin_ip = "10.0.0.1"

# Error: Backdoor (Security Issue)
def debug_access(secret_code):
    if secret_code == "backdoor123":
        return True  # Grant admin access
    return False

if __name__ == "__main__":
    main()
    # Error: Abrupt app termination (Reliability Issue)
    os._exit(1)