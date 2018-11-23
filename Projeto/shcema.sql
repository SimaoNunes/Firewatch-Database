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
    duracao INT NOT NULL,
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
    PRIMARY KEY(moradaLocal, numCamara),
    FOREIGN KEY(moradaLocal) REFERENCES local(moradaLocal) ON DELETE CASCADE,
    FOREIGN KEY(numCamara) REFERENCES camara(numCamara) ON DELETE CASCADE
);

CREATE TABLE eventoEmergencia(
    numTelefone VARCHAR(13) NOT NULL,
    instanteChamada TIMESTAMP NOT NULL,
    nomePessoa VARCHAR(255),
    moradaLocal VARCHAR(255),
    numProcessoSocorro INT,
    PRIMARY KEY(numTelefone, instanteChamada),
    FOREIGN KEY(moradaLocal) REFERENCES local(moradaLocal) ON DELETE CASCADE,
    FOREIGN KEY(numProcessoSocorro) REFERENCES processoSocorro(numProcessoSocorro) ON DELETE CASCADE
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
);

CREATE TABLE meioCombate(
    numMeio INT NOT NULL,
    nomeEntidade VARCHAR(255) NOT NULL,
    PRIMARY KEY(numMeio, nomeEntidade),
    FOREIGN KEY(numMeio, nomeEntidade) REFERENCES meio(numMeio, nomeEntidade) ON DELETE CASCADE
);

CREATE TABLE meioApoio(
    numMeio INT NOT NULL,
    nomeEntidade VARCHAR(255) NOT NULL,
    PRIMARY KEY(numMeio, nomeEntidade),
    FOREIGN KEY(numMeio, nomeEntidade) REFERENCES meio(numMeio, nomeEntidade) ON DELETE CASCADE
);

CREATE TABLE meioSocorro(
    numMeio INT NOT NULL,
    nomeEntidade VARCHAR(255) NOT NULL,
    PRIMARY KEY(numMeio, nomeEntidade),
    FOREIGN KEY(numMeio, nomeEntidade) REFERENCES meio(numMeio, nomeEntidade) ON DELETE CASCADE
);

CREATE TABLE transporta(
    numMeio INT NOT NULL,
    nomeEntidade VARCHAR(255) NOT NULL,
    numVitimas INT,
    numProcessoSocorro INT,
    PRIMARY KEY(numMeio, nomeEntidade, numProcessoSocorro),
    FOREIGN KEY(numMeio, nomeEntidade) REFERENCES meioSocorro(numMeio, nomeEntidade) ON DELETE CASCADE,
    FOREIGN KEY(numProcessoSocorro) REFERENCES processoSocorro(numProcessoSocorro) ON DELETE CASCADE
);

CREATE TABLE alocado(
    numMeio INT NOT NULL,
    nomeEntidade VARCHAR(255) NOT NULL,
    numHoras INT NOT NULL,
    numProcessoSocorro INT,
    FOREIGN KEY(numMeio, nomeEntidade) REFERENCES meioSocorro(numMeio, nomeEntidade) ON DELETE CASCADE,
    FOREIGN KEY(numProcessoSocorro) REFERENCES processoSocorro(numProcessoSocorro) ON DELETE CASCADE
);

CREATE TABLE acciona(
    numMeio INT NOT NULL,
    nomeEntidade VARCHAR(255) NOT NULL,
    numProcessoSocorro INT,
    PRIMARY KEY(numMeio, nomeEntidade, numProcessoSocorro),
    FOREIGN KEY(numMeio, nomeEntidade) REFERENCES meio(numMeio, nomeEntidade) ON DELETE CASCADE,
    FOREIGN KEY(numProcessoSocorro) REFERENCES processoSocorro(numProcessoSocorro) ON DELETE CASCADE
);

CREATE TABLE coordenador(
    idCoordenador INT NOT NULL UNIQUE,
    PRIMARY KEY(idCoordenador)
);

CREATE TABLE audita(
    idCoordenador INT NOT NULL UNIQUE,
    numMeio INT NOT NULL,
    nomeEntidade VARCHAR(255) NOT NULL,
    numProcessoSocorro INT,
    dataHoraInicio TIMESTAMP NOT NULL,
    dataHoraFim TIMESTAMP NOT NULL,
    dataAuditoria TIMESTAMP NOT NULL,
    texto TEXT NOT NULL,
    PRIMARY KEY(idCoordenador, numMeio, nomeEntidade, numProcessoSocorro, dataHoraInicio, dataHoraFim, dataAuditoria, texto),
    FOREIGN KEY(numMeio, nomeEntidade, numProcessoSocorro) REFERENCES acciona(numMeio, nomeEntidade, numProcessoSocorro) ON DELETE CASCADE,
    FOREIGN KEY(idCoordenador) REFERENCES coordenador(idCoordenador) ON DELETE CASCADE
);

CREATE TABLE solicita(
    idCoordenador INT NOT NULL UNIQUE,
    dataHoraInicioVideo TIMESTAMP NOT NULL,
    numCamara INT NOT NULL,
    dataHoraInicio TIMESTAMP NOT NULL,
    dataHoraFim TIMESTAMP NOT NULL,
    PRIMARY KEY(idCoordenador, dataHoraInicioVideo, numCamara),
    FOREIGN KEY(idCoordenador) REFERENCES coordenador(idCoordenador) ON DELETE CASCADE,
    FOREIGN KEY(dataHoraInicioVideo, numCamara) REFERENCES video(dataHoraInicioVideo, numCamara) ON DELETE CASCADE
);