let TIMES = {
    timeA: {nome: 'Brasil', pontos: 0, gols_feitos: 0, gols_diferenca: 0, gols_sofridos: 0,},
    timeB: {nome: 'França', pontos: 0, gols_feitos: 0, gols_diferenca: 0, gols_sofridos: 0,},
    timeC: {nome: 'Israel', pontos: 0, gols_feitos: 0, gols_diferenca: 0, gols_sofridos: 0,},
    timeD: {nome: 'Angola', pontos: 0, gols_feitos: 0, gols_diferenca: 0, gols_sofridos: 0,},
}
let PARTIDAS = [
  // Turno 1
    // Rodada 1
    {casa: TIMES.timeA, golsCasa: 0, fora: TIMES.timeB, golsFora: 0},
    {casa: TIMES.timeC, golsCasa: 0, fora: TIMES.timeD, golsFora: 0},
    // Rodada 2
    {casa: TIMES.timeA, golsCasa: 0, fora: TIMES.timeC, golsFora: 0},
    {casa: TIMES.timeB, golsCasa: 0, fora: TIMES.timeD, golsFora: 0},
    // Rodada 3
    {casa: TIMES.timeA, golsCasa: 0, fora: TIMES.timeD, golsFora: 0},
    {casa: TIMES.timeC, golsCasa: 0, fora: TIMES.timeB, golsFora: 0},
  // Turno 2
    // Rodada 4
    {fora: TIMES.timeA, golsCasa: 0, casa: TIMES.timeB, golsFora: 0},
    {fora: TIMES.timeC, golsCasa: 0, casa: TIMES.timeD, golsFora: 0},
    // Rodada 5
    {fora: TIMES.timeA, golsCasa: 0, casa: TIMES.timeC, golsFora: 0},
    {fora: TIMES.timeB, golsCasa: 0, casa: TIMES.timeD, golsFora: 0},
    // Rodada 6
    {fora: TIMES.timeA, golsCasa: 0, casa: TIMES.timeD, golsFora: 0},
    {fora: TIMES.timeB, golsCasa: 0, casa: TIMES.timeC, golsFora: 0},
]
function criarGols(max) {
    return Math.floor(Math.random() * max)
}
function distribuirGols(partida) {
    partida.golsCasa = criarGols(4)
    partida.golsFora = criarGols(4)
}
function aplicarGolsPartidas(partidas) {
    for (let partida of partidas) {
      distribuirGols(partida)
    }
}
function mostrarPartidas(partida) {
    console.log(`${partida.casa.nome}    ${partida.golsCasa}  x  ${partida.golsFora}   ${partida.fora.nome}`)
}
function relatorioPartidas(partidas) {
    let numeroPartida = 1
    let numeroRodada = 1
    let numeroTurno = 1
  
    for (let partida of partidas) {
      if (numeroPartida % 6 === 1) {
        console.log(`\nTurno ${numeroTurno}`)
        numeroTurno++
      }
      if (numeroPartida % 2 === 1) {
        console.log(`\nRodada ${numeroRodada}`)
        numeroRodada++
      }
      mostrarPartidas(partida)
      numeroPartida++
    }
}
function somarPontos(partidas) {
    for (let {casa, fora, golsCasa, golsFora} of partidas) {
      if (golsCasa > golsFora) {
        casa.pontos += 3
      } else if (golsCasa < golsFora) {
        fora.pontos += 3
      } else {
        casa.pontos++
        fora.pontos++
      }
      casa.gols_feitos += golsCasa
      fora.gols_feitos += golsFora
  
      casa.gols_sofridos += golsFora
      fora.gols_sofridos += golsCasa
  
      casa.gols_diferenca += golsCasa - golsFora
      fora.gols_diferenca += golsFora - golsCasa
    }
}
function classificarTimes(times) {
    let listaTimes = Object.values(times)
  
    listaTimes.sort((time1, time2) => {
      if(time1.pontos !== time2.pontos) {
        return time2.pontos - time1.pontos
      }
      if(time2.gols_feitos !== time2.gols_feitos) {
        return time2.gols_feitos - time1.gols_feitos
      }
      if(time1.gols_diferenca !== time2.gols_diferenca) {
        return time2.gols_diferenca - time1.gols_diferenca
      }
      return time1.gols_sofridos - time2.gols_sofridos
    })
    return listaTimes
}
function final(primeiro, segundo) {
    let partida = {fora: primeiro, golsCasa: 0, casa: segundo, golsFora: 0}
  
    distribuirGols(partida)
    mostrarPartidas(partida)
  
    let campeao = null
  
    if(partida.golsCasa === partida.golsFora) {
      let penaltiCasa = criarGols(6)
      let penaltiFora = criarGols(6)
  
      while(penaltiCasa === penaltiFora) {
        penaltiCasa += criarGols(2)
        penaltiFora += criarGols(2)
      }
  
      console.log('\nPênaltis')
      console.log(`${partida.casa.nome}     ${penaltiCasa}  x  ${penaltiFora}     ${partida.fora.nome}`)
  
      if(penaltiCasa > penaltiFora) {
        campeao = partida.casa
      } else {
        campeao = partida.fora
      }
    } else {
      if(partida.golsCasa > partida.golsFora) {
        campeao = partida.casa
      } else {
        campeao = partida.fora
      }    
    }
    console.log(`Campeão ${campeao.nome}`)
}  
aplicarGolsPartidas(PARTIDAS)
relatorioPartidas(PARTIDAS)
somarPontos(PARTIDAS)
let classificacao = classificarTimes(TIMES)
console.table(classificacao)

let [primeiro, segundo] = classificacao
final(primeiro, segundo)
