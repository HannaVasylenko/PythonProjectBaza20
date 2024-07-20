import re
import pytest
from playwright.sync_api import Page, expect


def test_motpr_empty_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").click()
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Вкажіть вашу мотивацію")


def test_motpr_space_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type(" ")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Вкажіть вашу мотивацію")


def test_motpr_1char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("ї")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Текст має бути не менше 10 знаків")


def test_motpr_2char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("їє")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Текст має бути не менше 10 знаків")

def test_motpr_5char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("їєабв")
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Текст має бути не менше 10 знаків")


def test_motpr_9char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("їєабвгійц")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Текст має бути не менше 10 знаків")


def test_motpr_10char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("їєабвгійцв")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_11char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("їєабвгійцва")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_20char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("йцукенгшщзфівапролдж")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_49char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("йцукенгшщзхїфівапролджєячсмитьбюйцукенгшфівапролд")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_50char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("йцукенгшщзхїфівапролджєячсмитьбюйцукенгшфівапролдз")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_51char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("йцукенгшщзхїфівапролджєячсмитьбюйцукенгшфівапролдзв")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Текст має бути не більше 50 знаків")


def test_motpr_70char_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("йцукенгшщзхїфівапролджєячсмитьбюйцукенгшфівапролдзйцукенгшщзфівапролдж")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Текст має бути не більше 50 знаків")


def test_motpr_symb1_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("С!-_().,<>&?@$=+{}#*/[\]")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_symb2_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("С|?%^:;`₴’’””<>&?@$=+*\[/]?%;:")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_num_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("числа 1234567890")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_upcase_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("ТЕСТУВАННЯ")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_lowcase_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("тестування")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


@pytest.mark.parametrize("test_input", [
    ("Пръерплрт"),
    ("Орамыьтор"),
    ("апмЭтиор"),
    ("потлоЁьтбоа"),
    ("Тиитрэтьтор"),
    ("Иимпаётир")
])
def test_motpr_piletters_ua(setup: Page, test_input) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").press("Control+A")
    setup.get_by_placeholder("Ваша відповідь").press("Delete")
    setup.get_by_placeholder("Ваша відповідь").type(test_input)
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Введіть коректний текст")

