import re
from playwright.sync_api import Page, expect


def test_country_space(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type(" ")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Enter the correct country name") #no error mes
    page.screenshot(path="country_screenshots/countryspace.png")


def test_countrypr_empty_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").click()
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countrypren_screenshots/countryempty.png")


def test_country_1char(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("u")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Enter the correct country name") #incorrect error mes
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char") #incorrect error mes
    page.screenshot(path="country_screenshots/country1char.png")


def test_country_2char(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("uk")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Enter the correct country name") #incorrect error mes
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char") #incorrect error mes
    page.screenshot(path="country_screenshots/country2char.png")


def test_country_3char(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("ukr")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Enter the correct country name") #incorrect error mes
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("error mes >4char") #incorrect error mes
    page.screenshot(path="country_screenshots/country3char.png")


def test_country_4char(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("ukra")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="country_screenshots/country4char.png")


def test_country_5char(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("ukrai")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="country_screenshots/country5char.png")


def test_country_15char(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("KharkivLvivSumy")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="country_screenshots/country15char.png")


def test_country_29char(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("qwertyuiopasdfghjklqqawsedrft")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="country_screenshots/country29char.png")


def test_country_30char(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("qwertyuiopasdfghjklqqawsedrftq")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="country_screenshots/country30char.png")


def test_country_31char(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("qwertyuiopasdfghjklqqawsedrftqa")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("The name of the country should not exceed 30 characters")
    page.screenshot(path="country_screenshots/country31char.png")


def test_country_50char(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("The name of the country should not exceed 30 characters")
    page.screenshot(path="country_screenshots/country50char.png")


def test_country_numbers(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("1234567890")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Enter the correct country name")
    page.screenshot(path="country_screenshots/countrynumbers.png")


def test_country_hyphen(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("K-harkiv-Lviv-Sumy")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="country_screenshots/countryhyphen.png")


def test_country_apostrophe(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("K'harkiv'Lviv'Sumy")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="country_screenshots/countryapostrophe.png")


def test_country_space_in(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("Kharkiv Lviv Sumy")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="country_screenshots/countryspacein.png")


def test_country_symbols(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("Kh@rk!vLv#v?umy")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='country']/../following-sibling::p")).to_have_text("Enter the correct country name")
    page.screenshot(path="country_screenshots/countrysymbols.png")


def test_country_сyrillic(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("Україна")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="country_screenshots/countryсyrillic.png")


def test_countrypr_upcase_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("KHARKIV")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countrypren_screenshots/countryupcase.png")


def test_countrypr_lowcase_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Ukraine").type("kharkiv")
    page.get_by_placeholder("Kyiv").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='country']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="countrypren_screenshots/countrylowcase.png")

