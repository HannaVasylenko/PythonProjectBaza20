import re
from playwright.sync_api import Page, expect


def test_discord_empty_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").click()
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть ім'я користувача в Discord")
    page.screenshot(path="discord_mentorua_scr/discordempty.png")


def test_discord_space_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type(" ")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть ім'я користувача в Discord")
    page.screenshot(path="discord_mentorua_scr/discordspace.png")


def test_discord_сyrillic_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("привіт")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    page.screenshot(path="discord_mentorua_scr/discordсyrillic.png")


def test_discord_latin_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("pryvit")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentorua_scr/discordlatin.png")


def test_discord_1char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("a")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #min char
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    page.screenshot(path="discord_mentorua_scr/discord1char.png")


def test_discord_2char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("au")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentorua_scr/discord2char.png")


def test_discord_3char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("oon")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentorua_scr/discord3char.png")


def test_discord_17char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("meredithmarjoryao")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentorua_scr/discord17char.png")


def test_discord_31char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgs")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentorua_scr/discord31char.png")


def test_discord_32char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgsa")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentorua_scr/discord32char.png")


def test_discord_33char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgsak")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    page.screenshot(path="discord_mentorua_scr/discord33char.png")


def test_discord_50char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    page.screenshot(path="discord_mentorua_scr/discord50char.png")


def test_discord_up_case_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("TESTING")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    page.screenshot(path="discord_mentorua_scr/discordupcase.png")


def test_discord_lowcase_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("testing")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentorua_scr/discordlowcase.png")


def test_discord_num_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("anya9876541230")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentorua_scr/discordnum.png")


def test_discord_underline_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("s_tepan_andriyovych_bandera")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentorua_scr/discordunderline.png")


def test_discord_point_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("s.tepan.andriyovych.bandera")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentorua_scr/discordpoint.png")


def test_discord_start_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("їyahoo")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    page.screenshot(path="discord_mentorua_scr/discordstart.png")


def test_discord_symb_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("v,i@ck!the?best")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    page.screenshot(path="discord_mentorua_scr/discordsymb.png")


def test_discord_spacein_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Iм'я користувача в Discord").type("testing test")
    page.get_by_placeholder("Лінк на профіль").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Введіть коректне ім'я користувача в Discord")
    page.screenshot(path="discord_mentorua_scr/discordspaceinb.png")

