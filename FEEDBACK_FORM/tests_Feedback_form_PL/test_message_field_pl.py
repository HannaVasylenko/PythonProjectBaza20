import re
from playwright.sync_api import Page, expect


def test_message_empty_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").click()
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Wpisz wiadomość")
    page.screenshot(path="message_ffpl_scr/messageemptyf.png")


def test_message_space_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type(" ")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Wpisz wiadomość")
    page.screenshot(path="message_ffpl_scr/messagespacef.png")


def test_message_1char_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type("ę")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Wiadomość musi zawierać co najmniej 10 znaków")
    page.screenshot(path="message_ffpl_scr/message1charf.png")


def test_message_2char_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type("ęŁ")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Wiadomość musi zawierać co najmniej 10 znaków")
    page.screenshot(path="message_ffpl_scr/message2charf.png")


def test_message_5char_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type("ężŚwę")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Wiadomość musi zawierać co najmniej 10 znaków")
    page.screenshot(path="message_ffpl_scr/message5charf.png")


def test_message_9char_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type("ężŚwęŁóżż")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Wiadomość musi zawierać co najmniej 10 znaków")
    page.screenshot(path="message_ffpl_scr/message9charf.png")


def test_message_10char_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type("ężŚwęŁóżęż")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffpl_scr/message10charf.png")


def test_message_11char_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type("ężŚwęŁóżęża")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffpl_scr/message11charf.png")


def test_message_150char_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszęż")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffpl_scr/message150charf.png")


def test_message_299char_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszę")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffpl_scr/message299charf.png")


def test_message_300char_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszęż")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffpl_scr/message300charf.png")


def test_message_301char_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszęża")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='message']/../following-sibling::p")).to_have_text("Prosimy o ograniczenie wiadomości do 300 znaków")
    page.screenshot(path="message_ffpl_scr/message301charf.png")


def test_message_upcase_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type("ŚŁBTESTINGTEST")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffpl_scr/messageupcasef.png")


def test_message_lowcase_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type("więtosławasławukaszożena")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffpl_scr/messagelowcasef.png")


def test_message_symb_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type("Świętosław Lasław Łukasz !-_().,<>&?@$=+{}#*/[]\|?%^:;`₴’’””<>&?@$=+*\[/]?%;:")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffpl_scr/messagesymbf.png")


def test_message_num_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Twoja wiadomość").type("Świętosław Lasław Łukasz 0123456789")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//textarea[@id='message']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="message_ffen_scr/messagenumf.png")