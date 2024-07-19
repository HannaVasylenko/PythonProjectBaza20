import re
import pytest
from playwright.sync_api import Page, expect


def test_citypr_space_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type(" ")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("error mes") #no error mes
    page.screenshot(path="cityprua_screenshots/cityspacepr.png")


def test_citypr_empty_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").click()
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprua_screenshots/citympty.png")


def test_citypr_1char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("х")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Введіть коректну назву міста")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text(">2char")#error mes
    page.screenshot(path="cityprua_screenshots/city1char.png")


def test_citypr_2char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("ха")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprua_screenshots/city2char.png")


def test_citypr_3char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("хар")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprua_screenshots/city3char.png")


def test_citypr_15char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("ХарківЛьвівСуми")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprua_screenshots/city15char.png")


def test_citypr_29char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("ХарківЛьвівСумиЧернігівЯворів")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprua_screenshots/city29char.png")


def test_citypr_30char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("ХарківЛьвівСумиЧернігівЯворівю")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprua_screenshots/city30char.png")


def test_citypr_31char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("ХарківЛьвівСумиЧернігівЯворівюа")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Назва міста повинна бути не більше 30 знаків")
    page.screenshot(path="cityprua_screenshots/city31char.png")


def test_citypr_50char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("ХарківЛьвівСумиЧернігівЯворівШепетівкаЧорнобильРим")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Назва міста повинна бути не більше 30 знаків")
    page.screenshot(path="cityprua_screenshots/city50char.png")


def test_citypr_numbers_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("0123456789")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Введіть коректну назву міста")
    page.screenshot(path="cityprua_screenshots/citynumbers.png")


def test_citypr_hyphen_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("Х-арків-Львів-Суми")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprua_screenshots/cityhyphen.png")


def test_citypr_apostrophe_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("Х'арків'Львів'Суми")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprua_screenshots/cityapostrophe.png")


def test_citypr_space_in_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("Харків Львів Суми")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprua_screenshots/cityspacein.png")


def test_citypr_symbols_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("Х,ар.кі!вЛ?ьв@ів")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Введіть коректну назву міста")
    page.screenshot(path="cityprua_screenshots/citysymbols.png")


def test_citypr_latin_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("Kharkiv")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprua_screenshots/citylatin.png")


def test_citypr_up_case_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("ХАРКІВ")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprua_screenshots/cityupcase.png")


def test_citypr_low_case_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").type("харків")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="cityprua_screenshots/citylowcase.png")


@pytest.mark.parametrize("test_input", [
    ("Пръерплрт"),
    ("Орамыьтор"),
    ("апмЭтиор"),
    ("потлоЁьтбоа"),
    ("Тиитрэтьтор"),
    ("Иимпаётир")
])
def test_piletterspr_ua(page: Page, test_input) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").press("Control+A")
    page.get_by_placeholder("Київ").press("Delete")
    page.get_by_placeholder("Київ").type(test_input)
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Введіть коректну назву міста")


@pytest.mark.skip(reason="Rewrote the test using “@pytest.mark.parametrize”")
def test_piletterspr1_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Київ").press("Control+A")
    page.get_by_placeholder("Київ").press("Delete")
    page.get_by_placeholder("Київ").type("Пръерплрт")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Введіть коректну назву міста")
    page.screenshot(path="cityprua_screenshots/city1piletters.png")

    page.get_by_placeholder("Київ").press("Control+A")
    page.get_by_placeholder("Київ").press("Delete")
    page.get_by_placeholder("Київ").type("Орамыьтор")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Введіть коректну назву міста")
    page.screenshot(path="cityprua_screenshots/city1piletters.png")

    page.get_by_placeholder("Київ").press("Control+A")
    page.get_by_placeholder("Київ").press("Delete")
    page.get_by_placeholder("Київ").type("апмЭтиор")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Введіть коректну назву міста")
    page.screenshot(path="cityprua_screenshots/city3piletters.png")

    page.get_by_placeholder("Київ").press("Control+A")
    page.get_by_placeholder("Київ").press("Delete")
    page.get_by_placeholder("Київ").type("потлоЁьтбоа")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Введіть коректну назву міста")
    page.screenshot(path="cityprua_screenshots/city4piletters.png")

    page.get_by_placeholder("Київ").press("Control+A")
    page.get_by_placeholder("Київ").press("Delete")
    page.get_by_placeholder("Київ").type("Тиитрэтьтор")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Введіть коректну назву міста")
    page.screenshot(path="cityprua_screenshots/city5piletters.png")

    page.get_by_placeholder("Київ").press("Control+A")
    page.get_by_placeholder("Київ").press("Delete")
    page.get_by_placeholder("Київ").type("Иимпаётир")
    page.get_by_placeholder("Україна").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Введіть коректну назву міста")
    page.screenshot(path="cityprua_screenshots/city6piletters.png")