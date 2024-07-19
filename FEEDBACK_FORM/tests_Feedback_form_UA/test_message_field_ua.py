import re
import pytest
from playwright.sync_api import Page, expect


def test_message_empty_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").click()
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Введіть повідомлення")


def test_message_space_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type(" ")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Введіть повідомлення")


def test_message_1char_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type("ї")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Повідомлення повинно мати не менше 10 знаків")


def test_message_2char_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type("їє")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Повідомлення повинно мати не менше 10 знаків")


def test_message_5char_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type("любов")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Повідомлення повинно мати не менше 10 знаків")


def test_message_9char_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type("привітики")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Повідомлення повинно мати не менше 10 знаків")


def test_message_10char_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type("привітусім")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_11char_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type("привіт усім")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_150char_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type("привітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривіт")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_299char_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type("привітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітприві")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_300char_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type("привітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривіт")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_301char_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type("привітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітп")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Просимо скоротити ваше повідомлення до 300 знаків")


def test_message_upcase_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type("УДОСКОНАЛЮЄМО НАВИЧКИ НА ПРАКТИЦІ")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_lowcase_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type("тестування продукту")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_symb_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type("Символи !-_().,<>&?@$=+{}#*/[]\|?%^:;`₴’’””<>&?@$=+*\[/]?%;:")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_message_num_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("Ваше повідомлення").type("Символи 1234567890")
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.parametrize("test_input", [
    ("Пръерплртфівапру"),
    ("Орамыьторйцукен"),
    ("апмЭтиорйцукенг"),
    ("потлоЁьтбоайцукенг"),
    ("Тиитрэтьторйцукенг"),
    ("Иимпаётирйцукенг")
])
def test_message_piletters_fieldf_ua(setup: Page, test_input) -> None:
    setup.get_by_placeholder("Ваше повідомлення").press("Control+A")
    setup.get_by_placeholder("Ваше повідомлення").press("Delete")
    setup.get_by_placeholder("Ваше повідомлення").type(test_input)
    setup.get_by_placeholder("email@gmail.com").click()
    expect(setup.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Введіть коректне повідомлення")

