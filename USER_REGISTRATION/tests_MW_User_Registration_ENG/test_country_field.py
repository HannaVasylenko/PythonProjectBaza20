import re
from playwright.sync_api import Page, expect


def test_country_space(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type(" ")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Enter the correct country name")


def test_countrypr_empty_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").click()
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_country_1char(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("u")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Enter the correct country name")
    expect(setup_en.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char")


def test_country_2char(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("uk")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Enter the correct country name")
    expect(setup_en.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char")


def test_country_3char(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("ukr")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Enter the correct country name")
    expect(setup_en.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char")


def test_country_4char(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("ukra")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_country_5char(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("ukrai")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_country_15char(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("KharkivLvivSumy")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_country_29char(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("qwertyuiopasdfghjklqqawsedrft")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_country_30char(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("qwertyuiopasdfghjklqqawsedrftq")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_country_31char(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("qwertyuiopasdfghjklqqawsedrftqa")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='country']/../following-sibling::p")).to_have_text("The name of the country should not exceed 30 characters")


def test_country_50char(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='country']/../following-sibling::p")).to_have_text("The name of the country should not exceed 30 characters")


def test_country_numbers(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("1234567890")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Enter the correct country name")


def test_country_hyphen(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("K-harkiv-Lviv-Sumy")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_country_apostrophe(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("K'harkiv'Lviv'Sumy")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_country_space_in(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("Kharkiv Lviv Sumy")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_country_symbols(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("Kh@rk!vLv#v?umy")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Enter the correct country name")


def test_country_сyrillic(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("Україна")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_countrypr_upcase_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("KHARKIV")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_countrypr_lowcase_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Ukraine").type("kharkiv")
    setup_en.get_by_placeholder("Kyiv").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")

