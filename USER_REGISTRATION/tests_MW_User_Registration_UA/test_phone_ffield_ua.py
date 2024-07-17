import re
from playwright.sync_api import Page, expect


def test_phonepr_valid_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phoneprua_screenshots/phonevalid.png")


def test_phonepr_empty_field_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть номер телефону")
    page.screenshot(path="phoneprua_screenshots/phoneemptyfield.png")


def test_phonepr_space_field_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type(" ")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть номер телефону")
    page.screenshot(path="phoneprua_screenshots/phonespacefield.png")


def test_phonepr_enter_digits_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("123456789")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phoneprua_screenshots/phoneenterdigits.png")


def test_phonepr_enter_value_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
    page.screenshot(path="phoneprua_screenshots/phoneentervalue.png")


def test_phonepr_1char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("1")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
    page.screenshot(path="phoneprua_screenshots/phone1char.png")


def test_phonepr_2char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("12")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
    page.screenshot(path="phoneprua_screenshots/phone2char.png")


def test_phonepr_6char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("12")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
    page.screenshot(path="phoneprua_screenshots/phone6char.png")


def test_phonepr_12char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("99999999")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
    page.screenshot(path="phoneprua_screenshots/phone12char.png")


def test_phonepr_13char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phoneprua_screenshots/phone13char.png")


def test_phonepr_14char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("9999999999")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
    page.screenshot(path="phoneprua_screenshots/phone14char.png")


def test_phonepr_20char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("9999999999999999")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
    page.screenshot(path="phoneprua_screenshots/phone20char.png")


def test_phonepr_сyrillic_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
    page.screenshot(path="phoneprua_screenshots/phoneсyrillic.png")


def test_phonepr_onlyсyrillic_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
    page.screenshot(path="phoneprua_screenshots/phoneonlyсyrillic.png")


def test_phonepr_latin_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
    page.screenshot(path="phoneprua_screenshots/phonelatin.png")


def test_phonepr_onlylatin_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
    page.screenshot(path="phoneprua_screenshots/phoneonlylatin.png")


def test_phonepr_without_start_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("1234567891230")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
    page.screenshot(path="phoneprua_screenshots/phonewithoutstart.png")


def test_phonepr_onlysymbols_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("*@#!?.#:;=+()")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
    page.screenshot(path="phoneprua_screenshots/phoneonlysymbols.png")


def test_phonepr_symbols_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("*@!?.#:;")
    page.get_by_placeholder("Київ").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Введіть дійсний номер телефону")
    page.screenshot(path="phoneprua_screenshots/phonesymbols.png")