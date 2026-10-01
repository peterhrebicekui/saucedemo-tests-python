# Konfigurácia a nastavenie prehliadača (tzv. fixtures)


import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Inicializácia prehliadača Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Poskytnutie driveru do testu
    yield driver

    # Ukončenie prehliadača po skončení testu
    driver.quit()