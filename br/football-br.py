from random import randint 
TIMES = {
    'time_a': {'nome': "Brasil",'pontos': 0,'gols_feitos': 0,'gols_diferenca': 0,'gols_sofridos': 0},
    'time_b': {'nome': "França",'pontos': 0,'gols_feitos': 0,'gols_diferenca': 0,'gols_sofridos': 0},
    'time_c': {'nome': "Israel",'pontos': 0,'gols_feitos': 0,'gols_diferenca': 0,'gols_sofridos': 0},
    'time_d': {'nome': "Angola",'pontos': 0,'gols_feitos': 0,'gols_diferenca': 0,'gols_sofridos': 0},
}

PARIDAS = [
# Turno 1
    # Rodada 1
    {'casa': TIMES['time_a'], 'gols_casa': 0, 'fora': TIMES['time_b'], 'gols_fora': 0},
    {'casa': TIMES['time_c'], 'gols_casa': 0, 'fora': TIMES['time_d'], 'gols_fora': 0},
    # Rodada 2
    {'casa': TIMES['time_a'], 'gols_casa': 0, 'fora': TIMES['time_c'], 'gols_fora': 0},
    {'casa': TIMES['time_b'], 'gols_casa': 0, 'fora': TIMES['time_d'], 'gols_fora': 0},
    # Rodada 3
    {'casa': TIMES['time_a'], 'gols_casa': 0, 'fora': TIMES['time_d'], 'gols_fora': 0},
    {'casa': TIMES['time_c'], 'gols_casa': 0, 'fora': TIMES['time_b'], 'gols_fora': 0},
# Turno 2
    # Rodada 4
    {'casa': TIMES['time_a'], 'gols_casa': 0, 'fora': TIMES['time_b'], 'gols_fora': 0},
    {'casa': TIMES['time_c'], 'gols_casa': 0, 'fora': TIMES['time_d'], 'gols_fora': 0},
    # Rodada 5
    {'casa': TIMES['time_a'], 'gols_casa': 0, 'fora': TIMES['time_c'], 'gols_fora': 0},
    {'casa': TIMES['time_b'], 'gols_casa': 0, 'fora': TIMES['time_d'], 'gols_fora': 0},
    # Rodada 6
    {'casa': TIMES['time_a'], 'gols_casa': 0, 'fora': TIMES['time_d'], 'gols_fora': 0},
    {'casa': TIMES['time_c'], 'gols_casa': 0, 'fora': TIMES['time_b'], 'gols_fora': 0},
]
def criar_gols():
    return randint(0,3) 
def distribuir_gols(partida):
    partida['gols_casa'] = criar_gols()
    partida['gols_fora'] = criar_gols()
def aplicar_gols_partidas(partidas):
    for partida in partidas:
        distribuir_gols(partida)
def mostrar_partida(partida):
    print(f"{partida['casa']['nome']} {partida['gols_casa']} X {partida['gols_fora']} {partida['fora']['nome']}")
def relatorio_partidas(partidas):
    numero_partida = 1
    numero_rodada = 1
    numero_turno = 1

    for partida in partidas:
        if (numero_partida % 6) == 1:
            print(f"\nTurno {numero_turno}")
            numero_turno += 1
        if (numero_partida % 2) == 1:
            print(f"\nRodada {numero_rodada}")
            numero_rodada += 1
        mostrar_partida(partida)
        numero_partida += 1
def somar_pontos(partidas):
    for partida in partidas:
        if partida['gols_casa'] > partida['gols_fora']:
            partida['casa']['pontos'] += 3
        elif partida['gols_casa'] < partida['gols_fora']:
            partida['fora']['pontos'] += 3
        else:
            partida['casa']['pontos'] += 1
            partida['fora']['pontos'] += 1

        partida['casa']['gols_feitos'] += partida['gols_casa']
        partida['fora']['gols_feitos'] += partida['gols_fora']

        partida['casa']['gols_diferenca'] += partida['gols_casa'] - partida['gols_fora']
        partida['fora']['gols_diferenca'] += partida['gols_fora'] - partida['gols_casa']

        partida['casa']['gols_sofridos'] += partida['gols_fora']
        partida['fora']['gols_sofridos'] += partida['gols_casa']
def classificar_times():
    lista_times = list(TIMES.values()) 
    lista_times = sorted(lista_times, key = lambda time: (time['pontos'], time['gols_feitos'], time['gols_diferenca'], time['gols_sofridos']), reverse = True)
    print("\n", sorted(lista_times, key = lambda time: (time['pontos'], time['gols_feitos'], time['gols_diferenca'], time['gols_sofridos']), reverse = True))
    return lista_times
def final(primeiro, segundo):
    partida = {'casa': primeiro, 'gols_casa': 0, 'fora': segundo, 'gols_fora': 0}
    
    distribuir_gols(partida)
    print("\n")
    mostrar_partida(partida)

    campeao = None

    if partida['gols_casa'] == partida['gols_fora']:
        penalti_casa = randint(0,5)
        penalti_fora = randint(0,5)
    
        while penalti_casa == penalti_fora:
            penalti_casa += randint(0,2)
            penalti_fora += randint(0,2)

        print("\nPênaltis")
        print(f"{partida['casa']['nome']} {penalti_casa} x {penalti_fora} {partida['fora']['nome']}")

        if penalti_casa > penalti_fora:
            campeao = partida['casa']
        else:
            campeao = partida['fora']
    else:
        if partida['gols_casa'] > partida['gols_fora']:
            campeao = partida['casa']
        else:
            campeao = partida['fora']
    print(f"Campeão {campeao['nome']}")
aplicar_gols_partidas(PARIDAS)
relatorio_partidas(PARIDAS)
somar_pontos(PARIDAS)

classificacao = classificar_times()
primeiro, segundo = classificacao[0], classificacao[1]
final(primeiro, segundo)
