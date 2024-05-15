-- SQLite
DROP TABLE IF EXISTS tb_os_inst;
DROP TABLE IF EXISTS tb_template_lista_inst;
DROP TABLE IF EXISTS tb_ids_inst;
DROP TABLE IF EXISTS tb_rev_info;
DROP TABLE IF EXISTS tb_ids_inst_rev;
DROP TABLE IF EXISTS tb_operational_list_inst;


CREATE TABLE tb_os_inst (
    tb_os_inst_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tb_os_inst_os_num VARCHAR(15) NOT NULL UNIQUE
);


CREATE TABLE tb_ids_inst (
    tb_ids_inst_id INTEGER PRIMARY KEY AUTOINCREMENT,
    --tb_ids_inst_id_os_init INTEGER REFERENCES tb_os_inst(tb_os_inst_id),
    tb_ids_inst_id_universal VARCHAR(255) NOT NULL UNIQUE
);


CREATE TABLE tb_rev_info (
    tb_rev_info_id INTEGER PRIMARY KEY AUTOINCREMENT,
    --tb_rev_info_id_os_int INTEGER REFERENCES tb_os_inst(tb_os_inst_id),
    tb_rev_info_num INTEGER NOT NULL UNIQUE,
    tb_rev_info_data DATETIME
);


CREATE TABLE tb_ids_inst_rev (
    tb_ids_inst_rev_id INTEGER PRIMARY KEY AUTOINCREMENT,
    --tb_ids_inst_rev_id_rev_info INTEGER REFERENCES tb_rev_info(tb_rev_info_id),
    --tb_ids_inst_rev_id_ids_inst INTEGER REFERENCES tb_ids_inst(tb_ids_inst_id),
    tb_ids_inst_rev_id_exist BOOL
);


CREATE TABLE tb_operational_list_inst (
    tb_oper_li_id INTEGER PRIMARY KEY AUTOINCREMENT,
    --tb_oper_li_id_ids_inst INTEGER REFERENCES tb_ids_inst(tb_ids_inst_id),
    --tb_oper_li_id_tmp_li INTEGER REFERENCES tb_template_lista_inst(tb_temp_li_id),
    tb_oper_li_info VARCHAR(255) NOT NULL
);


CREATE TABLE tb_template_lista_inst (
    tb_temp_li_id INTEGER PRIMARY KEY AUTOINCREMENT,
    --tb_temp_li_id_os_inst INTEGER REFERENCES tb_os_inst(tb_os_inst_id),
    tb_temp_li_coluna VARCHAR(15) NOT NULL UNIQUE,
    tb_temp_li_id_rev_temp INTEGER UNIQUE,
    tb_temp_li_ordem INTEGER,
    tb_temp_li_linha INTEGER,
    tb_temp_li_elemento VARCHAR(15) NOT NULL UNIQUE,
    tb_temp_li_tipo_dado ENUM
);



