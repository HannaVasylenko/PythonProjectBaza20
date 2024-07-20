import re
from playwright.sync_api import Page, expect


def test_emailpr_empty_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").click()
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть електронну пошту")


def test_emailpr_only_space_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type(" ")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть електронну пошту")


def test_emailpr_сyrillic_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("привіт@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_emailpr_latin_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("pryvit@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_1char_in_name_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("a@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_emailpr_2char_in_name_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("oa@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_3char_in_name_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("oao@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_35char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("qwertyuiopasdfghjklqqawse@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_49char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("qwertyuiopasdfghjklqqawseqwertyuiopasdf@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_50char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("sqwertyuiopasdfghjklqqawseqwertyuiopasdf@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_51char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("qsqwertyuiopasdfghjklqqawseqwertyuiopasdf@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_55char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("xasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_56char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").click()
    setup.get_by_placeholder("email@gmail.com").fill("dxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com") #must be error?
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_70char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("mnbvcxzlkjhgfddxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_emailpr_num_in_name_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("vicky1792345680@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_symb_in_name_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("vi*kt!ria@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_emailpr_space_in_name_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("test test@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_emailpr_hyphen_in_name_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("t-est-design-techniques@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_underline_in_name_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("T_est_design_techniques@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_point_in_name_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("T.est.design.techniques@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_onlysymb_in_name_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("!%?_+*@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_emailpr_without_first_domain_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("anya@gmail.")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_emailpr_without_name_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_emailpr_with_1char_in_first_domain_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("anya@gmail.c")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_emailpr_with_2char_in_first_domain_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("anya@gmail.co")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_without_dot_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("anyagmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_emailpr_with_incorrect_dot_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("@anyagmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_emailpr_with_incorrect_dot2_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("anyagmail.com@")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_emailpr_with_2_dots_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("a@nya@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Введіть дійсну електронну пошту")


def test_emailpr_with_upcase_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("TESTING@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_with_lowcase_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("testing@gmail.com")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_with_ru_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("pipipi@gmail.ru")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Домени .ru і .by не допускаються")


def test_emailpr_with_by_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("email@gmail.com").type("pipipi@gmail.by")
    setup.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Домени .ru і .by не допускаються")
