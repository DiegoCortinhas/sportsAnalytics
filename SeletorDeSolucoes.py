from random import randint
import pandas as pd
import sys

class SeletorDeSolucoes:
    def __init__(self, perfil, solucoes_jogadores, solucoes_eficiente, C):
        self.perfil = perfil
        self.solucoes_jogadores = solucoes_jogadores
        self.solucoes_eficiente = solucoes_eficiente
        self.C = C

    def EscolherSolucao(self):
        solucao_escolhida = []
        jogadores_solucao_escolhida = []

        if self.perfil == "prefere_mais_score":
            # Lembrar que as solucoes chegam como um Dataframe
            #for i in range(1, len(self.solucoes_eficiente) - 1):
            #    solucao_escolhida = self.solucoes_eficiente.iloc[-i]
            #    custo_solucao_escolhida = solucao_escolhida.iloc[1]
            #    if custo_solucao_escolhida <= self.C:
            #        jogadores_solucao_escolhida = self.solucoes_jogadores[-i]
            #        break
            solucao_escolhida = self.solucoes_eficiente.iloc[-1]
            custo_solucao_escolhida = solucao_escolhida.iloc[1]
            jogadores_solucao_escolhida = self.solucoes_jogadores[-1]


        elif self.perfil == "prefere_menos_preco":
            solucao_escolhida = self.solucoes_eficiente.iloc[0]
            custo_solucao_escolhida = solucao_escolhida.iloc[1]
            jogadores_solucao_escolhida = self.solucoes_jogadores[0]


        elif self.perfil == "balanceado":
            solucao_media_balanceada = round(len(self.solucoes_eficiente) / 2)
            solucao_escolhida = self.solucoes_eficiente.iloc[solucao_media_balanceada]
            jogadores_solucao_escolhida = self.solucoes_jogadores[solucao_media_balanceada]

        elif self.perfil == "aleatorio":
            numero_aleatorio = randint(0, len(self.solucoes_eficiente) - 1)
            solucao_escolhida = self.solucoes_eficiente.iloc[numero_aleatorio]
            jogadores_solucao_escolhida = self.solucoes_jogadores[numero_aleatorio]
            
        return solucao_escolhida, jogadores_solucao_escolhida
    
    def EscolherSolucaoBalanceada(self):
        solucao_escolhida = []
        jogadores_solucao_escolhida = []
        return solucao_escolhida, jogadores_solucao_escolhida

    def FormatarDataframeParaRetorno(self, data):
        dataframe = pd.DataFrame(data, columns=["Nome","Id","Posicao","Custo","Score","Media"])
        return dataframe