from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BugBankPage:
    register_button1 = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[3]/button[2]')
    text_register_button1 = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/form/div[3]/button[2]')
    email_field = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[2]/input')
    name_field = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[3]/input')
    password_field = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[4]/div/input')
    confirmation_field = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/div[5]/div/input')
    register_button2 = (By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/form/button')

    def __init__(self, driver):
        self.driver = driver

    # Prueba 1 -------------------------- Pagina de inicio Botón de Registro 1
    def click_register_button1(self):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(self.register_button1))
        self.driver.find_element(*self.register_button1).click()
        # no hay que dar clic ya que se verifica que este disponible

    def check_text_register_button1(self):
        return self.driver.find_element(*self.text_register_button1).text
        # verifica el elemento por el texto

    # Prueba 2 -------------------------- Página de Registro, campos email y name
    def set_email_field(self, fill_email):
        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.email_field))
        self.driver.find_element(*self.email_field).click()
        self.driver.find_element(*self.email_field).send_keys(fill_email)

    def set_name_field(self, fill_name):
        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.name_field))
        self.driver.find_element(*self.name_field).click()
        self.driver.find_element(*self.name_field).send_keys(fill_name)

    def get_email_field(self):
        return self.driver.find_element(*self.email_field).get_property('value')  # estos vienen de los localizadores

    def get_name_field(self):
        return self.driver.find_element(*self.name_field).get_property('value')  # estos vienen de los localizadores

    def set_data_logging(self, email_field, name_field):
        self.set_email_field(email_field)  # estos vienen de data
        self.set_name_field(name_field)  # estos vienen de data

    # Prueba 3 -------------------------- Página de Registro, campos password y confirm password
    def set_password_field(self, fill_password):
        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.password_field))
        self.driver.find_element(*self.password_field).send_keys(fill_password)

    def set_confirmation_field(self, fill_confirmation):
        WebDriverWait(self.driver, 4).until(expected_conditions.visibility_of_element_located(self.confirmation_field))
        self.driver.find_element(*self.confirmation_field).send_keys(fill_confirmation)

    def get_password_field(self):
        return self.driver.find_element(*self.password_field).get_property('value')  # estos vienen de los localizadores

    def get_confirmation_field(self):
        return self.driver.find_element(*self.confirmation_field).get_property('value')  # estos vienen de los localizadores

    def set_register_password(self, password_field, confirmation_field):
        self.set_password_field(password_field)   # estos vienen de data
        self.set_confirmation_field(confirmation_field)  # estos vienen de data

    # Prueba 4 -------------------------- Página de Registro, botón Registro2

    def click_register_button2(self, register_button2):
        WebDriverWait(self.driver, 6).until(expected_conditions.visibility_of_element_located(self.register_button2))
        self.driver.find_element(*self.register_button2).click()


