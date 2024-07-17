import re
from playwright.sync_api import Page, expect


def test_email_empty_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").click()
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Wprowadź swój email")
    page.screenshot(path="email_ffpl_scr/emailemptyf.png")


def test_email_space_fieldf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type(" ")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Wprowadź swój email")
    page.screenshot(path="email_ffpl_scr/emailspacef.png")


def test_email_сyrillic_in_namef_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("привіт@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_ffpl_scr/emailсyrillicinnamef.png")


def test_email_polski_in_namef_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("Świętosław@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_ffpl_scr/emailpolskiinnamef.png")


def test_email_latin_in_namef_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("test@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffpl_scr/emaillatininnamef.png")


def test_email_1char_in_namef_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("a@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #error mes >2char
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_ffpl_scr/email1charinnamef.png")


def test_email_2char_in_namef_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("au@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffpl_scr/email2charinnamef.png")


def test_email_3char_in_namef_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("oon@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffpl_scr/email3charinnamef.png")


def test_email_25charf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("designtechnique@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffpl_scr/email25charf.png")


def test_email_50charf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("asdqqwertyuiopasdfghjklqqawseqwertyuiopa@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffpl_scr/email50charf.png")


def test_email_51charf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("qasdqqwertyuiopasdfghjklqqawseqwertyuiopa@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #error mes >51char
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_ffpl_scr/email51charf.png")


def test_email_70charf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("mnbvcxzlkjhgfddxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #error mes >51char
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_ffpl_scr/email70charf.png")


def test_email_num_in_namef_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("vicky1792345680@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffpl_scr/emailnuminnamef.png")


def test_email_up_case_in_namef_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("TESTING@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffpl_scr/emailucaseinnamef.png")


def test_email_symb_in_namef_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("v?i*kt!ri,a@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_ffpl_scr/emailsymbinnamef.png")


def test_email_hyphen_in_namef_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("T-est-design-techniques@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffpl_scr/emailhypheninnamef.png")


def test_email_underline_in_namef_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("T_est_design_techniques@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffpl_scr/emailunderlineinnamef.png")


def test_email_point_in_namef_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("T.est.design.techniques@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffpl_scr/emailpointinnamef.png")


def test_email_space_in_namef_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("Test design@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_ffpl_scr/emailspaceinnamef.png")


def test_email_without_first_domainf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("test@gmail.")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_ffpl_scr/emailwithout1domf.png")


def test_email_without_namef_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_ffpl_scr/emailwithoutnamef.png")


def test_email_with_1char_in_first_domainf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("test@gmail.c")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_ffpl_scr/emailwith1charin1domf.png")


def test_email_with_2char_in_first_domainf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("test@gmail.co")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffpl_scr/emailwith2charin1domf.png")


def test_email_without_dotf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("testgmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_ffpl_scr/emailwithoutdotf.png")


def test_email_incorrect_dotf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("@testgmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_ffpl_scr/emailincorrectdotf.png")


def test_email_incorrect_dot2f_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("testgmail.com@")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_ffpl_scr/emailincorrectdot2f.png")


def test_email_with_2_dotsf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("t@est@gmail.com")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_ffpl_scr/emailwith2dotsf.png")


def test_email_with_ruf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("pipipi@gmail.ru")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Domeny .ru i .by są niedozwolone")
    page.screenshot(path="email_ffpl_scr/emailwithruf.png")


def test_email_with_byf_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("pipipi@gmail.by")
    page.get_by_placeholder("Twoja wiadomość").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Domeny .ru i .by są niedozwolone")
    page.screenshot(path="email_ffpl_scr/emailwithbyf.png")