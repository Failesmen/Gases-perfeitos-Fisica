import matplotlib.pyplot

print("\nOlá! Insira os dados. Caso não tenha algum, insira x.")

#cria listas para posteriormente serem adicionados os valores de T, V ou P
listaT=[]
listaV=[]
listaP=[]
subzero = 0

repetir=True
while repetir==True:

    
    #recebe os dados do usuário
    n=input("\nNum de mol: ")
    v=input("Volume: ")
    p=input("Pressão: ")

    #condição para transformar P de mmHg para atm >>CASO P não for a incógnita<<
    if p!="x":
        p=float(p)
        atm_ou_mmhg=input("P está em: 1 - atm  ou  2 - mmHg? ")
        if atm_ou_mmhg=="2":
            p=p/760
        
    t=input("temperatura: ")

    #condição para converter T kelvin >>CASO T não for a incognita<<
    if t!="x":
        t=float(t)
        conversao=input("T está em: 1 - Celsius, 2 - Kelvin  ou 3 - Fahrenheit? ")
        if conversao=="1":
            t=t+273
        elif conversao=="3":
            t=(t-32)*(5/9)+273

    r=0.082

    #calculo de N
    if n=="x":
        v=float(v)
        p=float(p)
        t=float(t)
        n=(p*v)/(r*t)
        print("\nN=", n, "mols")
        
    
    #calculo de P
    elif p=="x":
        n=float(n)
        v=float(v)
        t=float(t)
        p=(n*r*t)/v
        print("\nP=",p,"atm")
        #adiciona o valor de p na lista
        listaP.append(p)
        if len(listaP)==2:
            if listaP[0]==listaP[1]:
                print("\n",listaP)
                transformacao="isobárica"
                print("\nOcorreu uma transformação", transformacao)
                listaP=[]
                
                #Gráfico VxT

                listaT.append(t)
                listaV.append(v)
                listaT.append(subzero)
                listaV.append(subzero)

                matplotlib.pyplot.plot(listaT, listaV)
                matplotlib.pyplot.title('Volume x Temperatura')
                matplotlib.pyplot.xlabel('Temperatura(K)')
                matplotlib.pyplot.ylabel('Volume(L)')

                matplotlib.pyplot.show()
            else:
                del(listaP[0])
    
    #calculo de V
    elif v=="x":
        n=float(n)
        p=float(p)
        t=float(t)
        v=(n*r*t)/p
        print("\nV=",v,"L")
        #adiciona o valor de V na lista
        listaV.append(v)
        if len(listaV)==2:
            if listaV[0]==listaV[1]:
                print("\n",listaV)
                transformacao="isovolumétrica"
                print("\nOcorreu uma transformação", transformacao)
                listaV=[]
                
                #Gráfico PxT

                listaT.append(t)
                listaP.append(p)
                listaT.append(subzero)
                listaP.append(subzero)

                matplotlib.pyplot.plot(listaT, listaP)
                matplotlib.pyplot.title('Pressão x Temperatura')
                matplotlib.pyplot.xlabel('Temperatura(K)')
                matplotlib.pyplot.ylabel('Pressão(atm)')

                matplotlib.pyplot.show()
            else:
                del(listaV[0])

    #calculo de T
    elif t=="x":
        v=float(v)
        p=float(p)
        n=float(n)
        t=(p*v)/(n*r)
        print("\nT=",t, "K")
        #adiciona o valor de p na lista
        listaT.append(t)
        if len(listaT)==2:          
            if listaT[0]==listaT[1]:
                print("\n",listaT)
                transformacao="isotérmica"
                print("\nOcorreu uma transformação", transformacao)
                listaT=[]
            else:
                del(listaT[0])
        
    else:
        print("Você tem todos os dados... Tchau!")

