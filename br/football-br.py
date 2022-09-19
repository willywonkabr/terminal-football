import random
TIMES = {
    'timeA': {'nome': "Brasil",'pontos': 0,'gols_feitos': 0,'gols_diferenca': 0,'gols_sofridos': 0,},
    'timeB': {'nome': "França",'pontos': 0,'gols_feitos': 0,'gols_diferenca': 0,'gols_sofridos': 0,},
    'timeC': {'nome': "Israel",'pontos': 0,'gols_feitos': 0,'gols_diferenca': 0,'gols_sofridos': 0,},
    'timeD': {'nome': "Angola",'pontos': 0,'gols_feitos': 0,'gols_diferenca': 0,'gols_sofridos': 0,},
}

PARIDAS = [
# Turno 1
    # Rodada 1
    {'casa': TIMES['timeA'], 'golsCasa': 0, 'fora': TIMES['timeB'], 'golsFora': 0},
    {'casa': TIMES['timeC'], 'golsCasa': 0, 'fora': TIMES['timeD'], 'golsFora': 0},
    # Rodada 2
    {'casa': TIMES['timeA'], 'golsCasa': 0, 'fora': TIMES['timeC'], 'golsFora': 0},
    {'casa': TIMES['timeB'], 'golsCasa': 0, 'fora': TIMES['timeD'], 'golsFora': 0},
    # Rodada 3
    {'casa': TIMES['timeA'], 'golsCasa': 0, 'fora': TIMES['timeD'], 'golsFora': 0},
    {'casa': TIMES['timeC'], 'golsCasa': 0, 'fora': TIMES['timeB'], 'golsFora': 0},
# Turno 2
    # Rodada 4
    {'casa': TIMES['timeA'], 'golsCasa': 0, 'fora': TIMES['timeB'], 'golsFora': 0},
    {'casa': TIMES['timeC'], 'golsCasa': 0, 'fora': TIMES['timeD'], 'golsFora': 0},
    # Rodada 5
    {'casa': TIMES['timeA'], 'golsCasa': 0, 'fora': TIMES['timeC'], 'golsFora': 0},
    {'casa': TIMES['timeB'], 'golsCasa': 0, 'fora': TIMES['timeD'], 'golsFora': 0},
    # Rodada 6
    {'casa': TIMES['timeA'], 'golsCasa': 0, 'fora': TIMES['timeD'], 'golsFora': 0},
    {'casa': TIMES['timeC'], 'golsCasa': 0, 'fora': TIMES['timeB'], 'golsFora': 0},
]
def criarGols():
    return random.randint(0,3) 
def distribuirGols(partida):
    partida['golsCasa'] = criarGols()
    partida['golsFora'] = criarGols()
def aplicarGolsPartidas(partidas):
    for partida in partidas:
        distribuirGols(partida)
def mostrarPartida(partida):
    print(f"{partida['casa']['nome']} {partida['golsCasa']} X {partida['golsFora']} {partida['fora']['nome']}")
def relatorioPartidas(partidas):
    numeroPartida = 1
    numeroRodada = 1
    numeroTurno = 1

    for partida in partidas:
        if (numeroPartida % 6) == 1:
            print(f"\nTurno {numeroTurno}")
            numeroTurno += 1
        if (numeroPartida % 2) == 1:
            print(f"\nRodada {numeroRodada}")
            numeroRodada += 1
        mostrarPartida(partida)
        numeroPartida += 1
def somarPontos(partidas):
    for partida in partidas:
        if partida['golsCasa'] > partida['golsFora']:
            partida['casa']['pontos'] += 3
        elif partida['golsCasa'] < partida['golsFora']:
            partida['fora']['pontos'] += 3
        else:
            partida['casa']['pontos'] += 1
            partida['fora']['pontos'] += 1

        partida['casa']['gols_feitos'] += partida['golsCasa']
        partida['fora']['gols_feitos'] += partida['golsFora']

        partida['casa']['gols_diferenca'] += partida['golsCasa'] - partida['golsFora']
        partida['fora']['gols_diferenca'] += partida['golsFora'] - partida['golsCasa']

        partida['casa']['gols_sofridos'] += partida['golsFora']
        partida['fora']['gols_sofridos'] += partida['golsCasa']
def classificarTimes():
    listaTimes = list(TIMES.values()) 
    listaTimes = sorted(listaTimes, key = lambda time: (time['pontos'], time['gols_feitos'], time['gols_diferenca'], time['gols_sofridos']), reverse = True)
    print("\n",sorted(listaTimes, key = lambda time: (time['pontos'], time['gols_feitos'], time['gols_diferenca'], time['gols_sofridos']), reverse = True))
    return listaTimes
def final(primeiro, segundo):
    partida = {'casa': primeiro, 'golsCasa': 0, 'fora': segundo, 'golsFora': 0}
    
    distribuirGols(partida)
    print("\n")
    mostrarPartida(partida)

    campeao = None

    if partida['golsCasa'] == partida['golsFora']:
        penaltiCasa = random.randint(0,5)
        penaltiFora = random.randint(0,5)
    
        while penaltiCasa == penaltiFora:
            penaltiCasa += random.randint(0,2)
            penaltiFora += random.randint(0,2)

        print("\nPênaltis")
        print(f"{partida['casa']['nome']} {penaltiCasa} x {penaltiFora} {partida['fora']['nome']}")

        if penaltiCasa > penaltiFora:
            campeao = partida['casa']
        else:
            campeao = partida['fora']
    else:
        if partida['golsCasa'] > partida['golsFora']:
            campeao = partida['casa']
        else:
            campeao = partida['fora']
    print(f"Campeão {campeao['nome']}")
aplicarGolsPartidas(PARIDAS)
relatorioPartidas(PARIDAS)
somarPontos(PARIDAS)

classificacao = classificarTimes()
primeiro, segundo = classificacao[0], classificacao[1]
final(primeiro, segundo)
