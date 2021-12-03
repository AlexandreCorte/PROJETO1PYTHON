"""
Alexandre Corte
Primeiro Projeto de FP
JOGO DO GALO
"""
def eh_tabuleiro(tab):
    """
    Esta funcao recebe um argumento de qualquer tipo e retorna True
    se o argumento dado for um tabuleiro. Caso contrario retorna False
    sem nunca gerar erros.
    :param tab:(qualquer tipo)
    :return:(bool) True se for tuplo. False caso contrario
    """
    if type(tab)!=tuple or len(tab)!=3:
        return False
    for i in tab:
        if type(i)!=tuple or len(i)!=3:
            return False
    vetortab = tab[0] + tab[1] + tab[2]
    for i in range(len(vetortab)):
        if (vetortab[i]!=0 and vetortab[i]!=1 and vetortab[i]!=-1) or type(vetortab[i])!=int:
            return False
    return True


def eh_posicao(arg):
    """
    Esta funcao recebe um argumento de qualquer tipo e retorna True
    se este for uma posicao e False caso contrario, sem nunca gerar
    erros.
    :param arg:(qualquer tipo)
    :return:(bool) True se for posicao. False caso contrario
    """
    if type(arg)!=int or arg<1 or arg>9:
        return False
    else:
        return True

def obter_coluna(tab, coluna):
    """
    Esta funcao recebe um tabuleiro e um inteiro de 1 a 3, correspondente
    a uma coluna e retorna um vetor com os valores da respetiva coluna.
    Gera erro se a coluna nao for um inteiro de 1 a 3 ou se o tabuleiro
    fornecido nao retornar True na primeira funcao.
    :param tab:(tuplo) primeiro parametro
    :param coluna:(int) segundo parametro
    :return:(tuplo) vetor com os valores da coluna pretendida
    """
    t=()
    if coluna>3 or coluna<1 or eh_tabuleiro(tab)!=True or type(coluna)!=int:
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
    for i in range(len(tab)):
        t+=(tab[i][coluna-1],)
    return t

def obter_linha(tab,linha):
    """
    Esta funcao recebe um tabuleiro e um inteiro de 1 a 3, correspondente
    a uma linha e retorna um vetor com os valores da respetiva linha.
    Gera erro se a linha nao for um inteiro de 1 a 3 ou se o tabuleiro
    fornecido nao retornar True na primeira funcao.
    :param tab:(tuplo) primeiro parametro
    :param linha: (int) segundo parametro
    :return:(tuplo) vetor com os valores da linha pretendida
    """
    if linha<1 or linha>3 or eh_tabuleiro(tab)!=True or type(linha)!=int:
        raise ValueError('obter_linha: algum dos argumentos e invalido')
    for i in tab:
        return tab[linha-1]

def obter_diagonal(tab,diagonal):
    """
    Esta funcao recebe um tabuleiro e um inteiro (1 ou 2), correspondente
    a uma diagonal e retorna um vetor com os valores da respetiva diagonal.
    Gera erro se a diagonal nao for um inteiro (1 ou 2) ou se o tabuleiro
    fornecido nao retornar True na primeira funcao.
    :param tab:(tuplo) primeiro parametro
    :param diagonal: (int) segundo parametro
    :return:(tuplo) vetor com os valores da diagonal pretendida
    """
    t=()
    if diagonal>2 or diagonal<1 or eh_tabuleiro(tab)!=True or type(diagonal)!=int:
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    if diagonal==1:
        for i in range(len(tab)):
            t+=(tab[i][i]),
    elif diagonal==2:
        for i in range(len(tab)):
            tab1=tab[::-1]
            t+=(tab1[i][i]),
    return t

