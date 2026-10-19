# 1 - Bibliotecas / Imports
from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ==================================
# EDITAR DETALHES DE FATURAMENTO
# ================================== 
@when(u'acedo à secção Detalhes de faturamento')
def step_impl(context):  
    secao = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#billing-details")))
    context.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'start'});", secao)

@when(u'clico em Editar na secçao Detalhes de faturamento')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#billing-details button.lw-brand-text").click()
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'end'});", context.driver.find_element(By.CSS_SELECTOR, "#billing-details"))
    
@when(u'preencho os campos Name {Name}, Address {Address}, City {City}, Postal Code {Postal_Code} e Country {Country} com dados válidos')
def step_impl(context, Name, Address, City, Postal_Code, Country):

    campos = context.driver.find_elements(By.CSS_SELECTOR, "#billing-details input[type='text']")

    nome = campos[0]
    nome.click()
    nome.send_keys(Keys.CONTROL, "a")
    nome.send_keys(Keys.BACKSPACE)
    nome.send_keys(Name)

    address = campos[1]
    address.click()
    address.send_keys(Keys.CONTROL, "a")
    address.send_keys(Keys.BACKSPACE)
    address.send_keys(Address)

    city = campos[2]
    city.click()
    city.send_keys(Keys.CONTROL, "a")
    city.send_keys(Keys.BACKSPACE)
    city.send_keys(City)

    postal_code = campos[3]
    postal_code.click()
    postal_code.send_keys(Keys.CONTROL, "a")
    postal_code.send_keys(Keys.BACKSPACE)
    postal_code.send_keys(Postal_Code)

    context.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", context.driver.find_element(By.CSS_SELECTOR, ".account-input-select"))

    country = context.driver.find_element(By.CSS_SELECTOR, ".account-input-select")
    country.click()

    opcoes = context.driver.find_elements(By.CSS_SELECTOR, ".account-input-select-option")

    for opcao in opcoes:
        if opcao.text == Country:
            opcao.click()
            break

@when(u'clico em Salvar na secçao Detalhes de faturamento')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#billing-details button.lw-brand-text").click()

@then(u'a {mensagem} é exibida')
def step_impl(context, mensagem):
    context.driver.execute_script("window.scrollTo({top: document.documentElement.scrollHeight, behavior: 'instant'});")
    elemento = WebDriverWait(context.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".iziToast-title")))
    assert elemento.text == mensagem