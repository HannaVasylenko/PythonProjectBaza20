import re
from playwright.sync_api import Page, expect


def test_discordpr_empty_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").click()
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть ім'я користувача в Discord")  # Enter a nickname in Discord Введіть ім'я користувача в Discord Введіть ім'я користувача в Discord
    page.screenshot(path="discordprua_screenshots/discordempty.png")


def test_discordpr_space_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type(" ")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть ім'я користувача в Discord")  # Введіть коректне ім'я користувача в Discord Введіть коректне ім'я користувача в Discord
    page.screenshot(path="discordprua_screenshots/discordspace.png")


def test_discordpr_сyrillic_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("привіт")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")  # Введіть коректне ім'я користувача в Discord Введіть коректне ім'я користувача в Discord
    page.screenshot(path="discordprua_screenshots/discordсyrillic.png")


def test_discordpr_latin_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("pryvit")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprua_screenshots/discordlatin.png")


def test_discordpr_spacein_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("qa manual")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")  # Введіть коректне ім'я користувача в Discord Введіть коректне ім'я користувача в Discord
    page.screenshot(path="discordprua_screenshots/discordspacein.png")


def test_discordpr_1char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("a")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error mes >2char")
    page.screenshot(path="discordprua_screenshots/discord2char.png")


def test_discordpr_2char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("au")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprua_screenshots/discord2char.png")


def test_discordpr_3char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("duo")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprua_screenshots/discord3char.png")


def test_discordpr_17char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("meredithmarjoryao")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprua_screenshots/discord17char.png")


def test_discordpr_31char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgs")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprua_screenshots/discord31char.png")


def test_discordpr_32char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgsa")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprua_screenshots/discord32char.png")


def test_discordpr_33char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgsak")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error mes <32char")
    page.screenshot(path="discordprua_screenshots/discord33char.png")


def test_discordpr_50char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("error mes <32char")
    page.screenshot(path="discordprua_screenshots/discord50char.png")


def test_discordpr_up_case_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("NICK")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    page.screenshot(path="discordprua_screenshots/discordupcase.png")


def test_discordpr_numbers_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("test9876541230")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprua_screenshots/discordnumbers.png")


def test_discordpr_underline_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("t_anya_qa_manual")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprua_screenshots/discordunderline.png")


def test_discordpr_point_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("t.anya.qa.manu.al")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discordprua_screenshots/discordpoint.png")


def test_discordpr_begin_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("тatya")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    page.screenshot(path="discordprua_screenshots/discordbegin.png")


def test_discordpr_symbols_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("vi@ck!the?be%st")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    page.screenshot(path="discordprua_screenshots/discordsymbols.png")
