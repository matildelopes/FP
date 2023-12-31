#1.2.1 recebe uma string e substitui todos
# os caracteres brancos ASCII por espaços. 
# Caso hajam espaços brancos repetidos apaga o ultimo espaço 
# e substitui pela próxima letra da palavra seguinte.
def limpa_texto(strTexto):
    retirar = [0x09, 0x0a, 0xb, 0x0c, 0x0d]
    strtemp= strTexto
    if isinstance(strTexto, str):
        strTexto= strTexto.strip()
        for letra in strtemp:
            if ord(letra) in retirar:
                strTexto = strTexto.replace(letra, " ")
    finalstr = ""
    last = strTexto[0]
    for letra in strTexto:
        if ord(last) == 32 and ord(letra) == 32:
            continue
        finalstr += letra
        last = letra
    return finalstr


#1.2.2 função que recebe uma string e um número inteiro e verifica o s
    #seu tipo. O número inteiro corresponde á posição que iremos 
    # escrever a string recebida e retorna um tuplo com a string
    # até à posição recebida como primeiro membro e no segundo membro
    # retorna o resto da cadeia de caracteres.
def corta_texto(strTexto, intLargura):
    tempStr = limpa_texto(strTexto)
    final = ()
    strPrimeira=""
    strSegunda = ""
    listaPalavras = tempStr.split()
    strPrimeira=listaPalavras[0].strip() 
    blnFirst = True
    for i  in range(1,len(listaPalavras)):
        if ((len(listaPalavras[i]) + len(strPrimeira) +1 ) < intLargura) and blnFirst:
            strPrimeira += " " +  listaPalavras[i]
        else:
            strSegunda+= " " + listaPalavras[i]
            blnFirst = False

    final = (strPrimeira.strip(),strSegunda.strip())
    return final



#1.2.3 contar o numero de espaços entre strings e contar o número de 
#caracteres presente na strCadeia. De seguida subtraiu o número total de caracteres
#com o numero recebido(intNum) e o resultado obtido desta operação vai ser o  número 
# de espços que terei de adicionar à string final. Avalio se este número é par ou não 
# para adiconar entre cada palavra o mesmo número de espaços, se possivel
def insere_espacos(strCadeia, intNum):
    if  not(isinstance(strCadeia, str) and isinstance(intNum, int)):
        raise ValueError ("Não é possível.")
    listTemp = strCadeia.split()         #cria uma lista temporária, com cada palavra de strCadeia
    final = ""
    numTemp = 0
    
    numPalavras = len(listTemp)
    tamanhoLetras = 0 
    for palavra in listTemp:
        tamanhoLetras +=len(palavra)
    numEspaco = intNum - tamanhoLetras
    
    if (len(listTemp) == 1) or (len(listTemp) == 0):
        return(strCadeia+" "*numEspaco)
    
    espacosacolocar = numEspaco // (numPalavras-1)
    espacosresto = numEspaco % (numPalavras-1)
    intcont = 0
    strFinal = ""

    strFinal = listTemp[0]
    for i in range(1,len(listTemp)):
        if intcont< espacosresto:
            strFinal+=" " 
            intcont+=1
        strFinal+= " "*espacosacolocar + listTemp[i]            
    return (strFinal)


#1.2.4
#Função que recebe uma cadeia de caracteres e um inteiro. Caso o número de caracteres presentes na string for igual ao número inserido,
# o valor a returnar é a cadeia de carcateres. Caso o o número de caracteres seja menor ao número introduzido, a este tuplo irei inserir o número
#de espaços necessários até ficar igual ao númro introduzido inicialmente. 
# Por fim, se o número de caracteres for maior que o número introduzido, a este iremos retirar os espaços.
def justifica_texto(cadeStr, nInt):
    if not(isinstance(cadeStr, str) and cadeStr != "" and isinstance(nInt, int)
           and nInt> 0 and len(cadeStr)<= nInt):
        raise ValueError ("justifica_texto: argumentos invalidos")
    
    
    strLimpa = limpa_texto(cadeStr)
    
    listaPalavras=[]
    tplCorta = corta_texto(strLimpa, nInt)
    listaPalavras.append(insere_espacos(tplCorta[0],nInt))
    while len(tplCorta[1])> 0:
        tplCorta = corta_texto(tplCorta[1], nInt)
        if(len(tplCorta[1]) >0):
            listaPalavras.append(insere_espacos(tplCorta[0],nInt))
        else:
            strTemp = tplCorta[0] + " " * (nInt - len(tplCorta[0]))
            listaPalavras.append(strTemp)
    return tuple(listaPalavras)
        
        