def tabuleiro_str(tab):
    """
    Esta funcao recebe um tabuleiro e devolve uma cadeia de caracteres
    que representa o tabuleiro como nos o vemos.
    Gera erro se o tabuleiro passado nao retornar True na primeira
    funcao.
    :param tab:(tuplo)
    :return:(string) tabuleiro printado
    """
    if eh_tabuleiro(tab)!=True:
        raise ValueError('tabuleiro_str: o argumento e invalido')
    car=[]
    posicoes = list(tab[0] + tab[1] + tab[2])
    for i in posicoes:
        if i == 0:
            car.append('   ')
        if i == 1:
            car.append(' X ')
        if i == -1:
            car.append(' O ')
    tabuleiro= car[0]+ '|'+ car[1]+ '|'+ car[2]+ '\n-----------\n'+ car[3]+ '|'+ car[4]+ '|'+ car[5]+\
            '\n-----------\n'+ car[6]+ '|' + car[7]+ '|'+ car[8]
    return tabuleiro

def eh_posicao_livre(tab,pos):
    """
    Esta funcao recebe um tabuleiro e um inteiro correspondente a uma
    posicao e retorna True se esta posicao for livre e False caso contrario.
    Gera erro se o tabuleiro passado nao retornar True na primeira funcao
    ou se a posicao fornecida nao corresponder a uma posicao do tabuleiro.
    :param tab:(tuplo)primeiro parametro
    :param pos:(int)segundo parametro
    :return:(bool)True se for uma posicao livre e False caso contrario
    """
    if eh_tabuleiro(tab)!=True or eh_posicao(pos)!=True:
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    posicoes = list(tab[0] + tab[1] + tab[2])
    for i in range(len(posicoes)):
        posfinal=pos-1
        return posicoes[posfinal]==0

def obter_posicoes_livres(tab):
    """
    Esta funcao recebe um tabuleiro e retorna um vetor com todas as posicoes
    livres do tabuleiro.
    Gera erro se o tabuleiro passado nao retornar True na primeira funcao.
    :param tab:(tuplo)
    :return:(tuplo) posicoes livres
    """
    vetorlivre=()
    if eh_tabuleiro(tab)!=True:
        raise ValueError('obter_posicoes_livres: o argumento e invalido')
    posicoes = list(tab[0] + tab[1] + tab[2])
    for i in range(len(posicoes)):
        if posicoes[i]==0:
            vetorlivre+=(i+1),
    return vetorlivre

def jogador_ganhador(tab):
    """
    Esta funcao recebe um tabuleiro e retorna um inteiro correspondente ao
    vencedor do jogo. Retorna 1 se um vencedor for 'X' ou -1 se o vencedor for
    'O'.
    Gera erro se o tabuleiro passado nao for retornar True na primeira funcao.
    :param tab:(tuplo)
    :return:(int)jogador vencedor
    """
    if eh_tabuleiro(tab)!=True:
        raise ValueError('jogador_ganhador: o argumento e invalido')
    if obter_diagonal(tab,1)==(1,1,1) or obter_diagonal(tab,2)==(1,1,1)\
            or obter_linha(tab,1)==(1,1,1) or obter_linha(tab, 2)==(1,1,1)\
            or obter_linha(tab,3)==(1,1,1) or obter_coluna(tab,1)==(1,1,1)\
            or obter_coluna(tab,2)==(1,1,1) or obter_coluna(tab,3)==(1,1,1):
        return 1
    if obter_diagonal(tab,1)==(-1,-1,-1) or obter_diagonal(tab,2)==(-1,-1,-1)\
            or obter_linha(tab,1)==(-1,-1,-1) or obter_linha(tab, 2)==(-1,-1,-1)\
            or obter_linha(tab,3)==(-1,-1,-1) or obter_coluna(tab,1)==(-1,-1,-1)\
            or obter_coluna(tab,2)==(-1,-1,-1) or obter_coluna(tab,3)==(-1,-1,-1):
        return -1
    else:
        return 0

