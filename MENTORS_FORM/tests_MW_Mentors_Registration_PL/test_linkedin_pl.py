import re
import pytest
from playwright.sync_api import Page, expect


def test_ln_empty_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").click()
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź swój profil na Linkedin")
    page.screenshot(path="ln_mentorpl_scr/lnempty.png")


def test_ln_space_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type(" ")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź swój profil na Linkedin")
    page.screenshot(path="ln_mentorpl_scr/lnspace.png")


def test_ln_valid_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/Testdesigntechniques")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentorpl_scr/lnvalid.png")


def test_ln_lowcase_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/testdesigntechniques")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentorpl_scr/lnlowcase.png")


def test_ln_upcase_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/TESTING")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentorpl_scr/lnupcase.png")


def test_ln_199char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfgh")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentorpl_scr/ln199char.png")


def test_ln_200char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghj")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentorpl_scr/ln200char.png")


def test_ln_201char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghjl")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="ln_mentorpl_scr/ln201char.png")


def test_ln_250char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghjqwertyuiopasdfghjklpzxcvbnmlkjqwertyuiopqwertyuiop")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="ln_mentorpl_scr/ln250char.png")


def test_ln_without_http_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("www.linkedin.com/in/Testdesigntechniques")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="ln_mentorpl_scr/lnwithouthttp.png")


def test_ln_num_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("0123456789")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="ln_mentorpl_scr/lnnum.png")


def test_ln_symb_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("!@#?*")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="ln_mentorpl_scr/lnsymb.png")


def test_ln_num_in_username_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/Testtechniques1234567890")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentorpl_scr/lnnuminuname.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_symb_in_username_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/T.es,t!de?si@gn")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    #expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentorpl_scr/lnsymbinuname.png")


def test_ln_username_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("Testdesign1234567890")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="ln_mentorpl_scr/lnusername.png")


def test_ln_lnpart_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="ln_mentorpl_scr/lnlnpart.png")


def test_ln_сyrillic_in_username_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/Тестування")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="ln_mentorpl_scr/lnсyrillicinusername.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_polski_in_username_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/żęóżłŚŁ")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="ln_mentorpl_scr/lnpolskiinusername.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_polskianden_in_username_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/testżęóżłŚŁ")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="ln_mentorpl_scr/lnpolskiandeninusername.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_space_in_username_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/Testdesign techniques")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    #expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="ln_mentorpl_scr/lnspaceinusername.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_underline_in_username_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/t_est_ing_t")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="ln_mentorpl_scr/lnundinusername.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_ln_point_in_username_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Zostać mentorem").click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/t.est.ing.t")
    page.get_by_text("-15.00").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="ln_mentorpl_scr/lnpointinusername.png")

