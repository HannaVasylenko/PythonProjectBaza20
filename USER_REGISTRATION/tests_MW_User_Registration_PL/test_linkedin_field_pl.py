import re
from playwright.sync_api import Page, expect


def test_lnpr_empty_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").click()
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź swój profil na Linkedin")
    page.screenshot(path="lnprpl_screenshots/lnempty.png")


def test_lnpr_without_http_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("www.linkedin.com/in/tanya") #http
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="lnprpl_screenshots/lnwithouthttp.png")


def test_lnpr_valid_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/tanya")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnprpl_screenshots/lnvalid.png")


def test_lnpr_up_case_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/TANYA")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnprpl_screenshots/lnupcase.png")


def test_lnpr_low_case_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/tanyatest")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnprpl_screenshots/lnlowcase.png")


def test_lnpr_valid_сyrillic_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/таня")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin") #faild
    page.screenshot(path="lnprpl_screenshots/lnvalidсyrillic.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_valid_polski_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/łęęęł")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m") #Wprowadź prawidłowy link do profilu Linkedin
    page.screenshot(path="lnprpl_screenshots/lnvalidpolski.png")


def test_lnpr_numbers_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("1234567890")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="lnprpl_screenshots/lnnumbers.png")


def test_lnpr_numbers_in_user_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/tanya1758934602") #max char
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnprpl_screenshots/lnnumbusername.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_symb_in_user_name_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/ta.ny@no!v*a?")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnprpl_screenshots/lnsymbusername.png")


def test_lnpr_symbols_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("!@#?*")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="lnprpl_screenshots/lnsymbols.png")


def test_lnpr_space_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type(" ")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź swój profil na Linkedin")
    page.screenshot(path="lnprpl_screenshots/lnspace.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_space_in_username_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/test test")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź swój profil na Linkedin")
    page.screenshot(path="lnprpl_screenshots/lnspaceinusername.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_underline_in_username_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/t_est_test_t")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź swój profil na Linkedin")
    page.screenshot(path="lnprpl_screenshots/lnundinusername.png")


@pytest.mark.skip(reason="Verification is absent from the requirements")
def test_lnpr_point_in_username_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/t.est.test.t")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź swój profil na Linkedin")
    page.screenshot(path="lnprpl_screenshots/lnpointinusername.png")


def test_lnpr_lnpart_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='linkedin']/../following-sibling::p")).to_have_text("Wprowadź prawidłowy link do profilu Linkedin")
    page.screenshot(path="lnprpl_screenshots/lnlnpart.png")


def test_lnpr_199char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/hecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghj")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnprpl_screenshots/ln199char.png")


def test_lnpr_200char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheНашіпартнериtitleChecthatCheqwertyuioqweasdfghj")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnprpl_screenshots/ln200char.png")


def test_lnpr_201char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/sChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainsthqwertyuiopastitleChecthatCheqwertyuioqweasdfghjd")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnprpl_screenshots/ln201char.png")


def test_lnpr_250char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Link do profilu").type("https://www.linkedin.com/in/ChecktheplacementofthePartnersblockafterthearticlesblockCheckthesizeanddesignaccordingtothelayoutCheckthattheblockcontainstheqwertyuiopastitleChecthatCheqwertyuioqweasdfghjqwertyuiopasdfghjklpzxcvbnmlkjqwertyuiopqwertyuiop")
    page.locator("label").filter(has_text="Więc").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='linkedin']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="lnprpl_screenshots/ln250char.png")