# Aluno: Rosialdo Queivison Vidinho de Queiroz Vicente (2020018122)
# Disciplina: Inteligência Artificial


# Lista de vizinhos com cada uma de suas distâncias
romenia_map = {
    'Arad'      : {('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)},
    'Bucharest' : {('Pitesti', 101), ('Fagaras', 211), ('Giurgiu', 90), ('Urziceni', 85)},
    'Craiova'   : {('Pitesti', 138), ('Rimnicu Vicea', 146), ('Dobreta', 120)},
    'Dobreta'    : {('Craiova', 120), ('Mehadia', 75)},
    'Eforie'    : {('Hirsova', 86)},
    'Fagaras'    : {('Sibiu', 99), ('Bucharest', 211)},
    'Giurgiu'    : {('Bucharest', 90)},
    'Hirsova'    : {('Eforie', 86), ('Urziceni', 98)},
    'Lugoj'      : {('Mehadia', 70), ('Timisoara', 111)},
    'Iasi'       : {('Neamt', 87), ('Vaslui', 92)},
    'Mehadia'    : {('Lugoj', 70), ('Dobreta', 75)},
    'Neamt'    : {('Iasi', 87)},
    'Oradea'     : {('Zerind', 71), ('Sibiu', 151)},
    'Pitesti'   : {('Bucharest', 101), ('Craiova', 138), ('Rimnicu Vicea', 97)},
    'Rimnicu Vicea' : {('Craiova', 146), ('Sibiu', 80), ('Pitesti', 97)},
    'Sibiu'   : {('Fagaras', 99), ('Rimnicu Vicea', 80), ('Arad', 140), ('Oradea', 151)},
    'Timisoara' : {('Arad', 118), ('Lugoj', 111)},
    'Urziceni'   : {('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)},
    'Vaslui'    : {('Iasi', 92), ('Urziceni', 142)},
    'Zerind'     : {('Arad', 75), ('Oradea', 71)}
}

# Distancia em linha reta para Bucharest
dist_l = {
    'Arad':          366,
    'Bucharest':     0,
    'Craiova':       160,
    'Dobreta':       242,
    'Eforie':        161,
    'Fagaras':       178,
    'Giurgiu':       77,
    'Hirsova':       151,
    'Iasi':          226,
    'Lugoj':         244,
    'Mehadia':       241,
    'Neamt':         234,
    'Oradea':        380,
    'Pitesti':       98,
    'Rimnicu Vicea': 193,
    'Sibiu':         253,
    'Timisoara':     329,
    'Urziceni':      80,
    'Vaslui':        199,
    'Zerind':        374
}

# Pega a lista de vizinhos
def vizinhos(v):
    return romenia_map[v]

# Pega a distancia em linha reta
def h(n):
    return dist_l[n]

# Inicio do algoritimo
def algoritimo_a_estrela():

    # Define uma lista aberta
    open_list = set(['Arad'])

    # Define uma lista fechada
    closed_list = set([])

    g = {}

    g['Arad'] = 0

    # recebe o mapa de adjacência de todos os nos       
    parents = {}
    parents['Arad'] = 'Arad'

    while len(open_list) > 0:
        n = None

        # Procura o caminho com o menor valor para seguir
        for v in open_list:
            if n == None or g[v] + h(v) < g[n] + h(n):
                n = v;

        if n == None:
            print('Caminho inexistente!')
            return None

        # Faz a verificação se o destino foi alcançado, se foi printa o caminho
        if n == 'Bucharest':
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append('Arad')

            reconst_path.reverse()

            print('Caminho encontrado: {}'.format(reconst_path))
            return reconst_path

        # Realiza a verificação dos vizinhos
        for (m, weight) in vizinhos(n):
            # Verifica se em qual lista a codade esta
            # Se a cidade não estiver em nenhuma lista, é a dicionada na lista aberta e o cinada atual será o seu "Pai"
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            
            # Caso o resultado seja negativo
            # É atualizada com uma remoção na lista fechada e com uma adição na aberta

            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        # A cidade que está sendo verificade é removida da lista aberta e adicionada na lista fechada
        open_list.remove(n)
        closed_list.add(n)

    # Se a lista estiver vazia não havera nada para explorar e é devolvido o printe de aviso
    print('Caminho inexistente!')
    return None

# Chamando o algoritimo para verificação    
algoritimo_a_estrela()