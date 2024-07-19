import re
import pytest
from playwright.sync_api import Page, expect


def test_motpr_empty_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").click()
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Вкажіть вашу мотивацію")
    page.screenshot(path="motprua_screenshots/motempty.png")


def test_motpr_space_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type(" ")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Вкажіть вашу мотивацію")
    page.screenshot(path="motprua_screenshots/motspace.png")


def test_motpr_1char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("ї")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Текст має бути не менше 5 знаків")
    page.screenshot(path="motprua_screenshots/mot1char.png")


def test_motpr_2char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("їє")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Текст має бути не менше 5 знаків")
    page.screenshot(path="motprua_screenshots/mot2char.png")


def test_motpr_3char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("їєа")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Текст має бути не менше 5 знаків")
    page.screenshot(path="motprua_screenshots/mot3char.png")


def test_motpr_4char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("їєаб")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Текст має бути не менше 5 знаків")
    page.screenshot(path="motprua_screenshots/mot4char.png")


def test_motpr_5char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("їєабв")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprua_screenshots/mot5char.png")


def test_motpr_6char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("їєабвг")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprua_screenshots/mot6char.png")


def test_motpr_20char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("йцукенгшщзфівапролдж")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprua_screenshots/mot20char.png")


def test_motpr_49char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("йцукенгшщзхїфівапролджєячсмитьбюйцукенгшфівапролд")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprua_screenshots/mot49char.png")


def test_motpr_50char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("йцукенгшщзхїфівапролджєячсмитьбюйцукенгшфівапролдз")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprua_screenshots/mot50char.png")


def test_motpr_51char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("йцукенгшщзхїфівапролджєячсмитьбюйцукенгшфівапролдзв")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Текст має бути не більше 50 знаків")
    page.screenshot(path="motprua_screenshots/mot51char.png")


def test_motpr_70char_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("йцукенгшщзхїфівапролджєячсмитьбюйцукенгшфівапролдзйцукенгшщзфівапролдж")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Текст має бути не більше 50 знаків")
    page.screenshot(path="motprua_screenshots/mot70char.png")


def test_motpr_symb1_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("С!-_().,<>&?@$=+{}#*/[\]")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprua_screenshots/motsymb1.png")


def test_motpr_symb2_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("С|?%^:;`₴’’””<>&?@$=+*\[/]?%;:")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprua_screenshots/motsymb2.png")


def test_motpr_num_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("числа 1234567890")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprua_screenshots/motnum.png")


def test_motpr_upcase_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("ТЕСТУВАННЯ")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprua_screenshots/motupcase.png")


def test_motpr_lowcase_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").type("тестування")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprua_screenshots/motlowcase.png")


@pytest.mark.parametrize("test_input", [
    ("Пръерплрт"),
    ("Орамыьтор"),
    ("апмЭтиор"),
    ("потлоЁьтбоа"),
    ("Тиитрэтьтор"),
    ("Иимпаётир")
])
def test_motpr_piletters_ua(page: Page, test_input) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").press("Control+A")
    page.get_by_placeholder("Ваша відповідь").press("Delete")
    page.get_by_placeholder("Ваша відповідь").type(test_input)
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Введіть коректний текст")


@pytest.mark.skip(reason="Rewrote the test using “@pytest.mark.parametrize”")
def test_motpr_piletterspr_ua(page: Page) -> None:
    page.goto("/")
    page.get_by_role("banner").get_by_role("link", name="Стажування").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Доєднатись до проєкту").first.click()
    page.get_by_placeholder("Ваша відповідь").press("Control+A")
    page.get_by_placeholder("Ваша відповідь").press("Delete")
    page.get_by_placeholder("Ваша відповідь").type("Пръерплрт")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Введіть коректний текст")
    page.screenshot(path="motprua_screenshots/mot1piletters.png")

    page.get_by_placeholder("Ваша відповідь").press("Control+A")
    page.get_by_placeholder("Ваша відповідь").press("Delete")
    page.get_by_placeholder("Ваша відповідь").type("Орамыьтор")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Введіть коректний текст")
    page.screenshot(path="motprua_screenshots/mot2piletters.png")

    page.get_by_placeholder("Ваша відповідь").press("Control+A")
    page.get_by_placeholder("Ваша відповідь").press("Delete")
    page.get_by_placeholder("Ваша відповідь").type("апмЭтиор")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Введіть коректний текст")
    page.screenshot(path="motprua_screenshots/mot3piletters.png")

    page.get_by_placeholder("Ваша відповідь").press("Control+A")
    page.get_by_placeholder("Ваша відповідь").press("Delete")
    page.get_by_placeholder("Ваша відповідь").type("потлоЁьтбоа")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Введіть коректний текст")
    page.screenshot(path="motprua_screenshots/mot4piletters.png")

    page.get_by_placeholder("Ваша відповідь").press("Control+A")
    page.get_by_placeholder("Ваша відповідь").press("Delete")
    page.get_by_placeholder("Ваша відповідь").type("Тиитрэтьтор")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class","InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Введіть коректний текст")
    page.screenshot(path="motprua_screenshots/mot5piletters.png")

    page.get_by_placeholder("Ваша відповідь").press("Control+A")
    page.get_by_placeholder("Ваша відповідь").press("Delete")
    page.get_by_placeholder("Ваша відповідь").type("Иимпаётир")
    page.locator("label").filter(has_text="На сайті Baza Trainee Ukraine").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Введіть коректний текст")
    page.screenshot(path="motprua_screenshots/mot6piletters.png")