from playwright.sync_api import Page, expect


def test_phone_empty_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Wprowadź numer telefonu")


def test_phone_with_begin_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phone_valid_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_phone_enter_numb_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("123456789")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_phone_1char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("1")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phone_2char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("12")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phone_6char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("12")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phone_12char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("12345678")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phone_13char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_phone_14char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("9999999999")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phone_20char_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("9999999999123456")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phone_cyrillic_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phone_latin_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phone_polski_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("Świętosław")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phone_symb_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("*@!?.#:;")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")


def test_phone_without_begin_mentor_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("button", name="Zostać mentorem").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").type("1234567890123")
    setup_pl.locator("//input[@id='discord']").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_pl.locator("//label[@for='phone']/following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")

