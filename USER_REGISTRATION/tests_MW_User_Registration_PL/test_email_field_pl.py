import re
from playwright.sync_api import Page, expect


def test_emailpr_empty_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").click()
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Wprowadź swój email")


def test_emailpr_only_space_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type(" ")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Wprowadź swój email")


def test_emailpr_сyrillic_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("привіт@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_emailpr_polski_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("bożenaŁjózefaŁ@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_emailpr_latin_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("pryvit@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_1char_in_name_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("a@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_emailpr_2char_in_name_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("oa@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_3char_in_name_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("oao@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_35char(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("qwertyuiopasdfghjklqqawse@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")

def test_emailpr_49char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("xasdqqwertyuiopasdfghjklqqawseqwertyuio@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_50char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("axasdqqwertyuiopasdfghjklqqawseqwertyuio@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_51char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("aaxasdqqwertyuiopasdfghjklqqawseqwertyuio@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_55char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("xasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_56char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("dxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_70char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("mnbvcxzlkjhgfddxasdqqwertyuiopasdfghjklqqawseqwertyuiopasdfg@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")

    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_emailpr_num_in_name_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("vicky1792345680@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_hyphen_in_name_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("T-est-design-techniques@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_underline_in_name_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("T_est_design_techniques@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_point_in_name_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("T.est.design.techniques@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_symb_in_name_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("vi.kt!ri?a@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_emailpr_space_in_name_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("test test@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_emailpr_onlysymb_in_name_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type(".,!%?_+*@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_emailpr_without_first_domain_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("anya@gmail.")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_emailpr_without_name_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_emailpr_with_1char_in_first_domain_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("anya@gmail.c")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_emailpr_with_2char_in_first_domain_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("anya@gmail.co")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_without_dot_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("anyagmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_emailpr_with_incorrect_dot_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("@anyagmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_emailpr_with_incorrect_dot2_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("anyagmail.com@")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_emailpr_with_2_dots_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("a@nya@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Proszę podać poprawny adres e-mail")


def test_emailpr_with_upcase_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("TESTING@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_with_up_low_case_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("testing@gmail.com")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_emailpr_with_ru_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("pipipi@gmail.ru")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Domeny .ru i .by są niedozwolone")


def test_emailpr_with_by_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("email@gmail.com").type("pipipi@gmail.by")
    setup_pl.get_by_placeholder("+380 xx xxx xx xx").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='email']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='email']/../following-sibling::p")).to_have_text("Domeny .ru i .by są niedozwolone")
