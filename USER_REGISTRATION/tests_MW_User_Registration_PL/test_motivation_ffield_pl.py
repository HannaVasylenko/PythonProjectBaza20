import re
from playwright.sync_api import Page, expect


def test_motpr_empty_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").click()
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Podaj swoją motywację")


def test_motpr_space_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type(" ")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Podaj swoją motywację")


def test_motpr_1char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("ę")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst musi mieć co najmniej 10 znaków")


def test_motpr_2char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("óę")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst musi mieć co najmniej 10 znaków")


def test_motpr_5char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("óŁęża")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst musi mieć co najmniej 10 znaków")


def test_motpr_9char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("óŁężaóŁęż")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst musi mieć co najmniej 10 znaków")


def test_motpr_10char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("óŁężaóŁężd")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_11char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("óŁężaóŁężd")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class","InputField_input___Wj0m")


def test_motpr_20char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("ŚwiętoławRóżaWięcław")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_49char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukszęż")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_50char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszęż")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_51char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszęża")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst nie powinien przekraczać 50 znaków")


def test_motpr_70char_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklqqwertyuiopasdfghjklp")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(setup_pl.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst nie powinien przekraczać 50 znaków")


def test_motpr_symb1_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("s!-_().,<>&?@$=+{}#*/[\]")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_symb2_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("s|?%^:;`₴’’””<>&?@$=+*\[/]?%;:")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_num_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("num1234567890")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_upcase_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("ŚŁŻABCD")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")


def test_motpr_lowcase_pl(setup_pl: Page) -> None:
    setup_pl.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    setup_pl.get_by_role("button", name="Dołącz do projektu").first.click()
    setup_pl.get_by_placeholder("Twoja odpowiedź").type("ógłażejukaszęż")
    setup_pl.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(setup_pl.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
