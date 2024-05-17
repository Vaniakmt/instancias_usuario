class Usuario:
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre  # Atributo nombre
        self.apellidos = apellido  # Atributo apellido
        self.email = email  # Atributo email
        self.genero = genero  # Atributo genero

    def __str__(self):
        return f"Usuario(nombre={self.nombre}, apellidos={self.apellidos}, email={self.email}, genero={self.genero})"
