import os
from time import sleep
import random

def sorteio():
    #ain porque nao abriu um arquivo: PORQUE EU NAO QUIS'
    bag_of_words=["AVIAO",
                "ELEFANTE",
                "BOLA",
                "BEBE",
                "PEIXE",
                "FUTEBOL",
                "BELISCAO",
                "ROLO",
                "HIGIENICO",
                "BASQUETE",
                "CONTROLE",
                "REMOTO",
                "TRISTE",
                "GATO",
                "GOLFE",
                "TESOURA",
                "COLHER",
                "PULAR",
                "GALINHA",
                "SAPO",
                "ESPIRRO",
                "MARTELO",
                "VIOLAO",
                "APLAUDIR",
                "TOSSE",
                "CHIFRES",
                "PINGUIM",
                "CHORAR",
                "RABO",
                "PIADA",
                "ESCOVA",
                "CELULAR",
                "CACHORRO",
                "PATO",
                "SOFA",
                "FOTOGRAFO",
                "OCULOS",
                "BALE",
                "PIPA",
                "CAFE",
                "TAXI",
                "CADEIRA",
                "oNIBUS",
                "ELEVADOR",
                "BICICLETA",
                "FOGAO",
                "COPO",
                "ORELHAS",
                "CHOCOLATE",
                "PESCADOR",
                "NOTEBOOK",
                "LAPIS",
                "CICATRIZ",
                "COBERTOR",
                "HELICOPTERO",
                "ANIVERSARIO",
                "VULCAO",
                "PRESIDENTE",
                "NOIVA",
                "BABAR",
                "NATAL",
                "LUZ",
                "SOMBRA",
                "MAGIA",
                "MAQUIADORA",
                "SHOPPING",
                "BERcO",
                "MEDIR",
                "ESPELHO",
                "ARANHA",
                "MOTO",
                "JARDIM",
                "TRAMPOLIM",
                "CACHOEIRA",
                "JANELA",
                "GIRAFA",
                "RONCAR",
                "PESADELO",
                "LANTERNA",
                "CURIOSIDADE",
                "PANQUECAS",
                "APLICATIVO",
                "CONVITE",
                "ADOLESCENTE",
                "SATELITE",
                "JORNAL",
                "DIAMANTE",
                "LENHA",
                "SAPO",
                "ANDADOR",
                "INFANTIL",
                "RAcAO",
                "GOOGLE",
                "TOCHA",
                "ACAMPAR",
                "LAGO",
                "EMAGRECER",
                "FOFOCA",
                "SALARIO",
                "SORTE",
                ]
    # retorto a palavra sorteranda usando o método random como index da lista acima
    return bag_of_words[random.randrange(0,len(bag_of_words))]

def prepara_caminho(word):
    #pega a palavra sorteada de transforma um hide string com a quantidade de caracteres da palavra'
    return "*"*len(word)


def abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    print("\n")
    print ("Prepare-se para jogar este jogo mortal")

def entra_char():
    char=input("Forneca uma letra: ")
    #o usuário somente pode entrar com uma letra, caso entre com mais de uma ou com número nao deixa
    while len(char)>1 or char.isalpha()==False:
        char=input("Apenas uma letra: ")
    #retorno a letra em maiuscula
    return char.upper()

def find(word, ch):
    #a ideia aqui é criar uma lista de indexes onde a letra escolhida pelo usuário aparece
    #uso o enumarete porque ele separa a palavra por letra e insere um index a ele
    i_of_ch= [i for i, ltr in enumerate(word) if ltr == ch]
    #se retornar uma lista não vazia retorno a lista
    if len(i_of_ch)>0:
        return i_of_ch
    #caso contrário devolvo falso. Esta escolha deixa mais claro que deu "erro" ao tentar achar a letra na string
    else:
        return False

def desmascara(mascara, tentativa, chute):
    #aqui meramente insito a letra informada pelo usuário no seu respectivo lugar na palavra escondida
    #usando a lista de indexes que localizei na função find()
    for index_ch in tentativa:
        mascara=mascara[:index_ch]+ chute + mascara[index_ch+1:]
    
    return mascara

def caminh_erro(erros):
    #um pouco de terror psicológico porque é divertido
    frases=[
        "Sem erros até o momento, seu colega está seguro",
        "Errar é humano, mantenha a calma e vá devagar",
        "Olhe os olhinhos esperançosos dele, com tem fé em você",
        "Acho que seu colega sente um leve aperto na garganta",
        "Hum, ele está ficando na ponta dos pés, mas ainda tem esperanças",
        "Sabe, este cadafalso tem sede de almas",
            ]
    #a quantidade de erros reflete o index da lista e uso para poder mudar as frases de efeito
    return frases[erros]

#a partir daqui é meio óbvio
def jogo():
    erros=0
    palavra_chave=sorteio()
    mascara=prepara_caminho(palavra_chave)
    
    abertura()
    sleep(3)
    #sistema linux, caso windows use CLR
    os.system("clear")

    #para economizar logica e variáveis apenas vejo se a máscara ainda esta incompleta 
    #conferindo se ainda tem * na mascara e se os erros são inferiores a 6
    #sou da opiniao que sempre que possivel usar menos varáveis, desde que nao comprometa a leitura do programa
    while ("*" in mascara and erros<6):
        print("Status do jogo")
        print("Você tem mais {} tentativas".format(6-erros))
        print(caminh_erro(erros))
        print("Sua palvara escondida tem {} letras".format(len(palavra_chave)))
        print("E foram encontradas as seguintes letras em suas respectivas posições")
        print(mascara)

        chute=entra_char()
        tentativa=find(palavra_chave, chute)
        #olha só como o false da função fica mais facil de ver se deu ruim na escolha do usuário
        if tentativa==False:
            print("Que pena a letra {} não está no menu".format(chute))
            erros=erros+1
        #assm se nao é falso é lista, então desmascaro a mascara (há!)
        else:
            mascara=desmascara(mascara, tentativa, chute)
        sleep(2)
        os.system("clear")
    
    #ao acumular erros o desmascarar palavra escondida ele sai do loop e é hora de descobrir o que houve.
    #como só sai se uma condição ficar falsa, iniciemos com os erros se a condição não for satisfeita
    #quer dizer que a palavrafoi descoberta
    if erros==6:
        print("Você matou o seu companheiro")
        print("A palavra era {}".format(palavra_chave))
    else:
        print(mascara)
        print("Parabéns você não matou o seu companheiro")
    
    print("Até a próxima")

#para queme está aprendendo a linha de código abaixo é muito interessante sobre com o python funciona
#vale a pena parar para entender porque disso
if(__name__ == '__main__'):
    jogo()   
