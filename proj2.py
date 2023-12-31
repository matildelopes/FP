#2.1.1 TAD gerador
    #Construtores

'''
Função cria_gerador: recebe um inteiro b correpondente ao número de bits do gerador (32 ou 64) 
e um inteiro positivo s correspondendo ao estado e este valor será sempre menor a 2**b.
Como o gerador é um TAD(tipos abstratos de dados) optei que o meu gerador fosse do tipo list
e que retorna: [b,s] 
'''
def cria_gerador(b,s):  #type(gerador) = list and gerador=[b,s]
    if not(isinstance(b,int) and isinstance(s,int) and s>0 and (b==32 or b==64)):
        raise ValueError("cria_gerador: argumentos invalidos")
    if b==32 and s> 2**32:
        raise ValueError("cria_gerador: argumentos invalidos")
    if b==64 and s> 2**64:
        raise ValueError("cria_gerador: argumentos invalidos")
    gerador =[b,s]
    return gerador

'''
Função que cria uma cópia do gerador já criado de maneira a não ser alterado e alterar a cópia feita.
'''
def cria_copia_gerador(g):
    g_copia =g.copy()
    return g_copia

    #Seletores

'''
Função que me dá o valor correspondente ao estado do gerador criado.
'''
def obtem_estado(g):
    return g[1]        #o seu estado, ou seja , o número anterior gerado

    #Modificadores
    
'''
Função que atribui um novo valor do estado do gerador g como sendo s (type(s)==int), returnando esse valor.
'''
def define_estado(g,s):
    g[1] = s
    return g[1]

'''
Função que modifica o estado do gerador introduzido de acordo com o algoritmo xorshift,
gerando números pseudoaleatórios e devolve-os.
Para gerar os números de acordo com o algoritmo dito, as operações de deslocamento são os operadores << e >>,
o ou-exclusivo bit a bit o símbolo ^, e para o and bit a bit &.
'''
def atualiza_estado(g):
    if g[0] == 32:
        g[1] ^= ( g[1] << 13) & 0xFFFFFFFF
        g[1] ^= ( g[1] >> 17) & 0xFFFFFFFF
        g[1] ^= ( g[1] << 5) & 0xFFFFFFFF
    elif g[0] == 64:
        g[1] ^= ( g[1] << 13) & 0xFFFFFFFFFFFFFFFF
        g[1] ^= ( g[1] >> 7) & 0xFFFFFFFFFFFFFFFF
        g[1] ^= ( g[1] << 17) & 0xFFFFFFFFFFFFFFFF
    return g[1]
    
'''
Função que verifica os argumentos inseridos e comprova ou não se de facto é um gerador ou não.
'''
def eh_gerador(arg):
    return (isinstance(arg,dict) and arg=={}) or (isinstance(arg,list) and isinstance(arg[0], int) and isinstance(arg[1], int) and arg[1] > 0 and len(arg)==2 and (arg[0] ==32 or arg[0]==64) and (arg[1]<= 2**32 or arg[1]<= 2**64))


    #Teste

'''
Função que verifica se o gerador g1 e g2 introduzidos são de facto geradores e se são iguais.
Caso sejam, retorna True. Caso contrário, False.
'''
def geradores_iguais(g1, g2):
    return eh_gerador(g1) and eh_gerador(g2) and g1 == g2

    #Transformador

'''
Função que faz a alteração do tipo de apresentação de gerador, returnando o gerador em string, 
de acordo com este exemplo: ’xorshift...(s=..)’
'''
def gerador_para_str(g):
    return "xorshift"+ str(g[0]) + "(s=" + str(g[1]) + ")"

    #funções de alto nível
'''
Para que as próximas funções sejam de alto nível, é preciso utilizar as funções anteriormente criadas como utensílio para estas futuras.
'''

