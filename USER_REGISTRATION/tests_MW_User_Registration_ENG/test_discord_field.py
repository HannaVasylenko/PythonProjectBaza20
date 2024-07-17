import re
from playwright.sync_api import Page, expect


def test_discordpr_empty_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").click()
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter your Discord username") #Enter a nickname in Discord Enter your Discord username Enter your Discord username
    page.screenshot(path="discordpren_screenshots/discordempty.png")


def test_discordpr_space_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type(" ")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter your Discord username") #Enter a nickname in Discord Enter your Discord username Enter your Discord username
    page.screenshot(path="discordpren_screenshots/discordspace.png")


def test_discordpr_сyrillic_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("привіт")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username") # Enter a valid Discord username Enter a valid Discord username
    page.screenshot(path="discordpren_screenshots/discordсyrillic.png")


def test_discordpr_latin_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("pryvit")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordpren_screenshots/discordlatin.png")


def test_discordpr_spacein_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("test test")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username") #Enter a nickname in Discord Enter your Discord username Enter your Discord username
    page.screenshot(path="discordpren_screenshots/discordspacein.png")


def test_discordpr_1char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("a")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error mes >2char")
    page.screenshot(path="discordpren_screenshots/discord2char.png")


def test_discordpr_2char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("au")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordpren_screenshots/discord2char.png")


def test_discordpr_3char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("duo")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordpren_screenshots/discord3char.png")


def test_discordpr_17char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("meredithmarjoryao")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordpren_screenshots/discord17char.png")


def test_discordpr_31char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgs")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordpren_screenshots/discord31char.png")


def test_discordpr_32char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgsa")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordpren_screenshots/discord32char.png")


def test_discordpr_33char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgsak")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error mes <32char")
    page.screenshot(path="discordpren_screenshots/discord33char.png")


def test_discordpr_50char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error mes <32char")
    page.screenshot(path="discordpren_screenshots/discord50char.png")


def test_discordpr_up_case_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("NICK")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    page.screenshot(path="discordpren_screenshots/discordupcase.png")


def test_discordpr_numbers_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("test9876541230")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordpren_screenshots/discordnumbers.png")


def test_discordpr_underline_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("t_anya_qa_manual")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordpren_screenshots/discordunderline.png")


def test_discordpr_point_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("t.anya.qa.manu.al")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordpren_screenshots/discordpoint.png")


def test_discordpr_begin_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("тanya")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    page.screenshot(path="discordpren_screenshots/discordbegin.png")


def test_discordpr_symbols_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.locator("//input[@id='discord']").type("vi@ck!the?be%st")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    page.screenshot(path="discordpren_screenshots/discordsymbols.png")
    