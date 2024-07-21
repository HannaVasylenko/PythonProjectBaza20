import pytest
from playwright.sync_api import Page, expect


def test_name_empty_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").click()
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть ім’я")


def test_name_space_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type(" ")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть ім’я")


def test_name_1char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("ї")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно мати не менше 2 знаків")


def test_name_2char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("їє")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_3char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("їєа")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_15char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Шухевич Роман О")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_29char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Степан Андрійович Бандера ОУН")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_30char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("степан андрійович бандераоун-б")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_31char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Степан Андрійович Бандера ОУН-Б")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно бути не більше 30 знаків")


def test_name_50char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Степан Бандера Коновалець Євген Шухевич Романдіячі")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно бути не більше 30 знаків")


def test_name_apostrophe_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("С'тепан'Андрійович'Бандера")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_hyphen_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("С-тепан-Андрійович-Бандера")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_low_case_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("тестування")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_up_case_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("ТЕСТУВАННЯ")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_name_numb_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("СтепанБандера1234567890")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")


def test_name_symb_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("С.теп@н,Бандер*а!")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")


def test_name_html_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Тест&nbsp")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")


def test_name_latin_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Stepan Andriyovych Bandera")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.parametrize("test_input", [
    ("Пръерплрт"),
    ("Орамыьтор"),
    ("апмЭтиор"),
    ("потлоЁьтбоа"),
    ("Тиитрэтьтор"),
    ("Иимпаётир")
])
def test_name_piletters_fform_ua(setup: Page, test_input) -> None:
    setup.get_by_placeholder("Ім’я").press("Control+A")
    setup.get_by_placeholder("Ім’я").press("Delete")
    setup.get_by_placeholder("Ім’я").type(test_input)
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")




