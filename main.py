from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import dotenv
import os


class Main():
    def __init__(self) -> None:
        # Carrega as variaveis de ambiente
        dotenv.load_dotenv(dotenv.find_dotenv())
        pass

    def executar(self):
        self._carregarNavegador()
        self._login()
        self._baixarFaturaAtual()

    def _carregarNavegador(self):
        try:
            self._servico_responsavel_versao_chrome = Service(
                ChromeDriverManager().install())
            self.navegador = webdriver.Chrome(
                service=self._servico_responsavel_versao_chrome)
            # Maximiza o navegador
            self.navegador.maximize_window()
            time.sleep(3)
        except Exception as e:
            # Log de alerta informando que nao deu para abrir o navegador
            raise Exception("Erro ao carregar webdriver do chrome")

    def _login(self):
        # Acessa o site da EDP
        self.navegador.get(
            "https://www.edponline.com.br/para-sua-casa/login")

        # Aguarda o popup de aceitar cookies aparecer
        time.sleep(5)

        # Clica no botao de fechar o popup
        self.navegador.find_element(
            'xpath', '//*[@id="onetrust-close-btn-container"]/button').click()

        # Aguarda o popup de aceitar cookies desaparecer
        time.sleep(3)

        # Busca o elemento do checkbox e marca
        self.navegador.find_element(
            'xpath', '//*[@id="login-form"]/div[1]/div[2]/label').click()

        # Busca o elemento do email e digita
        self.navegador.find_element(
            'xpath', '//*[@id="Email"]').send_keys(os.getenv("EDP_ACCOUNT"))

        # Busca o elemento da senha e digita
        self.navegador.find_element(
            'xpath', '//*[@id="Senha"]').send_keys(os.getenv("EDP_PASSWORD"))

        # Busca o elemento do botao Acessar
        self.navegador.find_element(
            'xpath', '//*[@id="acessar"]').click()

        # Aguarda alterar a pagina
        time.sleep(10)

    def _baixarFaturaAtual(self):

        # Clica no link da instalação
        self.navegador.find_element(
            'xpath', '//*[@id="grid"]/table/tbody/tr/td[1]/a').click()

        # Aguarda carregar a pagina de resumo da conta
        time.sleep(5)

        # Fecha o modal de atualização cadastral
        self.navegador.find_element(
            'xpath', '//*[@id="modal-alteracao-cadastral"]/div/div/div[1]/button').click()

        # Aguarda o modal fechar
        time.sleep(3)

        # Fecha o modal de Protocolo de atendimento
        self.navegador.find_element(
            'xpath', '//*[@id="modal-protocolo-principal"]/div/div/div[1]/button').click()

        # Aguarda o modal fechar
        time.sleep(3)

        # Clica no botao de Abrir essa conta
        self.navegador.find_element(
            'xpath', '//*[@id="ultima-conta"]/div/div/div[3]/a[2]').click()

        # Aguarda carregar a pagina das faturas
        time.sleep(3)

        # Clica no botao de Abrir essa conta
        card_a_vencer = self.navegador.find_element(
            'xpath', '//*[@id="extrato-de-contas"]/div/div/div/div[1]/div/div/div/div[1]/div/div/div[3]')

        if card_a_vencer.is_displayed():
            # Clica no botao Ver Fatura
            self.navegador.find_element(
                'xpath', '//*[@id="extrato-de-contas"]/div/div/div/div[1]/div/div/div/div[1]/div/div/div[3]/div[2]/div[2]/a[1]').click()

            # Aguarda carregar o modal com a fatura
            time.sleep(5)

            # Clica no botao Baixar
            self.navegador.find_element(
                'xpath', '//*[@id="box-dados-fatura"]/div/div[3]/a').click()

        time.sleep(10)
        print("End of script...")


if __name__ == '__main__':
    try:
        Main().executar()
    except Exception as e:
        print("error: ", e)
