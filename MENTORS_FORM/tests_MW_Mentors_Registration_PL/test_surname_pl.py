import re
from playwright.sync_api import Page, expect


def test_surname_empty_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").click()
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Wpisz swoje nazwisko")
    page.screenshot(path="surname_mentorpl_scr/surnameempty.png")


def test_surname_space_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type(" ")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Wpisz swoje nazwisko")
    page.screenshot(path="surname_mentorpl_scr/surnamespace.png")


def test_surname_1char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("ę")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Nazwisko musi mieć co najmniej 2 znaki")
    page.screenshot(path="surname_mentorpl_scr/surname1char.png")


def test_surname_2char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("ęż")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorpl_scr/surname2char.png")


def test_surname_3char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("Łęż")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorpl_scr/surname3char.png")


def test_surname_25char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("ŚwiętosławRóżaWięcławBłaż")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorpl_scr/surname25char.png")


def test_surname_49char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("Świętosław Róża Więcław BłażejChwalibógBłażejŁuka")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorpl_scr/surname49char.png")


def test_surname_50char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("Świętosław Róża Więcław BłażejChwalibógBłażej Łuka")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorpl_scr/surname50char.png")


def test_surname_51char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("Świętosław Róża Więcław BłażejChwalibóg Błażej Łuka")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Nazwisko nie może przekraczać 50 znaków")
    page.screenshot(path="surname_mentorpl_scr/surname51char.png")


def test_surname_76char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszężŚwiętosławRóżaWięcławBłaże")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Nazwisko nie może przekraczać 50 znaków")
    page.screenshot(path="surname_mentorpl_scr/surname76char.png")


def test_surname_apostrophe_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("Ś'więtosław'Róża'Więcław")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorpl_scr/surnameapostrophe.png")


def test_surname_hyphen_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("Ś-więtosław-Róża-Więcław")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorpl_scr/surnamehyphen.png")


def test_surname_numb_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("Świętosław1234567890")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Wpisz poprawne nazwisko")
    page.screenshot(path="surname_mentorpl_scr/surnamenumb.png")


def test_surname_symbols_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("Ś_w,ię.to!sła@wRó?ża")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='lastName']/../following-sibling::p")).to_have_text("Wpisz poprawne nazwisko")
    page.screenshot(path="surname_mentorpl_scr/surnamesymbols.png")


def test_surname_сyrillic_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("Тестування")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorpl_scr/surnameсyrillic.png")


def test_surname_low_case_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("więtosław")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorpl_scr/surnamelcase.png")


def test_surname_upcase_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("ŚŁABCDE")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorpl_scr/surnameupcase.png")


def test_surname_space_in_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Nazwisko").type("więtosław więtosław więtosław")
    page.get_by_role("textbox", name="Imię", exact=True).click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='lastName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="surname_mentorpl_scr/surnamespacein.png")