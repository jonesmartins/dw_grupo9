CREATE TABLE IF NOT EXISTS `casos_em_hospitais` (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  casos_em_hospitais INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `capacidade_teste_profissionais` (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  capacidade_teste_profissionais INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `capacidade_teste_populacao` (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  capacidade_teste_populacao INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `capacidade_teste_anticorpos` (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  capacidade_teste_anticorpos INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `leitos_com_respiradores_ocupados` (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  leitos INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `admissoes_em_hospitais` (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  admissoes INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `capacidade_planejada` (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  capacidade_planejada INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `novos_testes` (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  numero_de_testes INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `pessoas_vacinadas_dose_1` (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  pessoas_vacinadas_dose_1 INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `pessoas_vacinadas_dose_2` (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  pessoas_vacinadas_dose_2 INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS `registro` (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  data DATE NOT NULL,
  casos_em_hospitais_id INTEGER NOT NULL,
  capacidade_teste_profissionais_id INTEGER NOT NULL,
  capacidade_teste_populacao_id INTEGER NOT NULL,
  capacidade_teste_anticorpos_id INTEGER NOT NULL,
  leitos_com_respiradores_ocupados_id INTEGER NOT NULL,
  admissoes_em_hospitais_id INTEGER NOT NULL,
  capacidade_planejada_id INTEGER NOT NULL,
  novos_testes_id INTEGER NOT NULL,
  pessoas_vacinadas_dose_1_id INTEGER NOT NULL,
  pessoas_vacinadas_dose_2_id INTEGER NOT NULL,
  FOREIGN KEY (casos_em_hospitais_id) REFERENCES casos_em_hospitais(id) ON DELETE CASCADE,
  FOREIGN KEY (capacidade_teste_profissionais_id) REFERENCES capacidade_teste_profissionais(id) ON DELETE CASCADE,
  FOREIGN KEY (capacidade_teste_populacao_id) REFERENCES capacidade_teste_populacao(id) ON DELETE CASCADE,
  FOREIGN KEY (capacidade_teste_anticorpos_id) REFERENCES capacidade_teste_anticorpos(id) ON DELETE CASCADE,
  FOREIGN KEY (leitos_com_respiradores_ocupados_id) REFERENCES leitos_com_respiradores_ocupados(id) ON DELETE CASCADE,
  FOREIGN KEY (admissoes_em_hospitais_id) REFERENCES admissoes_em_hospitais(id) ON DELETE CASCADE,
  FOREIGN KEY (capacidade_planejada_id) REFERENCES capacidade_planejada(id) ON DELETE CASCADE,
  FOREIGN KEY (novos_testes_id) REFERENCES novos_testes(id) ON DELETE CASCADE,
  FOREIGN KEY (pessoas_vacinadas_dose_1_id) REFERENCES pessoas_vacinadas_dose_1(id) ON DELETE CASCADE,
  FOREIGN KEY (pessoas_vacinadas_dose_2_id) REFERENCES pessoas_vacinadas_dose_2(id) ON DELETE CASCADE
);
