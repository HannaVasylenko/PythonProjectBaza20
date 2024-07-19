import re
import pytest
from playwright.sync_api import Page, expect


def test_countrypr_space_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type(" ")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Введіть коректну назву країни") #no error mes
    page.screenshot(path="countryprua_screenshots/countryspace.png")
    
    
def test_countrypr_empty_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").click()
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprua_screenshots/country1char.png")


def test_countrypr_1char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("х")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Введіть коректну назву країни")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char") #incorrect error mes
    page.screenshot(path="countryprua_screenshots/country1char.png")


def test_countrypr_2char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("ха")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Введіть коректну назву країни")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char") #incorrect error mes
    page.screenshot(path="countryprua_screenshots/country2char.png")


def test_countrypr_3char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("хар")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Введіть коректну назву країни")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char") #incorrect error mes
    page.screenshot(path="countryprua_screenshots/country3char.png")


def test_countrypr_4char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("харк")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprua_screenshots/country4char.png")


def test_countrypr_5char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("харкі")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprua_screenshots/country5char.png")


def test_countrypr_15char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("ХарківЛьвівСуми")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprua_screenshots/country15char.png")


def test_countrypr_29char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("ХарківЛьвівСумиЧернігівЯворів")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprua_screenshots/country29char.png")


def test_countrypr_30char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("ХарківЛьвівСумиЧернігівЯворівю")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprua_screenshots/country30char.png")


def test_countrypr_31char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("ХарківЛьвівСумиЧернігівЯворівюа")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Назва країни повинна бути не більше 30 знаків")
    page.screenshot(path="countryprua_screenshots/country31char.png")


def test_countrypr_50char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("ХарківЛьвівСумиЧернігівЯворівШепетівкаЧорнобильРим")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Назва країни повинна бути не більше 30 знаків")
    page.screenshot(path="countryprua_screenshots/country50char.png")


def test_countrypr_numbers_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("1234567890")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Введіть коректну назву країни")
    page.screenshot(path="countryprua_screenshots/countrynumbers.png")


def test_countrypr_hyphen_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("Х-арків-Львів-Чернівці")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprua_screenshots/countryhyphen.png")


def test_countrypr_apostrophe_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("Х'арків'Львів'Чернівці")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprua_screenshots/countryapostrophe.png")


def test_countrypr_space_in_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("Харків Львів Суми")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprua_screenshots/countryspacein.png")


def test_countrypr_symbols_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("Х.а,рк!ів@Льв?ів")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Введіть коректну назву країни")
    page.screenshot(path="countryprua_screenshots/countrysymbols.png")


def test_countrypr_latin_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("Kharkiv")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprua_screenshots/countrylatin.png")


def test_countrypr_upcase_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("ХАРКІВЛЬВІВ")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprua_screenshots/countryupcase.png")


def test_countrypr_lowcase_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").type("харківльвів")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countryprua_screenshots/countrylowcase.png")


@pytest.mark.parametrize("test_input", [
    ("Пръерплрт"),
    ("Орамыьтор"),
    ("апмЭтиор"),
    ("потлоЁьтбоа"),
    ("Тиитрэтьтор"),
    ("Иимпаётир")
])
def test_countrypr_piletters_ua(page: Page, test_input) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").press("Control+A")
    page.get_by_placeholder("Україна").press("Delete")
    page.get_by_placeholder("Україна").type(test_input)
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Введіть коректну назву країни")


@pytest.mark.skip(reason="Rewrote the test using “@pytest.mark.parametrize”")
def test_countrypr_piletterspr_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Україна").press("Control+A")
    page.get_by_placeholder("Україна").press("Delete")
    page.get_by_placeholder("Україна").type("Пръерплрт")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Введіть коректну назву країни")
    page.screenshot(path="countryprua_screenshots/country1piletters.png")

    page.get_by_placeholder("Україна").press("Control+A")
    page.get_by_placeholder("Україна").press("Delete")
    page.get_by_placeholder("Україна").type("Орамыьтор")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Введіть коректну назву країни")
    page.screenshot(path="countryprua_screenshots/country2piletters.png")

    page.get_by_placeholder("Україна").press("Control+A")
    page.get_by_placeholder("Україна").press("Delete")
    page.get_by_placeholder("Україна").type("апмЭтиор")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Введіть коректну назву країни")
    page.screenshot(path="countryprua_screenshots/country3piletters.png")

    page.get_by_placeholder("Україна").press("Control+A")
    page.get_by_placeholder("Україна").press("Delete")
    page.get_by_placeholder("Україна").type("потлоЁьтбоа")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Введіть коректну назву країни")
    page.screenshot(path="countryprua_screenshots/countryp4iletters.png")

    page.get_by_placeholder("Україна").press("Control+A")
    page.get_by_placeholder("Україна").press("Delete")
    page.get_by_placeholder("Україна").type("Тиитрэтьтор")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Введіть коректну назву країни")
    page.screenshot(path="countryprua_screenshots/country5piletters.png")

    page.get_by_placeholder("Україна").press("Control+A")
    page.get_by_placeholder("Україна").press("Delete")
    page.get_by_placeholder("Україна").type("Иимпаётир")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Введіть коректну назву країни")
    page.screenshot(path="countryprua_screenshots/country6piletters.png")