'''
A função seguinte consiste em ter o estado do gerador atualizado, devolvendo assim um número aleatório no intervalo de [1,n].
Este número é obtido através da seguinte operação: 1 + mod(s,n), em que mod() corresponde à operação resto da divisão inteira(%). 
'''
def gera_numero_aleatorio(g,n):
    g[1] = atualiza_estado(g)
    return 1+ (g[1] % n)
    
'''    
A função seguinte consiste em ter o estado do gerador atualizado, devolvendo assim um caracter aleatório no intervalo de "A" ao carácter que c corresponde.
Este carácter é obtido através do novo estado s de g como caracter na posição mod(s,l) da cadeia de caracteres de tamanho l, formada por todos os caracteres dentro do intervalo apresentado.
'''
def gera_carater_aleatorio(g,c):
    l = (ord(c) + 1) - (ord('A') )
    C = atualiza_estado(g) % l
    return chr(ord('A') + C) 


#2.1.2 TAD coordenada
    #Construtor

'''
Função que cria coordenada, a coordenada será um TAD imutável, ou seja a minha coordeanada será do tipo tuple, contendo apenas duas posições: coluna e linha.
A coluna será uma letra maiúscula entre "A" a "Z".
'''
def cria_coordenada(col, lin):
    if not (isinstance(col, str) and isinstance(lin, int) and 1<=lin<=99 and len(col)==1 and col.isupper() == True):
        raise ValueError("cria_coordenada: argumentos invalidos")
    alfa = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    if not(col in alfa):
        raise ValueError("cria_coordenada: argumentos invalidos")
    else:
        coordenada = (col, lin)     #imutável coordenada daí o tipo da coordenada ser tuplo
    return coordenada

    #Seletores
'''
Função que me dá o valor correspondente à coluna da coordenada criada.
'''   
def obtem_coluna(c):
    return c[0]

'''
Função que me dá o valor correspondente à linha da coordenada criado.
''' 
def obtem_linha(c):
    return c[1]

    #Teste

'''
Função que verifica os argumentos inseridos e comprova ou não se de facto é uma coordenada ou não.
'''
def eh_coordenada(arg):
    return isinstance(arg, tuple) and isinstance(arg[0], str) and isinstance(arg[1], int) and arg[0].isupper() and len(arg[0])==1 and ord("A")<=ord(arg[0]) <= ord("Z") and 1<=arg[1]<=99 and len(arg)==2

'''
Função que verifica se a coordenada c1 e c2 introduzidas são de facto coordenadas e se são iguais.
Caso sejam, retorna True. Caso contrário, False.
'''
def coordenadas_iguais(c1,c2):
    return eh_coordenada(c1) and eh_coordenada(c2) and c1 == c2

    #Transformador

'''
Função que faz a alteração do tipo de apresentação da coordenada, returnando a coordenada em string, 
de acordo com este exemplo: ’B01’ se a coordenada for ("B",1)
'''
def coordenada_para_str(c):
    if c[1] < 10:
        return str(c[0]) + "0"+ str(c[1])
    else:
        return str(c[0]) + str(c[1])

'''
Função que faz o inverso da função anterior passando de str(c) para type(c)== tuple
'''
def str_para_coordenada(s):
    return (s[0], int(s[1:]))

    # Funções de alto nível
'''
Para que as próximas funções sejam de alto nível, é preciso utilizar as funções anteriormente criadas como utensílio para estas futuras.
'''


'''
Função que devolve um tuplo com as coordenadas vizinhas à coordenada inserida, 
começando pela coordanada na diagonal acima-esquerda de c e seguindo no sentido horário.
'''
def obtem_coordenadas_vizinhas(c):
    lst=[]
    #coordenadas por cima da esquerda para a direita
    for coluna in range ( (ord(obtem_coluna(c))-1),ord(obtem_coluna(c))+2):
        if eh_coordenada((chr(coluna),obtem_linha(c)-1)):
            lst += [cria_coordenada(chr(coluna),obtem_linha(c)-1)]

    #coordenada do lado direito
    if eh_coordenada((chr(ord(obtem_coluna(c))+1),obtem_linha(c))):
        lst += [cria_coordenada(chr(ord(obtem_coluna(c))+1),obtem_linha(c))]
    #coordenadas por baixo da direira para a esquerda
    
    for coluna in range ( (ord(obtem_coluna(c))+1),ord(obtem_coluna(c))-2,-1):
        if eh_coordenada((chr(coluna),obtem_linha(c)+1)):
            lst += [cria_coordenada(chr(coluna),obtem_linha(c)+1)]
    #coordenada do lado esquerdo
    if eh_coordenada((chr(ord(obtem_coluna(c))-1),obtem_linha(c))):
        lst += [cria_coordenada(chr(ord(obtem_coluna(c))-1),obtem_linha(c))]
    return tuple(lst)
               
