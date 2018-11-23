from random import randint

#--------------------------------------
#   Camaras
#--------------------------------------

for i in range (1, 101):
    print('insert into camara values(' + str(i) + ');')

print()

#--------------------------------------
#   Video e SegmentoVideo
#--------------------------------------
used = []
i = 0

while i <= 100:
    dataHoraInicio = randint(1451606400, 1546300799) # 2016 <= time <= 2018
    duracao = randint(5, 30)
    dataHoraFim = dataHoraInicio + 60*duracao
    numCamara = randint(1, 100)

    if (dataHoraInicio not in used):
        used.append(dataHoraInicio)
    else:
        break

    print('insert into video values(' + str(dataHoraInicio) + ', ' + str(dataHoraFim) + ', ' + str(numCamara) + ');')

    numSegmentos = randint(1, 4)

    i += 1