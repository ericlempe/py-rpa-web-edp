from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


class Main():
    def __init__(self) -> None:
        pass

    def executar(self):
        self._carregarNavegador()
        self._login()

    def _carregarNavegador(self):
        try:
            self._servico_responsavel_versao_chrome = Service(
                ChromeDriverManager().install())
            self.navegador = webdriver.Chrome(
                service=self._servico_responsavel_versao_chrome)
        except Exception as e:
            # Log de alerta informando que nao deu para abrir o navegador
            raise Exception("Erro ao carregar webdriver do chrome")

    def _login(self):
        print("Iniciando o script...")
        # Acessa o site da EDP
        self.navegador.get("https://www.edponline.com.br/para-sua-casa/login")

        # Busca o elemento do usuario e digita a conta
        # self.navegador.find_element(
        #     'xpath', '//*[@id="normal_login_username"]').send_keys(self.contaPaytrack)

        # Busca o elemento do botao de Proximo e executa um click
        # self.navegador.find_element(
        #     'xpath', '//*[@id="root"]/main/div[2]/div[2]/form/div[4]/button').click()

        # Aguarda alterar a pagina
        time.sleep(20)

        print("Fim da execucao...")


if __name__ == '__main__':
    try:
        Main().executar()
    except Exception as e:
        print(e)
