drop table camara cascade;
drop table video cascade;
drop table segmentoVideo cascade;
drop table vigia cascade;
drop table eventoEmergencia cascade;
drop table processoSocorro cascade;
drop table entidadeMeio cascade;
drop table meio cascade;
drop table meioCombate cascade;
drop table meioApoio cascade;
drop table meioSocorro cascade;
drop table transporta cascade;
drop table alocado cascade;
drop table acciona cascade;
drop table coordenador cascade;
drop table audita cascade;
drop table solicita cascade;



----------------------------------------
-- Table Creation
----------------------------------------

create table camara (
    numCamara int not null unique,
    constraint pk_camara primary key(numCamara)
);

create table video (
    dataHoraInicio timestamp not null,
    dataHoraFim timestamp not null,
    numCamara int not null,
    constraint pk_video primary key(dataHoraInicio, numCamara),
    constraint fk_camara foreign key(numCamara) references camara(numCamara)
);

create table segmentoVideo (
    numSegmento
)