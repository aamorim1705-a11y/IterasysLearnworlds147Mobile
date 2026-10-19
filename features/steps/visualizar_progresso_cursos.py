# 1 - Bibliotecas / Imports
from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ================================
# VISUALIZAR PROGRESSO DOS  CURSOS
# ================================ 
@when(u'clico no programa disponível Pro na secção Cursos e programas')
def step_impl(context):
    elemento = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href^='/program-player?program=']")))
    context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elemento)
    elemento.click()

@then(u'consigo visualizar o progresso dos cursos')
def step_impl(context):
    link = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.card-link.lw-card-top[href*='/path-player']")))
    estado = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.lw-tag.in-progress")))
    progresso = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(., '%')]")))

    assert link.is_displayed()
    assert estado.text.strip() == "Em andamento"
    assert progresso.text.strip().startswith("12%")