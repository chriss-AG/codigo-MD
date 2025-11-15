import networkx as nx
import matplotlib.pyplot as plt

# ---------------------------
# Datos de películas y elencos
#---------------------------

peliculas = [
    "Piratas del Caribe",
    "El Llanero Solitario",
    "Alicia en el País de las Maravillas",
    "Cenicienta",
    "Expreso de Oriente",
    "En el Bosque",
    "Mary Poppins",
    "Bella y Bestia"
]

elencos = {
    "Piratas del Caribe": [
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
    "Expreso de Oriente": [
        "Kenneth Branagh", "Johnny Depp", "Judi Dench", "Daisy Ridley", "Penélope Cruz", "Emma Thompson"
    ],
    "En el Bosque": [
        "Meryl Streep", "Emily Blunt", "James Corden", "Anna Kendrick", "Johnny Depp"
    ],
    "Mary Poppins": [
        "Emily Blunt", "Lin-Manuel Miranda", "Meryl Streep", "Colin Firth", "Ben Whishaw"
    ],
    "Bella y Bestia": [
        "Emma Watson", "Dan Stevens", "Luke Evans", "Josh Gad", "Ewan McGregor", "Ian McKellen", "Emma Thompson"
    ]
}

# ---------------------------
# Crear grafo con networkx
# ---------------------------

G = nx.MultiGraph()
G.add_nodes_from(peliculas)

# Crear aristas por actores compartidos
for p1 in peliculas:
    for p2 in peliculas:
        if p1 < p2:
            comunes = set(elencos[p1]).intersection(elencos[p2])
            for actor in comunes:
                G.add_edge(p1, p2, actor=actor)

# Verificar conectividad
is_connected = nx.is_connected(G)
print("¿Es conexo el grafo?:", is_connected)

# ---------------------------
# Dibujar grafo
# ---------------------------

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(18, 14))

# Dibujar nodos
nx.draw_networkx_nodes(G, pos, node_size=2500, node_color="lightyellow", edgecolors="black")

# Dibujar aristas
nx.draw_networkx_edges(G, pos)

# Etiquetas de películas
nx.draw_networkx_labels(G, pos, font_size=10)

# Etiquetas de actores
edge_labels = {(u, v, k): d["actor"] for u, v, k, d in G.edges(keys=True, data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.title("Grafo de Colaboraciones entre Películas de Disney (No Animadas)")
plt.axis("off")
plt.show()