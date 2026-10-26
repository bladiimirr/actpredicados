from collections import defaultdict


hechos = {
    
    ("guepardo", "TienePelo", True),
    ("guepardo", "DaLeche", True),
    ("guepardo", "ComeCarne", True),
    ("guepardo", "ColorLeonado", True),
    ("guepardo", "TieneManchas", True),
    ("guepardo", "TieneRayas", False),

    ("tigre", "TienePelo", True),
    ("tigre", "DaLeche", True),
    ("tigre", "ComeCarne", True),
    ("tigre", "ColorLeonado", True),
    ("tigre", "TieneManchas", False),
    ("tigre", "TieneRayas", True),

    ("jirafa", "TienePelo", True),
    ("jirafa", "DaLeche", True),
    ("jirafa", "ComeCarne", False),
    ("jirafa", "TienePezunas", True),
    ("jirafa", "CuelloLargo", True),
    ("jirafa", "TieneManchas", True),
    ("jirafa", "TieneRayas", False),
   
    ("cebra", "TienePelo", True),
    ("cebra", "DaLeche", True),
    ("cebra", "ComeCarne", False),
    ("cebra", "TienePezunas", True),
    ("cebra", "CuelloLargo", False),
    ("cebra", "TieneManchas", False),
    ("cebra", "TieneRayas", True),
  
    ("pinguino", "TienePlumas", True),
    ("pinguino", "Vuela", False),
    ("pinguino", "PoneHuevos", True),
    ("pinguino", "Nada", True),
    ("pinguino", "BlancoYNegro", True),
    ("pinguino", "VuelaMuyBien", False),
  
    ("albatros", "TienePlumas", True),
    ("albatros", "Vuela", True),
    ("albatros", "PoneHuevos", True),
    ("albatros", "Nada", False),
    ("albatros", "BlancoYNegro", False),
    ("albatros", "VuelaMuyBien", True),
  
    ("gato", "TienePelo", True),
    ("gato", "DaLeche", True),
    ("gato", "ComeCarne", True),
    ("gato", "TamanoPequeno", True),
    ("gato", "MechonesEnOrejas", False),
    ("gato", "ViveConHumanos", True),
    ("gato", "ViveEnEstadoSalvaje", False),
  
    ("caracal", "TienePelo", True),
    ("caracal", "DaLeche", True),
    ("caracal", "ComeCarne", True),
    ("caracal", "TamanoPequeno", False),
    ("caracal", "MechonesEnOrejas", True),
    ("caracal", "ViveConHumanos", False),
    ("caracal", "ViveEnEstadoSalvaje", True),

    ("lobo", "TienePelo", True),
    ("lobo", "DaLeche", True),
    ("lobo", "ComeCarne", True),
    ("lobo", "TieneHocicoGrande", True),
    ("lobo", "VidaSalvajeEnManada", True),

   
    ("perro", "TienePelo", True),
    ("perro", "DaLeche", True),
    ("perro", "ComeCarne", True),
    ("perro", "TieneHocicoGrande", False),
    ("perro", "VidaSalvajeEnManada", False),
    ("perro", "Perro", True),
}



vinculos_jerarquia = {
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
}


atributos = defaultdict(dict)
for animal, atributo, valor in hechos:
    atributos[animal][atributo] = valor

jerarquia_hijos = defaultdict(list)
jerarquia_padre = {}
for padre, hijo in vinculos_jerarquia:
    jerarquia_hijos[padre].append(hijo)
    jerarquia_padre[hijo] = padre


def get(animal, atributo):
    """Consulta directa O(1) de un atributo de un animal.""" 
    return atributos.get(animal, {}).get(atributo, False)


def consultar(s=None, p=None, o=None):
     
    return [
        (a, b, c)
        for (a, b, c) in hechos
        if s in (None, a) and p in (None, b) and o in (None, c)
    ]



def Mamifero(animal):
  
    return get(animal, "TienePelo") or get(animal, "DaLeche")


def Ave(animal):
 
    return get(animal, "TienePlumas") or (get(animal, "Vuela") and get(animal, "PoneHuevos"))


def Carnivoro(animal):
   
    return Mamifero(animal) and get(animal, "ComeCarne")


def Ungulado(animal):
  
    return Mamifero(animal) and get(animal, "TienePezunas")


def Guepardo(animal):
    
    return Carnivoro(animal) and get(animal, "ColorLeonado") and get(animal, "TieneManchas")


def Tigre(animal):
   
    return Carnivoro(animal) and get(animal, "TieneRayas")


def Jirafa(animal):
   
    return Ungulado(animal) and get(animal, "CuelloLargo") and get(animal, "TieneManchas")


def Cebra(animal):
  
    return Ungulado(animal) and get(animal, "TieneRayas")


def Pinguino(animal):
    
    return Ave(animal) and get(animal, "Nada") and get(animal, "BlancoYNegro")


def Albatros(animal):
   
    return Ave(animal) and get(animal, "VuelaMuyBien")


def Gato(animal):
    
    return (
        Carnivoro(animal)
        and get(animal, "TamanoPequeno")
        and not get(animal, "MechonesEnOrejas")
    )


def Caracal(animal):
    
    return (
        Carnivoro(animal)
        and get(animal, "MechonesEnOrejas")
        and get(animal, "ViveEnEstadoSalvaje")
    )


def Lobo(animal):
    
    regla_hocico = get(animal, "TieneHocicoGrande")
    regla_manada = Carnivoro(animal) and get(animal, "VidaSalvajeEnManada")
    return regla_hocico or regla_manada


def Perro(animal):
    
    return get(animal, "Perro")


def main():
    print(" Clasificacion de animales \n")

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

    print("\nEjemplos de consulta por patron \n")
    print("Atributos de 'lobo':", consultar(s="lobo"))
    print("\nQuienes tienen rayas (True):", consultar(p="TieneRayas", o=True))

    print("\n Ejemplo de indice jerarquico derivado \n")
    print("Hijos de 'Carnivoro':", jerarquia_hijos["Carnivoro"])
    print("Padre de 'Lobo':", jerarquia_padre["Lobo"])


if __name__ == "__main__":
    main()