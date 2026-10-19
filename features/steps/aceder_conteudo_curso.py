# 1 - Bibliotecas / Imports
from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# =========================
# ACEDER CONTEÚDO CURSOS
# ======================== 
@when(u'clico em Pro na secção Cursos e programas')
def step_impl(context):
    elemento = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href^='/program-player?program=']")))
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)
    elemento.click()

@then(u'sou direcionado para página dos Cursos')
def step_impl(context):
    assert WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.learnworlds-heading"))).text == "Pro"

@then(u'posso aceder ao conteúdo dos cursos')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.card-link.lw-card-top"))).click()