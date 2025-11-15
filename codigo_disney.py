# Archivo generado con el código proporcionado por el usuario

peliculas = {
    "Piratas del Caribe: La maldición del Perla Negra": [
        "Johnny Depp", "Orlando Bloom", "Keira Knightley", "Geoffrey Rush"
    ],
    "El llanero solitario": [
        "Johnny Depp", "Armie Hammer", "Helena Bonham Carter", "William Fichtner"
    ],
    "Alicia en el país de las maravillas": [
        "Johnny Depp", "Helena Bonham Carter", "Anne Hathaway", "Mia Wasikowska"
    ],
    "Cenicienta": [
        "Lily James", "Cate Blanchett", "Richard Madden", "Helena Bonham Carter"
    ],
    "Asesinato en el Expreso de Oriente": [
        "Kenneth Branagh", "Johnny Depp", "Judi Dench", "Daisy Ridley", "Penélope Cruz", "Emma Thompson"
    ],
    "En el bosque": [
        "Meryl Streep", "Emily Blunt", "James Corden", "Anna Kendrick", "Johnny Depp"
    ],
    "El regreso de Mary Poppins": [
        "Emily Blunt", "Lin-Manuel Miranda", "Meryl Streep", "Colin Firth", "Ben Whishaw"
    ],
    "La Bella y la Bestia": [
        "Emma Watson", "Dan Stevens", "Luke Evans", "Josh Gad", "Ewan McGregor", "Ian McKellen", "Emma Thompson"
    ]
}

actor = input("Ingrese el nombre del actor o actriz: ").strip()

encontrado = False

for pelicula, elenco in peliculas.items():
    if actor in elenco:
        encontrado = True
        otros = [a for a in elenco if a != actor]
        print(f"\n{actor} participó en '{pelicula}' junto a:")
        print(" - " + "\n - ".join(otros))

if not encontrado:
    print(f"El actor o actriz '{actor}' no hace parte del grafo.")
