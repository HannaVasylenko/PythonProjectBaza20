import re
from playwright.sync_api import Page, expect


def test_email_empty_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").click()
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть електронну пошту")
    page.screenshot(path="email_ffua_scr/emailemptyf.png")


def test_email_space_fieldf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type(" ")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть електронну пошту")
    page.screenshot(path="email_ffua_scr/emailspacef.png")


def test_email_сyrillic_in_namef_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("привіт@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")
    page.screenshot(path="email_ffua_scr/emailсyrillicinnamef.png")


def test_email_latin_in_namef_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("test@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffua_scr/emaillatininnamef.png")


def test_email_1char_in_namef_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("a@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #error mes >2char
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")
    page.screenshot(path="email_ffua_scr/email1charinnamef.png")


def test_email_2char_in_namef_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("au@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffua_scr/email2charinnamef.png")


def test_email_3char_in_namef_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("oon@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffua_scr/email3charinnamef.png")


def test_email_25charf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("designtechnique@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffua_scr/email25charf.png")


def test_email_50charf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("asdqqwertyuiopasdfghjklqqawseqwertyuiopa@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffua_scr/email50charf.png")


def test_email_51charf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("qasdqqwertyuiopasdfghjklqqawseqwertyuiopa@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #error mes >51char
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")
    page.screenshot(path="email_ffua_scr/email51charf.png")


def test_email_70charf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("mnbvcxzlkjhgfddxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #error mes >51char
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")
    page.screenshot(path="email_ffua_scr/email70charf.png")


def test_email_num_in_namef_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("vicky1792345680@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffua_scr/emailnuminnamef.png")


def test_email_up_case_in_namef_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("TESTING@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffua_scr/emailucaseinnamef.png")


def test_email_symb_in_namef_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("v?i*kt!ri,a@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")
    page.screenshot(path="email_ffua_scr/emailsymbinnamef.png")


def test_email_hyphen_in_namef_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("S-tepan-Bandera-OUN@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffua_scr/emailhypheninnamef.png")


def test_email_underline_in_namef_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("S_tepan_Bandera_OUN@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffua_scr/emailunderlineinnamef.png")


def test_email_point_in_namef_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("S.tepan.Bandera.OUN@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffua_scr/emailpointinnamef.png")


def test_email_space_in_namef_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("Stepan Bandera@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")
    page.screenshot(path="email_ffua_scr/emailspaceinnamef.png")


def test_email_without_first_domainf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("test@gmail.")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")
    page.screenshot(path="email_ffua_scr/emailwithout1domf.png")


def test_email_without_namef_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")
    page.screenshot(path="email_ffua_scr/emailwithoutnamef.png")


def test_email_with_1char_in_first_domainf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("test@gmail.c")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")
    page.screenshot(path="email_ffua_scr/emailwith1charin1domf.png")


def test_email_with_2char_in_first_domainf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("test@gmail.co")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_ffua_scr/emailwith2charin1domf.png")


def test_email_without_dotf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("testgmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")
    page.screenshot(path="email_ffua_scr/emailwithoutdotf.png")


def test_email_incorrect_dotf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("@testgmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")
    page.screenshot(path="email_ffua_scr/emailincorrectdotf.png")


def test_email_incorrect_dot2f_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("testgmail.com@")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")
    page.screenshot(path="email_ffua_scr/emailincorrectdot2f.png")


def test_email_with_2_dotsf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("t@st@gmail.com")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")
    page.screenshot(path="email_ffua_scr/emailwith2dotsf.png")


def test_email_with_ruf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("pipipi@gmail.ru")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Домени .ru і .by не допускаються")
    page.screenshot(path="email_ffua_scr/emailwithruf.png")


def test_email_with_byf_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_placeholder("email@gmail.com").type("pipipi@gmail.by")
    page.get_by_placeholder("Ваше повідомлення").click()
    expect(page.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Домени .ru і .by не допускаються")
    page.screenshot(path="email_ffua_scr/emailwithbyf.png")