'''
Função que recebe uma coordenada c e um gerador g e devolve uma coordenada gerada aleatoriamente
e para isso irei usar a função básica: gera_numero-aleatorio para obter a maior coluna e a maior linha possíveis.
'''
def obtem_coordenada_aleatoria(c,g):
    return (gera_carater_aleatorio(g,obtem_coluna(c)), gera_numero_aleatorio(g,obtem_linha(c)))


#2.1.3 TAD parcela
    #Construtor

'''
Função que não recebe nada e apenas devolve um dicionário correspondendo à parcela com os dados do seu tipo de estado e tem ou não uma mina escondida.
'''
def cria_parcela():
    parcela ={"estado":"tapada" , "mina" : False}
    return parcela

'''
Função que cria uma cópia da parcela já criada de maneira a não ser alterada e alterar a cópia feita.
'''
def cria_copia_parcela(p):
    pcopy = p.copy()
    return pcopy

    #Modificadores

'''
Função que modifica destrutivamente a parcela criada, atribuindo o valor do "estado" como "limpa", devolvendo a própria parcela.
'''
def limpa_parcela(p):
    #p=cria_parcela()
    p["estado"] = "limpa"
    return p

'''
Função que modifica destrutivamente a parcela criada, atribuindo o valor do "estado" como "marcada", devolvendo a própria parcela.
'''
def marca_parcela(p):
    #p=cria_parcela()
    p["estado"] = "marcada"
    return p

'''
Função que modifica destrutivamente a parcela criada, atribuindo o valor do "estado" como "tapada", devolvendo a própria parcela.
'''
def desmarca_parcela(p):
    #p=cria_parcela()
    p["estado"] = "tapada"
    return p

'''
Função que modifica destrutivamente a parcela criada, atribuindo o valor de "mina" como True, devolvendo a própria parcela.
'''
def esconde_mina(p):
    #p=cria_parcela()
    p["mina"] = True
    return p
    
    #Reconhecedor
'''
Função que verifica os argumentos inseridos e comprova ou não se de facto é uma parcela ou não.
'''
def eh_parcela(arg):
    return isinstance(arg,dict) and "estado" in arg and "mina" in arg and isinstance(arg["estado"], str) and isinstance(arg["mina"],bool)

'''
Função que verifica os argumentos inseridos e comprova ou não se de facto é uma parcela ou não e se o valor do "estado" é "tapada".
'''
def eh_parcela_tapada(p):
    return eh_parcela(p) and p["estado"] == "tapada"

'''
Função que verifica os argumentos inseridos e comprova ou não se de facto é uma parcela ou não e se o valor do "estado" é "marcada".
'''
def eh_parcela_marcada(p):
    return  eh_parcela(p) and p["estado"] == "marcada"

'''
Função que verifica os argumentos inseridos e comprova ou não se de facto é uma parcela ou não e se o valor do "estado" é "limpa".
'''
def eh_parcela_limpa(p):
    return  eh_parcela(p) and p["estado"] == "limpa"

'''
Função que verifica os argumentos inseridos e comprova ou não se de facto é uma parcela ou não e se o valor do "mina" é True.
'''
def eh_parcela_minada(p):
    return  eh_parcela(p) and p["mina"] == True

    #Teste

