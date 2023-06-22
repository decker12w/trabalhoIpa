def simulacao_crescimento_populacional(populacao_inicial, taxa_reproducao, taxa_mortalidade, tempo_simulacao, caracteristicas_ecossistema):
    tempo_atual = 0
    populacao_atual = populacao_inicial
    maxPop = 100000
    
    while tempo_atual < tempo_simulacao:
        novos_individuos = taxa_reproducao * populacao_atual * caracteristicas_ecossistema
        individuos_mortos = taxa_mortalidade * populacao_atual * caracteristicas_ecossistema
        
        populacao_atual = populacao_atual + novos_individuos - individuos_mortos
        
        if populacao_atual >= maxPop:
            populacao_atual = maxPop
            break
        
        tempo_atual += 1
    
    return populacao_atual

# Exemplo de utilização da função simulacao_crescimento_populacional
populacao_inicial = 100
taxa_reproducao = 0.05
taxa_mortalidade = 0.03
tempo_simulacao = 100
caracteristicas_ecossistema = 1.2

populacao_final = simulacao_crescimento_populacional(populacao_inicial, taxa_reproducao, taxa_mortalidade, tempo_simulacao, caracteristicas_ecossistema)
print(f"População final:{populacao_final:.2f}")