import re
from playwright.sync_api import Page, expect


def test_message_empty_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").click()
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Enter a message")
    page.screenshot(path="message_ffen_scr/messageemptyf.png")


def test_message_space_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type(" ")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Enter a message")
    page.screenshot(path="message_ffen_scr/messagespacef.png")


def test_message_1char_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type("a")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("The message must have at least 10 characters")
    page.screenshot(path="message_ffen_scr/message1charf.png")


def test_message_2char_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type("au")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("The message must have at least 10 characters")
    page.screenshot(path="message_ffen_scr/message2charf.png")


def test_message_5char_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type("tests")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("The message must have at least 10 characters")
    page.screenshot(path="message_ffen_scr/message5charf.png")


def test_message_9char_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type("technique")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("The message must have at least 10 characters")
    page.screenshot(path="message_ffen_scr/message9charf.png")


def test_message_10char_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type("techniques")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffen_scr/message10charf.png")


def test_message_11char_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type("techniquese")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffen_scr/message11charf.png")


def test_message_150char_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type("ChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuioh")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffen_scr/message150charf.png")


def test_message_299char_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type("ChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuio")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffen_scr/message299charf.png")


def test_message_300char_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type("ChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuioW")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffen_scr/message300charf.png")


def test_message_301char_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type("ChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuiohChecktheplacementofthePartnersblockafterqwertyuioWE")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Please limit your message to 300 characters")
    page.screenshot(path="message_ffen_scr/message301charf.png")


def test_message_upcase_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type("TESTINGTESTTEST")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffen_scr/messageupcasef.png")


def test_message_lowcase_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type("testingtesttest")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffen_scr/messagelowcasef.png")


def test_message_symb_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type("Test design techniques !-_().,<>&?@$=+{}#*/[]\|?%^:;`₴’’””<>&?@$=+*\[/]?%;:")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffen_scr/messagesymbf.png")


def test_message_num_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Your message").type("Test design techniques 1234567890")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffen_scr/messagenumf.png")