DROP TABLE IF EXISTS tb_local_ocupacao;
DROP TABLE IF EXISTS tb_dim_saida;
DROP TABLE IF EXISTS tb_lg_minima;

CREATE TABLE tb_local_ocupacao (
    tb_local_ocupacao_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    tb_local_ocupacao_grupo TEXT NOT NULL,
    tb_local_ocupacao_ocupacao TEXT NOT NULL,
    tb_local_ocupacao_divisao TEXT NOT NULL,
    tb_local_ocupacao_descricao TEXT NOT NULL,
    tb_local_ocupacao_exemplos TEXT NOT NULL,
    UNIQUE (tb_local_ocupacao_grupo, tb_local_ocupacao_ocupacao, tb_local_ocupacao_divisao, tb_local_ocupacao_descricao, tb_local_ocupacao_exemplos)
);


CREATE TABLE tb_dim_saida (
    tb_dim_saida_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    tb_dim_saida_id_grupo INTEGER REFERENCES tb_local_ocupacao(tb_local_ocupacao_id),
    tb_dim_saida_capacidade TEXT NOT NULL,
    tb_dim_saida_variavel TEXT NOT NULL,
    tb_dim_saida_formula TEXT NOT NULL,
    tb_dim_saida_descargas INT NOT NULL,
    tb_dim_saida_escadas INT NOT NULL,
    tb_dim_saida_portas INT NOT NULL,
    UNIQUE (tb_dim_saida_id_grupo)
);


CREATE TABLE tb_lg_minima (
    tb_lg_minima_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    tb_lg_minima_n_min INTEGER,
    tb_lg_minima_n_max INTEGER,
    tb_lg_minima_valor INTEGER NOT NULL
);