def marcar_posicao(tab,jog,pos):
    """
    Esta funcao recebe um tabuleiro, um inteiro correspondente a um jogador
    e um inteiro correspondente a uma posicao do tabuleiro e retorna um
    tabuleiro com a posicao ja marcada.
    Gera erro se o tabuleiro passado nao retornar True na primeira funcao
    ou se a posicao fornecida nao corresponder a uma posicao possivel e livre
    ou se o jogador for diferente de -1 e 1.
    :param tab:(tuplo) primeiro parametro
    :param jog:(int)segundo parametro
    :param pos:(int)terceiro parametro
    :return:(tuplo) tabuleiro com a posicao marcada
    """
    if eh_tabuleiro(tab)!=True or eh_posicao(pos)!=True or (jog!=-1 and jog!=1) or type(jog)!=int:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    poslivres = obter_posicoes_livres(tab)
    if pos not in poslivres:
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    listatab = list(tab[0] + tab[1] + tab[2])
    for i in range(len(poslivres)):
        if poslivres[i]==pos:
            listatab[pos-1]=jog
    tf=tuple(listatab)
    tuplo1, tuplo2, tuplo3=(tf[0],tf[1],tf[2],) , (tf[3],tf[4],tf[5],) , (tf[6],tf[7],tf[8],)
    tuplomarcado=(tuplo1,tuplo2,tuplo3)
    return tuplomarcado

def escolher_posicao_manual(tab):
    """
    Esta funcao recebe uma tabuleiro e pede uma posicao ao utilizador e
    retorna essa mesma posicao se esta for livre.
    Gera erro se o tabuleiro fornecido nao retornar True na primeira funcao
    ou se a posicao passada pelo utilizador nao for possivel e livre.
    :param tab:(tuplo)
    :return:(int) posicao passada
    """
    if eh_tabuleiro(tab)!=True:
        raise ValueError('escolher_posicao_manual: o argumento e invalido')
    posicao = eval(input('Turno do jogador. Escolha uma posicao livre: '))
    if eh_posicao(posicao)!=True:
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')
    if eh_posicao_livre(tab,posicao)==True:
        return posicao
    else:
        raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida')

def vitoria(tab,bot):
    """
    Esta funcao recebe um tabuleiro e um inteiro correspondente ao jogador
    e retorna uma posicao que permite ao jogador fornecido ganhar o jogo,
    ou seja, fazer um 3 em linha.
    :param tab:(tuplo) primeiro parametro
    :param bot:(int) segundo parametro
    :return:(int) posicao que permite ao jogador vencer
    """
    poslivres=obter_posicoes_livres(tab)
    for i in poslivres:
        if jogador_ganhador(marcar_posicao(tab,bot,i))==bot:
            return i
    return 0

def bloqueio(tab,bot):
    """
    Esta funcao recebe um tabuleiro e um inteiro correspondente ao jogador
    e retorna uma posicao que permite ao jogador fornecido bloquear o seu
    adversario de vencer, ou seja, de fazer um 3 em linha.
    :param tab:(tuplo) primeiro parametro
    :param bot:(int) segundo parametro
    :return:(int) posicao que permite ao jogador bloquear a vitoria do oponente
    """
    poslivres = obter_posicoes_livres(tab)
    for i in poslivres:
        if jogador_ganhador(marcar_posicao(tab, -bot, i)) ==-bot:
            return i
    return 0

def posicao_central_livre(tab):
    """
    Esta funcao recebe um tabuleiro e retorna um inteiro, correspondente
    a posicao 5, se esta estiver livre.
    :param tab:(tuplo)
    :return:(int) posicao 5 se esta estiver livre
    """
    poslivres = obter_posicoes_livres(tab)
    if 5 in poslivres:
        return 5
    else:
        return 0

def canto_oposto(tab,bot):
    """
    Esta funcao recebe um tabuleiro e um inteiro correspondente a um jogador
    e retorna uma posicao correspondente a um canto se o canto diagonalmente
    oposto estiver ocupado pelo oponente.
    :param tab:(tuplo)primeiro parametro
    :param bot:(int)segundo parametro
    :return:(int) canto oposto ao do oponente
    """
    lst = list(tab[0] + tab[1] + tab[2])
    elementos=(lst[0], lst[2], lst[6], lst[8])#cantos
    cantos =(1,3,7,9)
    for i in range(len(cantos)):
        if elementos[i]==-bot and eh_posicao_livre(tab,cantos[-i-1])==True:
            return cantos[-i-1]
    return 0

