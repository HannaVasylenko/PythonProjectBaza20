import pytest
from playwright.sync_api import Page, expect


def test_name_empty_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Введіть своє ім’я")


def test_name_space_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type(" ")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Введіть своє ім’я")


def test_name_1char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("ї")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Ім’я повинно мати не менше 2 знаків")


def test_name_2char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("їє")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_3char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("їєа")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_15char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Тестування прод")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_29char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Тестування продукту за допомо")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_30char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Тестування продукту за допомог")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_31char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Тестування продукту за допомого")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Ім’я повинно бути не більше 30 знаків")


def test_name_50char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Тестування продукту за допомогою спеціальної прогр")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Ім’я повинно бути не більше 30 знаків")


def test_name_apostrophe_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Т'ес'тува'ння про'дукту")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_hyphen_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Т-ес-тува-ння про-дукту")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_numb_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Тестування1234567890")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Введіть коректне ім’я")


def test_name_symbols_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Т.ест@у,ванняп*р!")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Введіть коректне ім’я")


def test_name_latin_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Stepan Andriyovych Bandera")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_low_case_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("тестування")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_up_case_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("ТЕСТУВАННЯ")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_name_space_in_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).type("Техніки тест дизайну")
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe")


@pytest.mark.parametrize("test_input", [
    ("Пръерплрт"),
    ("Орамыьтор"),
    ("апмЭтиор"),
    ("потлоЁьтбоа"),
    ("Тиитрэтьтор"),
    ("Иимпаётир")
])
def test_name_piletters_mentor_ua(setup: Page, test_input) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).press("Control+A")
    setup.get_by_role("textbox", name="Ім’я", exact=True).press("Delete")
    setup.get_by_role("textbox", name="Ім’я", exact=True).type(test_input)
    setup.get_by_placeholder("Прізвище").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='firstName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='firstName']/following-sibling::p")).to_have_text("Введіть коректне ім’я")
    
    