import pytest
from playwright.sync_api import Page, expect


def test_email_empty_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").click()
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть електронну пошту")


def test_email_space_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type(" ")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть електронну пошту")


def test_email_cyrillic_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("привіт@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_latin_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("test@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_1char_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("a@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_2char_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("au@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_3char_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("oon@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_35char_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("qwertyuiopasdfghjklqqawse@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_49char_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("wertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_50char_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("awertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


@pytest.mark.skip(reason="The field contains restrictions")
def test_email_51char_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("qawertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_70char_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("mnbvcxzlkjhgfddxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_numb_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("vicky1792345680@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_hyphen_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("t-est-design-techniques@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_underline_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("t_est_design_techniques@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_point_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("t.est.design.techniques@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_symb_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("vi*kt!ria@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_space_in_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("Stepan Bandera@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_without_first_domain_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("anya@gmail.")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_without_name_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_1char_in_first_domain_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("anya@gmail.c")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_2char_in_first_domain_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("anya@gmail.co")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_without_dot_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("anyagmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_incorrect_dot1_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("@anyagmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_incorrect_dot2_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("anyagmail.com@")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_2_dots_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("a@nya@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_low_case_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("testing@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_with_up_case_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("TESTING@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_with_ru_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("pipipi@gmail.ru")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Домени .ru і .by не допускаються")


def test_email_with_by_mentor_ua(setup: Page) -> None:
    setup.get_by_role("button", name="Стати ментором").click()
    setup.get_by_role("textbox", name="email@gmail.com").type("pipipi@gmail.by")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Домени .ru і .by не допускаються")
