import pyautogui
import platform
import time
import pandas as pd
import pyperclip


class Imagem:
    def __init__(self):
        self.imagem = ''

    def procurar_imagem(self, imagem: str):
        self.imagem = imagem
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(self.imagem)))


class Contatos:
    def __init__(self):
        self.pausa = 1
        self.navegador = 'chrome'

    def alterar_pausa(self, pausa):
        self.pausa = pausa

    def mudar_navegador(self, navegador):
        self.navegador = navegador

    def abrir_navegador(self):
        pyautogui.PAUSE = self.pausa
        if platform.system() == 'Windows':
            pyautogui.press('win')
        else:
            pass
        pyautogui.write(self.navegador)
        pyautogui.press('enter')

    def abrir_aplicacao(self, aplicacao):
        pyautogui.write(aplicacao)
        pyautogui.press('enter')
        while not pyautogui.locateOnScreen('busca_google.png'):
            time.sleep(1)
        Imagem.procurar_imagem(self, imagem='busca_google.png')
        time.sleep(2)
        pyautogui.press('tab', presses=2)
        pyautogui.press('enter')
        while not pyautogui.locateOnScreen('logo_gmail.png'):
            time.sleep(1)

    def _abrir_contatos(self):
        Imagem.procurar_imagem(self, imagem='pontinhos_menu.png')
        Imagem.procurar_imagem(self, imagem='contatos.png')
        while not pyautogui.locateOnScreen('tela_contatos.png'):
            time.sleep(1)

    def exportar_contatos(self):
        self._abrir_contatos()
        Imagem.procurar_imagem(self, imagem='exportar.png')
        Imagem.procurar_imagem(self, imagem='confirmar_exportar.png')


class Correio:
    def __init__(self):
        self.aplicacao = 'gmail'

    def _ler_contatos(self):
        pyautogui.hotkey('ctrl', 'pgup')
        return pd.read_csv(r'C://Users/evlos/Downloads/contacts.csv')

    def escrever_email(self):
        df = self._ler_contatos()
        while not pyautogui.locateOnScreen('escrever.png'):
            time.sleep(1)
        for email in df['E-mail 1 - Value']:
            Imagem.procurar_imagem(self, imagem='escrever.png')
            pyautogui.write(email)
            pyautogui.press('enter')
            pyautogui.press('tab')
            pyautogui.write('Teste de Envio de E-mail - DESCONSIDERAR O CONTEUDO')
            pyautogui.press('tab')
            texto = """
            Coe Irmão,
            
            Beleza?
            
            Abraços"""
            pyperclip.copy(texto)
            pyautogui.hotkey('ctrl', 'v')
            # descomentar para enviar os e-mails
            # pyautogui.hotkey('ctrl', 'enter')


if __name__ == '__main__':
    pyautogui.alert("O código vai começar. POr favor, não mexa em NADA enquanto o código tiver rodando! Eu aviso assim que terminar.")
    contato = Contatos()
    contato.abrir_navegador()
    contato.abrir_aplicacao('gmail')
    contato.exportar_contatos()
    correio = Correio()
    correio.escrever_email()
    pyautogui.alert("O código terminou. Assuma o computador novamente!")

