import re
from playwright.sync_api import Page, expect


def test_ln_empty_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").click()
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть профіль в Linkedin")
    page.screenshot(path="ln_mentorua_scr/lnempty.png")


def test_ln_space_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type(" ")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть профіль в Linkedin")
    page.screenshot(path="ln_mentorua_scr/lnspace.png")


def test_ln_valid_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/StepanBandera")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentorua_scr/lnvalid.png")


def test_ln_upcase_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/TESTING")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentorua_scr/lnupcase.png")


def test_ln_lowcase_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/testing")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentorua_scr/lnlowcase.png")


def test_ln_199char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfgh")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentorua_scr/ln199char.png")


def test_ln_200char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfghj")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentorua_scr/ln200char.png")


#cant type >200
def test_ln_201char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfghjj")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")
    page.screenshot(path="ln_mentorua_scr/ln201char.png")


#cant type >200
def test_ln_250char_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfghjqwertyuiopasdfghjklpzxcvbnmlkjqwertyuiopqwertyuiop")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")
    page.screenshot(path="ln_mentorua_scr/ln250char.png")


def test_ln_without_http_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("www.linkedin.com/in/StepanBandera")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")
    page.screenshot(path="ln_mentorua_scr/lnwithouthttp.png")


def test_ln_num_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("0123456789")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")
    page.screenshot(path="ln_mentorua_scr/lnnum.png")


def test_ln_symb_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("!@#?*")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")
    page.screenshot(path="ln_mentorua_scr/lnsymb.png")


def test_ln_num_in_username_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/StepanBandera1234567890")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentorua_scr/lnnuminuname.png")


def test_ln_symb_in_username_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/S!epan,Ban?era@")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")
    page.screenshot(path="ln_mentorua_scr/lnsymbinuname.png")


def test_ln_username_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("StepanBandera1234567890")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")
    page.screenshot(path="ln_mentorua_scr/lnusername.png")


def test_ln_lnpart_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")
    page.screenshot(path="ln_mentorua_scr/lnlnpart.png")


def test_ln_сyrillic_in_username_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/СтепанАндрійовичБандера")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")
    page.screenshot(path="ln_mentorua_scr/lnсyrillicinusername.png")


def test_ln_space_in_username_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/Testdesign techniques")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")
    page.screenshot(path="ln_mentorua_scr/lnspaceinusername.png")


def test_ln_underline_in_username_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/t_est_ing_tt")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")
    page.screenshot(path="ln_mentorua_scr/lnundinusername.png")


def test_ln_point_in_username_ua(page: Page) -> None:
    page.goto("/")
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Стати ментором").click()
    page.get_by_placeholder("Лінк на профіль").type("https://www.linkedin.com/in/t.est.ing.tt")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Введіть дійсне посилання на профіль в Linkedin")
    page.screenshot(path="ln_mentorua_scr/lnpointinusername.png")