'''
Função que verifica se a parcela p1 e p2 introduzidas são de facto parcelas e se são iguais.
Caso sejam, retorna True. Caso contrário, False.
'''
def parcelas_iguais(p1,p2):
    return eh_parcela(p1) and eh_parcela(p2) and p1==p2

    #Transformadores

'''
Função que faz a alteração do tipo de apresentação da parcela, returnando uma string de acordo com o estado da parcela. 
Se a p["estado"]== "tapada" --> retorna "#"
Se a p["estado"]== "marcada" --> retorna "@"
Se a p["estado"]== "limpa" and p["mina"]== False --> retorna "?"
Se a p["estado"]== "limpa" and p["mina"]== True  --> retorna "X"
'''
def parcela_para_str(p):
    if eh_parcela_tapada(p):
        return "#"
    if eh_parcela_marcada(p):
        return "@"
    if eh_parcela_limpa(p) and eh_parcela_minada(p)== False:
        return "?"
    elif eh_parcela_limpa(p) and eh_parcela_minada(p)== True:
        return "X"

    #Funções de alto nível
'''
Para que as próximas funções sejam de alto nível, é preciso utilizar as funções anteriormente criadas como utensílio para estas futuras.
'''

'''
Função que recebe uma parcela e modifica-a destrutivamente utilizando as funções anteriores para o fazer.
Da seguinte forma: desmarca se estiver marcada e marca se estiver tapada, devolvendo True e em qualquer outro caso, não modifica a parcela e apenas retorna False. 
'''
def alterna_bandeira(p):
    if eh_parcela_marcada(p):
        p=limpa_parcela(p)
        return True
    elif eh_parcela_tapada(p):
        p=marca_parcela(p)
        return True
    else:
        return False



#2.1.4 TAD campo
    #Funções auxiliares
def get_coluna_int(c):
    return ord(c) - ord("A")

def get_coluna_chr(n):
    return chr(ord("A")+ n)


    #Construtor
'''
Função que recebe uma cadeia de caracteres correspondendo à última coluna e recebe um inteiro correspondendo à última linha do campo de minas.
Devolve uma lista de listas correpondento ao campo como se fosse uma matriz.
'''
def cria_campo(c,l):
    if not(isinstance(c,str) and isinstance(l,int) and l >0 and len(c)==1):
        raise ValueError("cria_campo: argumentos invalidos")
    if not(ord("A")<=ord(c)<=ord("Z") and 1<=l<=99):
        raise ValueError("cria_campo: argumentos invalidos")
    campo =[]
    col= ord(c)+1 - ord("A")
    for i in range(l):
        linha= []
        for p in range(col):
            linha.append(cria_parcela())
        campo.append(linha)
    return campo 
            
'''
Função que cria uma cópia do campo já criado de maneira a não ser alterado e alterar a cópia feita.
'''
def cria_copia_campo(m):
    m_copia = m.copy()
    return m_copia

    #Seletores
'''
Função que me dá o valor correspondente à última coluna criada.
'''
def obtem_ultima_coluna(m):
    return chr(len(m[0])+ ord("A")-1)

'''
Função que me dá o valor correspondente à última linha criada.
'''
def obtem_ultima_linha(m):
    return len(m)


def obtem_parcela(m,c):
    return m[obtem_linha(c)-1][ord(obtem_coluna(c)) - ord("A")]


def obtem_coordenadas(m,s):
    lst=[]
    for l in range(len(m)-1):
        for p in range(len(m[l])):
            if s == "minadas":
                if eh_parcela_minada(m[l][p]): 
                    lst.append((chr(p+ord("A")),l+1))
            else:
                if m[l][p]["estado"] == s:
                    lst.append(chr(p+ord("A")),l+1)
    return  tuple(lst)

def obtem_numero_minas_vizinhas(m,c):
    cv = obtem_coordenadas_vizinhas(c)
    mv = obtem_coordenadas(m,"minadas")
    contador =0
    for ctemp in cv:
        for mtemp in mv:
            if coordenadas_iguais(ctemp,mtemp):
                contador +=1
    return contador
            
            
    #Reconhecedores

