import mysql.connector
from mysql.connector import Error

class DbConnector:
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost', database='cartolafc', user='root', password='')
        self.nome_tabela = "valorizacao_new"
        #self.nome_tabela = "valorizacao_mock"
        self.ano_base = "2019"

    def InsertBanco(self,linha):
        # Variáveis para preparar a inserção no banco
        cursor = self.connection.cursor()
        add_item = "insert into " + self.nome_tabela + " (local_id, atletas_nome, atletas_slug, atletas_apelido, atletas_foto, atletas_atleta_id," \
                   "atletas_rodada_id, atletas_clube_id, atletas_posicao_id, atletas_status_id, atletas_pontos_num," \
                   "atletas_preco_num, atletas_variacao_num, atletas_media_num, atletas_clube_id_full_name, ANO)" \
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(add_item, linha)
        self.connection.commit()

    def BuscarJogadoresPorRodadaEPosicao(self, rodada, posicao = ""):
        cursor = self.connection.cursor()
        parametros = (str(rodada), )
        sql = "SELECT atletas_nome, atletas_atleta_id, atletas_preco_num, atletas_pontos_num, atletas_variacao_num, atletas_posicao_id \
            FROM " + self.nome_tabela + " where atletas_rodada_id = %s \
                AND ANO = " + self.ano_base + " AND atletas_pontos_num <> '0'"

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
        sql = "SELECT atletas_nome, atletas_atleta_id, atletas_preco_num, atletas_pontos_num, atletas_media_num \
            FROM " + self.nome_tabela + " where atletas_rodada_id = %s \
                AND ANO = " + self.ano_base + " AND atletas_pontos_num <> '0' order by atletas_posicao_id, atletas_atleta_id;"
        
        cursor.execute(sql, parametros)
        resultado = cursor.fetchall()
        return resultado


    def BuscarJogadorPorId(self, jogador_id):
        cursor = self.connection.cursor(buffered=True)
        parametros = (str(jogador_id), )
        sql = "SELECT atletas_nome, atletas_atleta_id, atletas_posicao_id, atletas_preco_num, atletas_media_num, atletas_variacao_num \
            FROM " + self.nome_tabela + " where atletas_atleta_id = %s AND ANO = " + self.ano_base
        
        cursor.execute(sql, parametros)
        resultado = cursor.fetchone()
        return resultado
    
    def BuscarJogadorPorRodadaEId(self, rodada,jogador_id):
        cursor = self.connection.cursor(buffered=True)
        parametros = (str(rodada), str(jogador_id), )
        sql = "SELECT atletas_nome, atletas_atleta_id, atletas_posicao_id, atletas_preco_num, atletas_pontos_num, atletas_media_num \
            FROM " + self.nome_tabela + " where atletas_rodada_id = %s AND atletas_pontos_num <> '0' \
                AND  atletas_atleta_id = %s AND ANO = " + self.ano_base
        cursor.execute(sql, parametros)
        resultado = cursor.fetchone()
        return resultado

    def BuscarJogadorComMenorCustoProximaRodada(self, rodada, posicao):
        cursor = self.connection.cursor()
        proxima_rodada = rodada + 1
        parametros = (str(proxima_rodada), posicao, str(proxima_rodada), posicao)


        sql = "SELECT atletas_nome, atletas_atleta_id, atletas_posicao_id, atletas_preco_num, atletas_pontos_num, atletas_media_num \
            FROM " + self.nome_tabela + " where atletas_rodada_id = %s AND atletas_pontos_num <> '0' \
             AND ANO = " + self.ano_base + " AND atletas_posicao_id = %s"
        
        sql_menor_custo_proxima_rodada = " AND atletas_preco_num = (SELECT MIN(cast(atletas_preco_num as double)) from " + self.nome_tabela + " where atletas_rodada_id = %s AND atletas_pontos_num <> '0' AND ANO = " + self.ano_base + " AND atletas_posicao_id = %s)"

        sql = sql + sql_menor_custo_proxima_rodada
        cursor.execute(sql, parametros)
        resultado = cursor.fetchall()

        if len(resultado) == 0:
            return None
        else:
            return resultado[0]

    def CalcularMediaScorePorRodadaEAno(self, rodada, ano, id_jogador):
        cursor = self.connection.cursor()
        if rodada is not None:
            parametros = (str(ano), str(id_jogador), str(rodada), )
            sql = "SELECT atletas_media_num \
                FROM " + self.nome_tabela + " WHERE ANO=%s AND atletas_atleta_id = %s \
                AND atletas_rodada_id between 1 and %s  AND atletas_pontos_num <> '0'\
                ORDER BY atletas_atleta_id asc"
        else:
            parametros = (str(ano), str(id_jogador), )
            sql = "SELECT atletas_media_num \
                FROM " + self.nome_tabela + " WHERE ANO=%s AND atletas_atleta_id = %s \
                AND atletas_rodada_id = 38 AND atletas_pontos_num <> '0'\
                ORDER BY atletas_atleta_id asc"

        cursor.execute(sql, parametros)
        resultado = cursor.fetchall()
        
        if len(resultado) == 0:
            return [(0,)]
        else:
            return resultado

    def InserirMedia(self, id_jogador, rodada, media_rodadas_anteriores, media_total, ano_base_calculo):
        cursor = self.connection.cursor()
        
        parametros = (str(id_jogador), str(rodada), str(media_rodadas_anteriores), str(media_total), str(ano_base_calculo))
        
        sql = "INSERT INTO valorizacao_medias_rodadas_anteriores(id_jogador, rodada_atual, media_rodadas_anteriores, media_total, ano) \
                VALUES(%s, %s, %s, %s, %s)"
        cursor.execute(sql, parametros)
        self.connection.commit()

    def BuscarMediaJogadorPorRodadaEAno(self, id_jogador, rodada, ano):

        cursor = self.connection.cursor()
        parametros = (str(id_jogador), str(ano), str(rodada))
        if rodada is not None:
            sql = "SELECT media_rodadas_anteriores, media_total, ano FROM valorizacao_medias_rodadas_anteriores \
                WHERE id_jogador = %s AND ano = %s AND rodada_atual = %s"
        # Se nÃo receber a rodada, retorna toda a média de 2018 do jogador
        else:
            sql = "SELECT media_rodadas_anteriores, media_total, ano FROM valorizacao_medias_rodadas_anteriores \
                WHERE id_jogador = %s AND ano = %s AND rodada_atual = 38"

        cursor.execute(sql, parametros)
        resultado = cursor.fetchall()
        return resultado