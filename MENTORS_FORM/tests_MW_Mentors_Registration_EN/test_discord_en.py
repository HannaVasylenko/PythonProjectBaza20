import re
from playwright.sync_api import Page, expect


def test_discord_empty_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").click()
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter your Discord username")
    page.screenshot(path="discord_mentoren_scr/discordempty.png")


def test_discord_space_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type(" ")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter your Discord username")
    page.screenshot(path="discord_mentoren_scr/discordspace.png")


def test_discord_сyrillic_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("привіт")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    page.screenshot(path="discord_mentoren_scr/discordсyrillic.png")


def test_discord_latin_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("pryvit")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentoren_scr/discordlatin.png")


def test_discord_1char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("a")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #min char
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    page.screenshot(path="discord_mentoren_scr/discord1char.png")


def test_discord_2char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("au")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentoren_scr/discord2char.png")


def test_discord_3char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("oon")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentoren_scr/discord3char.png")


def test_discord_17char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("meredithmarjoryao")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentoren_scr/discord17char.png")


def test_discord_31char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgs")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentoren_scr/discord31char.png")


def test_discord_32char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgsa")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentoren_scr/discord32char.png")


def test_discord_33char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgsak")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    page.screenshot(path="discord_mentoren_scr/discord33char.png")


def test_discord_50char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    page.screenshot(path="discord_mentoren_scr/discord50char.png")


def test_discord_up_case_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("TESTING")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    page.screenshot(path="discord_mentoren_scr/discordupcase.png")


def test_discord_lowcase_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("testing")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentoren_scr/discordlowcase.png")


def test_discord_spacein_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("testing test")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    page.screenshot(path="discord_mentoren_scr/discordspacein.png")


def test_discord_num_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("test9876541230")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentoren_scr/discordnum.png")


def test_discord_underline_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("t_est_design_techniques")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentoren_scr/discordunderline.png")


def test_discord_point_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("t.est.design.techniques")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="discord_mentoren_scr/discordpoint.png")


def test_discord_start_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("їyahoo")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    page.screenshot(path="discord_mentoren_scr/discordstart.png")


def test_discord_symb_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("v,i@ck!the?best")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #max char
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    page.screenshot(path="discord_mentoren_scr/discordsymb.png")


def test_discord_space_in_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.locator("//input[@id='discord']").type("test design")
    page.get_by_placeholder("Link to profile").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='discord']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='discord']/../following-sibling::p")).to_have_text("Enter a valid Discord username")
    page.screenshot(path="discord_mentoren_scr/discordspacein.png")

