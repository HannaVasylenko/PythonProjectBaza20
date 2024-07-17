import re
from playwright.sync_api import Page, expect


def test_citypr_space_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type(" ")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Enter the correct city name") #no error mes
    page.screenshot(path="citypren_screenshots/cityspace.png")


def test_citypr_empty_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").click()
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="citypren_screenshots/cityempty.png")


def test_citypr_1char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("k")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Enter the correct city name")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("error mes >2char") #error mes
    page.screenshot(path="citypren_screenshots/city1char.png")


def test_citypr_2char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("kh")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="citypren_screenshots/city2char.png")


def test_citypr_3char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("kha")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="citypren_screenshots/city3char.png")


def test_citypr_15char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("KharkivLvivSumy")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="citypren_screenshots/city15char.png")


def test_citypr_29char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("qwertyuiopasdfghjklqqawsedrft")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="citypren_screenshots/city29char.png")


def test_citypr_30char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("qwertyuiopasdfghjklqqawsedrftq")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="citypren_screenshots/city30char.png")


def test_citypr_31char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("qwertyuiopasdfghjklqqawsedrftqs")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("The name of the city should not exceed 30 characters")
    page.screenshot(path="citypren_screenshots/city31char.png")


def test_citypr_50char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("The name of the city should not exceed 30 characters")
    page.screenshot(path="citypren_screenshots/city50char.png")


def test_citypr_numbers_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("0123456789")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Enter the correct city name")
    page.screenshot(path="citypren_screenshots/citynumbers.png")


def test_citypr_hyphen_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("K-harkiv-Lviv-Sumy")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="citypren_screenshots/cityhyphen.png")


def test_citypr_apostrophe_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("K'harkiv'Lviv'Sumy")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="citypren_screenshots/cityapostrophe.png")


def test_citypr_space_in_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("Kharkiv Lviv Sumy")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="citypren_screenshots/cityspacein.png")


def test_citypr_symbols_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("K.h@rk!vLv#v?umy")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Enter the correct city name")
    page.screenshot(path="citypren_screenshots/citysymbols.png")


def test_citypr_сyrillic_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("Харків")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="citypren_screenshots/cityсyrillic.png")


def test_citypr_up_case_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("KHARKIV")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="citypren_screenshots/cityupcase.png")


def test_citypr_low_case_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").type("kharkiv")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="citypren_screenshots/citylowcase.png")
    
    
def test_citypr_piletters_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Kyiv").press("Control+A")
    page.get_by_placeholder("Kyiv").press("Delete")
    page.get_by_placeholder("Kyiv").type("Пръерплрт")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Enter the correct city name")
    page.screenshot(path="citypren_screenshots/city1piletters.png")

    page.get_by_placeholder("Kyiv").press("Control+A")
    page.get_by_placeholder("Kyiv").press("Delete")
    page.get_by_placeholder("Kyiv").type("Орамыьтор")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Enter the correct city name")
    page.screenshot(path="citypren_screenshots/city2piletters.png")

    page.get_by_placeholder("Kyiv").press("Control+A")
    page.get_by_placeholder("Kyiv").press("Delete")
    page.get_by_placeholder("Kyiv").type("апмЭтиор")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Enter the correct city name")
    page.screenshot(path="citypren_screenshots/city3piletters.png")

    page.get_by_placeholder("Kyiv").press("Control+A")
    page.get_by_placeholder("Kyiv").press("Delete")
    page.get_by_placeholder("Kyiv").type("потлоЁьтбоа")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Enter the correct city name")
    page.screenshot(path="citypren_screenshots/city4piletters.png")

    page.get_by_placeholder("Kyiv").press("Control+A")
    page.get_by_placeholder("Kyiv").press("Delete")
    page.get_by_placeholder("Kyiv").type("Тиитрэтьтор")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Enter the correct city name")
    page.screenshot(path="citypren_screenshots/city5piletters.png")

    page.get_by_placeholder("Kyiv").press("Control+A")
    page.get_by_placeholder("Kyiv").press("Delete")
    page.get_by_placeholder("Kyiv").type("Иимпаётир")
    page.get_by_placeholder("Ukraine").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='city']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='city']/../following-sibling::p")).to_have_text("Enter the correct city name")
    page.screenshot(path="citypren_screenshots/city6piletters.png")