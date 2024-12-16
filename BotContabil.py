from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep 
import openpyxl 

driver = webdriver.Chrome()
driver.get('https://rafaelsobral.pythonanywhere.com/')
sleep(5)

modelos = openpyxl.load_workbook('./planilha.xlsx')
pagina_modelo = modelos['data']

for linha in pagina_modelo.iter_rows(min_row=2,values_only=True):
    Modelo, Marca, Ano = linha

    driver.find_element(By.XPATH,"//a[contains(@class, 'btn-success') and text()='Adicionar']").click()
    sleep(5)

    modelo = driver.find_element(By.XPATH,"//input[@id='id_modelo']")
    modelo.send_keys(Modelo)

    marca = driver.find_element(By.XPATH,"//input[@id='id_marca']")
    marca.send_keys(Marca)

    ano = driver.find_element(By.XPATH,"//input[@id='id_ano']")
    ano.send_keys(Ano)

    driver.find_element(By.XPATH,"//button[contains(@class, 'btn-success') and text()='Enviar']").click()



