import re
from playwright.sync_api import Page, expect


def test_citypr_space_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type(" ")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Enter the correct city name") #no error mes


def test_citypr_empty_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").click()
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_1char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("k")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Enter the correct city name")
    expect(setup_en.locator("//label[@for='city']/../following-sibling::p")).to_have_text("error mes >2char") #error mes


def test_citypr_2char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("kh")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_3char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("kha")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_15char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("KharkivLvivSumy")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_29char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("qwertyuiopasdfghjklqqawsedrft")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_30char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("qwertyuiopasdfghjklqqawsedrftq")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_31char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("qwertyuiopasdfghjklqqawsedrftqs")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='city']/../following-sibling::p")).to_have_text("The name of the city should not exceed 30 characters")


def test_citypr_50char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='city']/../following-sibling::p")).to_have_text("The name of the city should not exceed 30 characters")


def test_citypr_numbers_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("0123456789")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Enter the correct city name")


def test_citypr_hyphen_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("K-harkiv-Lviv-Sumy")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_apostrophe_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("K'harkiv'Lviv'Sumy")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_space_in_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("Kharkiv Lviv Sumy")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_symbols_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("K.h@rk!vLv#v?umy")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Enter the correct city name")


def test_citypr_сyrillic_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("Харків")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_up_case_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("KHARKIV")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_citypr_low_case_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("Kyiv").type("kharkiv")
    setup_en.get_by_placeholder("Ukraine").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")

