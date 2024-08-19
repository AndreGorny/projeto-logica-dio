def classificar_heroi(heroi, xp):

    if xp <= 1000:
        nivel = "Ferro"
    elif 1000 < xp <= 2000:
        nivel = "Bronze"
    elif 2000 < xp <= 5000:
        nivel = "Prata"
    elif 5000 < xp <= 7000:
        nivel = "Ouro"
    elif 7000 < xp <= 8000:
        nivel = "Platina"
    elif 8000 < xp <= 9000:
        nivel = "Ascendente"
    elif 9000 < xp <= 10000:
        nivel = "Imortal"
    elif xp > 10000:
        nivel = "Radiante"

    print(f"O herói {heroi} possui {xp} pontos de XP e está no nível {nivel}.")


while 1:
    heroi = input("Informe o nome do herói: ")
    xp = int(input("Informe a XP do herói: "))
    classificar_heroi(heroi, xp)
    continuar = input("Deseja classificar outro herói? (s/n): ")

    if continuar.lower() == "s":
        continue
    else:
        print("Até a próxima!")
        break
