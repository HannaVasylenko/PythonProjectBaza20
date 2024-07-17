import re
from playwright.sync_api import Page, expect


def test_motpr_empty_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").click()
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Podaj swoją motywację")
    page.screenshot(path="motprpl_screenshots/motempty.png")


def test_motpr_space_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type(" ")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Podaj swoją motywację")
    page.screenshot(path="motprpl_screenshots/motspace.png")


def test_motpr_1char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("ę")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst musi mieć co najmniej 5 znaków")
    page.screenshot(path="motprpl_screenshots/mot1char.png")


def test_motpr_2char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("óę")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst musi mieć co najmniej 5 znaków")
    page.screenshot(path="motprpl_screenshots/mot2char.png")


def test_motpr_3char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("łóę")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst musi mieć co najmniej 5 znaków")
    page.screenshot(path="motprpl_screenshots/mot3char.png")


def test_motpr_4char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("óŁęż")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst musi mieć co najmniej 5 znaków")
    page.screenshot(path="motprpl_screenshots/mot4char.png")


def test_motpr_5char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("łóŁęż")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprpl_screenshots/mot5char.png")


def test_motpr_6char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("łżóŁęż")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprpl_screenshots/mot6char.png")


def test_motpr_20char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("ŚwiętoławRóżaWięcław")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprpl_screenshots/mot20char.png")


def test_motpr_49char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukszęż")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprpl_screenshots/mot49char.png")


def test_motpr_50char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszęż")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprpl_screenshots/mot50char.png")


def test_motpr_51char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("ŚwiętosławRóżaWięcławBłażejChwalibógBłażejŁukaszęża")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst nie powinien przekraczać 50 znaków")
    page.screenshot(path="motprpl_screenshots/mot51char.png")


def test_motpr_70char_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("qwertyuiopasdfghjklqqawsedrftgqwertyuiopasdfghjklqqwertyuiopasdfghjklp")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m InputField__error__s2LFM")
    expect(page.locator("//label[@for='motivation']/../following-sibling::p")).to_have_text("Tekst nie powinien przekraczać 50 znaków")
    page.screenshot(path="motprpl_screenshots/mot70char.png")


def test_motpr_symb1_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("s!-_().,<>&?@$=+{}#*/[\]")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprpl_screenshots/motsymb1.png")


def test_motpr_symb2_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("s|?%^:;`₴’’””<>&?@$=+*\[/]?%;:")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprpl_screenshots/motsymb2.png")


def test_motpr_num_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("num1234567890")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprpl_screenshots/motnum.png")


def test_motpr_upcase_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("ŚŁŻABCD")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprpl_screenshots/motupcase.png")


def test_motpr_lowcase_pl(page: Page) -> None:
    page.goto("/")
    page.get_by_label("для зміни мови сторінки. вибрана мова").click()
    page.get_by_text("PL").click()
    page.get_by_role("banner").get_by_role("link", name="Praktyka").click()
    page.locator("//button[@class='CloseBtn_btn__ij9AH CookiesModal_close__tvIj3']").click()
    page.get_by_role("button", name="Dołącz do projektu").first.click()
    page.get_by_placeholder("Twoja odpowiedź").type("ógłażejukaszęż")
    page.locator("label").filter(has_text="Na stronie Bazy Trainee Ukraina").locator("use").click()
    expect(page.locator("//div[@class='RegistrationFormModal_wrapper__bgALB']//input[@id='motivation']")).to_have_attribute("class", "InputField_input___Wj0m")
    page.screenshot(path="motprpl_screenshots/motlowcase.png")