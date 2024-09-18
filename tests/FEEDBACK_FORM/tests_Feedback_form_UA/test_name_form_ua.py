import pytest
from playwright.sync_api import Page, expect


def test_name_empty_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").click()
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Введіть ім’я")


def test_name_space_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type(" ")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Введіть ім’я")


def test_name_1char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("ї")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Ім’я повинно мати не менше 2 знаків")


def test_name_2char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("їє")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_3char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("їєа")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_15char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Тестування прод")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_29char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Тестування продукту за допомо")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_30char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Тестування продукту за допомог")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_31char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Тестування продукту за допомого")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Ім’я повинно бути не більше 30 знаків")


def test_name_50char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Тестування продукту за допомогою спеціальної прогр")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Ім’я повинно бути не більше 30 знаків")


def test_name_apostrophe_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Т'ес'тува'ння про'дукту")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_hyphen_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Т-ес-тува-ння про-дукту")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_low_case_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("тестування")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_up_case_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("ТЕСТУВАННЯ")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_numb_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Тестування1234567890")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Введіть коректне ім’я")


def test_name_symb_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Т.ест@у,ванняп*р!")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Введіть коректне ім’я")


def test_name_html_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Тест&nbsp")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Введіть коректне ім’я")


def test_name_latin_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ім’я").type("Stepan Andriyovych Bandera")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


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
    expect(setup.locator("//label[@for='firstName']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Введіть коректне ім’я")




