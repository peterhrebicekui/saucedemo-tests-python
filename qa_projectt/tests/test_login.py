from selenium.webdriver.common.by import By


def test_successful_login(driver):
    """Pozitívny test: Overenie úspešného prihlásenia so správnymi údajmi."""
    driver.get("https://www.saucedemo.com/")

    # Vyplnenie správnych údajov
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Overenie presmerovania na stránku s produktmi
    assert (
        "inventory.html" in driver.current_url
    ), "Chyba: Nepodarilo sa úspešne prihlásiť!"


def test_invalid_password_login(driver):
    """Negatívny test: Overenie zobrazenia chybovej hlášky pri zlom hesle."""
    driver.get("https://www.saucedemo.com/")

    # Vyplnenie mena so zlou kombináciou hesla
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("zle_heslo_123")
    driver.find_element(By.ID, "login-button").click()

    # 1. Lokalizácia prsúceho elementu chybovej správy
    error_element = driver.find_element(
        By.XPATH, "//h3[@data-test='error']"
    )

    # 2. Overenie, či sa chybová hláška zobrazuje na stránke
    assert (
        error_element.is_displayed()
    ), "Chyba: Chybová hláška sa nezobrazuje!"

    # 3. Overenie presného textu chybovej správy
    expected_error = (
        "Epic sadface: Username and password do not match any user in this service"
    )
    assert (
        expected_error in error_element.text
    ), f"Očakával sa text '{expected_error}', ale zobrazil sa: '{error_element.text}'"