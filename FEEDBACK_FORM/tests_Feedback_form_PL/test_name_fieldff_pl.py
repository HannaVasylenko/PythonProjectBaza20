import re
from playwright.sync_api import Page, expect


def test_name_empty_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").click()
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Wpisz imię")
    page.screenshot(path="name_ffpl_scr/nameemptyf.png")


def test_name_space_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type(" ")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Wpisz imię")
    page.screenshot(path="name_ffpl_scr/namespacef.png")


def test_name_1char_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("ę")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Nazwa musi mieć co najmniej 2 znaki")
    page.screenshot(path="name_ffpl_scr/name1charf.png")


def test_name_2char_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("ęŁ")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffpl_scr/name2charf.png")


def test_name_3char_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("śćę")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffpl_scr/name2charf.png")


def test_name_15char_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("Świętosław Róża")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffpl_scr/name15charf.png")


def test_name_29char_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("ŚwiętosławRóżaWięcławBłażejŁę")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffpl_scr/name29charf.png")


def test_name_30char_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("ęŚwiętosławRóżaWięcławBłażejŁę")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffpl_scr/name30charf.png")


def test_name_31char_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("ęŚwiętosławRóżaWięcławBłażejŁęł")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Nazwa nie może przekraczać 30 znaków")
    page.screenshot(path="name_ffpl_scr/name31charf.png")


def test_name_50char_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszęż")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Nazwa nie może przekraczać 30 znaków")
    page.screenshot(path="name_ffpl_scr/name50charf.png")


def test_name_apostrophe_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("Ś'więt'osław'Róża'Więcław")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffpl_scr/nameapostrophef.png")


def test_name_hyphen_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("Ś-więtosław-Róża-Więcław")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffpl_scr/namehyphenf.png")


def test_name_lowcase_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("swiętosławóżaięcław")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffpl_scr/namelowcasef.png")


def test_name_upcase_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("ŚŁABC")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffpl_scr/nameupcasef.png")


def test_name_num_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("1234567890Świętosław")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="name_ffpl_scr/namenumf.png")


def test_name_symb_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("Ś,w.ię!tos@ław?")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="name_ffpl_scr/namesymbf.png")


def test_name_html_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("Świętosław&nbsp")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='firstName']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="name_ffpl_scr/namehtmlf.png")


def test_name_сyrillic_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("Степан Андрійович Бандера")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffpl_scr/nameсyrillicf.png")


def test_name_latin_field_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("Imię").type("Stepan Andriyovych Bandera")
    page.get_by_placeholder("email@gmail.com").click()
    expect(page.locator("//input[@id='firstName']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="name_ffpl_scr/namelatinf.png")


