import re
from playwright.sync_api import Page, expect


def test_message_empty_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").click()
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Введіть повідомлення")
    page.screenshot(path="message_ffua_scr/messageemptyf.png")


def test_message_space_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type(" ")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Введіть повідомлення")
    page.screenshot(path="message_ffua_scr/messagespacef.png")


def test_message_1char_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type("ї")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Повідомлення повинно мати не менше 10 знаків")
    page.screenshot(path="message_ffua_scr/message1charf.png")


def test_message_2char_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type("їє")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Повідомлення повинно мати не менше 10 знаків")
    page.screenshot(path="message_ffua_scr/message2charf.png")


def test_message_5char_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type("любов")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Повідомлення повинно мати не менше 10 знаків")
    page.screenshot(path="message_ffua_scr/message5charf.png")


def test_message_9char_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type("привітики")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Повідомлення повинно мати не менше 10 знаків")
    page.screenshot(path="message_ffua_scr/message9charf.png")


def test_message_10char_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type("привітусім")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffua_scr/message10charf.png")


def test_message_11char_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type("привіт усім")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffua_scr/message11charf.png")


def test_message_150char_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type("привітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривіт")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffua_scr/message150charf.png")


def test_message_299char_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type("привітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітприві")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffua_scr/message299charf.png")


def test_message_300char_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type("привітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривіт")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffua_scr/message300charf.png")


def test_message_301char_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type("привітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітпривітп")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Просимо скоротити ваше повідомлення до 300 знаків")
    page.screenshot(path="message_ffua_scr/message301charf.png")


def test_message_upcase_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type("УДОСКОНАЛЮЄМО НАВИЧКИ НА ПРАКТИЦІ")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffua_scr/messageupcasef.png")


def test_message_lowcase_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type("тестування продукту")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffua_scr/messagelowcasef.png")


def test_message_symb_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type("Символи !-_().,<>&?@$=+{}#*/[]\|?%^:;`₴’’””<>&?@$=+*\[/]?%;:")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffua_scr/messagesymbf.png")


def test_message_num_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Ваше повідомлення").type("Символи 1234567890")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffua_scr/messagenumf.png")


def test_message_piletters_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()

    page.get_by_placeholder("Ваше повідомлення").press("Control+A")
    page.get_by_placeholder("Ваше повідомлення").press("Delete")
    page.get_by_placeholder("Ваше повідомлення").type("Пръерплртфівапру")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Введіть коректне повідомлення")
    page.screenshot(path="message_ffua_scr/message1pilettersf.png")

    page.get_by_placeholder("Ваше повідомлення").press("Control+A")
    page.get_by_placeholder("Ваше повідомлення").press("Delete")
    page.get_by_placeholder("Ваше повідомлення").type("Орамыьторйцукен")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Введіть коректне повідомлення")
    page.screenshot(path="message_ffua_scr/message2pilettersf.png")

    page.get_by_placeholder("Ваше повідомлення").press("Control+A")
    page.get_by_placeholder("Ваше повідомлення").press("Delete")
    page.get_by_placeholder("Ваше повідомлення").type("апмЭтиорйцукенг")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Введіть коректне повідомлення")
    page.screenshot(path="message_ffua_scr/message3pilettersf.png")

    page.get_by_placeholder("Ваше повідомлення").press("Control+A")
    page.get_by_placeholder("Ваше повідомлення").press("Delete")
    page.get_by_placeholder("Ваше повідомлення").type("потлоЁьтбоайцукенг")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Введіть коректне повідомлення")
    page.screenshot(path="message_ffua_scr/message4pilettersf.png")

    page.get_by_placeholder("Ваше повідомлення").press("Control+A")
    page.get_by_placeholder("Ваше повідомлення").press("Delete")
    page.get_by_placeholder("Ваше повідомлення").type("Тиитрэтьторйцукенг")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Введіть коректне повідомлення")
    page.screenshot(path="message_ffua_scr/message5pilettersf.png")

    page.get_by_placeholder("Ваше повідомлення").press("Control+A")
    page.get_by_placeholder("Ваше повідомлення").press("Delete")
    page.get_by_placeholder("Ваше повідомлення").type("Иимпаётирйцукенг")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Введіть коректне повідомлення")
    page.screenshot(path="message_ffua_scr/message6pilettersf.png")