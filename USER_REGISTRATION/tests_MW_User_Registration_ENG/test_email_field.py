import re
from playwright.sync_api import Page, expect


def test_emailpr_empty_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Enter your email")


def test_emailpr_only_space_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type(" ")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Enter your email")


def test_emailpr_сyrillic_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("привіт@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_emailpr_latin_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("pryvit@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_1char_in_name_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("a@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_emailpr_2char_in_name_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("oa@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_3char_in_name_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("oao@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_35char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("qwertyuiopasdfghjklqqawse@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_49char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("qwertyuiopasdfqwertyuiopasdfghjklqqawse@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_50char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("aqwertyuiopasdfqwertyuiopasdfghjklqqawse@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_51char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("daqwertyuiopasdfqwertyuiopasdfghjklqqawse@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_55char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("xasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_56char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").click()
    setup_en.get_by_placeholder("email@gmail.com").fill("dxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com") #must be error?
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_70char_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("mnbvcxzlkjhgfddxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_emailpr_num_in_name_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("vicky1792345680@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_symb_in_name_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("vi*kt!ria@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_emailpr_space_in_name_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("test test@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_emailpr_numb_in_name_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("1234567890@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_hyphen_in_name_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("T-est-design-techniques@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_underline_in_name_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("T_est_design_techniques@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_point_in_name_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("T.est.design.techniques@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_onlysymb_in_name_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("!%?_+*@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_emailpr_without_first_domain_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("anya@gmail.")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_emailpr_without_name_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_emailpr_with_1char_in_first_domain_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("anya@gmail.c")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_emailpr_with_2char_in_first_domain_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("anya@gmail.co")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_without_dot_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("anyagmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_emailpr_with_incorrect_dot_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("@anyagmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_emailpr_with_incorrect_dot2_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("anyagmail.com@")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_emailpr_with_2_dots_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("a@nya@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Please enter a valid email")


def test_emailpr_with_upcase_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("TESTING@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_with_lowcase_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("testing@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_with_ru_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("pipipi@gmail.ru")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text(".ru and .by domains are not allowed")


def test_emailpr_with_by_en(setup_en: Page) -> None:
    setup_en.get_by_role("banner").get_by_role("link", name="Internship").click()
    setup_en.get_by_role("button", name="Join the project").first.click()
    setup_en.get_by_placeholder("email@gmail.com").type("pipipi@gmail.by")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_en.locator("//label[@for='email']/../following-sibling::p")).to_have_text(".ru and .by domains are not allowed")
