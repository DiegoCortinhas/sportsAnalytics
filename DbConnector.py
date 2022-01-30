import mysql.connector
from mysql.connector import Error

class DbConnector:
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost', database='cartolafc', user='root', password='admin')
        #self.nome_tabela = "valorizacao_old"
        self.nome_tabela = "valorizacao_mock"
        self.ano_base = "2019"

    def InsertBanco(self,linha):
        # Variáveis para preparar a inserção no banco
        cursor = self.connection.cursor()
        '''
        add_item = "insert into " + self.nome_tabela + " (local_id, atletas_nome, atletas_slug, atletas_apelido, atletas_foto, atletas_atleta_id,"\
                   "atletas_rodada_id, atletas_clube_id, atletas_posicao_id, atletas_status_id, atletas_pontos_num,"\
                   "atletas_preco_num, atletas_variacao_num, atletas_media_num, atletas_clube_id_full_name,"\
                   "FS, RB, PE, FC, G, FF, FT, FD, DD, GS, SG, A, CA, I, CV, PP, GC, DP)"\
                   "VALUES (%d,%s,%s,%s,%s,%d,%d,%d,%s,%s,%f,%f,%f,%f,%s,%d,%d,%d,%d,%d,%d,%d,%d,"\
                   "%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)"
        '''
        add_item = "insert into " + self.nome_tabela + " (local_id, atletas_nome, atletas_slug, atletas_apelido, atletas_foto, atletas_atleta_id," \
                   "atletas_rodada_id, atletas_clube_id, atletas_posicao_id, atletas_status_id, atletas_pontos_num," \
                   "atletas_preco_num, atletas_variacao_num, atletas_media_num, atletas_clube_id_full_name, ANO)" \
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(add_item, linha)
        self.connection.commit()

    def BuscarJogadoresPorRodadaEPosicao(self, rodada, posicao = ""):
        cursor = self.connection.cursor()
        parametros = (str(rodada), )
        #sql = "SELECT atletas_nome, atletas_rodada_id, atletas_preco_num, atletas_variacao_num \
        #    FROM valorizacao where atletas_rodada_id = %s AND atletas_status_id = 'Provável'"
        sql = "SELECT atletas_nome, atletas_atleta_id, atletas_preco_num, atletas_pontos_num, atletas_variacao_num, atletas_posicao_id \
            FROM " + self.nome_tabela + " where atletas_rodada_id = %s \
                AND ANO = " + self.ano_base


        if posicao != "":
            sql += " AND atletas_posicao_id = %s"
            parametros = (rodada, posicao)

        sql += " order by atletas_posicao_id, atletas_atleta_id"
        cursor.execute(sql, parametros)
        resultado = cursor.fetchall()
        return resultado

    def BuscarTodosJogadoresPorRodada(self, rodada):
        cursor = self.connection.cursor()
        parametros = (str(rodada), )
        # Vamos deixar o "atletas_nome" por enquanto para facilitar o debug
        sql = "SELECT atletas_nome, atletas_atleta_id, atletas_preco_num, atletas_pontos_num, atletas_variacao_num \
            FROM " + self.nome_tabela + " where atletas_rodada_id = %s \
                AND ANO = " + self.ano_base + " group by atletas_atleta_id order by atletas_posicao_id, atletas_atleta_id;"
        
        cursor.execute(sql, parametros)
        resultado = cursor.fetchall()
        return resultado


    def BuscarJogadorPorId(self, jogador_id):
        cursor = self.connection.cursor(buffered=True)
        parametros = (str(jogador_id), )
        # Vamos deixar o "atletas_nome" por enquanto para facilitar o debug
        sql = "SELECT atletas_nome, atletas_atleta_id, atletas_posicao_id, atletas_preco_num, atletas_pontos_num, atletas_variacao_num \
            FROM " + self.nome_tabela + " where atletas_atleta_id = %s AND ANO = " + self.ano_base
        
        cursor.execute(sql, parametros)
        resultado = cursor.fetchone()
        return resultado
    
    def BuscarJogadorPorRodadaEId(self, rodada,jogador_id):
        cursor = self.connection.cursor(buffered=True)
        parametros = (str(rodada), str(jogador_id), )
        sql = "SELECT atletas_nome, atletas_atleta_id, atletas_posicao_id, atletas_preco_num, atletas_pontos_num, atletas_variacao_num \
            FROM " + self.nome_tabela + " where atletas_rodada_id = %s \
                AND  atletas_atleta_id = %s AND ANO = " + self.ano_base
        cursor.execute(sql, parametros)
        resultado = cursor.fetchone()
        return resultado

    def CalcularMediaScorePorRodadaEAno(self, rodada, ano, id_jogador):
        cursor = self.connection.cursor()
        #rodadas_formatado = ""
        #rodadas = range(1,rodada)
        #for r in rodadas:
        #    rodadas_formatado += r + ","
        #    
        #rodadas_formatado = rodadas_formatado[0:-1]

        if rodada is not None:
            parametros = (str(ano), str(id_jogador), str(rodada), )
            sql = "SELECT COALESCE(avg(atletas_pontos_num), 0) \
                FROM " + self.nome_tabela + " WHERE ANO=%s AND atletas_atleta_id = %s \
                AND atletas_rodada_id between 1 and %s  \
                AND (atletas_status_id = 'Provável' or atletas_status_id = 'Nulo') \
                GROUP BY atletas_atleta_id ORDER BY atletas_atleta_id asc"
        else:
            parametros = (str(ano), str(id_jogador), )
            sql = "SELECT COALESCE(avg(atletas_pontos_num), 0) \
                FROM " + self.nome_tabela + " WHERE ANO=%s AND atletas_atleta_id = %s \
                AND (atletas_status_id = 'Provável' or atletas_status_id = 'Nulo') \
                GROUP BY atletas_atleta_id ORDER BY atletas_atleta_id asc"


        cursor.execute(sql, parametros)
        resultado = cursor.fetchall()
        #print(resultado, "resultado")

        if len(resultado) == 0:
            return 0
        else:
            #Retorna o valor como número ao invés de tupla
            return resultado[0][0]