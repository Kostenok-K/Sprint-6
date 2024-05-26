from selenium.webdriver.common.by import By


class OrderPageLocators:
    name_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    surname_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    underground_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    SELECT_underground = (By.XPATH, ".//*[@class='select-search__row']")
    PHONE_number_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, ".//*[text()='Далее']")
    date_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, ".//*[text()='* Срок аренды']")
    RENTAL_PERIOD_ONE_DAY = (By.XPATH, ".//*[text()='сутки']")
    SELECT_COLOR_GREY = (By.XPATH, "//input[@id='black']")
    comment_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    ORDER_STATUS = (By.XPATH, "//*[text()='Посмотреть статус']")
