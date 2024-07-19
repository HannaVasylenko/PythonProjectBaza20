import re
import pytest
from playwright.sync_api import Page, expect


def test_surname_empty_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").click()
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть своє прізвище")
    page.screenshot(path="surname_mentorua_scr/surnameempty.png")


def test_surname_space_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type(" ")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть своє прізвище")
    page.screenshot(path="surname_mentorua_scr/surnamespace.png")


def test_surname_1char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("ї")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Прізвище повинно мати не менше 2 знаків")
    page.screenshot(path="surname_mentorua_scr/surname1char.png")


def test_surname_2char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("їє")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorua_scr/surname2char.png")


def test_surname_3char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("їєа")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorua_scr/surname3char.png")


def test_surname_25char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("Степан Андрійович Бандера")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorua_scr/surname25char.png")


def test_surname_49char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("СтепанАндрійовичБандера КоновалецьЄвгенМихайлович")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorua_scr/surname49char.png")


def test_surname_50char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("Степан Бандера Коновалець Євген Шухевич Романдіячі")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorua_scr/surname50char.png")


def test_surname_51char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("Степан Бандера Коновалець Євген Шухевич Роман діячі")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Прізвище повинно бути не більше 50 знаків")
    page.screenshot(path="surname_mentorua_scr/surname51char.png")


def test_surname_76char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("Степан Андрійович Бандера Коновалець Євген Михайлович Шухевич Роман Осипович")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Прізвище повинно бути не більше 50 знаків")
    page.screenshot(path="surname_mentorua_scr/surname76char.png")


def test_surname_apostrophe_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("С'тепан'Андрійович'Бандера")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorua_scr/surnameapostrophe.png")


def test_surname_hyphen_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("С-тепан-Андрійович-Бандера")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorua_scr/surnamehyphen.png")


def test_surname_numb_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("СтепанБандера1234567890")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище")
    page.screenshot(path="surname_mentorua_scr/surnamenumb.png")


def test_surname_symbols_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("С.теп@н,Бандер*а!")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище")
    page.screenshot(path="surname_mentorua_scr/surnamesymbols.png")


def test_surname_latin_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("Stepan Andriyovych Bandera")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorua_scr/surnamelatin.png")


def test_low_case_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("тестування")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorua_scr/surnamelcase.png")


def test_upcase_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("ТЕСТУВАННЯ")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorua_scr/surnameupcase.png")


def test_space_in_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").type("тестування тестування тестування")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorua_scr/surnamespacein.png")


@pytest.mark.parametrize("test_input", [
    ("Пръерплрт"),
    ("Орамыьтор"),
    ("апмЭтиор"),
    ("потлоЁьтбоа"),
    ("Тиитрэтьтор"),
    ("Иимпаётир")
])
def test_surname_piletters_ua(page: Page, test_input) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").press("Control+A")
    page.get_by_placeholder("Прізвище").press("Delete")
    page.get_by_placeholder("Прізвище").type(test_input)
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище")


@pytest.mark.skip(reason="Rewrote the test using “@pytest.mark.parametrize”")
def test_surname_pilettersm_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Прізвище").press("Control+A")
    page.get_by_placeholder("Прізвище").press("Delete")
    page.get_by_placeholder("Прізвище").type("Пръерплрт")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище")
    page.screenshot(path="surname_mentorua_scr/surname1piletters.png")

    page.get_by_placeholder("Прізвище").press("Control+A")
    page.get_by_placeholder("Прізвище").press("Delete")
    page.get_by_placeholder("Прізвище").type("Орамыьтор")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище")
    page.screenshot(path="surname_mentorua_scr/surname2piletters.png")

    page.get_by_placeholder("Прізвище").press("Control+A")
    page.get_by_placeholder("Прізвище").press("Delete")
    page.get_by_placeholder("Прізвище").type("апмЭтиор")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище")
    page.screenshot(path="surname_mentorua_scr/surname3piletters.png")

    page.get_by_placeholder("Прізвище").press("Control+A")
    page.get_by_placeholder("Прізвище").press("Delete")
    page.get_by_placeholder("Прізвище").type("потлоЁьтбоа")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище")
    page.screenshot(path="surname_mentorua_scr/surname4piletters.png")

    page.get_by_placeholder("Прізвище").press("Control+A")
    page.get_by_placeholder("Прізвище").press("Delete")
    page.get_by_placeholder("Прізвище").type("Тиитрэтьтор")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище")
    page.screenshot(path="surname_mentorua_scr/surname5piletters.png")

    page.get_by_placeholder("Прізвище").press("Control+A")
    page.get_by_placeholder("Прізвище").press("Delete")
    page.get_by_placeholder("Прізвище").type("Иимпаётир")
    page.get_by_role("textbox", name="Ім’я", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Введіть коректне Прізвище")
    page.screenshot(path="surname_mentorua_scr/surname6piletters.png")