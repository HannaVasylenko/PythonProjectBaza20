import re
import pytest
from playwright.sync_api import Page, expect


def test_surnamepr_1char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("ї")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Прізвище повинно мати не менше 2 знаків")


def test_surnamepr_empty_field_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").click()
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть своє прізвище")


def test_surnamepr_2char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("їє")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surnamepr_3char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("їєа")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surnamepr_25char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("Технікитестдизайнучекліст")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surnamepr_49char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("Технікитестдизайнучеклістидефектрепортитесткейсию")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surnamepr_50char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("Технікитестдизайнучеклістидефектрепортитесткейсиюа")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surnamepr_51char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("Технікитестдизайнучеклістидефектрепортитесткейсиюаю")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Прізвище повинно бути не більше 50 знаків")


def test_surnamepr_70char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("Технікитестдизайнучеклістидефектрепортитесткейсиюайцукенгшщзфівапролдї")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Прізвище повинно бути не більше 50 знаків")


def test_surnamepr_apostrophe_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("Т'ехніки'тест'дизайну")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surnamepr_hyphen_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("Т-ехніки-тест-дизайну")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surnamepr_space_in_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("Техніки тест дизайну")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surnamepr_low_case_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("технікитестдизайну")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surnamepr_up_case_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("ТЕХНІКИТЕСТДИЗАЙНУ")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_surnamepr_numbers_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("Технікитестдизайну1234567890")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище") #last name


def test_surnamepr_symbols_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type("Т.ех,ні!ките@стдиз_айну")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище") #last name


def test_surnamepr_only_spce_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").type(" ")
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть своє прізвище")


@pytest.mark.parametrize("test_input", [
    ("Пръерплрт"),
    ("Орамыьтор"),
    ("апмЭтиор"),
    ("потлоЁьтбоа"),
    ("Тиитрэтьтор"),
    ("Иимпаётир")
])
def test_surnamepr_piletters_ua(setup: Page, test_input) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Прізвище").press("Control+A")
    setup.get_by_placeholder("Прізвище").press("Delete")
    setup.get_by_placeholder("Прізвище").type(test_input)
    setup.get_by_placeholder("Ім’я").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище") #last name










