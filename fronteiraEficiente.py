import pandas as pd

class FronteiraEficiente:
  def __init__(self, data, jogadores_escolhidos):
    self.jogadores_escolhidos = jogadores_escolhidos
    self.dataframe = pd.DataFrame(data, columns=['score','custo','rodada','indice_jogadores'])

  def CalcularFronteiraEficiente(self): 

    df_front = pd.DataFrame(columns=self.dataframe.columns)

    for i in range(0,self.dataframe.shape[0]):

      flag = True

      for j in range(0,self.dataframe.shape[0]):

        if i != j:

          if self.dataframe.iloc[i][0] < self.dataframe.iloc[j][0] and self.dataframe.iloc[i][1] > self.dataframe.iloc[j][1]:

            flag = False

            break

      if flag == True :
        
        df_front = df_front.append(self.dataframe.iloc[i])

    df_front = df_front.sort_values(by=['score', 'custo'])
    jogadores_solucoes_eficiente = self.RetornaJogadoresSolucoesEficiente(df_front)
    return df_front, jogadores_solucoes_eficiente

  def RetornaJogadoresSolucoesEficiente(self, df_front):
    #print(self.jogadores_escolhidos, "\n(fronteiraEficiente.py) self.jogadores_escolhidos\n")
    #print(self.dataframe, "\n(fronteiraEficiente.py) self.dataframe\n")
    #print(len(self.jogadores_escolhidos), "\n(fronteiraEficiente.py) len(self.jogadores_escolhidos)\n")
    #print(len(self.dataframe), "\n(fronteiraEficiente.py) len(self.dataframe)\n")
    #print(self.dataframe.iloc[-1], "\n(fronteiraEficiente.py) self.dataframe.iloc[-1]\n")
    #print(self.jogadores_escolhidos[-1], "\n(fronteiraEficiente.py) self.jogadores_escolhidos[-1]\n")

    jogadores_solucoes_eficiente = []
    limite_jogadores_escolhidos = len(self.jogadores_escolhidos)
    for i in range(len(df_front)):
      indice_busca_jogadores = int(df_front.iloc[i]['indice_jogadores'])
      if indice_busca_jogadores < limite_jogadores_escolhidos:
        jogadores_solucoes_eficiente.append(self.jogadores_escolhidos[indice_busca_jogadores])
    return jogadores_solucoes_eficiente