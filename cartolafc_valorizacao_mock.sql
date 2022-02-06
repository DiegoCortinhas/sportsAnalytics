insert into valorizacao_mock (atletas_nome, atletas_atleta_id, atletas_preco_num, atletas_pontos_num, atletas_media_num, atletas_posicao_id, atletas_rodada_id, ano) SELECT atletas_nome, atletas_atleta_id, 
cast(atletas_preco_num as char), cast(atletas_pontos_num as char), cast(atletas_media_num as char), atletas_posicao_id, atletas_rodada_id, ano 
FROM `valorizacao_new` 
where atletas_atleta_id in (68901,86757,84709,52950,38509,68872,42500,78445,97868,87863,51772,78548,85465,40006,41929,92273,60819,89493,52253,49651,99891,73896,88669,69012,98412,72018,101846,93797,37662,54395,
95798,37246,79437,38515,51495,91772,83817,83257,78117,73741,95799,91607,62121,82453,95466,63110,78850,90444,91888,38229,
80393,92496,77570,50301,50307,38648,98706,98057,70800,84930,51415,87225,91573,69014,80853) 
and atletas_rodada_id in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38) order by atletas_atleta_id;

