# 1 - Bibliotecas / Imports
from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ===================================
# VISUALIZAR HISTÓRICO DE PAGAMENTOS
# ===================================

@when(u'acedo à secção Pagamentos')
def step_impl(context):
    secao = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#payments")))
    context.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'start'});", secao)

@then(u'o histórico de pagamentos é apresentado para consulta')
def step_impl(context):
    historico = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='payment-history-table']")))
    assert historico.is_displayed(), "Histórico de pagamentos"