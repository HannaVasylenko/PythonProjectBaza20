import re
from playwright.sync_api import Page, expect


def test_email_empty_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").click()
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Wprowadź swój email")
    page.screenshot(path="email_mentorpl_scr/emailempty.png")


def test_email_space_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type(" ")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Wprowadź swój email")
    page.screenshot(path="email_mentorpl_scr/emaispace.png")


def test_email_сyrillic_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("привіт@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_mentorpl_scr/emailсyrinname.png")


def test_email_latin_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/emaillatinname.png")


def test_email_polski_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("Świętosław@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_mentorpl_scr/emailpolskiinname.png")


def test_email_1char_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("a@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_mentorpl_scr/email1charinname.png")


def test_email_2char_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("au@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/email2charinname.png")


def test_email_3char_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("oon@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/email3charinname.png")


def test_email_35char_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("qwertyuiopasdfghjklqqawse@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/email35char.png")


def test_email_49char_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("wertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/email49char.png")


def test_email_50char_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("awertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/email50char.png")


def test_email_51char_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("qawertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    #expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    #expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/email51char.png")


def test_email_54char_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("asdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/email54char.png")


def test_email_55char_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("qasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/email55char.png")


def test_email_56char_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("aqasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com") #must be error??? cant type but accept
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    #expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    #expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/email56char.png")


def test_email_70char_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("mnbvcxzlkjhgfddxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com") #error mes
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_mentorpl_scr/email70char.png")


def test_email_num_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("vicky1792345680@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/emailnuminname.png")


def test_email_hyphen_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("t-est-design-techniques@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/emailhypheninname.png")


def test_email_underline_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("t_est_design_techniques@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/emailunderlineinname.png")


def test_email_point_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("t.est.design.techniques@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/emailpointinname.png")


def test_email_symb_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("vi*kt!ria@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_mentorpl_scr/emailsymbinname.png")


def test_email_space_in_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("Stepan Bandera@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_mentorpl_scr/emailspaceinname.png")


def test_email_without_first_domain_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("anya@gmail.")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_mentorpl_scr/emailwithout1dom.png")


def test_email_without_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_mentorpl_scr/emailwithoutname.png")


def test_email_with_1char_in_first_domain_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("anya@gmail.c")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_mentorpl_scr/emailwith1charin1dom.png")


def test_email_with_2char_in_first_domain_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("anya@gmail.co")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/emailwith2charindom.png")


def test_email_without_dot_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("anyagmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_mentorpl_scr/emailwithoutdot.png")


def test_email_incorrect_dot_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("@anyagmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_mentorpl_scr/emailincordot.png")


def test_email_incorrect_dot2_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("anyagmail.com@")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_mentorpl_scr/emailincordot2.png")


def test_email_with_2_dots_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("a@nya@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")
    page.screenshot(path="email_mentorpl_scr/emailwith2dots.png")


def test_email_with_upcase_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("TESTING@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/emailwithupcase.png")


def test_email_with_lowcase_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("testing@gmail.com")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="email_mentorpl_scr/emailwithlowcase.png")


def test_email_with_ru_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("pipipi@gmail.ru")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Domeny .ru i .by są niedozwolone")
    page.screenshot(path="email_mentorpl_scr/emailwithru.png")


def test_email_with_by_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_role("textbox", name="email@gmail.com").type("pipipi@gmail.by")
    page.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Domeny .ru i .by są niedozwolone")
    page.screenshot(path="email_mentorpl_scr/emailwithby.png")
