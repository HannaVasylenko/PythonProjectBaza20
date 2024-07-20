import re
from playwright.sync_api import Page, expect


def test_phonepr_valid_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phonepr_empty_field_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть номер телефону")


def test_phonepr_space_field_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type(" ")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть номер телефону")


def test_phonepr_enter_digits_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("123456789")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phonepr_enter_value_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phonepr_1char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("1")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phonepr_2char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("12")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phonepr_6char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("12")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phonepr_12char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("99999999")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phonepr_13char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_phonepr_14char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("9999999999")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phonepr_20char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("9999999999999999")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phonepr_сyrillic_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phonepr_onlyсyrillic_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phonepr_latin_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phonepr_onlylatin_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phonepr_without_start_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("1234567891230")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phonepr_onlysymbols_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("*@#!?.#:;=+()")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")


def test_phonepr_symbols_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup.get_by_placeholder("+380 xx xxx xx xx").type("*@!?.#:;")
    setup.get_by_placeholder("Київ").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
