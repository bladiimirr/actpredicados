"""
Practica: Desarrollo de predicados
Instituto Tecnologico de Ensenada - Programacion Logica y funcional 2026-1
Elaborada por: Guillermo Guzman Mendoza, Bladimir Nava Vergara
"""

# ============================================================
# PASO 1: Hechos base por animal
# ============================================================

hechos = {
    "guepardo": {
        "TienePelo": True,
        "DaLeche": True,
        "ComeCarne": True,
        "ColorLeonado": True,
        "TieneManchas": True,
        "TieneRayas": False,
    },
    "tigre": {
        "TienePelo": True,
        "DaLeche": True,
        "ComeCarne": True,
        "ColorLeonado": True,
        "TieneManchas": False,
        "TieneRayas": True,
    },
    "jirafa": {
        "TienePelo": True,
        "DaLeche": True,
        "ComeCarne": False,
        "TienePezunas": True,
        "CuelloLargo": True,
        "TieneManchas": True,
        "TieneRayas": False,
    },
    "cebra": {
        "TienePelo": True,
        "DaLeche": True,
        "ComeCarne": False,
        "TienePezunas": True,
        "CuelloLargo": False,
        "TieneManchas": False,
        "TieneRayas": True,
    },
    "pinguino": {
        "TienePlumas": True,
        "Vuela": False,
        "PoneHuevos": True,
        "Nada": True,
        "BlancoYNegro": True,
        "VuelaMuyBien": False,
    },
    "albatros": {
        "TienePlumas": True,
        "Vuela": True,
        "PoneHuevos": True,
        "Nada": False,
        "BlancoYNegro": False,
        "VuelaMuyBien": True,
    },
    "gato": {
        "TienePelo": True,
        "DaLeche": True,
        "ComeCarne": True,
        "TamanoPequeno": True,
        "MechonesEnOrejas": False,
        "ViveConHumanos": True,
        "ViveEnEstadoSalvaje": False,
    },
    "caracal": {
        "TienePelo": True,
        "DaLeche": True,
        "ComeCarne": True,
        "TamanoPequeno": False,
        "MechonesEnOrejas": True,
        "ViveConHumanos": False,
        "ViveEnEstadoSalvaje": True,
    },
    "lobo": {
        "TienePelo": True,
        "DaLeche": True,
        "ComeCarne": True,
        "TieneHocicoGrande": True,
        "VidaSalvajeEnManada": True,
    },
    "perro": {
        "TienePelo": True,
        "DaLeche": True,
        "ComeCarne": True,
        "TieneHocicoGrande": False,
        "VidaSalvajeEnManada": False,
        "Perro": True,
    },
}


# ============================================================
# PASO 2: Vinculos entre hechos (relacion jerarquica como tuplas)
# ============================================================

vinculos_jerarquia = [
    ("Animal", "Mamifero"),
    ("Animal", "Ave"),
    ("Mamifero", "Carnivoro"),
    ("Mamifero", "Ungulado"),
    ("Carnivoro", "Guepardo"),
    ("Carnivoro", "Tigre"),
    ("Carnivoro", "Gato"),
    ("Carnivoro", "Caracal"),
    ("Carnivoro", "Lobo"),
    ("Carnivoro", "Perro"),
    ("Ungulado", "Jirafa"),
    ("Ungulado", "Cebra"),
    ("Ave", "Pinguino"),
    ("Ave", "Albatros"),
]


# ============================================================
# PASO 3: Predicados / reglas como funciones
# ============================================================

def get(animal, caracteristica):
    """Busca una caracteristica de un animal; si no existe, regresa False."""
    return hechos.get(animal, {}).get(caracteristica, False)


def Mamifero(animal):
    """Regla 1 y 2: tiene pelo O da leche a sus crias"""
    return get(animal, "TienePelo") or get(animal, "DaLeche")


def Ave(animal):
    """Regla 3 y 4: tiene plumas O (vuela Y pone huevos)"""
    return get(animal, "TienePlumas") or (get(animal, "Vuela") and get(animal, "PoneHuevos"))


def Carnivoro(animal):
    """Regla 5: es mamifero Y come carne"""
    return Mamifero(animal) and get(animal, "ComeCarne")


def Ungulado(animal):
    """Regla 6: es mamifero Y tiene pezunas"""
    return Mamifero(animal) and get(animal, "TienePezunas")


def Guepardo(animal):
    """Regla 7: carnivoro Y color leonado Y manchas"""
    return Carnivoro(animal) and get(animal, "ColorLeonado") and get(animal, "TieneManchas")


def Tigre(animal):
    """Regla 8: carnivoro Y rayas negras"""
    return Carnivoro(animal) and get(animal, "TieneRayas")


def Jirafa(animal):
    """Regla 9: ungulado Y cuello largo Y manchas"""
    return Ungulado(animal) and get(animal, "CuelloLargo") and get(animal, "TieneManchas")


def Cebra(animal):
    """Regla 10: ungulado Y rayas negras"""
    return Ungulado(animal) and get(animal, "TieneRayas")


def Pinguino(animal):
    """Regla 11: ave Y nada Y blanco y negro"""
    return Ave(animal) and get(animal, "Nada") and get(animal, "BlancoYNegro")


def Albatros(animal):
    """Regla 12: ave Y vuela muy bien"""
    return Ave(animal) and get(animal, "VuelaMuyBien")


def Gato(animal):
    """Entrevista 1: carnivoro Y tamano pequeno Y NO tiene mechones en orejas"""
    return (
        Carnivoro(animal)
        and get(animal, "TamanoPequeno")
        and not get(animal, "MechonesEnOrejas")
    )


def Caracal(animal):
    """Entrevista 1: carnivoro Y tiene mechones en orejas Y vive en estado salvaje"""
    return (
        Carnivoro(animal)
        and get(animal, "MechonesEnOrejas")
        and get(animal, "ViveEnEstadoSalvaje")
    )


def Lobo(animal):
    """Entrevista 2: tiene hocico grande, O (carnivoro Y vive en manada salvaje)"""
    regla_hocico = get(animal, "TieneHocicoGrande")
    regla_manada = Carnivoro(animal) and get(animal, "VidaSalvajeEnManada")
    return regla_hocico or regla_manada


def Perro(animal):
    """Hecho base directo (el documento no formaliza una regla derivada)"""
    return get(animal, "Perro")


# ============================================================
# PASO 4: Consultas de comprobacion
# ============================================================

def main():
    print("=== Clasificacion de animales segun las reglas de la practica ===\n")

    consultas = [
        ("guepardo", Guepardo, "Guepardo"),
        ("tigre", Tigre, "Tigre"),
        ("jirafa", Jirafa, "Jirafa"),
        ("cebra", Cebra, "Cebra"),
        ("pinguino", Pinguino, "Pinguino"),
        ("albatros", Albatros, "Albatros"),
        ("gato", Gato, "Gato"),
        ("caracal", Caracal, "Caracal"),
        ("lobo", Lobo, "Lobo"),
        ("perro", Perro, "Perro"),
    ]

    for animal, funcion, nombre_regla in consultas:
        resultado = funcion(animal)
        print(f"{nombre_regla}('{animal}') -> {resultado}")


if __name__ == "__main__":
    main()