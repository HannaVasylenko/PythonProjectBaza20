import pytest
from playwright.sync_api import Page, expect


def test_surname_empty_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").click()
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Введіть своє прізвище")


def test_surname_space_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type(" ")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Введіть своє прізвище")


def test_surname_1char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("ї")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Прізвище повинно мати не менше 2 знаків")


def test_surname_2char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("їє")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_3char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("їєа")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_25char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("Тестування продукту за до")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_49char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("Тестування продукту за допомогою спеціальної прог")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_50char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("Тестування продукту за допомогою спеціальної прогр")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_51char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("Тестування продукту за допомогою спеціальної програ")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Прізвище повинно бути не більше 50 знаків")


def test_surname_76char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("Тестування продукту за допомогою спеціальної програми для покращення якостіп")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Прізвище повинно бути не більше 50 знаків")


def test_surname_apostrophe_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("Т'ес'тува'ння про'дукту")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_hyphen_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("Т-ес-тува-ння про-дукту")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_surname_numb_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("Тестуванняпродукту1234567890")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Введіть коректне Прізвище")


def test_surname_symbols_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("Т.ест@у,ванняп*р!")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Введіть коректне Прізвище")


def test_surname_latin_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("Stepan Andriyovych Bandera")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_low_case_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("тестування")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_up_case_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("ТЕСТУВАННЯ")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_space_in_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").type("тестування тестування тестування")
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe")


@pytest.mark.parametrize("test_input", [
    ("Пръерплрт"),
    ("Орамыьтор"),
    ("апмЭтиор"),
    ("потлоЁьтбоа"),
    ("Тиитрэтьтор"),
    ("Иимпаётир")
])
def test_surname_piletters_mentor_ua(setup: Page, test_input) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Прізвище").press("Control+A")
    setup.get_by_placeholder("Прізвище").press("Delete")
    setup.get_by_placeholder("Прізвище").type(test_input)
    setup.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='lastName']/following-sibling::p")).to_have_text("Введіть коректне Прізвище")

