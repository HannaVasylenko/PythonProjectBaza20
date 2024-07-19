import re
import pytest
from playwright.sync_api import Page, expect


def test_name_empty_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть своє ім’я")


def test_name_space_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type(" ")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть своє ім’я")


def test_name_1char_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("ї")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно мати не менше 2 знаків")


def test_name_2char_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("їє")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_3char_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("їєа")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_15char_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Шухевич Роман О")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_29char_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Степан Андрійович Бандера ОУН")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_30char_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("степан андрійович бандераоун-б")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_31char_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Степан Андрійович Бандера ОУН-Б")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно бути не більше 30 знаків")


def test_name_50char_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Степан Бандера Коновалець Євген Шухевич Романдіячі")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно бути не більше 30 знаків")


def test_name_apostrophe_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("С'тепан'Андрійович'Бандера")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_hyphen_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("С-тепан-Андрійович-Бандера")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_numb_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("СтепанБандера1234567890")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")


def test_name_symbols_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("С.теп@н,Бандер*а!")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")


def test_name_latin_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Stepan Andriyovych Bandera")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_low_case_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("тестування")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_up_case_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("ТЕСТУВАННЯ")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_spacein_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Техніки тест дизайну")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.parametrize("test_input", [
    ("Пръерплрт"),
    ("Орамыьтор"),
    ("апмЭтиор"),
    ("потлоЁьтбоа"),
    ("Тиитрэтьтор"),
    ("Иимпаётир")
])
def test_name_piletters_ua(setup: Page, test_input) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).press("Control+A")
    setup.get_by_role("textbox", name="Ім’я", exact=True).press("Delete")
    setup.get_by_role("textbox", name="Ім’я", exact=True).type(test_input)
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    
    