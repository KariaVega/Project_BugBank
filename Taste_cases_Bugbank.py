import Data
import time
from selenium import webdriver
from main import BugBankPage


class TestBugBank:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    # Prueba 1 Hacer Clic en botón Registro 1 en pagina de inicio
    def test_select_register_button1(self):
        self.driver.get(Data.Bug_Bank_url)
        bugbank_page = BugBankPage(self.driver)
        bugbank_page.click_register_button1()

    # Prueba 2 Rellenar campo de email y name
    def test_set_data_logging(self):
        bugbank_page = BugBankPage(self.driver)
        email_field = Data.email_field
        name_field = Data.name_field
        bugbank_page.set_data_logging(email_field, name_field)
        assert bugbank_page.get_email_field() == email_field
        assert bugbank_page.get_name_field() == name_field

    # Prueba 3 Rellenar campo de password y confirmation password
    def test_set_register_password(self):
        bugbank_page = BugBankPage(self.driver)
        password_field = Data.password_field
        confirmation_field = Data.confirmation_field
        bugbank_page.set_register_password(password_field, confirmation_field)
        assert bugbank_page.get_password_field() == password_field
        assert bugbank_page.get_confirmation_field() == confirmation_field

    # Prueba 4 Hacer Clic en botón Registro 2 en pagina de formulario
    def test_select_form_page_button2(self):
        bugbank_page = BugBankPage(self.driver)
        bugbank_page.click_register_button2()


