# ==========================================
# 🎬 Grafo conexo Disney (versión en español)
# ==========================================

peliculas = [
    "Piratas del Caribe: La maldición del Perla Negra",
    "El Llanero Solitario",
    "Alicia en el País de las Maravillas",
    "Cenicienta",
    "Asesinato en el Expreso de Oriente",
    "En el Bosque",
    "El Regreso de Mary Poppins",
    "La Bella y la Bestia"
]

elencos = {
    "Piratas del Caribe: La maldición del Perla Negra": [
        "Johnny Depp", "Orlando Bloom", "Keira Knightley", "Geoffrey Rush"
    ],
    "El Llanero Solitario": [
        "Johnny Depp", "Armie Hammer", "Helena Bonham Carter", "William Fichtner"
    ],
    "Alicia en el País de las Maravillas": [
        "Johnny Depp", "Helena Bonham Carter", "Anne Hathaway", "Mia Wasikowska"
    ],
    "Cenicienta": [
        "Lily James", "Cate Blanchett", "Richard Madden", "Helena Bonham Carter"
    ],
    "Asesinato en el Expreso de Oriente": [
        "Kenneth Branagh", "Johnny Depp", "Judi Dench", "Daisy Ridley", "Penélope Cruz", "Emma Thompson"
    ],
    "En el Bosque": [
        "Meryl Streep", "Emily Blunt", "James Corden", "Anna Kendrick", "Johnny Depp"
    ],
    "El Regreso de Mary Poppins": [
        "Emily Blunt", "Lin-Manuel Miranda", "Meryl Streep", "Colin Firth", "Ben Whishaw"
    ],
    "La Bella y la Bestia": [
        "Emma Watson", "Dan Stevens", "Luke Evans", "Josh Gad", "Ewan McGregor", "Ian McKellen", "Emma Thompson"
    ]
}

# Crear grafo
G = Graph(multiedges=True, loops=True)
G.add_vertices(peliculas)

# Conexiones entre películas que comparten actores
for p1 in peliculas:
    for p2 in peliculas:
        if p1 < p2:
            comunes = set(elencos[p1]).intersection(elencos[p2])
            for actor in comunes:
                G.add_edge(p1, p2, label=actor)

# Bucles para actores exclusivos (que solo aparecen en una película)
for peli, elenco in elencos.items():
    for actor in elenco:
        if sum(actor in elencos[p] for p in peliculas) == 1:
            G.add_edge(peli, peli, label=actor)

# Mostrar si el grafo es conexo
print("¿Es conexo el grafo?:", G.is_connected())
if not G.is_connected():
    print(" Componentes desconectados:", G.connected_components())

# Visualización del grafo
G.plot(
    vertex_size=2500,
    vertex_color="lightyellow",
    vertex_labels=True,
    edge_labels=True,
    layout="spring",
    figsize=[26, 20]
).show()
