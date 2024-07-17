import re
from playwright.sync_api import Page, expect


def test_motpr_empty_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").click()
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("State your motivation")
    page.screenshot(path="motpren_screenshots/motempty.png")


def test_motpr_space_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type(" ")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("State your motivation")
    page.screenshot(path="motpren_screenshots/motspace.png")


def test_motpr_1char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("t")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Modal_form.error_message.motivation_min")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("error mes >5")
    page.screenshot(path="motpren_screenshots/mot1char.png")


def test_motpr_2char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("te")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Modal_form.error_message.motivation_min")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("error mes >5")
    page.screenshot(path="motpren_screenshots/mot2char.png")


def test_motpr_3char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("tes")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Modal_form.error_message.motivation_min")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("error mes >5")
    page.screenshot(path="motpren_screenshots/mot3char.png")


def test_motpr_4char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("test")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Modal_form.error_message.motivation_min")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("error mes >5")
    page.screenshot(path="motpren_screenshots/mot4char.png")


def test_motpr_5char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("testi")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motpren_screenshots/mot5char.png")


def test_motpr_6char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("testin")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motpren_screenshots/mot6char.png")


def test_motpr_20char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("qwertyuiopasdfghjklq")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motpren_screenshots/mot20char.png")


def test_motpr_49char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjkl")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motpren_screenshots/mot49char.png")


def test_motpr_50char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklq")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motpren_screenshots/mot50char.png")


def test_motpr_51char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklqr")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("The text should not exceed 50 characters")
    page.screenshot(path="motpren_screenshots/mot51char.png")


def test_motpr_70char_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklqqwertyuiopasdfghjklp")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("The text should not exceed 50 characters")
    page.screenshot(path="motpren_screenshots/mot70char.png")


def test_motpr_symb1_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("s!-_().,<>&?@$=+{}#*/[\]")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motpren_screenshots/motsymb1.png")
    
    
def test_motpr_symb2_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("s|?%^:;`₴’’””<>&?@$=+*\[/]?%;:")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motpren_screenshots/motsymb2.png")


def test_motpr_num_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("num1234567890")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motpren_screenshots/motnum.png")


def test_motpr_upcase_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("TESTING")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motpren_screenshots/motupcase.png")


def test_motpr_lowcase_en(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("EN").click()
    page.get_by_role("banner").get_by_role("link", name="Internship").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Join the project").first.click()
    page.get_by_placeholder("Your answer").type("testing")
    page.locator("label").filter(has_text="On the Baza Trainee Ukraine website").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motpren_screenshots/motlowcase.png")