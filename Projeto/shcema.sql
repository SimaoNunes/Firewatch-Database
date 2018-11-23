DROP TABLE camara;
DROP TABLE video;
DROP TABLE segmentoVideo;
DROP TABLE vigia;
DROP TABLE eventoEmergencia;
DROP TABLE processoSocorro;
DROP TABLE entidadeMeio;
DROP TABLE meio;
DROP TABLE meioCombate;
DROP TABLE meioApoio;
DROP TABLE meioSocorro;
DROP TABLE transporta;
DROP TABLE alocado;
DROP TABLE acciona;
DROP TABLE coordenador;
DROP TABLE audita;
DROP TABLE solicita;



----------------------------------------
-- Table Creation
----------------------------------------

CREATE TABLE camara (
    numCamara INT NOT NULL UNIQUE,
    PRIMARY KEY(numCamara)
);

CREATE TABLE video (
    dataHoraInicio TIMESTAMP NOT NULL,
    dataHoraFim TIMESTAMP NOT NULL,
    numCamara INT NOT NULL,
    PRIMARY KEY(dataHoraInicio, numCamara),
    FOREIGN KEY(numCamara) REFERENCES camara(numCamara) ON DELETE CASCADE
);

CREATE TABLE segmentoVideo (
    numSegmento INT NOT NULL UNIQUE,
    duracao INT,
    dataHoraInicio TIMESTAMP NOT NULL,
    numCamara INT NOT NULL,
    PRIMARY KEY(numSegmento, dataHoraInicio, numCamara),
    FOREIGN KEY(dataHoraInicio, numCamara) REFERENCES video(dataHoraInicio, numCamara) ON DELETE CASCADE
);

CREATE TABLE local(
    moradaLocal VARCHAR(255),
    PRIMARY KEY(moradaLocal)
);


CREATE TABLE vigia(
    moradaLocal VARCHAR(255),
    numCamara INT NOT NULL,
    FOREIGN KEY(moradaLocal) REFERENCES local(moradaLocal) ON DELETE CASCADE,
    FOREIGN KEY(numCamara) REFERENCES camara(numCamara) ON DELETE CASCADE
);

CREATE TABLE eventoEmergencia(
    numTelefone VARCHAR(13) NOT NULL,
    instanteChamada TIMESTAMP NOT NULL,
    nomePessoa VARCHAR(255),
    moradaLocal VARCHAR(255),
    numProcessoSocorro INT,
    FOREIGN KEY(moradaLocal) REFERENCES local(moradaLocal) ON DELETE CASCADE,
    FOREIGN KEY(numProcessoSocorro) REFERENCES processoSocorro(numProcessoSocorro) ON DELETE CASCADE,
    UNIQUE KEY(numTelefone, nomePessoa)
);

CREATE TABLE processoSocorro(
    numProcessoSocorro INT,
    PRIMARY KEY(numProcessoSocorro)
);

CREATE TABLE entidadeMeio(
    nomeEntidade VARCHAR(255) NOT NULL,
    PRIMARY KEY(nomeEntidade)
);

CREATE TABLE meio(
    numMeio INT NOT NULL,
    nomeMeio VARCHAR(255) NOT NULL,
    PRIMARY KEY(numMeio, nomeEntidade),
    FOREIGN KEY(nomeEntidade) REFERENCES entidadeMeio(nomeEntidade) ON DELETE CASCADE
)


