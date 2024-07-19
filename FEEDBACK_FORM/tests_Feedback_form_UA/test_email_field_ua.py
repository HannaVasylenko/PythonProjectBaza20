import re
from playwright.sync_api import Page, expect


def test_email_empty_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").click()
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть електронну пошту")


def test_email_space_fieldf_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type(" ")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть електронну пошту")


def test_email_сyrillic_in_namef_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("привіт@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_latin_in_namef_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("test@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_1char_in_namef_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("a@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #error mes >2char
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_2char_in_namef_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("au@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_3char_in_namef_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("oon@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_25charf_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("designtechnique@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_50charf_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("asdqqwertyuiopasdfghjklqqawseqwertyuiopa@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_51charf_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("qasdqqwertyuiopasdfghjklqqawseqwertyuiopa@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #error mes >51char
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_70charf_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("mnbvcxzlkjhgfddxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM") #error mes >51char
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_num_in_namef_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("vicky1792345680@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_up_case_in_namef_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("TESTING@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_symb_in_namef_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("v?i*kt!ri,a@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_hyphen_in_namef_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("S-tepan-Bandera-OUN@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_underline_in_namef_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("S_tepan_Bandera_OUN@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_point_in_namef_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("S.tepan.Bandera.OUN@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_space_in_namef_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("Stepan Bandera@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_without_first_domainf_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("test@gmail.")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_without_namef_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_1char_in_first_domainf_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("test@gmail.c")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_2char_in_first_domainf_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("test@gmail.co")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_email_without_dotf_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("testgmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_incorrect_dotf_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("@testgmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_incorrect_dot2f_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("testgmail.com@")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_2_dotsf_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("t@st@gmail.com")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_email_with_ruf_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("pipipi@gmail.ru")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Домени .ru і .by не допускаються")


def test_email_with_byf_ua(setup: Page) -> None:
    setup.get_by_placeholder("email@gmail.com").type("pipipi@gmail.by")
    setup.get_by_placeholder("Ваше повідомлення").click()
    expect(setup.locator("//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Домени .ru і .by не допускаються")