'''
Função auxiliar para verificar se dentro do arg está só presente enúmeras listas
'''
def tem_sublistas(arg):
    for i in range(len(arg)):
        if isinstance(arg[i],list):
            return True
        else:
            return False
'''
Função que verifica os argumentos inseridos e comprova ou não se de facto é um campo ou não.
'''
def eh_campo(arg):
    return isinstance(arg, list) and len(arg) > 0 and tem_sublistas(arg)

'''
Função que verifica os argumentos inseridos e comprova ou não se de facto é um campo ou não e se c é uma coordenada do campo.
'''
def eh_coordenada_do_campo(m,c):
    return eh_coordenada(c) and eh_campo(m) and ord(obtem_coluna(c))<= ord(obtem_ultima_coluna(m)) and obtem_linha(c)<= obtem_ultima_linha(m)
    
    
    #Teste
    
'''
Função que verifica se o campo c1 e c2 introduzidos são de facto campos e se são iguais.
Caso sejam, retorna True. Caso contrário, False.
'''
def campos_iguais(m1,m2):
    return eh_campo(m1) and eh_campo(m2) and m1 == m2

    #Transformador

'''
Função que faz a alteração do tipo de apresentação do campo, returnando o campo em string.
'''
def campo_para_str(m):
    c = obtem_ultima_coluna(m)
    li =obtem_ultima_linha(m)
    colunas ="   "
    matriz =""
    final =""
    l = ord(c) - ord("A")
    for i in range(ord("A"), ord(c)+1):
        colunas += chr(i)
    for e in range(1,li+1):
        if e<10:
            linhas= "0" + str(e) +"|"
        else:
            linhas = str(e) +"|"
        for i in m[e-1]:
            linhas += parcela_para_str(i)
        matriz += linhas +  "|\n"
    separador = "  +" + "-"*len(m[0])+ "+"
    final += colunas + "\n" + separador +"\n"+ matriz + separador
    return final

    #Funções de alto nível
    
'''
Função que modifica destrutivamente o campo m escondendo n minas em parcelas dentro do campo.
A coordenada c não pode coincidir com nenhuma das coordenadas, as coordenadas vizinhas de c não podem ser nenhuma das que está na lista de coordenadas geradas pelo gerador.
As coordenadas geradas não podem coincidir com nenhuma parcela vizinha de c, nem se podem sobrepor com minas colocadas anteriormente.
'''
def coloca_minas(m,c,g,n):
    i = 1
    while i <= n:
        ctemp =(gera_carater_aleatorio(g,obtem_ultima_coluna(m)),gera_numero_aleatorio(g,obtem_ultima_linha(m)))
        if not(coordenadas_iguais(ctemp,c)):
            if not(ctemp in obtem_coordenadas_vizinhas(c)):
                if not(eh_parcela_minada(m[obtem_linha(ctemp)][get_coluna_int(obtem_coluna(ctemp))])):
                    esconde_mina(m[obtem_linha(ctemp)-1][get_coluna_int(obtem_coluna(ctemp))])
                    i+=1
    return m          
        
        
        
#def limpa_campo(m,c):


#2.2 FUNÇÕES ADICIONAIS

#2.2.1

'''
Função que retorna True caso todas as parcelas do campo sem minas se encontram limpas e retorna False caso contrário.
'''
def jogo_ganho(m):
    i = 0
    contador = 0
    for l in range(len(m)):
        for c in m[l]:
            if eh_parcela_minada(c) or eh_parcela_limpa(c):
                contador += 1
        if contador == (ord(obtem_ultima_coluna(m))-ord("A")) * obtem_ultima_coluna(m):
            return True
        return False


#2.2.2
#def turo_jogador(m):

#2.2.3
def minas(c,l,n,d,s):
    if True:
        raise ValueError ("minas: argumentos invalidos")
    return True

#def limpa_campo(m,c):
    
