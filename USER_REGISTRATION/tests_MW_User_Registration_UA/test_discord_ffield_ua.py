import re
from playwright.sync_api import Page, expect


def test_discordpr_empty_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").click()
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть ім'я користувача в Discord")  # Enter a nickname in Discord Введіть ім'я користувача в Discord Введіть ім'я користувача в Discord


def test_discordpr_space_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type(" ")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть ім'я користувача в Discord")  # Введіть коректне ім'я користувача в Discord Введіть коректне ім'я користувача в Discord


def test_discordpr_сyrillic_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("привіт")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")  # Введіть коректне ім'я користувача в Discord Введіть коректне ім'я користувача в Discord


def test_discordpr_latin_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("pryvit")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_spacein_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("qa manual")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")  # Введіть коректне ім'я користувача в Discord Введіть коректне ім'я користувача в Discord


def test_discordpr_1char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("a")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    expect(setup.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error mes >2char")


def test_discordpr_2char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("au")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_3char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("duo")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_17char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("meredithmarjoryao")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_31char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgs")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_32char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgsa")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_33char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgsak")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    expect(setup.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error mes <32char")


def test_discordpr_50char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    expect(setup.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error mes <32char")


def test_discordpr_up_case_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("NICK")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")


def test_discordpr_numbers_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("test9876541230")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_underline_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("t_anya_qa_manual")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_point_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("t.anya.qa.manu.al")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_discordpr_begin_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("тatya")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")


def test_discordpr_symbols_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("vi@ck!the?be%st")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
