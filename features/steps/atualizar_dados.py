# 1 - Bibliotecas / Imports
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# ====================
# ACEDER A APLICAÇAO 
# ==================== 
@given(u'que acesso o site Iterasys Learnworlds')
def step_impl(context):
    context.driver.get("https://iterasys.learnworlds.com")

def preencher(campo, texto):
    campo.send_keys(texto)
    time.sleep(0.0003)

@when(u'clico em Entrar')
def step_impl(context):
    menu = WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-node-type='hamburger-menu'] button.lw-topbar-hamburger-button")))
    menu.click()

    WebDriverWait(context.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.mobile-nav-menu")))

    seletor = (By.XPATH, "//ul[contains(@class,'mobile-nav-menu')]//span[normalize-space()='Entrar']")
    elementos = WebDriverWait(context.driver, 15).until(EC.presence_of_all_elements_located(seletor))

    elemento = next((e for e in elementos if e.is_displayed()), None)
    assert elemento is not None, "Opção Entrar não encontrada no menu mobile"

    context.driver.execute_script("arguments[0].click();", elemento)

@when(u'preencho os campos de login')
def step_impl(context): 
    email = os.getenv("ITERASYS_EMAIL")
    senha = os.getenv("ITERASYS_PASSWORD")

    preencher(context.driver.find_element(By.CSS_SELECTOR, "#signin-email"), email)
    preencher(context.driver.find_element(By.CSS_SELECTOR, "#signin-password"), senha)

@when(u'clico no botão Entrar')
def step_impl(context):  
    context.driver.find_element(By.CSS_SELECTOR, "#submitLogin").click()

@then(u'sou direcionado para página Home')
def step_impl(context):
    assert WebDriverWait(context.driver, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h2[data-element-id='heading1Normal']"), "Hi, Andréa Souza"))

# =====================================
# ACEDER A SECÇAO PERFIL
# =====================================    
@when(u'acesso ao Perfil através do botao Visit profile')
def step_impl(context):
    elemento = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Visit profile']"))); elemento.click()

@when(u'clico em Edit profile')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "button.learnworlds-button-solid-brand.learnworlds-button-small").click()

# ============================
# ATUALIZAR DADOS PESSOAIS
# ============================ 
@when(u'clico no botao Editar na secçao Dados pessoais')
def step_impl(context):   
    context.driver.find_element(By.CSS_SELECTOR, "#personal-details button").click() 

@when(u'preencho os campos Nome {Nome} e E-mail {Email}')
def step_impl(context, Nome, Email):
    # Preenche o nome
    nome = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='personal-details-username-input']")))
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", nome)
    nome.click()
    nome.send_keys(Keys.CONTROL, "a")
    nome.send_keys(Keys.BACKSPACE)
    nome.send_keys(Nome)

    # Preenche o email
    email = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='personal-details-email-input']")))
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", email)
    email.click()
    email.send_keys(Keys.CONTROL, "a")
    email.send_keys(Keys.BACKSPACE)
    email.send_keys(Email)
    
@when(u'clico no botão Salvar')
def step_impl(context):
    context.driver.find_element( By.CSS_SELECTOR, "#personal-details button.lw-brand-text").click()

# =============
# NOME VAZIO
# =============
@when(u'preencho os campos Nome  e E-mail {Email}')
def step_impl(context, Email):
    nome = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='personal-details-username-input']")))
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", nome)
    nome.click()
    nome.send_keys(Keys.CONTROL, "a")
    nome.send_keys(Keys.BACKSPACE)

    email = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='personal-details-email-input']")))
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", email)
    email.click()
    email.send_keys(Keys.CONTROL, "a")
    email.send_keys(Keys.BACKSPACE)
    email.send_keys(Email)

# =============
# E-MAIL VAZIO
# =============
@when(u'preencho os campos Nome {Nome} e E-mail ')
def step_impl(context, Nome):
    nome = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='personal-details-username-input']")))
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", nome)
    nome.click()
    nome.send_keys(Keys.CONTROL, "a")
    nome.send_keys(Keys.BACKSPACE)
    nome.send_keys(Nome)

    email = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='personal-details-email-input']")))
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", email)
    email.click()
    email.send_keys(Keys.CONTROL, "a")
    email.send_keys(Keys.BACKSPACE)

# ===============
# VALIDAR DADOS 
# ================   
@then(u'os dados pessoais sao atualizados com sucesso')
def step_impl(context):
    assert context.driver.find_element(By.ID, "text_input_1").get_attribute("value") == "Andréa Souza"
    assert context.driver.find_element(By.ID, "text_input_2").get_attribute("value") == "aamorim1705@gmail.com"
 
@then(u'exibe a {mensagem} de erro')
def step_impl(context, mensagem):
    assert context.driver.find_element(By.CSS_SELECTOR, "#personal-details span.lw-red-text").text == mensagem