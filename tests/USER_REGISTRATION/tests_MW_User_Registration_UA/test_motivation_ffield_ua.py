import pytest
from playwright.sync_api import Page, expect


def test_motivation_empty_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").click()
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='motivation']/following-sibling::p")).to_have_text("Вкажіть вашу мотивацію")


def test_motivation_space_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type(" ")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='motivation']/following-sibling::p")).to_have_text("Вкажіть вашу мотивацію")


def test_motivation_1char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("ї")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='motivation']/following-sibling::p")).to_have_text("Текст має бути не менше 10 знаків")


def test_motivation_2char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("їє")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='motivation']/following-sibling::p")).to_have_text("Текст має бути не менше 10 знаків")


def test_motivation_5char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("їєабв")
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class","InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='motivation']/following-sibling::p")).to_have_text("Текст має бути не менше 10 знаків")


def test_motivation_9char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("їєабвгійц")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class","InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='motivation']/following-sibling::p")).to_have_text("Текст має бути не менше 10 знаків")


def test_motivation_10char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("їєабвгійцв")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_motivation_11char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("їєабвгійцва")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_motivation_20char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("йцукенгшщзфівапролдж")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_motivation_49char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("йцукенгшщзхїфівапролджєячсмитьбюйцукенгшфівапролд")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_motivation_50char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("йцукенгшщзхїфівапролджєячсмитьбюйцукенгшфівапролдз")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_motivation_51char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("йцукенгшщзхїфівапролджєячсмитьбюйцукенгшфівапролдзв")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='motivation']/following-sibling::p")).to_have_text("Текст має бути не більше 50 знаків")


def test_motivation_70char_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("йцукенгшщзхїфівапролджєячсмитьбюйцукенгшфівапролдзйцукенгшщзфівапролдж")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='motivation']/following-sibling::p")).to_have_text("Текст має бути не більше 50 знаків")


def test_motivation_symb1_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("С!-_().,<>&?@$=+{}#*/[\]")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_motivation_symb2_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("С|?%^:;`₴’’””<>&?@$=+*\[/]?%;:")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_motivation_numb_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("числа 1234567890")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_motivation_up_case_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("ТЕСТУВАННЯ")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe")


def test_motivation_low_case_user_reg_ua(setup: Page) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").type("тестування")
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe")


@pytest.mark.parametrize("test_input", [
    ("Пръерплрт"),
    ("Орамыьтор"),
    ("апмЭтиор"),
    ("потлоЁьтбоа"),
    ("Тиитрэтьтор"),
    ("Иимпаётир")
])
def test_motivation_piletters_user_reg_ua(setup: Page, test_input) -> None:
    setup.get_by_role("banner").get_by_role("link", name="Стажування").click()
    setup.get_by_role("button", name="Доєднатись до проєкту").first.click()
    setup.get_by_placeholder("Ваша відповідь").press("Control+A")
    setup.get_by_placeholder("Ваша відповідь").press("Delete")
    setup.get_by_placeholder("Ваша відповідь").type(test_input)
    setup.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(setup.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input__KEXwe InputField__error__hbnwz")
    expect(setup.locator("//label[@for='motivation']/following-sibling::p")).to_have_text("Введіть коректний текст")

