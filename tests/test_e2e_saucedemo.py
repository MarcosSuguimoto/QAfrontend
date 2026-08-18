import os
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Garante que a pasta de imagens exista antes de salvar
OS_PATH = "docs/images"
os.makedirs(OS_PATH, exist_ok=True)

def test_login_com_sucesso(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    # Asserção
    assert inventory_page.get_title() == "Products"
    
    # Print de Evidência
    driver.save_screenshot(f"{OS_PATH}/evidencia_login_sucesso.png")

def test_login_usuario_bloqueado(driver):
    login_page = LoginPage(driver)
    
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    
    # Asserção
    assert "Epic sadface: Sorry, this user has been locked out." in login_page.get_error_message()
    
    # Print de Evidência
    driver.save_screenshot(f"{OS_PATH}/evidencia_usuario_bloqueado.png")

def test_adicionar_produto_ao_carrinho(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()
    
    # Asserção
    assert inventory_page.get_cart_count() == "1"
    
    # Print de Evidência
    driver.save_screenshot(f"{OS_PATH}/evidencia_produto_carrinho.png")