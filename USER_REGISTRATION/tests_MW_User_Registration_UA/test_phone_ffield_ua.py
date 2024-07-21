import re
from playwright.sync_api import Page, expect


def test_phone_valid_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phone_empty_field_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть номер телефону")


def test_phone_space__user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type(" ")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть номер телефону")


def test_phone_enter_digits_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("123456789")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phone_enter_value_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phone_1char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("1")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phone_2char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("12")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phone_6char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("12")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phone_12char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("99999999")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phone_13char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phone_14char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("9999999999")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phone_20char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("9999999999999999")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phone_cyrillic_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phone_only_cyrillic_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phone_latin_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phone_only_latin_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phone_without_start_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("1234567891230")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phone_only_symbols_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("*@#!?.#:;=+()")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phone_symbols_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("*@!?.#:;")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
