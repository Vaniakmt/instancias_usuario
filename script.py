import json
import traceback
from usuario import Usuario

def crear_instancias_usuarios(archivo_usuarios, archivo_error):
    usuarios = []

    with open(archivo_usuarios, 'r') as archivo:
        for linea in archivo:
            try:
                datos_usuario = json.loads(linea)  # Intenta decodificar la línea como JSON
                usuario = Usuario(**datos_usuario)  # Intenta crear una instancia de Usuario
                usuarios.append(usuario)  # Añade la instancia a la lista
            except json.JSONDecodeError as e:
                # Captura errores de decodificación JSON y los registra en error.log
                with open(archivo_error, 'a') as log:
                    log.write(f"Error procesando la línea: {linea}\n")
                    log.write(f"{e}\n")
                    log.write(traceback.format_exc() + "\n")
            except TypeError as e:
                # Captura errores de tipo (e.g., faltan campos) y los registra en error.log
                with open(archivo_error, 'a') as log:
                    log.write(f"Error creando instancia de Usuario con datos: {linea}\n")
                    log.write(f"{e}\n")
                    log.write(traceback.format_exc() + "\n")
            except Exception as e:
                # Captura cualquier otra excepción y la registra en error.log
                with open(archivo_error, 'a') as log:
                    log.write(f"Error inesperado con la línea: {linea}\n")
                    log.write(f"{e}\n")
                    log.write(traceback.format_exc() + "\n")
    
    return usuarios  # Devuelve la lista de instancias de usuario creadas

if __name__ == "__main__":
    archivo_usuarios = 'usuarios.txt'
    archivo_error = 'error.log'
    
    usuarios = crear_instancias_usuarios(archivo_usuarios, archivo_error)
    
    # Imprime la cantidad de usuarios creados y sus detalles
    print(f"Se crearon {len(usuarios)} instancias de usuario.")
    for usuario in usuarios:
        print(f"Nombre: {usuario.nombre}, Apellido: {usuario.apellidos}, Email: {usuario.email}, Género: {usuario.genero}")