def canto_lateral_livre(tab):
    """
    Esta funcao recebe um tabuleiro e retorna uma posicao correspondente
    a um canto se houver algum canto livre ou uma lateral se houver alguma
    lateral livre. Retorna sempre o primeiro canto ou lateral livre.
    :param tab:(tuplo)
    :return:(int) canto ou lateral livre
    """
    cantoslivres,lateralivre, poslivres=(), (), obter_posicoes_livres(tab)
    for i in poslivres:
        if i%2!=0:#cantos sao todos impares
            cantoslivres+=i,
        else:#laterais sao todas pares
            lateralivre+=i,
    if cantoslivres!=():
        return min(cantoslivres)
    else:
        return min(lateralivre)

def bifurcacao(tab,bot):
    """
    Esta funcao recebe um tabuleiro e um inteiro correspondente a um jogador
    e retorna uma posicao que permite criar uma bifurcacao( 2 formas de vencer
    na jogada seguinte).
    :param tab:(tuplo) primeiro parametro
    :param bot:(int) segundo parametro
    :return:(int) posicao que cria uma bifurcacao
    """
    poslivres=obter_posicoes_livres(tab)
    for i in range(1,10):
        if i in poslivres:
            hipoteses_de_ganhar = 0
            novotab = marcar_posicao(tab, bot, i)
            poslivres = obter_posicoes_livres(novotab)
            for j in poslivres:
                vencedor = jogador_ganhador(marcar_posicao(novotab, bot, j))
                if vencedor==bot:# o bot ganha o jogo com esta jogada? se sim, contador soma 1
                    hipoteses_de_ganhar+=1
            if hipoteses_de_ganhar == 2:#possivel bifurcacao
                return i

def bloqueio_bifurcacao(tab,bot):
    """
    Esta funcao recebe um tabuleiro e um inteiro correspondente a um jogador
    e retorna uma posicao que permite bloquear uma bifurcacao( 2 formas de perder
    na jogada seguinte). Caso o oponente tenha a hipotese de ter 2 bifurcacoes
    entao o jogador deve fazer um 2 em linha para forcar o adversario a defender.
    :param tab:(tuplo) primeiro parametro
    :param bot:(int) segundo parametro
    :return:(int) posicao de bloqueio de bifurcacao
    """
    poslivres = obter_posicoes_livres(tab)
    total_hipoteses=0
    pos=0
    for i in range(1, 10):
        if i in poslivres:
            hipoteses_de_ganhar = 0
            novotab = marcar_posicao(tab, -bot, i)
            poslivres = obter_posicoes_livres(novotab)
            for j in poslivres:
                vencedor = jogador_ganhador(marcar_posicao(novotab, -bot, j))
                if vencedor == -bot:
                    hipoteses_de_ganhar += 1
                    if hipoteses_de_ganhar >= 2: #se for mais do que 2, entao ha mais que 1 bifurcacao
                        total_hipoteses += 1
                        pos = i
    if total_hipoteses==1: #se for 1, entao so ha 2 hipoteses de ganhar e portanto 1 bifurcacao
        return pos
    if total_hipoteses>1:# mais do que uma bifurcacao
        for k in poslivres:
            novotab=marcar_posicao(tab,bot,k)
            poslivresnovo= obter_posicoes_livres(novotab)
            for l in poslivresnovo:
                if jogador_ganhador(marcar_posicao(novotab,bot,l))==bot:
                    pos_bifurcacao=bifurcacao(novotab,-bot)
                    if pos_bifurcacao!=l:
                        return k

