import os
import subprocess  # Error: Importación no utilizada
import time  # Error: Importación no utilizada

# Error: Variable global sin usar
GLOBAL_CONSTANT = "This is never used"

# Error: Hardcoded credentials
DATABASE_PASSWORD = "supersecretpassword123"  

def read_file(file_path):
    # Error: Indentación inconsistente (mezcla de espacios y tabs)
    try: 
	with open(file_path, 'r') as file:  # Error: Indentación con tabulador en lugar de espacios
            data = file.read()
            # Error: Variable no utilizada
            line_count = len(data.split('\n'))
        return data
    except FileNotFoundError:
        # Error: Uso de print en lugar de logging para errores
        print(f"The file at {file_path} does not exist.")
        return None
    # Error: Exception handling demasiado general
    except Exception as e:
        pass  # Error: Excepción silenciada sin manejo adecuado
    
def write_file(file_path, data):
    # Error: Falta manejo de excepciones
    with open(file_path, 'w') as file:
        file.write(data)
    # Error: Función sin return explícito

def get_user_input():
    # Error: Entrada de usuario sin validación
    user_input = input("Enter some text: ")
    # Error: Uso inseguro de eval con entrada del usuario
    if user_input.startswith('calc:'):
        result = eval(user_input[5:])  # Error: uso de eval (vulnerabilidad de seguridad)
        return str(result)
    return user_input

def process_data(data):
    # Error: Complejidad ciclomática alta (muchas condiciones anidadas)
    if data:
        if len(data) > 10:
            if data.isupper():
                processed_data = data.lower()
            else:
                if data.islower():
                    processed_data = data.upper()
                else:
                    if data.isdigit():
                        processed_data = data * 2
                    else:
                        processed_data = data.lower()
        else:
            processed_data = data.lower()
    else:
        processed_data = ""
    
    # Error: String concatenación ineficiente en lugar de format o f-strings
    debug_message = "Processing completed for data: " + processed_data + " with length: " + str(len(processed_data))
    
    # Error: Código muerto (nunca se ejecuta)
    if False:
        print("This will never execute")
    
    return processed_data

# Error: Función duplicada con lógica similar
def process_text(text):
    return text.lower()

def main():
    # Error: Hard-coded ruta de archivo
    file_path = "/home/user/documents/example.txt"
    
    # Error: Command injection vulnerability
    os_command = "ls " + file_path
    os.system(os_command)  # Error: Ejecución de comando con entrada potencialmente no validada
    
    # Reading from a file
    data = read_file(file_path)
    if data is None:
        return

    # Processing data
    processed_data = process_data(data)
    # Error: Print de datos potencialmente sensibles
    print(f"Processed Data: {processed_data}")

    # Getting user input and writing to a file
    user_input = get_user_input()
    write_file(file_path, user_input)
    
    # Error: Recurso no cerrado adecuadamente
    f = open("temp.txt", "w")
    f.write("Temporary data")
    # Error: Falta f.close()
    
    # Error: Código commented-out
    # old_function_call()
    
    # Error: Asignación innecesaria
    x = 5
    y = x
    x = 10
    
    # Error: Sleep innecesario
    time.sleep(2)

# Error: Función definida pero nunca utilizada
def unused_function():
    return "This function is never called"

if __name__ == "__main__":
    main()
    # Error: Salida del programa con código de error fijo
    exit(1)  # Error: salida abrupta con código de error