#2.2.1  
#Função que recbe um dicionário e um número. A cada chave do dicionário vai corresponder uma lista em que 
# o primeiro elemento é o valor correspondente a cada chave do dicionário.
# Para se calcular os quocientes, ao primeiro valor da lista vai-se dividindo por 1 até ao número introduzido, adicionando este resultado
#á lista final.(variável: lstFinal)
def calcula_quocientes(d1,nInt):
    v = 0
    dfinal ={}
    for k in d1:
        valores =[]
        for i in range(1,nInt+1):
            v = d1[k]/i
            valores.append(v)
        dfinal[k] = valores
    return dfinal
    

#2.2.2      
def atribui_mandatos(dct, nInt):
    lstFinal = []
    valor = -1
    chave = ""
    tempDct = calcula_quocientes(dct,nInt)
    for i in range(0, nInt):
        valor = 0
        for q in tempDct:
            if valor < tempDct[q][0]:
                valor = tempDct[q][0]
                chave = q
            if valor == tempDct[q][0]:
                if lstFinal.count(chave) > lstFinal.count(q):
                    chave = q
        lstFinal.append(chave)
        del tempDct[chave][0:1]
    return lstFinal



#2.2.3
#Função que recebe um dicionário e avalia cada chave do dicionário principal e percorre os valores correspondentes a esta chave 
# e avalia os valores correspondentes à chave "votos" e numa lista (variável:lstFinal) vou adicionar por ordem alfabética as chaves do dicionário 
# correspondente aos valor da chave "votos" 
def obtem_partidos(dct):
    lstFinal = []
    for n in dct:
        for k in dct[n]["votos"]:
            if k not in lstFinal:
                lstFinal.append(k)
        lstFinal.sort()
    return lstFinal


#2.2.4
def obtem_resultado_eleicoes(dct):
    lstFinal = []
    tuplo = ()
    if not (isinstance(dct,dict)) or len(dct)==0: 
        raise ValueError("obtem_resultado_eleicoes: argumento invalido")
    for kd in dct:
        if not(isinstance(kd,str)):
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
    for d2 in dct.values():
        if not (isinstance(d2,dict)) or len(d2) == 0 or len(d2) !=2:
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        if "deputados" not in d2:
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        if "votos" not in d2:
            raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        for depValor in d2["deputados"]:
            if not(isinstance(depValor,int)) or depValor <= 0:
                raise ValueError("obtem_resultado_eleicoes: argumento invalido")
        for dctdentr in d2["votos"]:
            if not(isinstance(dctdentr,dict)) or len(dctdentr)==0:
                raise ValueError("obtem_resultado_eleicoes: argumento invalido")
            for kVotos in dctdentr:
                if not (isinstance(kVotos,str)) or dctdentr[kVotos] < 0:
                    raise ValueError("obtem_resultado_eleicoes: argumento invalido")
    nomesPartidos=obtem_partidos(dct)
    mandatos = atribui_mandatos()
    nVotos = []
    for i in range(len(nomesPartidos)):
        for k in mandatos[i]:
            nVotos[i] += k.count(i)
    return 0







        


#3.2.1
#Função que recebe dois tuplos (dois vetores)e devolve um número real que relaciona o comprimento desses dois vetores.
def produto_interno(t1,t2):
    if not(isinstance(t1,tuple) and isinstance(t2,tuple) and len(t1)==len(t2)):
        raise ValueError("produto_interno: não é possível")
    for d1 in t1:
        for d2 in t2:
            if not(isinstance(d2,int) or isinstance(d2,float)):
                raise ValueError("produto_interno: não é possível")
    res = 0.0
    i =0
    for i in range(len(t1)):
        res += t1[i] * t2[i]
    return res
        
    
        
