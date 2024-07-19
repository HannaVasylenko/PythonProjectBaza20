import re
import pytest
from playwright.sync_api import Page, expect


def test_lnpr_empty_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").click()
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter your Linkedin profile")
    page.screenshot(path="lnpren_screenshots/lnempty.png")


def test_lnpr_without_http_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("www.linkedin.com/in/tanya")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="lnpren_screenshots/lnwithouthttp.png")


def test_lnpr_сyrillic_in_username_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/тетянка")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="lnpren_screenshots/lncyrinusername.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_symb_in_username_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/te.s,t?i!n@g")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="lnpren_screenshots/lnsymbinusername.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_space_in_username_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/test test")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="lnpren_screenshots/lnspacebinusername.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_underline_in_username_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/t_est_test_t")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="lnpren_screenshots/lnundbinusername.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_point_in_username_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/t.est.test.t")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="lnpren_screenshots/lnpointbinusername.png")


def test_lnpr_lnpart_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="lnpren_screenshots/lnlnpart.png")


def test_lnpr_valid_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/tanya")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnpren_screenshots/lnvalid.png")


def test_lnpr_upcase_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/TESTING")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnpren_screenshots/lnupcase.png")


def test_lnpr_lowcase_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/testing")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnpren_screenshots/lnlowcase.png")


@pytest.mark.skip(reason="The field contains restrictions")
def test_lnpr_199char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/hecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfghj")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnpren_screenshots/ln199char.png")


@pytest.mark.skip(reason="The field contains restrictions")
def test_lnpr_200char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/ahecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfghj")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnpren_screenshots/ln200char.png")


@pytest.mark.skip(reason="The field contains restrictions")
def test_lnpr_201char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfghjs")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="lnpren_screenshots/ln201char.png")


@pytest.mark.skip(reason="The field contains restrictions")
def test_lnpr_250char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/qqwertyuiqwertyuiopasdfghjklzqwertyuiophecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghjsqasdfghjklo")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="lnpren_screenshots/ln250char.png")


def test_numb_in_username_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("https://www.linkedin.com/in/tanya1234567890")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnpren_screenshots/lnnuminusername.png")


def test_lnpr_numbers_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("1234567890")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="lnpren_screenshots/lnnumbers.png")


def test_lnpr_symbols_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type("!@#?*")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter a valid Linkedin profile link")
    page.screenshot(path="lnpren_screenshots/lnsymbols.png")


def test_lnpr_space_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Link to profile").type(" ")
    page.locator("label").filter(has_text="Yes").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Enter your Linkedin profile")
    page.screenshot(path="lnpren_screenshots/lnspace.png")