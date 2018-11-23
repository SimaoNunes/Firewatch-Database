from random import randint

camaras = []
videos = []
segmentos = []

#--------------------------------------
#   Camaras, Video e SegmentoVideo
#--------------------------------------
used = []

for i in range (0, 100):
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
#   Prints
#--------------------------------------

for x in camaras:
    print(x)

print()

for x in videos:
    print(x)

print()

for x in segmentos:
    print(x)