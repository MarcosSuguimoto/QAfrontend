# QA Frontend - Automação E2E com Selenium & Python

Suíte de testes automatizados End-to-End (E2E) desenvolvida para a aplicação [SauceDemo](https://www.saucedemo.com/), aplicando o padrão de arquitetura **Page Object Model (POM)** e captura automática de evidências visuais.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**
* **Selenium WebDriver** (Automação de interações Web)
* **Pytest** (Framework de testes)
* **Webdriver-Manager** (Gerenciamento do ChromeDriver)
* **Pytest-HTML** (Relatórios visuais de execução)

---

## Arquitetura do Projeto (Page Object Model)

O projeto utiliza a arquitetura **POM** para desacoplar o mapeamento dos elementos da página da lógica dos cenários de teste, facilitando a reusabilidade e manutenção do código:

```text
QAFRONTEND/
├── pages/                  # Camada de Page Objects (elementos e ações)
│   ├── login_page.py
│   └── inventory_page.py
├── tests/                  # Camada de cenários e asserções de teste
│   └── test_e2e_saucedemo.py
├── docs/
│   └── images/             # Capturas de tela (screenshots) de evidência
├── conftest.py             # Fixture global do Selenium WebDriver
├── report.html             # Relatório gerado pelo Pytest
└── README.md