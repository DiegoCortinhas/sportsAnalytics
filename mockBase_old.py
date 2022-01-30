def MockBase():
    # (nome_jogador, id_jogador, custo_jogador, score_jogador, valorizacao_jogador, posicao)

    #Base Mock Contem 3 Jogadores de cada posição e seus respectivos desempenhos nas 4 primeiras rodadas de 2018 e 2019
    return [
    [
        ('Rodrigo Pimpão Viana','68901','2.36','-1.6','-2.64','ata','2019'),
        ('Rodrigo Pimpão Viana','68901','2.11','2','-0.25','ata','2019'),
        ('Rodrigo Pimpão Viana','68901','1.87','0.5','-0.24','ata','2019'),
        ('Rodrigo Pimpão Viana','68901','1.33',-'1.2','-0.54','ata','2019'),
        ('Rodrigo Pimpão Viana','68901','6.48','0.4','-2.52','ata','2018'),
        ('Rodrigo Pimpão Viana','68901','3.66',-'2.4','-2.82','ata','2018'),
        ('Rodrigo Pimpão Viana','68901','3.44','0.7','-0.22','ata','2018'),
        ('Rodrigo Pimpão Viana','68901','3.63','1.7','0.19','ata','2018'),
        ('Everton Sousa Soares','86757','16.37','10.6','3.37','ata','2019'),
        ('Everton Sousa Soares','86757','14.78','-0.3','-1.59','ata','2019'),
        ('Everton Sousa Soares','86757','16.99','10.9','2.21','ata','2019'),
        ('Everton Sousa Soares','86757','15.03','0.6','-1.96','ata','2019'),
        ('Everton Sousa Soares','86757','11.71','10','4.71','ata','2018'),
        ('Everton Sousa Soares','86757','13.16','5','1.4','5','ata','2018'),
        ('Everton Sousa Soares','86757','13.16','0','0','ata','2018'),
        ('Everton Sousa Soares','86757','16.92','18.4','3.76','ata','2018'),
        ('Nicolás Federico López Alonso','84709','17.77','18.8','10.77','ata','2018'),
        ('Nicolás Federico López Alonso','84709','17.41','-0.9','-0.36','ata','2018'),
        ('Nicolás Federico López Alonso','84709','16.07','0.8','-1.34','ata','2018'),
        ('Nicolás Federico López Alonso','84709','16.07','0','0','ata','2018'),
        ('Nicolás Federico López Alonso','84709','22.0','0.0','0.0','ata','2019'),
        ('Nicolás Federico López Alonso','84709','18.43','5.8','-3.57','ata','2019'),
        ('Nicolás Federico López Alonso','84709','16.88','3.2','-1.55','ata','2019'),
        ('Nicolás Federico López Alonso','84709','17.3','6.8','0.42','ata','2019')
    ],
    [
        ('Victor Leandro Bagy','52950','6.24','-2','-4.76','gol','2019'),
        ('Victor Leandro Bagy','52950','5.41','3.4','-0.83','gol','2019'),
        ('Victor Leandro Bagy','52950','5.75','3.7','0.34','gol','2019'),
        ('Victor Leandro Bagy','52950','3.82','-4','-1.93','gol','2019'),
        ('Victor Leandro Bagy','52950','12.47','4.1','-1.53','gol','2018'),
        ('Victor Leandro Bagy','52950','10.35','1','-2.12','gol','2018'),
        ('Victor Leandro Bagy','52950','11.57','7'.'7','1.22','gol','2018'),
        ('Victor Leandro Bagy','52950','9.04','-4.3','-2.53','gol','2018'),
        ('Diego Alves Carreira','38509','9.71','1.1','-3.29','gol','2018'),
        ('Diego Alves Carreira','38509','9.71','0','0','gol','2018'),
        ('Diego Alves Carreira','38509','8.79','5.2','-0.92','gol','2018'),
        ('Diego Alves Carreira','38509','12.65','16.4','3.86','gol','2018'),
        ('Diego Alves Carreira','38509','5','0','0','gol','2019'),
        ('Diego Alves Carreira','38509','5','0','0','gol','2019'),
        ('Diego Alves Carreira','38509','5','0','0','gol','2019'),
        ('Diego Alves Carreira','38509','3.96','1','-1.04','gol','2019'),
        ('Marcelo Lomba do Nascimento','68872','9.02','2','-1.98','gol','2019'),
        ('Marcelo Lomba do Nascimento','68872','7.54','1','-1.48','gol','2019'),
        ('Marcelo Lomba do Nascimento','68872','8.11','4.5','0.57','gol','2019'),
        ('Marcelo Lomba do Nascimento','68872','8.29','4','0.18','gol','2019'),
        ('Marcelo Lomba do Nascimento','68872','7.72','5.2','1.72','gol','2018'),
        ('Marcelo Lomba do Nascimento','68872','7.72','0','0','gol','2018'),
        ('Marcelo Lomba do Nascimento','68872','7.72','0','0','gol','2018'),
        ('Marcelo Lomba do Nascimento','68872','7.72','0','0','gol','2018')
    ],

    [  
        ('Fagner Conserva Lemos','42500','12.06','0.5','-4.94','lat','2018'),
        ('Fagner Conserva Lemos','42500','14.11','13','2.05','lat','2018'),
        ('Fagner Conserva Lemos','42500','11.7','-0.3','-2.41','lat','2018'),
        ('Fagner Conserva Lemos','42500','11.7','0','0','lat','2018'),
        ('Fagner Conserva Lemos','42500','5.83','3.4','0.83','lat','2019'),
        ('Fagner Conserva Lemos','42500','11.32','14.1','5.49','lat','2019'),
        ('Fagner Conserva Lemos','42500','11.32','0','0','lat','2019'),
        ('Fagner Conserva Lemos','42500','11.27','6','-0.05','lat','2019'),
        ('Renê Rodrigues Martins','78445','8.74','0.6','-3.26','lat','2019'),
        ('Renê Rodrigues Martins','78445','6.02','-1.1','-2.72','lat','2019'),
        ('Renê Rodrigues Martins','78445','6.02','0','0','lat','2019'),
        ('Renê Rodrigues Martins','78445','6.02','0','0','lat','2019'),
        ('Renê Rodrigues Martins','78445','5.03','2.3','0.03','lat','2018'),
        ('Renê Rodrigues Martins','78445','8.15','9.4','3.12','lat','2018'),
        ('Renê Rodrigues Martins','78445','10.43','10.8','2.28','lat','2018'),
        ('Renê Rodrigues Martins','78445','11.73','9','1.3','lat','2018'),
        ('Iago Amaral Borduchi','97868','9.85','8.3','3.85','lat','2018'),
        ('Iago Amaral Borduchi','97868','9.73','1.1','-0.12','lat','2018'),
        ('Iago Amaral Borduchi','97868','9.72','3.1','-0.01','lat','2018'),
        ('Iago Amaral Borduchi','97868','8.95','-0.2','-0.77','lat','2018'),
        ('Iago Amaral Borduchi','97868','12','0','0','lat','2019'),
        ('Iago Amaral Borduchi','97868','8.68','0','-3.32','lat','2019'),
        ('Iago Amaral Borduchi','97868','8.82','3.9','0.14','lat','2019'),
        ('Iago Amaral Borduchi','97868','7.54','-0.8','-1.28','lat','2019')
        
    ],

    [
        ('Giorgian Daniel de Arrascaeta Benedetti','87863','11.45','1.5','-3.55','mei','2019'),
        ('Giorgian Daniel de Arrascaeta Benedetti','87863','13.75','11.6','2.3','mei','2019'),
        ('Giorgian Daniel de Arrascaeta Benedetti','87863','13.75','0','0','mei','2019'),
        ('Giorgian Daniel de Arrascaeta Benedetti','87863','13.75','0','0','mei','2019'),
        ('Giorgian Daniel de Arrascaeta Benedetti','87863','17.15','9.9','2.15','mei','2018'),
        ('Giorgian Daniel de Arrascaeta Benedetti','87863','15.74','2.1','-1.41','mei','2018'),
        ('Giorgian Daniel de Arrascaeta Benedetti','87863','15.74','0','0','mei','2018'),
        ('Giorgian Daniel de Arrascaeta Benedetti','87863','17.55','13.2','1.81','mei','2018'),
        ('Éverton Augusto de Barros Ribeiro','51772','2.89','-5.8','-7.11','mei','2018'),
        ('Éverton Augusto de Barros Ribeiro','51772','2.89','0','0','mei','2018'),
        ('Éverton Augusto de Barros Ribeiro','51772','2.47','4.6','-0.42','mei','2018'),
        ('Éverton Augusto de Barros Ribeiro','51772','4.72','9.8','2.25','mei','2018'),
        ('Éverton Augusto de Barros Ribeiro','51772','15.54','8'.'4','1.54','mei','2019'),
        ('Éverton Augusto de Barros Ribeiro','51772','13.93','0.6','-1.61','mei','2019'),
        ('Éverton Augusto de Barros Ribeiro','51772','13.93','0','0','mei','2019'),
        ('Éverton Augusto de Barros Ribeiro','51772','11.83','-0.3','-2.1','mei','2019'),
        ('Jean Mota Oliveira de Sousa','78548','8.61','5.5','1.61','mei','2018'),
        ('Jean Mota Oliveira de Sousa','78548','8.83','2.9','0.22','mei','2018'),
        ('Jean Mota Oliveira de Sousa','78548','8.83','0','0','mei','2018'),
        ('Jean Mota Oliveira de Sousa','78548','11.02','11.4','2.19','mei','2018'),
        ('Jean Mota Oliveira de Sousa','78548','10.96','3.8','-1.04','mei','2019'),
        ('Jean Mota Oliveira de Sousa','78548','9.03','0','-1.93','mei','2019'),
        ('Jean Mota Oliveira de Sousa','78548','8.4','1.2','-0.63','mei','2019'),
        ('Jean Mota Oliveira de Sousa','78548','7.66','0','-0.74','mei','2019'),
        ('Alex Paulo Menezes Santana','85465','10','0','0','mei','2019'),
        ('Alex Paulo Menezes Santana','85465','7.1','-0.3','-2.9','mei','2019'),
        ('Alex Paulo Menezes Santana','85465','9.43','9.7','2.33','mei','2019'),
        ('Alex Paulo Menezes Santana','85465','10.78','10','1.35','mei','2019'),
        ('Alex Paulo Menezes Santana','85465','3','0','0','mei','2018'),
        ('Alex Paulo Menezes Santana','85465','3','0','0','mei','2018'),
        ('Alex Paulo Menezes Santana','85465','3','0','0','mei','2018'),
        ('Alex Paulo Menezes Santana','85465','3','0','0','mei','2018'),

    ],

    [
        ('Abel Carlos da Silva Braga','40006','10.06','3.61','-0.94','tec','2018'),
        ('Abel Carlos da Silva Braga','40006','10.39','5.45','0.33','tec','2018'),
        ('Abel Carlos da Silva Braga','40006','10.21','3.85','-0.18','tec','2018'),
        ('Abel Carlos da Silva Braga','40006','10.8','4.75','0.59','tec','2018'),
        ('Abel Carlos da Silva Braga','40006','10.59','5.26','0.59','tec','2019'),
        ('Abel Carlos da Silva Braga','40006','10.48','2.98','-0.11','tec','2019'),
        ('Abel Carlos da Silva Braga','40006','9.85','1.79','-0.63','tec','2019'),
        ('Abel Carlos da Silva Braga','40006','10.28','4.3','0.43','tec','2019'),
        ('Renato Portaluppi','41929','11.47','4.53','-0.53','tec','2019'),
        ('Renato Portaluppi','41929','10.27','1.53','-1.2','tec','2019'),
        ('Renato Portaluppi','41929','11.07','5.94','0.8','tec','2019'),
        ('Renato Portaluppi','41929','11.16','4.76','0.09','tec','2019'),
        ('Renato Portaluppi','41929','15.36','7.29','0.36','tec','2018'),
        ('Renato Portaluppi','41929','14.75','4.47','-0.61','tec','2018'),
        ('Renato Portaluppi','41929','13.31','1.35','-1.44','tec','2018'),
        ('Renato Portaluppi','41929','15.21','9.02','1.9','tec','2018'),
        ('Odair Hellman','92273','8.92','7.95','3.92','tec','2018'),
        ('Odair Hellman','92273','9.08','1.35','0.16','tec','2018'),
        ('Odair Hellman','92273','9.85','5.25','0.77','tec','2018'),
        ('Odair Hellman','92273','9.47','1.75','-0.38','tec','2018'),
        ('Odair Hellman','92273','7.39','2.65','-0.61','tec','2019'),
        ('Odair Hellman','92273','8.35','5.16','0.96','tec','2019'),
        ('Odair Hellman','92273','8.11','2.62','-0.24','tec','2019'),
        ('Odair Hellman','92273','9.07','5.85','0.96','tec','2019')

    ],

    [
        ('Anderson Vital da Silva','60819','14.15','0.4','-5.85','zag','2019'),
        ('Anderson Vital da Silva','60819','14.95','10.6','0.8','zag','2019'),
        ('Anderson Vital da Silva','60819','15.63','8.7','0.68','zag','2019'),
        ('Anderson Vital da Silva','60819','16.62','9.6','0.99','zag','2019'),
        ('Anderson Vital da Silva','60819','5.99','2.7','-0.01','zag','2018'),
        ('Anderson Vital da Silva','60819','5.86','2.1','-0.13','zag','2018'),
        ('Anderson Vital da Silva','60819','5.86','0','0','zag','2018'),
        ('Anderson Vital da Silva','60819','9.69','15.8','3.83','zag','2018'),
        ('Igor Rabello da Costa','89493','13.92','9.2','2.92','zag','2018'),
        ('Igor Rabello da Costa','89493','11.92','-1.1','-2','zag','2018'),
        ('Igor Rabello da Costa','89493','10.13','-1.6','-1.79','zag','2018'),
        ('Igor Rabello da Costa','89493','11','4.2','0.87','zag','2018'),
        ('Igor Rabello da Costa','89493','12','0','0','zag','2019'),
        ('Igor Rabello da Costa','89493','10.07','3.2','-1.93','zag','2019'),
        ('Igor Rabello da Costa','89493','11.03','7.1','0.96','zag','2019'),
        ('Igor Rabello da Costa','89493','9.77','0.6','-1.26','zag','2019'),
        ('Réver Humberto Alves Araújo','52253','16','0','0','zag','2019'),
        ('Réver Humberto Alves Araújo','52253','12.23','1.5','-3.77','zag','2019'),
        ('Réver Humberto Alves Araújo','52253','11.14','1.8','-1.09','zag','2019'),
        ('Réver Humberto Alves Araújo','52253','11.15','3.6','0.01','zag','2019'),
        ('Réver Humberto Alves Araújo','52253','16.6','10.1','2.6','zag','2018'),
        ('Réver Humberto Alves Araújo','52253','18.02','8.3','1.42','zag','2018'),
        ('Réver Humberto Alves Araújo','52253','17.78','6.3','-0.24','zag','2018'),
        ('Réver Humberto Alves Araújo','52253','18.22','6','0.44','zag','2018'),
        ('Ernando Rodrigues Lopes','49651','5.86','0.5','-2.14','zag','2018'),
        ('Ernando Rodrigues Lopes','49651','4.14','-0.3','-1.72','zag','2018'),
        ('Ernando Rodrigues Lopes','49651','3.28','-0.9','-0.86','zag','2018'),
        ('Ernando Rodrigues Lopes','49651','4.91','6','1.63','zag','2018'),
        ('Ernando Rodrigues Lopes','49651','6.24','4','1.24','zag','2019'),
        ('Ernando Rodrigues Lopes','49651','9.14','8','2.9','zag','2019'),
        ('Ernando Rodrigues Lopes','49651','9.93','6','0.79','zag','2019'),
        ('Ernando Rodrigues Lopes','49651','8.82','0','-1.11','zag','2019')
    ]
]

def MockJ():
    retorno = [
        68901,86757,84709,52950,38509,68872,42500,78445,97868,87863,51772,78548,85465,40006,41929,92273,60819,89493,52253,49651
    ]
    return retorno


"""
'Glaybson Yago Souza Lisboa',80196,11.1,2,-2.9,'mei',2019),
'Glaybson Yago Souza Lisboa',80196,9.22,1.4,-1.88,'mei',2019),
'Glaybson Yago Souza Lisboa',80196,9.11,3.2,-0.11,'mei',2019),
'Glaybson Yago Souza Lisboa',80196,9.03,3,-0.08,'mei',2019),
'Glaybson Yago Souza Lisboa',80196,14.33,12.8,6.33,'lat',2018),
'Glaybson Yago Souza Lisboa',80196,14.15,1.1,-0.18,'lat',2018),
'Glaybson Yago Souza Lisboa',80196,14.15,0,0,'lat',2018),
'Glaybson Yago Souza Lisboa',80196,13.75,4.3,-0.4,'lat',2018), """