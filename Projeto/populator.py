from random import randint

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

camaras = []
videos = []
segmentos = []
locais = []
vigia = []

#--------------------------------------
#   Camaras, Video e SegmentoVideo
#--------------------------------------
used = []

for i in range (0, 103):
    camaras.append('insert into camara values(' + str(i) + ');')

    j = 0
    while j < 4:
        dataHoraInicio = randint(1451606400, 1546300799) # 2016 <= time <= 2018
        duracao = randint(5, 30)
        dataHoraFim = dataHoraInicio + duracao*60
        numCamara = randint(1, 100)

        if (dataHoraInicio not in used):
            used.append(dataHoraInicio)
            videos.append('insert into video values(' + str(dataHoraInicio) + ', ' + str(dataHoraFim) + ', ' + str(numCamara) + ');')
            numSegmentos = randint(1, 4)

            for k in range (0, numSegmentos):
                numSegmento = k

                if (k != numSegmentos - 1):
                    duracaoSegmento = 1
                    duracao -= 1

                else:
                    duracaoSegmento = duracao

                segmentos.append('insert into segmentoVideo values(' + str(numSegmento) + ', ' + str(duracaoSegmento) + ', ' + str(dataHoraInicio) + ', ' + str(numCamara) + ');')
                dataHoraInicio += duracaoSegmento*60

            j += 1



#--------------------------------------
#   Local, Vigia
#--------------------------------------

for cidade in cidades:
    locais.append('insert into local values(' + cidade + ');')

    for i in range(0, 103):
        vigia.append('insert into vigia values(' + cidade + ', ' + str(i) + ');')



#--------------------------------------
#   Prints
#--------------------------------------

'''for x in camaras:
    print(x)

print()

for x in videos:
    print(x)

print()

for x in segmentos:
    print(x)

for x in locais:
    print(x)'''