#3.2.2
#Função que verifica os arguntos, se t1,t2,t3 são tuplos de igual comprimento, se o valores de todos os tuplos são 
#e se o número introduzido for um inteiro positivo. 
#O objetivo desta função é returnar True caso o valor absoluto do erro de todas as equações seja inferior à pressão,
#e falso o contrário. 
def verifica_convergencia(t1,t2,t3,nReal):
    if not(isinstance(t1,tuple) and isinstance(t2,tuple)and isinstance(t3,tuple)
           and len(t1)==len(t2)==len(t3)):
        raise ValueError("verifica_convergencia: não é possível")          
    for e in t1:
        if not(isinstance(e,tuple) and len(e)==len(t1)):
            raise ValueError("verifica_convergencia: não é possível")
        for ee1 in e:
            if not(isinstance(ee1,int) or isinstance(ee1,float)):
                raise ValueError("verifica_convergencia: não é possível")
    for ee2 in t2:
        if not(isinstance(ee2,int) or isinstance(ee2,float)):
                raise ValueError("verifica_convergencia: não é possível")
    for ee3 in t3:
        if not(isinstance(ee3,int) or isinstance(ee3,float)):
                raise ValueError("verifica_convergencia: não é possível")
    if not(isinstance(nReal, float) or isinstance(nReal,int)):
        raise ValueError("verifica_convergencia: não é possível")
    num = 0
    precisao = 0
    for i in range(len(t1)):
        num = produto_interno(t1[i],t3)
        precisao = abs(num - t2[i])
        if precisao >= nReal:
            return False
    return True
            
  

#3.2.3
#Função que troca a ordem de listas.
def trocalinhas(lista, i, j):
    lstTemp= lista[i]
    lista[i]= lista[j]
    lista[j]=lstTemp
    return lista


#Função que recebe duas matriz (tipo tuplos) e na diagonal principal não podem haver zeros, para que isto aconteça verifico se nas linhas de cima 
#existe alguma linha que não contenha 0 na diagonal(ou seja, lst[i][i]), 
# se isto acontecer troco as duas linhas de posição usando a função auxiliar que criei: trocalinhas(). 
# No final irei returnar  um tuplo, contendo a matriz com as trocas feitas para que a diagonal principal não contenha 0´s e um tuplo com as trocas feitas 
def retira_zeros_diagonal(t1,t2):
    lt1 =list(t1)
    lt2= list(t2)
    final = ()
    for i in range(len(t1)):
        if lt1[i][i]==0:
            for j in range(len(lt1)):
                if lt1[i][j]!=0 and lt1[j][i]!=0:
                    trocalinhas(lt1,i,j)
                    trocalinhas(lt2,i,j)
    t1Temp= tuple(lt1)
    t2Temp= tuple(lt2)
    t1Temp= list(t1Temp)
    t1Temp.append(t2Temp)
    t1Temp= tuple(t1Temp)
    return t1Temp

   
#3.2.4
#Função que recebe um tuplo (variável: mQuadrada) e retorna True se o valor absoluto do valor da diagonal é maior ou igual 
# à soma dos restantes valores absolutos da linha
def eh_diagonal_dominante(mQuadrada):
    for l in range(len(mQuadrada)):
        somaLinha=0
        for c in range(len(mQuadrada)):
            if l != c:
                somaLinha += abs(mQuadrada[l][c])
        if not(abs(mQuadrada[l][l]) >= somaLinha):
            return False
    return True 
            
            
#3.2.5
def resolve_sistema(t1,t2, num):
    if not(isinstance(t1,tuple) and isinstance(t2,tuple)
           and len(t1)==len(t2)):
        raise ValueError("resolve_sistema: argumentos invalidos")          
    for e in t1:
        if not(isinstance(e,tuple) and len(e)==len(t1)):
            raise ValueError("resolve_sistema: argumentos invalidos")
        for ee1 in e:
            if not(isinstance(ee1,int) or isinstance(ee1,float)):
                raise ValueError("resolve_sistema: argumentos invalidos")
    for ee2 in t2:
        if not(isinstance(ee2,int) or isinstance(ee2,float)):
                raise ValueError("resolve_sistema: argumentos invalidos")
    t1,t2 = retira_zeros_diagonal(t1,t2)
    if eh_diagonal_dominante(t1) == False and eh_diagonal_dominante(t2) == False:
        return ValueError("resolve_sistema: matriz nao diagonal dominante")
