import re
from playwright.sync_api import Page, expect


def test_email_empty_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").click()
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Enter your email")
    page.screenshot(path="email_ffen_scr/emailemptyf.png")


def test_email_space_fieldf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type(" ")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Enter your email")
    page.screenshot(path="email_ffen_scr/emailspacef.png")


def test_email_сyrillic_in_namef_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("привіт@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")
    page.screenshot(path="email_ffen_scr/emailсyrillicinnamef.png")


def test_email_latin_in_namef_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("test@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffen_scr/emaillatininnamef.png")


def test_email_1char_in_namef_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("a@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #error mes >2char
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")
    page.screenshot(path="email_ffen_scr/email1charinnamef.png")


def test_email_2char_in_namef_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("au@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffen_scr/email2charinnamef.png")


def test_email_3char_in_namef_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("oon@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffen_scr/email3charinnamef.png")


def test_email_25charf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("designtechnique@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffen_scr/email25charf.png")


def test_email_50charf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("asdqqwertyuiopasdfghjklqqawseqwertyuiopa@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffen_scr/email50charf.png")


def test_email_51charf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("qasdqqwertyuiopasdfghjklqqawseqwertyuiopa@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #error mes >51char
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")
    page.screenshot(path="email_ffen_scr/email51charf.png")


def test_email_70charf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("mnbvcxzlkjhgfddxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #error mes >51char
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")
    page.screenshot(path="email_ffen_scr/email70charf.png")


def test_email_num_in_namef_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("vicky1792345680@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffen_scr/emailnuminnamef.png")


def test_email_up_case_in_namef_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("TESTING@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffen_scr/emailucaseinnamef.png")


def test_email_symb_in_namef_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("v?i*kt!ri,a@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")
    page.screenshot(path="email_ffen_scr/emailsymbinnamef.png")


def test_email_hyphen_in_namef_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("T-est-design-techniques@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffen_scr/emailhypheninnamef.png")


def test_email_underline_in_namef_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("T_est_design_techniques@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffen_scr/emailunderlineinnamef.png")


def test_email_point_in_namef_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("T.est.design.techniques@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffen_scr/emailpointinnamef.png")


def test_email_space_in_namef_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("Test design@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")
    page.screenshot(path="email_ffen_scr/emailspaceinnamef.png")


def test_email_without_first_domainf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("test@gmail.")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")
    page.screenshot(path="email_ffen_scr/emailwithout1domf.png")


def test_email_without_namef_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")
    page.screenshot(path="email_ffen_scr/emailwithoutnamef.png")


def test_email_with_1char_in_first_domainf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("test@gmail.c")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")
    page.screenshot(path="email_ffen_scr/emailwith1charin1domf.png")


def test_email_with_2char_in_first_domainf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("test@gmail.co")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffen_scr/emailwith2charin1domf.png")


def test_email_without_dotf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("testgmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")
    page.screenshot(path="email_ffen_scr/emailwithoutdotf.png")


def test_email_incorrect_dotf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("@testgmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")
    page.screenshot(path="email_ffen_scr/emailincorrectdotf.png")


def test_email_incorrect_dot2f_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("testgmail.com@")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")
    page.screenshot(path="email_ffen_scr/emailincorrectdot2f.png")


def test_email_with_2_dotsf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("t@est@gmail.com")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")
    page.screenshot(path="email_ffen_scr/emailwith2dotsf.png")


def test_email_with_ruf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("pipipi@gmail.ru")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text(".ru and .by domains are not allowed")
    page.screenshot(path="email_ffen_scr/emailwithruf.png")


def test_email_with_byf_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("pipipi@gmail.by")
    page.get_by_placeholder("Your message").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text(".ru and .by domains are not allowed")
    page.screenshot(path="email_ffen_scr/emailwithbyf.png")