import matplotlib as pls


print("1 - Isotermica")
print("2 - Isobarica")
print("3 - Isocorica")

termodinamica = int(input("Escolha uma das transformações termodinamicas:"))

#Calculo Isotermico

if termodinamica == 1:
    print("1 - Volume Inicial")
    print("2 - Volume Final")
    print("3 - Pressão Inicial")
    print("4 - Pressão Final")
    opcao = int(input("O que deseja calcular:"))

    if opcao == 1:
        V1 = float(input("Volume Final:"))
        P0 = float(input("Pressão Inicial:"))
        P1 = float(input("Pressão Final:"))

        VTermica0 = (V1*P1) / P0
        print("Volume Inicial: ", int(VTermica0),"l")

    elif opcao == 2:
        V0 = float(input("Volume Inicial:"))
        P0 = float(input("Pressão Inicial:"))
        P1 = float(input("Pressão Final:"))

        VTermica1 = (V0*P0) / P1
        print("Volume Final: ", int(VTermica1),"l")

    elif opcao == 3:
        V0 = float(input("Volume Inicial:"))
        V1 = float(input("Volume Final:"))
        P1 = float(input("Pressão Final:"))

        PTermica0 = (V1*P1) / V0
        print("Pressão Inicial: ", int(PTermica0),"Hmg")

    else:
        V0 = float(input("Volume Inicial:"))
        V1 = float(input("Volume Final:"))
        P0 = float(input("Pressão Inicial:"))

        PTermica1 = (V0*P0) / V1
        print("Pressão Final: ", int(PTermica1),"Hmg")


#Calculo Isobarico

elif termodinamica == 2:

    print("1 - Volume Inicial")
    print("2 - Volume Final")
    print("3 - Temperatura Inicial")
    print("4 - Temperatura Final")
    opcao = int(input("O que deseja calcular:"))

    if opcao == 1:
        V1 = float(input("Volume Final:"))
        T0 = float(input("Temperatura Inicial:"))
        T1 = float(input("Temperatura Final:"))

        VBarica0 = (V1*T0) / T1
        print("Volume Inicial: ",int(VBarica0),"l")

    elif opcao == 2:
        V0 = float(input("Volume Inicial:"))
        T0 = float(input("Temperatura Inicial:"))
        T1 = float(input("Temperatura Final:"))

        VBarica1 = (V0*T1) / T0
        print("Volume Final: ",int(VBarica1),"l")

    elif opcao == 3:
        V0 = float(input("Volume Inicial:"))
        V1 = float(input("Volume Final:"))
        T1 = float(input("Temperatura Final:"))

        TempBarica0 = (V0*T1) / V1
        print("Temperatura Inicial: ", int(TempBarica0),"ºC")

    else:
        V0 = float(input("Volume Inicial:"))
        V1 = float(input("Volume Final:"))
        T0 = float(input("Temperatura Inicial:"))

        TempBarica1 = (V1*T0) / V0
        print("Temperatura Final: ",int(TempBarica1),"ºC")



