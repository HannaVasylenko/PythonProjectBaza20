import re
from playwright.sync_api import Page, expect


def test_ln_empty_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").click()
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter your Linkedin profile")
    page.screenshot(path="ln_mentoren_scr/lnempty.png")


def test_ln_space_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type(" ")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter your Linkedin profile")
    page.screenshot(path="ln_mentoren_scr/lnspace.png")


def test_ln_valid_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/Testdesigntechniques")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentoren_scr/lnvalid.png")


def test_ln_lowcase_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/testing")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentoren_scr/lnlowcase.png")


def test_ln_upcase_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/TESTING")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentoren_scr/lnupcase.png")


def test_ln_199char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfgh")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentoren_scr/ln199char.png")


def test_ln_200char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghj")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentoren_scr/ln200char.png")


def test_ln_201char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghjj")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="ln_mentoren_scr/ln201char.png")


def test_ln_250char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghjqwertyuiopasdfghjklpzxcvbnmlkjqwertyuiopqwertyuiop")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="ln_mentoren_scr/ln250char.png")


def test_ln_without_http_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("www.linkedin.com/in/Testdesigntechniques")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="ln_mentoren_scr/lnwithouthttp.png")


def test_ln_num_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("0123456789")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="ln_mentoren_scr/lnnum.png")


def test_ln_symb_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("!@#?*")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="ln_mentoren_scr/lnsymb.png")


def test_ln_num_in_username_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/Testtechniques1234567890")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentoren_scr/lnnuminuname.png")


def test_ln_symb_in_username_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/T.es,t!de?si@gn")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    #expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentoren_scr/lnsymbinuname.png")


def test_ln_username_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("Testdesign1234567890")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="ln_mentoren_scr/lnusername.png")


def test_ln_lnpart_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="ln_mentoren_scr/lnlnpart.png")


def test_ln_сyrillic_in_username_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/Тестування")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="ln_mentoren_scr/lnсyrillicinusername.png")


def test_ln_space_in_username_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/Testdesign techniques")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    #expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentoren_scr/lnspaceinusername.png")


def test_ln_underline_in_username_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/t_est_ing_t")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="ln_mentoren_scr/lnundinusername.png")


def test_ln_point_in_username_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Become a mentor").click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/t.est.ing.t")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="ln_mentoren_scr/lnpointinusername.png")

