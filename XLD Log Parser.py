import glob
import yaml
import random
from termcolor import colored  # Permite Texto colorido


def textTagger(type, message):
    if type == 0:
        print("[" + colored("  MENSAGEM  ", 'magenta') + "] " + message)
    elif type == 1:
        print("[" + colored("  NORMAL  ", 'green') + "] " + message)
    elif type == 2:
        print("[" + colored("  AVISO  ", 'yellow') + "] " + message)
    elif type == 3:
        print("[" + colored("  ERRO  ", 'red') + "] " + message)


def intro():
    print("                        ")
    print("                        ")
    print("             .--------------------------------------.")
    print("             |        XLD CD RIPPER Log Parser      |")
    print("             |                                      |")
    print("             |             Version: 0.1             |")
    print("             |                                      |")
    print("             .--------------------------------------.")
    print("                        ")
    print("                        ")
    textTagger(0, "Iniciando Aplicação...")
    textTagger(0, "Vai Começar a putaria....")

def logcrawler():
    log_list = []
    for file in glob.glob("**/*.log", recursive=True):
        log_list.append(file)
    log_amount = len(log_list)
    if log_amount != 0:
        textTagger(1, "Foi encontrado: " + str(log_amount) + " Logs")
    else:
        textTagger(3, "Nenhum Log Encontrado")
        textTagger(3, "Saindo")
    for i, item in enumerate(log_list):
        textTagger(1, "(" + str(i) + "/" + str(len(log_list) - 1) + ") " + item)

    return log_list


def logsparser(logs):
    cd = {}
    cds = {}
    listafaixas = {}
    faixas = {}
    for i, item in enumerate(logs):
        textTagger(1, "ABRINDO:(" + str(i) + "/" + str(len(logs) - 1) + ") " + item)
        with open(logs[i], 'r') as f:
            f_conteudo = f.readlines()
            print("Tamanho do Arquivo de log: " + str(len(f_conteudo)) + " Linhas")  # ToDo: Remover essa linha de teste

            if any("Disc not found in AccurateRip DB." in word for word in f_conteudo):
                textTagger(2, "O CD " + (f_conteudo[4]).replace("\n", "") + " Não usou AccurateRip")
                AccurateRip = False

            else:
                AccurateRip = True

            print(f_conteudo[4])  # ToDo: Remover essa linha de teste \btodo
            Artista_titulo = f_conteudo[4].split(" / ")
            Artista_titulo[1] = Artista_titulo[1].replace("\n", "")
            cds[i] = cd[i] = {"Artista": Artista_titulo[0], "Titulo": Artista_titulo[1], "AccurateRip": AccurateRip}
            print(len(cds))
        line_counter = 19
        while line_counter < len(f_conteudo):
            if f_conteudo[line_counter] == '\n':
                numero_faixas = (line_counter - 19)
                print("numero de Faixas:" + str(numero_faixas))  # ToDo: Remover essa linha de teste

                break
            else:
                print(f_conteudo[line_counter])
                line_counter += 1


intro()
crawler_results = logcrawler()
logsparser(crawler_results)
