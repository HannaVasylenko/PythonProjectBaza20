import pytest
from playwright.sync_api import Page, expect


def test_email_empty_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").click()
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть електронну пошту")


def test_email_space_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type(" ")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть електронну пошту")


def test_email_cyrillic_in_name_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("привіт@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_latin_in_name_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("test@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_1char_in_name_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("a@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_2char_in_name_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("au@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_3char_in_name_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("oon@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_25char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("designtechnique@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_50char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("asdqqwertyuiopasdfghjklqqawseqwertyuiopa@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


@pytest.mark.skip(reason="The field contains restrictions")
def test_email_51char_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("qasdqqwertyuiopasdfghjklqqawseqwertyuiopa@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_numb_in_name_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("vicky1792345680@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_up_case_in_name_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("TESTING@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_symb_in_name_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("v?i*kt!ri,a@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_hyphen_in_name_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("t-est-ing-pro@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_underline_in_name_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("t_es_ting_pro@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_point_in_name_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("t.es.ting.pro@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_space_in_name_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("test program@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_without_first_domain_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("test@gmail.")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_without_name_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_1char_in_first_domain_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("test@gmail.c")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_2char_in_first_domain_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("test@gmail.co")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe")


def test_email_without_dot_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("testgmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_incorrect_dot1_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("@testgmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_incorrect_dot2_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("testgmail.com@")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_2_dots_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("t@st@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_ru_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("pipipi@gmail.ru")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Домени .ru і .by не допускаються")


def test_email_with_by_fform_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("pipipi@gmail.by")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//label[@for='email']/following-sibling::input")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='email']/following-sibling::p")).to_have_text("Домени .ru і .by не допускаються")
