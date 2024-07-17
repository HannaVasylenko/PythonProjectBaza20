import re
from playwright.sync_api import Page, expect


def test_discordpr_empty_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").click()
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wpisz swoją nazwę użytkownika Discord") #Wpisz pseudonim na Discordzie Wpisz swoją nazwę użytkownika Discord
    page.screenshot(path="discordprpl_screenshots/discordempty.png")


def test_discordpr_space_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type(" ")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wpisz swoją nazwę użytkownika Discord") #Wpisz pseudonim na Discordzie Wpisz swoją nazwę użytkownika Discord
    page.screenshot(path="discordprpl_screenshots/discordspace.png")


def test_discordpr_сyrillic_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("привіт")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord") #Wprowadź prawidłową nazwę użytkownika Discord
    page.screenshot(path="discordprpl_screenshots/discordсyrillic.png")


def test_discordpr_polski_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("ożenaózefwiętosław")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")
    page.screenshot(path="discordprpl_screenshots/discordсyrillic.png")


def test_discordpr_latin_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("pryvit")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprpl_screenshots/discordlatin.png")


def test_discordpr_spacein_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("test test")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord") #Wpisz pseudonim na Discordzie Wpisz swoją nazwę użytkownika Discord
    page.screenshot(path="discordprpl_screenshots/discordspacein.png")


def test_discordpr_1char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("a")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error min 2 char")#min char
    page.screenshot(path="discordprpl_screenshots/discord2char.png")


def test_discordpr_2char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("au")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprpl_screenshots/discord2char.png")


def test_discordpr_3char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("duo")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprpl_screenshots/discord3char.png")


def test_discordpr_17char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("meredithmarjoryao")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprpl_screenshots/discord17char.png")


def test_discordpr_31char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgs")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprpl_screenshots/discord31char.png")


def test_discordpr_32char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgsa")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprpl_screenshots/discord32char.png")


def test_discordpr_33char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgsak")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error max 32 char")
    page.screenshot(path="discordprpl_screenshots/discord33char.png")


def test_discordpr_50char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error max 32 char")
    page.screenshot(path="discordprpl_screenshots/discord50char.png")


def test_discordpr_up_case_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("NICK")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")
    page.screenshot(path="discordprpl_screenshots/discordupcase.png")


def test_discordpr_numbers_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("test9876541230")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprpl_screenshots/discordnumbers.png")


def test_discordpr_underline_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("t_anya_qa_manual")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprpl_screenshots/discordunderline.png")


def test_discordpr_point_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("t.anya.qa.manu.al")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprpl_screenshots/discordpoint.png")


def test_discordpr_begin_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("тanya")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")
    page.screenshot(path="discordprpl_screenshots/discordbegin.png")


def test_discordpr_symbols_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.locator("//input[@id='discord']").type("vi@ck!the?be%st")
    page.get_by_placeholder("Link do profilu").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Wprowadź prawidłową nazwę użytkownika Discord")
    page.screenshot(path="discordprpl_screenshots/discordsymbols.png")
