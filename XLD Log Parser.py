import glob

from termcolor import colored  # Permite Texto colorido


class TagedTextOutput:
    def __init__(self, color, text):
        self.color = color
        self.text = text
        self.message = ''

    def PrintTaggedMsg(self, message):
        self.message = message
        return "[  " + colored(self.text, self.color) + "  ] " + message


class CDrippaddo:
    def __init__(self, id, artista, nome, status, log):
        self.id = id
        self.artista = artista
        self.Nome = nome
        self.status = status
        self.LOG = log


class Tracksdocd:
    def __init__(self):
        self.tracknumber = ""
        self.trackstatus = ""


TagAviso = TagedTextOutput('yellow', 'Aviso')
TagNormal = TagedTextOutput('green', 'Normal')
TagMensagem = TagedTextOutput('magenta', 'Mensagem')
TagErro = TagedTextOutput('red', 'Erro')


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
    print(TagMensagem.PrintTaggedMsg("Iniciando Aplicação..."))
    print(TagMensagem.PrintTaggedMsg("Vai Começar a putaria...."))


def logcrawler():
    log_list = []
    for file in glob.glob("**/*.log", recursive=True):
        log_list.append(file)
    log_amount = len(log_list)
    if log_amount != 0:
        print(TagNormal.PrintTaggedMsg("Foi encontrado: " + str(log_amount) + " Logs"))
    else:
        print(TagErro.PrintTaggedMsg("Nenhum Log Encontrado"))
        print(TagErro.PrintTaggedMsg("Saindo"))
    for i, item in enumerate(log_list):
        print(TagNormal.PrintTaggedMsg("(" + str(i) + "/" + str(len(log_list) - 1) + ") " + item))

    return log_list


def logsparser(logs):
    for i, item in enumerate(logs):
        print(TagNormal.PrintTaggedMsg("ABRINDO:(" + str(i) + "/" + str(len(logs) - 1) + ") " + item))
        with open(logs[i], 'r') as f:
            f_conteudo = f.readlines()
            if any("Disc not found in AccurateRip DB." in word for word in f_conteudo):
                print(TagAviso.PrintTaggedMsg("CD Não usou AccurateRip"))
        print(f_conteudo[4])


intro()
crawler_results = logcrawler()
logsparser(crawler_results)
