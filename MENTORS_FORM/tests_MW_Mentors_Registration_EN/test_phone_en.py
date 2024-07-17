import re
from playwright.sync_api import Page, expect


def test_phone_empty_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Enter a phone number")
    page.screenshot(path="phone_mentoren_scr/phoneempty.png")


def test_phone_with_begin_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phone_mentoren_scr/phonewithbegin.png")


def test_phone_valid_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phone_mentoren_scr/phonevalid.png")


def test_phone_enter_num_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("123456789")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phone_mentoren_scr/phoneenternum.png")


def test_phone_1char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("1")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phone_mentoren_scr/phone1char.png")


def test_phone_2char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("12")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phone_mentoren_scr/phone2char.png")


def test_phone_6char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("12")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phone_mentoren_scr/phone6char.png")


def test_phone_12char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("12345678")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phone_mentoren_scr/phone12char.png")


def test_phone_13char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("999999999")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="phone_mentoren_scr/phone13char.png")


def test_phone_14char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("9999999999")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phone_mentoren_scr/phone14char.png")


def test_phone_20char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("9999999999123456")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phone_mentoren_scr/phone20char.png")


def test_phone_сyrillic_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("привіт")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phone_mentoren_scr/phoneсyrillic.png")


def test_phone_latin_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("pryvit")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phone_mentoren_scr/phonelatin.png")


def test_phone_symb_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").type("*@!?.#:;")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phone_mentoren_scr/phonesymb.png")


def test_phone_without_begin_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("+380 xx xxx xx xx").press("Control+A")
    page.get_by_placeholder("+380 xx xxx xx xx").press("Delete")
    page.get_by_placeholder("+380 xx xxx xx xx").type("1234567890123")
    page.locator("//input[@id='discord']").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='phone']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='phone']/../following-sibling::p")).to_have_text("Please enter a valid phone number")
    page.screenshot(path="phone_mentoren_scr/phonewithoutbegin.png")

