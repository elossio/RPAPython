import pyautogui
import platform
import time


class MeuRPA:
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

    def _procurar_imagem(self, imagem: str):
        self.imagem = imagem
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(self.imagem)))

    def abrir_aplicacao(self, aplicacao):
        pyautogui.write(aplicacao)
        pyautogui.press('enter')
        while not pyautogui.locateOnScreen('busca_google.png'):
            time.sleep(1)
        self._procurar_imagem(imagem='busca_google.png')
        time.sleep(2)
        pyautogui.press('tab', presses=2)
        pyautogui.press('enter')
        while not pyautogui.locateOnScreen('logo_gmail.png'):
            time.sleep(1)

    def _abrir_contatos(self):
        self._procurar_imagem(imagem='pontinhos_menu.png')
        self._procurar_imagem(imagem='contatos.png')
        while not pyautogui.locateOnScreen('tela_contatos.png'):
            time.sleep(1)

    def exportar_contatos(self):
        self._abrir_contatos()
        self._procurar_imagem(imagem='exportar.png')
        self._procurar_imagem(imagem='confirmar_exportar.png')

if __name__ == '__main__':
    controlador = MeuRPA()
    controlador.abrir_navegador()
    controlador.abrir_aplicacao('gmail')
    controlador.exportar_contatos()

