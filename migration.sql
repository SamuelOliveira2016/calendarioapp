BEGIN;
--
-- Create model Areatecnologica
--
CREATE TABLE "webpages_areatecnologica" ("id" bigserial NOT NULL PRIMARY KEY, "nome" varchar(255) NOT NULL, "descricao" text NOT NULL);
--
-- Create model Aula
--
CREATE TABLE "webpages_aula" ("id" bigserial NOT NULL PRIMARY KEY, "horario_inicio" time NOT NULL, "horario_fim" time NOT NULL);
--
-- Create model CalendarioAcademico
--
CREATE TABLE "webpages_calendarioacademico" ("id" bigserial NOT NULL PRIMARY KEY, "ano_letivo" integer NOT NULL, "semestre" integer NOT NULL, "inicio" date NOT NULL, "termino" date NOT NULL);
--
-- Create model Curso
--
CREATE TABLE "webpages_curso" ("id" bigserial NOT NULL PRIMARY KEY, "nome" varchar(100) NOT NULL, "quantidade_horas_total" integer NULL);
CREATE TABLE "webpages_curso_areatecnologica" ("id" bigserial NOT NULL PRIMARY KEY, "curso_id" bigint NOT NULL, "areatecnologica_id" bigint NOT NULL);
--
-- Create model Infraestrutura
--
CREATE TABLE "webpages_infraestrutura" ("id" bigserial NOT NULL PRIMARY KEY, "nome" varchar(50) NULL, "tipo" varchar(20) NOT NULL, "capacidade" integer NULL);
--
-- Create model Pessoa
--
CREATE TABLE "webpages_pessoa" ("id" bigserial NOT NULL PRIMARY KEY, "nome" varchar(255) NOT NULL, "telefone" varchar(20) NULL, "email" varchar(254) NOT NULL);
--
-- Create model Tipocurso
--
CREATE TABLE "webpages_tipocurso" ("id" bigserial NOT NULL PRIMARY KEY, "nome_tipo_curso" varchar(20) NOT NULL UNIQUE);
--
-- Create model Vinculo
--
CREATE TABLE "webpages_vinculo" ("id" bigserial NOT NULL PRIMARY KEY, "vinculo" varchar(20) NOT NULL, "pessoa_id" bigint NOT NULL);
--
-- Create model UnidadeCurricular
--
CREATE TABLE "webpages_unidadecurricular" ("id" bigserial NOT NULL PRIMARY KEY, "nome" varchar(100) NOT NULL, "carga_horaria" integer NULL, "capacidadesSociais" text NOT NULL, "capacidadeTecnicaFundamentos" text NOT NULL, "horas_sala_aula" integer NULL, "horas_laboratorio" integer NULL, "horas_oficina" integer NULL, "curso_id" bigint NULL);
--
-- Create model Professor
--
CREATE TABLE "webpages_professor" ("id" serial NOT NULL PRIMARY KEY, "nif" varchar(20) NOT NULL UNIQUE, "nivel" varchar(100) NULL, "pessoa_id" bigint NULL);
CREATE TABLE "webpages_professor_cursos" ("id" bigserial NOT NULL PRIMARY KEY, "professor_id" integer NOT NULL, "curso_id" bigint NOT NULL);
--
-- Create model HoratrabProf
--
CREATE TABLE "webpages_horatrabprof" ("id" bigserial NOT NULL PRIMARY KEY, "horatrabIni" time NOT NULL, "horatrabFim" time NOT NULL, "selected_days" varchar(3)[] NOT NULL, "quanthorames" integer NOT NULL, "pessoa_id" bigint NULL);
--
-- Create model Evento
--
CREATE TABLE "webpages_evento" ("id" bigserial NOT NULL PRIMARY KEY, "nome" varchar(100) NOT NULL, "data" date NOT NULL, "descricao" text NOT NULL, "calendario_academico_id" bigint NOT NULL);
--
-- Create model DiaLetivo
--
CREATE TABLE "webpages_dialetivo" ("id" bigserial NOT NULL PRIMARY KEY, "data" date NOT NULL, "e_dia_de_aula" boolean NOT NULL, "observacao" text NULL, "calendario_academico_id" bigint NOT NULL);
--
-- Create model CursoUnidadeCurricularProfessor
--
CREATE TABLE "webpages_cursounidadecurricularprofessor" ("id" bigserial NOT NULL PRIMARY KEY, "curso_id" bigint NOT NULL, "unidade_curricular_id" bigint NOT NULL);
CREATE TABLE "webpages_cursounidadecurricularprofessor_professores" ("id" bigserial NOT NULL PRIMARY KEY, "cursounidadecurricularprofessor_id" bigint NOT NULL, "professor_id" integer NOT NULL);
--
-- Add field tipo_curso to curso
--
ALTER TABLE "webpages_curso" ADD COLUMN "tipo_curso_id" bigint NULL CONSTRAINT "webpages_curso_tipo_curso_id_ab42ed22_fk_webpages_tipocurso_id" REFERENCES "webpages_tipocurso"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "webpages_curso_tipo_curso_id_ab42ed22_fk_webpages_tipocurso_id" IMMEDIATE;
--
-- Create model CalendarioAula
--
CREATE TABLE "webpages_calendarioaula" ("id" bigserial NOT NULL PRIMARY KEY, "aula_id" bigint NOT NULL, "dia_letivo_id" bigint NOT NULL);
--
-- Add field curso_uc_professor to aula
--
ALTER TABLE "webpages_aula" ADD COLUMN "curso_uc_professor_id" bigint NOT NULL CONSTRAINT "webpages_aula_curso_uc_professor_i_6874e31d_fk_webpages_" REFERENCES "webpages_cursounidadecurricularprofessor"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "webpages_aula_curso_uc_professor_i_6874e31d_fk_webpages_" IMMEDIATE;
--
-- Add field infraestrutura to aula
--
ALTER TABLE "webpages_aula" ADD COLUMN "infraestrutura_id" bigint NOT NULL CONSTRAINT "webpages_aula_infraestrutura_id_785877bb_fk_webpages_" REFERENCES "webpages_infraestrutura"("id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "webpages_aula_infraestrutura_id_785877bb_fk_webpages_" IMMEDIATE;
ALTER TABLE "webpages_curso_areatecnologica" ADD CONSTRAINT "webpages_curso_areatecno_curso_id_areatecnologica_9675f7e4_uniq" UNIQUE ("curso_id", "areatecnologica_id");
ALTER TABLE "webpages_curso_areatecnologica" ADD CONSTRAINT "webpages_curso_areat_curso_id_aee3acd7_fk_webpages_" FOREIGN KEY ("curso_id") REFERENCES "webpages_curso" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "webpages_curso_areatecnologica" ADD CONSTRAINT "webpages_curso_areat_areatecnologica_id_4e3be597_fk_webpages_" FOREIGN KEY ("areatecnologica_id") REFERENCES "webpages_areatecnologica" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "webpages_curso_areatecnologica_curso_id_aee3acd7" ON "webpages_curso_areatecnologica" ("curso_id");
CREATE INDEX "webpages_curso_areatecnologica_areatecnologica_id_4e3be597" ON "webpages_curso_areatecnologica" ("areatecnologica_id");
CREATE INDEX "webpages_tipocurso_nome_tipo_curso_bc3460ae_like" ON "webpages_tipocurso" ("nome_tipo_curso" varchar_pattern_ops);
ALTER TABLE "webpages_vinculo" ADD CONSTRAINT "webpages_vinculo_pessoa_id_5016ba6f_fk_webpages_pessoa_id" FOREIGN KEY ("pessoa_id") REFERENCES "webpages_pessoa" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "webpages_vinculo_pessoa_id_5016ba6f" ON "webpages_vinculo" ("pessoa_id");
ALTER TABLE "webpages_unidadecurricular" ADD CONSTRAINT "webpages_unidadecurr_curso_id_ba22e121_fk_webpages_" FOREIGN KEY ("curso_id") REFERENCES "webpages_curso" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "webpages_unidadecurricular_curso_id_ba22e121" ON "webpages_unidadecurricular" ("curso_id");
ALTER TABLE "webpages_professor" ADD CONSTRAINT "webpages_professor_pessoa_id_92bb2ff6_fk_webpages_pessoa_id" FOREIGN KEY ("pessoa_id") REFERENCES "webpages_pessoa" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "webpages_professor_nif_7e23a40a_like" ON "webpages_professor" ("nif" varchar_pattern_ops);
CREATE INDEX "webpages_professor_pessoa_id_92bb2ff6" ON "webpages_professor" ("pessoa_id");
ALTER TABLE "webpages_professor_cursos" ADD CONSTRAINT "webpages_professor_cursos_professor_id_curso_id_06e37864_uniq" UNIQUE ("professor_id", "curso_id");
ALTER TABLE "webpages_professor_cursos" ADD CONSTRAINT "webpages_professor_c_professor_id_d00fecbd_fk_webpages_" FOREIGN KEY ("professor_id") REFERENCES "webpages_professor" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "webpages_professor_cursos" ADD CONSTRAINT "webpages_professor_c_curso_id_2d9c61bb_fk_webpages_" FOREIGN KEY ("curso_id") REFERENCES "webpages_curso" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "webpages_professor_cursos_professor_id_d00fecbd" ON "webpages_professor_cursos" ("professor_id");
CREATE INDEX "webpages_professor_cursos_curso_id_2d9c61bb" ON "webpages_professor_cursos" ("curso_id");
ALTER TABLE "webpages_horatrabprof" ADD CONSTRAINT "webpages_horatrabprof_pessoa_id_5b037f29_fk_webpages_pessoa_id" FOREIGN KEY ("pessoa_id") REFERENCES "webpages_pessoa" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "webpages_horatrabprof_pessoa_id_5b037f29" ON "webpages_horatrabprof" ("pessoa_id");
ALTER TABLE "webpages_evento" ADD CONSTRAINT "webpages_evento_calendario_academico_76cbe126_fk_webpages_" FOREIGN KEY ("calendario_academico_id") REFERENCES "webpages_calendarioacademico" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "webpages_evento_calendario_academico_id_76cbe126" ON "webpages_evento" ("calendario_academico_id");
ALTER TABLE "webpages_dialetivo" ADD CONSTRAINT "webpages_dialetivo_calendario_academico_35d1695f_fk_webpages_" FOREIGN KEY ("calendario_academico_id") REFERENCES "webpages_calendarioacademico" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "webpages_dialetivo_calendario_academico_id_35d1695f" ON "webpages_dialetivo" ("calendario_academico_id");
ALTER TABLE "webpages_cursounidadecurricularprofessor" ADD CONSTRAINT "webpages_cursounidad_curso_id_a73d347c_fk_webpages_" FOREIGN KEY ("curso_id") REFERENCES "webpages_curso" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "webpages_cursounidadecurricularprofessor" ADD CONSTRAINT "webpages_cursounidad_unidade_curricular_i_9f820d46_fk_webpages_" FOREIGN KEY ("unidade_curricular_id") REFERENCES "webpages_unidadecurricular" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "webpages_cursounidadecurricularprofessor_curso_id_a73d347c" ON "webpages_cursounidadecurricularprofessor" ("curso_id");
CREATE INDEX "webpages_cursounidadecurri_unidade_curricular_id_9f820d46" ON "webpages_cursounidadecurricularprofessor" ("unidade_curricular_id");
ALTER TABLE "webpages_cursounidadecurricularprofessor_professores" ADD CONSTRAINT "webpages_cursounidadecur_cursounidadecurricularpr_6a45e64d_uniq" UNIQUE ("cursounidadecurricularprofessor_id", "professor_id");
ALTER TABLE "webpages_cursounidadecurricularprofessor_professores" ADD CONSTRAINT "webpages_cursounidad_cursounidadecurricul_ad038ea3_fk_webpages_" FOREIGN KEY ("cursounidadecurricularprofessor_id") REFERENCES "webpages_cursounidadecurricularprofessor" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "webpages_cursounidadecurricularprofessor_professores" ADD CONSTRAINT "webpages_cursounidad_professor_id_426a1312_fk_webpages_" FOREIGN KEY ("professor_id") REFERENCES "webpages_professor" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "webpages_cursounidadecurri_cursounidadecurricularprof_ad038ea3" ON "webpages_cursounidadecurricularprofessor_professores" ("cursounidadecurricularprofessor_id");
CREATE INDEX "webpages_cursounidadecurri_professor_id_426a1312" ON "webpages_cursounidadecurricularprofessor_professores" ("professor_id");
CREATE INDEX "webpages_curso_tipo_curso_id_ab42ed22" ON "webpages_curso" ("tipo_curso_id");
ALTER TABLE "webpages_calendarioaula" ADD CONSTRAINT "webpages_calendarioaula_aula_id_ae982a17_fk_webpages_aula_id" FOREIGN KEY ("aula_id") REFERENCES "webpages_aula" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "webpages_calendarioaula" ADD CONSTRAINT "webpages_calendarioa_dia_letivo_id_ab6a6404_fk_webpages_" FOREIGN KEY ("dia_letivo_id") REFERENCES "webpages_dialetivo" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "webpages_calendarioaula_aula_id_ae982a17" ON "webpages_calendarioaula" ("aula_id");
CREATE INDEX "webpages_calendarioaula_dia_letivo_id_ab6a6404" ON "webpages_calendarioaula" ("dia_letivo_id");
CREATE INDEX "webpages_aula_curso_uc_professor_id_6874e31d" ON "webpages_aula" ("curso_uc_professor_id");
CREATE INDEX "webpages_aula_infraestrutura_id_785877bb" ON "webpages_aula" ("infraestrutura_id");
COMMIT;
