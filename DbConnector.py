import mysql.connector
from mysql.connector import Error

class DbConnector:
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost', database='cartolafc', user='root', password='')

    def InsertBanco(self,linha):
        # Variáveis para preparar a inserção no banco
        cursor = self.connection.cursor()
        '''
        add_item = "insert into valorizacao (local_id, atletas_nome, atletas_slug, atletas_apelido, atletas_foto, atletas_atleta_id,"\
                   "atletas_rodada_id, atletas_clube_id, atletas_posicao_id, atletas_status_id, atletas_pontos_num,"\
                   "atletas_preco_num, atletas_variacao_num, atletas_media_num, atletas_clube_id_full_name,"\
                   "FS, RB, PE, FC, G, FF, FT, FD, DD, GS, SG, A, CA, I, CV, PP, GC, DP)"\
                   "VALUES (%d,%s,%s,%s,%s,%d,%d,%d,%s,%s,%f,%f,%f,%f,%s,%d,%d,%d,%d,%d,%d,%d,%d,"\
                   "%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)"
        '''
        add_item = "insert into valorizacao (local_id, atletas_nome, atletas_slug, atletas_apelido, atletas_foto, atletas_atleta_id," \
                   "atletas_rodada_id, atletas_clube_id, atletas_posicao_id, atletas_status_id, atletas_pontos_num," \
                   "atletas_preco_num, atletas_variacao_num, atletas_media_num, atletas_clube_id_full_name," \
                   "FS, RB, PE, FC, G, FF, FT, FD, DD, GS, SG, A, CA, I, CV, PP, GC, DP)" \
                   "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                   "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        print(linha)
        cursor.execute(add_item, linha)
        self.connection.commit()

    def BuscarJogadoresPorRodadaEPosicao(self, rodada, posicao):
        # Variáveis para preparar a inserção no banco
        cursor = self.connection.cursor()
        sql = "SELECT atletas_nome, atletas_rodada_id, atletas_preco_num, atletas_variacao_num \
            FROM valorizacao where atletas_rodada_id = %s"

        cursor.execute(sql, (str(rodada), ))
        resultado = cursor.fetchall()
        return resultado

