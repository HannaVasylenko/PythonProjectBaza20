import pytest
from playwright.sync_api import Page, expect


def test_email_empty_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").click()
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Enter your email")


def test_email_space_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type(" ")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Enter your email")


def test_email_cyrillic_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("привіт@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_latin_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_1char_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("a@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_2char_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("au@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_3char_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("oon@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_35char_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("qwertyuiopasdfghjklqqawse@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_49char_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("qwertasdfghjklqwertyuiopasdfghjklqqawse@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_50char_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("aqwertasdfghjklqwertyuiopasdfghjklqqawse@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


@pytest.mark.skip(reason="The field contains restrictions")
def test_email_51char_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("qaqwertasdfghjklqwertyuiopasdfghjklqqawse@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_70char_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("mnbvcxzlkjhgfddxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_numb_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("vicky1792345680@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_hyphen_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("t-est-design-techniques@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_underline_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("t_est_design_techniques@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_point_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("t.est.design.techniques@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_symb_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("vi*kt!ria@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_space_in_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("test program@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_without_first_domain_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("anya@gmail.")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_without_name_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_with_1char_in_first_domain_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("anya@gmail.c")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_with_2char_in_first_domain_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("anya@gmail.co")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_without_dot_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("anyagmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_incorrect_dot1_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("@anyagmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_incorrect_dot2_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("anyagmail.com@")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_with_2_dots_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("a@nya@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text("Please enter a valid email")


def test_email_with_low_case_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("testing@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_with_up_case_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("TESTING@gmail.com")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_with_ru_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("pipipi@gmail.ru")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text(".ru and .by domains are not allowed")


def test_email_with_by_mentor_en(setup_en: Page) -> None:
    setup_en.get_by_role("button", name="Become a mentor").click()
    setup_en.get_by_role("textbox", name="email@gmail.com").type("pipipi@gmail.by")
    setup_en.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_en.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup_en.locator("//label[@for='email']/following-sibling::p")).to_have_text(".ru and .by domains are not allowed")
