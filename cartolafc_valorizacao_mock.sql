insert into valorizacao_mock (atletas_nome, atletas_atleta_id, atletas_preco_num, atletas_pontos_num, atletas_media_num, atletas_posicao_id, atletas_rodada_id, ano) SELECT atletas_nome, atletas_atleta_id, 
cast(atletas_preco_num as char), cast(atletas_pontos_num as char), cast(atletas_media_num as char), atletas_posicao_id, atletas_rodada_id, ano 
FROM `valorizacao_new` 
where atletas_atleta_id in (68901,86757,84709,52950,38509,68872,42500,78445,97868,87863,51772,78548,85465,40006,41929,92273,60819,89493,52253,49651,99891,73896,88669,69012,98412,72018,101846,93797,37662,54395,54395,95798,37246,79437,38515,51495,91772) 
and atletas_rodada_id in (1,2,3,4,38) order by atletas_atleta_id;