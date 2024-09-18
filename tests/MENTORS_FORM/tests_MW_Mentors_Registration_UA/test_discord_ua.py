from playwright.sync_api import Page, expect


def test_discord_empty_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").click()
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Введіть ім'я користувача в Discord")


def test_discord_space_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type(" ")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Введіть ім'я користувача в Discord")


def test_discord_cyrillic_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("привіт")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")


def test_discord_latin_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("pryvit")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_1char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("a")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")


def test_discord_2char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("au")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_3char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("oon")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_17char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("meredithmarjoryao")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_31char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgs")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_32char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgsa")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_33char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgsak")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")


def test_discord_50char_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")


def test_discord_up_case_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("TESTING")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")


def test_discord_low_case_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("testing")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_numb_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("anya9876541230")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_underline_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("t_es_tpro_gram")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_point_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("t.es.tpro.gram")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_discord_start_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("їyahoo")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")


def test_discord_symb_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("v,i@ck!the?best")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")


def test_discord_space_in_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_placeholder("Iм'я користувача в Discord").type("testing test")
    setup.get_by_placeholder("Лінк на профіль").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='discord']/following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")

