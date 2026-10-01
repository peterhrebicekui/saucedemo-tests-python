# 🧪 SauceDemo UI Test Automation Suite

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Automation-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)

Automated end-to-end (E2E) UI test automation framework built for the **SauceDemo** web application (`https://www.saucedemo.com/`). Designed with **Python**, **pytest**, and **Selenium WebDriver** to demonstrate automated QA best practices.

---

## 📌 Project Features

- **Fixtures Management:** Uses `conftest.py` for dynamic browser setup and tear-down execution.
- **E2E UI Testing:** Validates critical user journeys (positive & negative authentication scenarios).
- **Assertion Validation:** Clear and descriptive error reporting upon test failures.
- **Clean Project Structure:** Separation of framework configuration and test scripts.

---

## 📁 Repository Structure

```text
saucedemo-tests-python/
│
├── conftest.py          # Pytest fixtures for WebDriver initialization
├── tests/
│   └── test_login.py    # Test scenarios for login functionality
├── .gitignore           # Ignored files (.venv, cache, IDE settings)
└── README.md            # Project documentation