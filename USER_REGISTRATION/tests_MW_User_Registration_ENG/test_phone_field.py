import re
from playwright.sync_api import Page, expect


def test_phonepr_valid_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phonepren_screenshots/phonevalid.png")


def test_phonepr_empty_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Enter a phone number")
    page.screenshot(path="phonepren_screenshots/phoneemptyfield.png")


def test_phonepr_space_field_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type(" ")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Enter a phone number")
    page.screenshot(path="phonepren_screenshots/phonespacefield.png")


def test_phonepr_enter_digits_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("123456789")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phonepren_screenshots/phoneenterdigits.png")


def test_phonepr_enter_value_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_value("+380")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phonepren_screenshots/phoneentervalue.png")


def test_phonepr_1char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("1")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phonepren_screenshots/phone1char.png")


def test_phonepr_2char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("12")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phonepren_screenshots/phone2char.png")


def test_phonepr_6char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("12")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phonepren_screenshots/phone6char.png")


def test_phonepr_12char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("99999999")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phonepren_screenshots/phone12char.png")


def test_phonepr_13char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phonepren_screenshots/phone13char.png")


def test_phonepr_14char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("9999999999")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phonepren_screenshots/phone14char.png")


def test_phonepr_20char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("9999999999999999")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phonepren_screenshots/phone20char.png")


def test_phonepr_сyrillic_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phonepren_screenshots/phoneсyrillic.png")


def test_phonepr_onlyсyrillic_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phonepren_screenshots/phoneonlyсyrillic.png")


def test_phonepr_latin_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phonepren_screenshots/phonelatin.png")


def test_phonepr_onlylatin_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phonepren_screenshots/phoneonlylatin.png")


def test_phonepr_without_start_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("1234567891230")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phonepren_screenshots/phonewithoutstart.png")


def test_phonepr_onlysymbols_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("*@#!?.#:;=+()")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phonepren_screenshots/phoneonlysymbols.png")


def test_phonepr_symbols_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("*@!?.#:;")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phonepren_screenshots/phonesymbols.png")