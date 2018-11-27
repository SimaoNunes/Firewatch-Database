#---------------------------------------------------------------
#--   Para correr:    python3 populator.py > populate.txt
#---------------------------------------------------------------

from random import randint
import datetime

cidades = ["Portimão", "Vila Real", "Bragança", "Viana do Castelo", "Alcobaça", "Sintra", 
        "Funchal", "Portalegre", "Aveiro", "Almada", "Barreiro", "Cartaxo", "Elvas", 
        "Chaves", "Fátima", "Espinho", "Guarda", "Gouveia", "Fundão", "Leiria", 
        "Maia", "Loures", "Moura", "Mirandela", "Penafiel", "Pinhel", "Praia da Vitória", 
        "Queluz", "Ribeira Grande", "Santana", "Santa Cruz", "Seia", "São Pedro do Sul", "Tomar", 
        "Tavira", "Trancoso", "Trofa", "Lisboa", "Porto", "Braga", "Coimbra", 
        "Amadora", "Vila Nova de Gaia", "Setúbal", "Beja", "Évora", "Faro", "Sines", 
        "Monchique", "Viseu", "Montijo", "Alcochete", "Oliveira do Hospital", "Albufeira", "Olhão", 
        "Redondo", "Vila das Aves", "Abrantes", "Águeda", "Alcácer do Sal", "Alcobaça", "Alfena", 
        "Chaves", "Costa da Caparica", "Cartaxo", "Esmoriz", "Estarreja",
        "Fafe", "Santo André", "Felgueiras", "Fátima", "Funchal", "Gondomar", "Nazaré", 
        "Horta", "Lagoa", "Lagos", "Sagres", "Loulé", "Castro Daire", "Marco de Canavezes", 
        "Montemor-o-Novo", "Ovar", "Peniche", "Ericeira", "Pombal", "Cascais", 
        "Rio Maior", "Sabugal", "Santana", "Santo Tirso", "Seixal", "Silves", "Tondela", 
        "Valongo", "Vizela", "Ílhavo", "Lamego", "Lixa", "Lourosa", "Macedo de Cavaleiros",
        "Machico"]

nomes = ["João", "Joana", "Maria", "Rita", "Miguel", 
        "Simão", "Catarina", "Ana", "Luís", "Tomás", 
        "Pedro", "Margarida", "Madalena", "Carolina", "Ricardo", 
        "Éder", "Cristiano Ronaldo", "Bruno Fernandes", "Sancidino", "Jonas", 
        "Marega", "Camões"]

tiposEntidades = ["Bombeiros de ", "Polícia de ", "Junta de Freguesia de "]

nomesMeios = ["Ambulância", "Camião", "Carrinha", "Helicóptero"]

camaras = []
videos = []
segmentos = []
locais = []
vigia = []
eventos = []
processos = []
entidades = []
meios = []
meiosCombate = []
meiosApoio = []
meiosSocorro = []
transporta = []
alocado = []
acciona = []
coordenadores = []
audita = []
solicita = []



def toTimestamp(timestamp):
    string = datetime.datetime.fromtimestamp(timestamp)

    return '\'' + string.strftime('%Y-%m-%d %H:%M:%S') + '\''



#-----------------------------------------
#--   Camaras, Video e SegmentoVideo
#-----------------------------------------

todosVideos = []
used = []

for i in range (0, 102):
    camaras.append('insert into camara values(' + str(i) + ');')

    j = 0
    numVideos = randint(2,4)
    while j < numVideos:
        dataHoraInicio = randint(1451606400, 1546300799) # 2016 <= dataHoraInicio <= 2018
        duracao = randint(10, 30)
        dataHoraFim = dataHoraInicio + duracao*60

        if (dataHoraInicio not in used):
            used.append(dataHoraInicio)
            todosVideos.append(str(dataHoraInicio) + ', ' + str(i))

            timeStampInicio = toTimestamp(dataHoraInicio)
            timeStampFim = toTimestamp(dataHoraFim)
            videos.append('insert into video values(' + timeStampInicio + ', ' + timeStampFim + ', ' + str(i) + ');')
            numSegmentos = randint(1, 2)

            for k in range (0, numSegmentos):
                numSegmento = k

                if (k != numSegmentos - 1):
                    duracaoSegmento = 2
                    duracao -= 2

                else:
                    duracaoSegmento = duracao

                timeStampInicio = toTimestamp(dataHoraInicio)

                segmentos.append('insert into segmentoVideo values(' + str(numSegmento) + ', ' + str(duracaoSegmento) + ', ' + timeStampInicio + ', ' + str(i) + ');')

            j += 1



#-----------------------------------------
#--   Local, Vigia
#-----------------------------------------

for cidade in cidades:
    locais.append('insert into local values(\'' + cidade + '\');')

for i in range(0, 102):
    vigia.append('insert into vigia values(\'' + cidades[randint(0, len(cidades) - 1)] + '\', ' + str(i) + ');')



#-----------------------------------------
#--   EventoEmergencia
#-----------------------------------------

numTelefone = 960000000
numProcessoSocorro = 0

for i in range(0, 150):
    nome = nomes[randint(0, len(nomes) - 1)]
    morada = cidades[randint(0, len(cidades) - 1)]
    instanteChamada = randint(1451606400,1546300799)

    timeStampInicio = toTimestamp(instanteChamada)
    eventos.append('insert into eventoEmergencia values(' + str(numTelefone) + ', ' + timeStampInicio + ', \'' + nome + '\', \'' + morada + '\', ' + str(numProcessoSocorro) + ');')

    numTelefone += 1
    numProcessoSocorro += 1
    numProcessoSocorro = numProcessoSocorro % 102   #Numero de processos socorro



