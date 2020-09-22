from termcolor import colored  # Permite Texto colorido
import os
import glob

class TagedTextOutput:
    def __init__(self, color, text):
        self.color = color
        self.text = text
        self.message = ''

    def PrintTaggedMsg(self, message):
        self.message = message
        return "[  " + colored(self.text, self.color) + "  ] " + message


class CD_rippaddo:
    def __init__(self, ID, Artista, Nome, status, LOG):
        self.ID = ID
        self.Artista = Artista
        self.Nome = Nome
        self.status = status
        self.LOG = LOG


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

def LogCrawler():
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
        print(TagNormal.PrintTaggedMsg("(" + str(i)+"/" + str(len(log_list)-1) + ") " +item))

    return

intro()
LogCrawler()