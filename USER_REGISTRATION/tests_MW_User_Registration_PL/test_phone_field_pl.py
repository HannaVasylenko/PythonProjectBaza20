import re
from playwright.sync_api import Page, expect


def test_phonepr_valid_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phoneprpl_screenshots/phonevalid.png")


def test_phonepr_empty_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Wprowadź numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phoneemptyfield.png")


def test_phonepr_space_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type(" ")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Wprowadź numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phoneemptyfield.png")


def test_phonepr_enter_digits_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("123456789")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phoneprpl_screenshots/phoneenterdigits.png")


def test_phonepr_enter_value_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_value("+380")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phoneentervalue.png")


def test_phonepr_1char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("1")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phone1char.png")


def test_phonepr_2char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("12")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phone2char.png")


def test_phonepr_6char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("12")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phone6char.png")


def test_phonepr_12char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("99999999")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phone12char.png")


def test_phonepr_13char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phoneprpl_screenshots/phone13char.png")


def test_phonepr_14char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("9999999999")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phone14char.png")


def test_phonepr_20char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("9999999999999999")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phone20char.png")


def test_phonepr_сyrillic_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phoneсyrillic.png")


def test_phonepr_onlyсyrillic_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phoneonlyсyrillic.png")


def test_phonepr_latin_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phonelatin.png")


def test_phonepr_onlylatin_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phoneonlylatin.png")


def test_phonepr_polski_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("Świętosław")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phonepolski.png")


def test_phonepr_onlypolski_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("Świętosław")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phoneonlypolski.png")


def test_phonepr_without_start_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("1234567891230")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phonewithoutstart.png")


def test_phonepr_onlysymbols_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("*@#!?.#:;=+()")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phoneonlysymbols.png")
    
    
def test_phonepr_symbols_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("*@!?.#:;")
    page.get_by_placeholder("Kijów").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Proszę wpisać poprawny numer telefonu")
    page.screenshot(path="phoneprpl_screenshots/phonesymbols.png")