def escolher_posicao_auto(tab,bot,estrategia):
    """
    Esta funcao recebe um tabuleiro, um inteiro correspondente a um jogador
    e uma cadeia de caracteres correspondente a uma estrategia que o bot
    vai aplicar no jogo e retorna uma posicao, consoante a estrategia aplicada.
    As estrategias utilizam algumas das funcoes auxiliares criadas antes.
    Gera erro se o tabuleiro passado nao for retornar True na primeira funcao
    ou se o jogador passado for diferente de 1 e -1 ou se a estrategia passada
    for diferente de basico e normal e perfeito.
    :param tab:(tuplo) primeiro parametro
    :param bot:(int) segundo parametro
    :param estrategia:(string) terceiro parametro
    :return:(int) posicao
    """
    if eh_tabuleiro(tab)!=True or type(bot)!=int or (bot!=1 and bot!=-1) or\
            (estrategia!="basico" and estrategia!="normal" and estrategia!="perfeito"):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
    if estrategia=="basico":
        if posicao_central_livre(tab)!=0:
            return posicao_central_livre(tab)
        else:
            return canto_lateral_livre(tab)
    if estrategia=="normal":
        if vitoria(tab,bot)!=0:
            return vitoria(tab,bot)
        if bloqueio(tab,bot)!=0:
            return bloqueio(tab,bot)
        if posicao_central_livre(tab)!=0:
            return posicao_central_livre(tab)
        if canto_oposto(tab,bot)!=0:
            return canto_oposto(tab,bot)
        else:
            return canto_lateral_livre(tab)
    if estrategia=='perfeito':
        if vitoria(tab,bot)!=0:
            return vitoria(tab,bot)
        if bloqueio(tab,bot)!=0:
            return bloqueio(tab,bot)
        if bifurcacao(tab,bot)!=None:
            return bifurcacao(tab,bot)
        if bloqueio_bifurcacao(tab,bot)!=None:
            return bloqueio_bifurcacao(tab,bot)
        if posicao_central_livre(tab)!=0:
            return posicao_central_livre(tab)
        if canto_oposto(tab,bot)!=0:
            return canto_oposto(tab,bot)
        else:
            return canto_lateral_livre(tab)

def jogo_do_galo(jog,estrategia):
    """
    Esta funcao recebe duas cadeias de caracteres, um jogador, 'X' ou 'O'
    e uma estrategia, basico, normal ou perfeito, e retorna sucessivamente
    cadeias de caracteres correspondentes a tabuleiros e no final uma
    cadeia de caracteres correspondente ao vencedor do jogo ou empate
    se nenhum dos jogadores vencer.
    Gera erro se o jogador nao for 'X' e 'O' ou se a estrategia nao for
    basico, normal e perfeito.
    :param jog:(string) primeiro parametro
    :param estrategia:(string) segundo parametro
    :return:(string)tabuleiros sucessivos e vencedor ou empate
    """
    tab=((0,0,0),(0,0,0),(0,0,0))
    if (jog!='X' and jog!='O') or (estrategia!='basico' and estrategia!='normal' and estrategia!='perfeito'):
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
    print('Bem-vindo ao JOGO DO GALO.')
    if jog=='X':
        print("O jogador joga com 'X'.")
        while len(obter_posicoes_livres(tab))>0:
            posicao = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab,1,posicao)
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab)==1:
                return 'X'
            if jogador_ganhador(tab)==-1:
                return 'O'
            if len(obter_posicoes_livres(tab))==0:
                return 'EMPATE'
            print('Turno do computador ('+estrategia+'):')
            posicao = escolher_posicao_auto(tab,-1,estrategia)
            tab = marcar_posicao(tab,-1,posicao)
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab)==1:
                return 'X'
            if jogador_ganhador(tab)==-1:
                return 'O'
            if len(obter_posicoes_livres(tab))==0:
                return 'EMPATE'
    if jog=='O':
        print("O jogador joga com 'O'.")
        while len(obter_posicoes_livres(tab)) > 0:
            print('Turno do computador (' + estrategia + '):')
            posicao = escolher_posicao_auto(tab, 1, estrategia)
            tab = marcar_posicao(tab, 1, posicao)
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) == 1:
                return 'X'
            if jogador_ganhador(tab) == -1:
                return 'O'
            if len(obter_posicoes_livres(tab)) == 0:
                return 'EMPATE'
            posicao = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab, -1, posicao)
            print(tabuleiro_str(tab))
            if jogador_ganhador(tab) == 1:
                return 'X'
            if jogador_ganhador(tab) == -1:
                return 'O'
            if len(obter_posicoes_livres(tab)) == 0:
                return 'EMPATE'


