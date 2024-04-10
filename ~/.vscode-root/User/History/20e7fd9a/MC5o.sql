CREATE OR REPLACE FUNCTION periodo_after_update()
RETURNS TRIGGER AS $ $
DECLARE aula_count INT;
tempo_aula_min INT;
i INT;
horaInicio TIME;
horaFim TIME;
id_intervalo INT;
hora_inicio_intervalo_M TIME;
hora_fim_intervalo_M TIME;
hora_inicio_intervalo_t TIME;
hora_fim_intervalo_t TIME;
hora_inicio_intervalo_n TIME;
hora_fim_intervalo_n TIME;
hora_inicio_intervalo_a TIME;
hora_fim_intervalo_a TIME;
TURNO INT;
id_intervalo_M INT DEFAULT 0;
id_intervalo_t INT DEFAULT 0;
id_intervalo_n INT DEFAULT 0;
id_intervalo_a INT DEFAULT 0;
BEGIN
  IF
    NEW.aulasPorDia IS NOT NULL
  THEN
    aula_count: = NEW.aulasPorDia;
    tempo_aula_min: = NEW.tempo_aula_min;
    SELECT
      COALESCE(
        CAST(
          SUBSTRING(
            NEW.turno
            , 1
            , 1
          ) AS INTEGER
        )
        , 0
      )
    INTO
      TURNO
    FROM
      PERIODO
    WHERE
      PERIODO.id = NEW.id;
    horaInicio: = CASE
      WHEN TURNO = 1 THEN '07:30:00'
      WHEN TURNO = 2 THEN '13:00:00'
      WHEN TURNO = 3 THEN '19:00:00'
      ELSE NULL
    END;
    DELETE FROM
      webpages_periododetalhe
    WHERE
      periodo_id = NEW.periodo_id;
    i: = 1;
    WHILE i <= aula_count DO
      horaFim: = horaInicio + (interval '1 minute' * tempo_aula_min);
      INSERT INTO
        webpages_periododetalhe (
          periodo_id
          , tipoRegistro
          , horaInicio
          , horaFim
          , dataInicio
          , dataFim
        )
      VALUES
        (
          NEW.periodo_id
          , 1
          , horaInicio
          , horaFim
          , NULL
          , NULL
        );
      horaInicio: = horaFim;
      SELECT
        webpages_horaintervalo.id
        , webpages_horaintervalo.horaInicio
        , webpages_horaintervalo.horaFim
      INTO
        id_intervalo_M
        , hora_inicio_intervalo_M
        , hora_fim_intervalo_M
      FROM
        webpages_horaintervalo
        LEFT JOIN webpages_periodointervalo
      ON webpages_periodointervalo.id = webpages_horaintervalo.id
      WHERE
        webpages_periodointervalo.periodo = 1
        AND webpages_periodointervalo.idPeriodo_id = NEW.periodo_id
        AND webpages_horaintervalo.horaInicio = horaFim;
      IF id_intervalo_M > 0 THEN
        INSERT INTO
          webpages_periododetalhe (
            periodo_id
            , tipoRegistro
            , horaInicio
            , horaFim
            , dataInicio
            , dataFim
          )
        VALUES
          (
            NEW.periodo_id
            , 2
            , hora_inicio_intervalo_M
            , hora_fim_intervalo_M
            , NULL
            , NULL
          );
        horaInicio: = hora_fim_intervalo_M;
        id_intervalo_M: = 0;
      END IF;
      SELECT
        webpages_horaintervalo.id
        , webpages_horaintervalo.horaInicio
        , webpages_horaintervalo.horaFim
      INTO
        id_intervalo_t
        , hora_inicio_intervalo_t
        , hora_fim_intervalo_t
      FROM
        webpages_horaintervalo
        LEFT JOIN webpages_periodointervalo
      ON webpages_periodointervalo.id = webpages_horaintervalo.id
      WHERE
        webpages_periodointervalo.periodo = 2
        AND webpages_periodointervalo.idPeriodo_id = NEW.periodo_id
        AND webpages_horaintervalo.horaInicio = horaFim;
      IF id_intervalo_t > 0 THEN
        INSERT INTO
          webpages_periododetalhe (
            periodo_id
            , tipoRegistro
            , horaInicio
            , horaFim
            , dataInicio
            , dataFim
          )
        VALUES
          (
            NEW.periodo_id
            , 2
            , hora_inicio_intervalo_t
            , hora_fim_intervalo_t
            , NULL
            , NULL
          );
        horaInicio: = hora_fim_intervalo_t;
        id_intervalo_t: = 0;
      END IF;
      SELECT
        webpages_horaintervalo.id
        , webpages_horaintervalo.horaInicio
        , webpages_horaintervalo.horaFim
      INTO
        id_intervalo_n
        , hora_inicio_intervalo_n
        , hora_fim_intervalo_n
      FROM
        webpages_horaintervalo
        LEFT JOIN webpages_periodointervalo
      ON webpages_periodointervalo.id = webpages_horaintervalo.id
      WHERE
        webpages_periodointervalo.periodo = 3
        AND webpages_periodointervalo.idPeriodo_id = NEW.periodo_id
        AND webpages_horaintervalo.horaInicio = horaFim;
      IF id_intervalo_n > 0 THEN
        INSERT INTO
          webpages_periododetalhe (
            periodo_id
            , tipoRegistro
            , horaInicio
            , horaFim
            , dataInicio
            , dataFim
          )
        VALUES
          (
            NEW.periodo_id
            , 2
            , hora_inicio_intervalo_n
            , hora_fim_intervalo_n
            , NULL
            , NULL
          );
        horaInicio: = hora_fim_intervalo_n;
        id_intervalo_n: = 0;
      END IF;
      SELECT
        webpages_horaintervalo.id
        , webpages_horaintervalo.horaInicio
        , webpages_horaintervalo.horaFim
      INTO
        id_intervalo_a
        , hora_inicio_intervalo_a
        , hora_fim_intervalo_a
      FROM
        webpages_horaintervalo
        LEFT JOIN webpages_periodointervalo
      ON webpages_periodointervalo.id = webpages_horaintervalo.id
      WHERE
        webpages_periodointervalo.periodo = 4
        AND webpages_periodointervalo.idPeriodo_id = NEW.periodo_id
        AND webpages_horaintervalo.horaInicio = horaFim;
      IF id_intervalo_a > 0 THEN
        INSERT INTO
          webpages_periododetalhe (
            periodo_id
            , tipoRegistro
            , horaInicio
            , horaFim
            , dataInicio
            , dataFim
          )
        VALUES
          (
            NEW.periodo_id
            , 2
            , hora_inicio_intervalo_a
            , hora_fim_intervalo_a
            , NULL
            , NULL
          );
        horaInicio: = hora_fim_intervalo_a;
        id_intervalo_a: = 0;
      END IF;
      i: = i + 1;
  END LOOP;
END IF;
END;
$ $
LANGUAGE plpgsql;