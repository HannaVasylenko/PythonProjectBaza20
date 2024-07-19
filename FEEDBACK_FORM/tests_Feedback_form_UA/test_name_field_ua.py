import re
import pytest
from playwright.sync_api import Page, expect


def test_name_empty_field_ua(page: Page) -> None:
    #page.goto("/")
    #page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").click()
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть ім’я")
    page.screenshot(path="name_ffua_scr/nameemptyf.png")


def test_name_space_field_ua(page: Page, setup) -> None:
    #page.goto("/")
    #page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type(" ")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть ім’я")
    #page.screenshot(path="name_ffua_scr/namespacef.png")


def test_name_1char_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("ї")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно мати не менше 2 знаків")
    page.screenshot(path="name_ffua_scr/name1charf.png")


def test_name_2char_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("їє")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffua_scr/name2charf.png")


def test_name_3char_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("їєа")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffua_scr/name2charf.png")


def test_name_15char_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("Шухевич Роман О")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffua_scr/name15charf.png")


def test_name_29char_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("Степан Андрійович Бандера ОУН")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffua_scr/name29charf.png")


def test_name_30char_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("степан андрійович бандераоун-б")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffua_scr/name30charf.png")


def test_name_31char_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("Степан Андрійович Бандера ОУН-Б")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно бути не більше 30 знаків")
    page.screenshot(path="name_ffua_scr/name31charf.png")


def test_name_50char_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("Степан Бандера Коновалець Євген Шухевич Романдіячі")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    #expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    #expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно бути не більше 30 знаків")
    page.screenshot(path="name_ffua_scr/name50charf.png")


def test_name_51char_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("Степан Бандера Коновалець Євген Шухевич Романдіячію")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Ім’я повинно бути не більше 50 знаків")
    page.screenshot(path="name_ffua_scr/name51charf.png")


def test_name_apostrophe_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("С'тепан'Андрійович'Бандера")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffua_scr/nameapostrophef.png")


def test_name_hyphen_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("С-тепан-Андрійович-Бандера")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffua_scr/namehyphenf.png")


def test_name_lowcase_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("тестування")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffua_scr/namelowcasef.png")


def test_name_upcase_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("ТЕСТУВАННЯ")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffua_scr/nameupcasef.png")


def test_name_num_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("СтепанБандера1234567890")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_ffua_scr/namenumf.png")


def test_name_symb_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("С.теп@н,Бандер*а!")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_ffua_scr/namesymbf.png")


def test_name_html_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("Тест&nbsp")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_ffua_scr/namehtmlf.png")


def test_name_latin_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").type("Stepan Andriyovych Bandera")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffua_scr/namelatinf.png")


@pytest.mark.parametrize("test_input", [
    ("Пръерплрт"),
    ("Орамыьтор"),
    ("апмЭтиор"),
    ("потлоЁьтбоа"),
    ("Тиитрэтьтор"),
    ("Иимпаётир")
])
def test_name_piletters_field_ua(page: Page, test_input) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ім’я").press("Control+A")
    page.get_by_placeholder("Ім’я").press("Delete")
    page.get_by_placeholder("Ім’я").type(test_input)
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")


@pytest.mark.skip(reason="Rewrote the test using “@pytest.mark.parametrize”")
def test_name_piletterspr_field_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()

    page.get_by_placeholder("Ім’я").press("Control+A")
    page.get_by_placeholder("Ім’я").press("Delete")
    page.get_by_placeholder("Ім’я").type("Пръерплрт")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_ffua_scr/name1pilettersf.png")

    page.get_by_placeholder("Ім’я").press("Control+A")
    page.get_by_placeholder("Ім’я").press("Delete")
    page.get_by_placeholder("Ім’я").type("Орамыьтор")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_ffua_scr/name2pilettersf.png")

    page.get_by_placeholder("Ім’я").press("Control+A")
    page.get_by_placeholder("Ім’я").press("Delete")
    page.get_by_placeholder("Ім’я").type("апмЭтиор")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_ffua_scr/name3pilettersf.png")

    page.get_by_placeholder("Ім’я").press("Control+A")
    page.get_by_placeholder("Ім’я").press("Delete")
    page.get_by_placeholder("Ім’я").type("потлоЁьтбоа")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_ffua_scr/name4pilettersf.png")

    page.get_by_placeholder("Ім’я").press("Control+A")
    page.get_by_placeholder("Ім’я").press("Delete")
    page.get_by_placeholder("Ім’я").type("Тиитрэтьтор")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_ffua_scr/name5pilettersf.png")

    page.get_by_placeholder("Ім’я").press("Control+A")
    page.get_by_placeholder("Ім’я").press("Delete")
    page.get_by_placeholder("Ім’я").type("Иимпаётир")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Введіть коректне ім’я")
    page.screenshot(path="name_ffua_scr/name6pilettersf.png")