#-----------------------------------------
#--   ProcessoSocorro
#-----------------------------------------

for i in range(0, 102):
    processos.append('insert into processoSocorro values(' + str(i) + ');')



#-----------------------------------------
#--   Entidade Meio
#-----------------------------------------

todasEntidades = []
i = 0

while i < 102:
    entidade = tiposEntidades[randint(0, len(tiposEntidades) - 1)] + cidades[randint(0, len(cidades) - 1)]

    if entidade not in todasEntidades:
        todasEntidades.append(entidade)

        entidades.append('insert into entidadeMeio values(\'' + entidade + '\');')

        i += 1



#-----------------------------------------
#--   Meio (Combate, Apoio, Socorro)
#-----------------------------------------

todosMeios = []
todosMeiosApoio = []
todosMeiosSocorro = []

for nomeEntidade in todasEntidades:

    for i in range (0, randint(3,5)):
        meio = str(i) + ', \'' + nomeEntidade
        todosMeios.append(meio)

        meios.append('insert into meio values(' + str(i) + ', \'' + nomesMeios[randint(0, len(nomesMeios) - 1)] + '\', \'' + nomeEntidade + '\');')

        if i % 3 == 0:
            meiosCombate.append('insert into meioCombate values(' + str(i) + ', \'' + nomeEntidade + '\');')

        elif i % 3 == 1:
            todosMeiosApoio.append(meio)

            meiosApoio.append('insert into meioApoio values(' + meio + '\');')

        else:
            todosMeiosSocorro.append(meio)

            meiosSocorro.append('insert into meioSocorro values(' + meio + '\');')



#-----------------------------------------
#--   Tranporta, Alocado
#-----------------------------------------

for i in range(0, 102):
    for j in range(0,2):
        transporta.append('insert into transporta values(' + todosMeiosSocorro[(i+j) % len(todosMeiosSocorro) - 1] + '\', ' + str(randint(5, 20)) + ', ' + str(i) + ');')
        alocado.append('insert into alocado values(' + todosMeiosApoio[(i+j) % len(todosMeiosApoio) - 1] + '\', ' + str(randint(1, 10)) + ', ' + str(i) + ');')



#-----------------------------------------
#--   Acciona
#-----------------------------------------

accionamentos = []

for i in range(0, 102):
    for j in range(0,3):
        accionamento = todosMeios[(i+j) % len(todosMeios)] + '\', ' + str(i)
        accionamentos.append(accionamento)

        acciona.append('insert into acciona values(' + accionamento + ');')



#-----------------------------------------
#--   Coordenador
#-----------------------------------------

for i in range (0, 102):
    coordenadores.append('insert into coordenador values(' + str(i) + ');')



#-----------------------------------------
#--   Audita
#-----------------------------------------

texto = "Auditado."

for i in range (0, 102):
    dataHoraInicio = randint(1451606400, 1546300699)
    dataHoraFim = dataHoraInicio + randint(120, 1200)
    dataAuditoria = dataHoraInicio
    accionamento = accionamentos[randint(0, len(accionamentos) - 1)]

    timeStampInicio = toTimestamp(dataHoraInicio)
    timeStampFim = toTimestamp(dataHoraFim)

    audita.append('insert into audita values(' + str(i) + ', ' + accionamento + ', ' + timeStampInicio + ', ' + timeStampFim + ', ' + timeStampInicio + ', \'' + texto + '\');')



#-----------------------------------------
#--   Solicita
#-----------------------------------------

for i in range (0, 102):
    dataHoraInicio = randint(1451606400, 1546300699)
    dataHoraFim = dataHoraInicio + randint(120, 1200)
    video = todosVideos[randint(0, len(todosVideos) - 1)]

    timeStampInicio = toTimestamp(dataHoraInicio)
    timeStampFim = toTimestamp(dataHoraInicio)

    solicita.append('insert into solicita values(' + str(i) + ', ' + video + ', ' + timeStampInicio + ', ' + timeStampFim + ');')



#-----------------------------------------
#--   Prints
#-----------------------------------------

def printAll():
    for x in camaras:
        print(x)

    print('\n\n')

    for x in videos:
        print(x)

    print('\n\n')

    for x in segmentos:
        print(x)

    print('\n\n')

    for x in locais:
        print(x)

    print('\n\n')

    for x in vigia:
        print(x)

    print('\n\n')

    for x in eventos:
        print(x)

    print('\n\n')

    for x in processos:
        print(x)

    print('\n\n')

    for x in entidades:
        print(x)

    print('\n\n')

    for x in meios:
        print(x)

    print('\n\n')

    for x in meiosCombate:
        print(x)

    print('\n\n')

    for x in meiosApoio:
        print(x)

    print('\n\n')

    for x in meiosSocorro:
        print(x)

    print('\n\n')

    for x in transporta:
        print(x)

    print('\n\n')

    for x in alocado:
        print(x)

    print('\n\n')

    for x in acciona:
        print(x)

    print('\n\n')

    for x in coordenadores:
        print(x)

    print('\n\n')

    for x in audita:
        print(x)

    print('\n\n')

    for x in solicita:
        print(x)

    

printAll()