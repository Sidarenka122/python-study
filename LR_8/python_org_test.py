import time
import unittest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class PythonOrgSearchClasswork(unittest.TestCase):
    def setUp(self):
        # запуск Chrome при начале каждого теста
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        # открытие в Chrome страницы http://www.python.org
        # selenium.open()
        # selenium.click()
        # selenium.getTitle()
        # selenium.type()
        # selenium.goBack()
        # selenium.close()
        driver.get("http://www.python.org")
        # проверка наличия слова Python в заголовке страницы
        self.assertIn("Python", driver.title)
        # ждем 5 секунд
        # time.sleep(5)
        # получение элемента страницы с именем q (строка поиска)
        # (откройте вручную в любом браузере сайт http://www.python.org,
        # нажмите правой кнопкой мыши по строке поиска,
        # выберите пункт "просмотреть код",
        # убедитесь, что у этого элемента name="q")
        input_elem = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.NAME, 'q')))
        # набор слова chupakabra в найденном элементе
        input_elem.send_keys("chupakabra")
        # нажатие кнопки Enter в найденном элементе
        input_elem.send_keys(Keys.RETURN)
        # проверка наличия строки "No results found."
        # на странице с результатами поиска
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='No results found.']")))
        # получение элемента страницы с именем q
        # на обновленной странице
        elem = driver.find_element(By.NAME, "q")
        # очищаем строку поиска
        elem.clear()
        # набор слова pycon в найденном элементе
        elem.send_keys("pycon")
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # проверка строки "No results found."
        # на странице с результатами поиска
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='No results found.']")))
        self.assertIn("No results found.", driver.page_source)

    def test_login_logout(self):
        driver = self.driver
        # открытие в Firefox страницы http://www.python.org/psf-landing/
        # на которой есть кнопка Sign In
        driver.get("https://www.python.org/psf-landing/")
        elem = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign In")))
        # поиск ссылки с текстом "Sign In"
        # elem = driver.find_element(By.LINK_TEXT, "Sign In")
        # нажатие на ссылку
        elem.click()
        # поиск текстового поля для ввода логина по XPath
        # (тег input с name='login')
        elem = driver.find_element(By.XPATH, "//input[@name='login']")
        # ввод логина
        elem.send_keys("Aliona_Sidarenka")
        # поиск текстового поля для ввода пароля по XPath
        # (тег input с name='password')
        elem = driver.find_element(By.XPATH, "//input[@name='password']")
        # ввод логина
        elem.send_keys("#iqF_y9cff6m5RY")
        # жмем ввод для отправки формы
        elem.send_keys(Keys.RETURN)
        # проверка наличия на странице строки "Your account"
        # после входа
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Your account']")))
        # self.assertIn("Your account", driver.page_source)
        # вывод кода страницы для отладки, потом можно будет убрать
        # print(driver.page_source)
        # поиск ссылки с текстом "Sign out"
        hover = ActionChains(driver).move_to_element(driver.find_element(By.LINK_TEXT, "Your account"))
        hover.perform()
        driver.find_element(By.LINK_TEXT, "Sign out").click()
        # нажатие на ссылку
        # driver.get("https://www.python.org/accounts/logout/")
        # поиск кнопки на форме в главной области страницы
        # по CSS-селектору
        elem = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.container section.main-content form button')))

        # elem = driver.find_element(By.CSS_SELECTOR,
        #                            'div.container section.main-content form button'
        #                           )
        # нажатие на кнопку
        elem.click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//p[@role='success']")))
        # проверка отсутствия на странице строки "Your account"
        # после выхода
        self.assertNotIn("Your account", driver.page_source)

    def test_about_breadcrumbs(self):
        driver = self.driver
        # открытие в Firefox страницы http://www.python.org
        driver.get("http://www.python.org")
        # получаем список ссылок в меню About по CSS-селектору
        elems = driver.find_elements(By.CSS_SELECTOR, '#about ul li a')
        # перебираем полученные подпункты меню,
        # выписываем названия и ссылки в отдельные списки
        # потому что при переходе по ссылкам на другие страницы
        # связь со списком подпунктов будет потеряна
        href_list = []
        name_list = []
        for e in elems:
            href_list.append(e.get_attribute("href"))
            name_list.append(e.get_attribute('innerHTML'))

        # перебираем полученные ссылки (кроме последней)
        for i in range(len(href_list) - 1):
            # переходим по ссылке
            driver.get(
                href_list[i]
            )
            # получаем строчку хлебных крошек
            elem = driver.find_element(By.CSS_SELECTOR, '.breadcrumbs')
            # проверка наличия в хлебных крошках ссылки на пункт About
            self.assertIn("About", elem.get_attribute('innerHTML'))
            # проверка наличия в хлебных крошках
            # наличия названия текущего пункта
            self.assertIn(
                # название текущего пункта
                name_list[i],
                # строчка хлебных крошек
                elem.get_attribute('innerHTML')
            )

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()

class PageHelper:
    @classmethod
    def wait_for_element_to_present(cls, driver, selector):
        return WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, selector)))

    @classmethod
    def wait_for_element_to_be_interactable(cls, driver, selector):
        return WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, selector)))


class PythonOrgSearchHomework(unittest.TestCase):
    def setUp(self):
        # запуск Chrome при начале каждого теста
        self.driver = webdriver.Chrome()

    def test_download_nav_item_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        # wait until Main nav is loaded
        PageHelper.wait_for_element_to_present(self.driver, "//ul[@aria-label='Main Navigation']")
        # hover over Downloads menu item
        hover = ActionChains(driver).move_to_element(driver.find_element(By.LINK_TEXT, "Downloads"))
        hover.perform()

        # should display downloads child items
        self.assertTrue(driver.find_element(By.XPATH, "//ul[@role='menu']//a[normalize-space()='All releases']")
                        .is_displayed())

        self.assertTrue(
            driver.find_element(By.LINK_TEXT, "Source code").is_displayed())
        self.assertTrue(
            driver.find_element(By.CSS_SELECTOR, "li[id='downloads'] li:nth-child(2) a:nth-child(1)").is_displayed())
        self.assertTrue(
            driver.find_element(By.XPATH, "//ul[@role='menu']//a[normalize-space()='macOS']").is_displayed())
        self.assertTrue(
            driver.find_element(By.LINK_TEXT, "Other Platforms").is_displayed())
        self.assertTrue(
            driver.find_element(By.LINK_TEXT, "License").is_displayed())
        self.assertTrue(
            driver.find_element(By.LINK_TEXT, "Alternative Implementations").is_displayed())

    def test_download_page(self):
        driver = self.driver
        # открытие в Chrome страницы http://www.python.org/downloads
        driver.get("http://www.python.org/downloads")

        # wait until Main nav is loaded
        PageHelper.wait_for_element_to_present(self.driver, "//ul[@aria-label='Main Navigation']")

        # should display h1 with download CTA
        h1 = driver.find_element(By.CSS_SELECTOR, 'h1.call-to-action')
        self.assertIn("Download the latest version", h1.get_attribute('innerHTML'))

        # should display active python releases
        h2 = driver.find_element(By.CSS_SELECTOR, '.active-release-list-widget h2')
        self.assertIn("Active Python Releases", h2.get_attribute('innerHTML'))

    def test_socialize_button(self):
        driver = self.driver
        # открытие в Chrome страницы http://www.python.org
        driver.get("http://www.python.org")

        # wait until Main nav is loaded
        PageHelper.wait_for_element_to_present(self.driver, "//ul[@aria-label='Main Navigation']")

        # should display Socialize button
        hover = ActionChains(driver).move_to_element(driver.find_element(By.LINK_TEXT, "Socialize"))

        # doesn't show facebook button by default
        self.assertFalse(driver.find_element(By.CSS_SELECTOR, '.icon-facebook').is_displayed())
        hover.perform()
        facebook = driver.find_element(By.CSS_SELECTOR, '.icon-facebook')

        # should show facebook button on socialize hover
        self.assertTrue(facebook.is_displayed())

        facebook.click()
        self.assertEqual(driver.current_url, 'https://www.facebook.com/pythonlang?fref=ts')

    def test_jobs_page(self):
        driver = self.driver
        # открытие в Chrome страницы http://www.python.org/jobs
        driver.get("http://www.python.org/jobs")

        # wait until Main nav is loaded
        PageHelper.wait_for_element_to_present(self.driver, "//ul[@aria-label='Main Navigation']")

        for x in ['Types', 'Categories', 'Locations']:
            button = driver.find_element(By.LINK_TEXT, x)
            # click on menu item
            button.click()

            # expect redirect to appropriate page
            self.assertEqual(driver.current_url, f'https://www.python.org/jobs/{x.lower()}/')

    def test_console_main_page(self):
        driver = self.driver
        # открытие в Chrome страницы http://www.python.org
        driver.get("http://www.python.org")

        # wait for start shell button
        shell_start = PageHelper.wait_for_element_to_be_interactable(self.driver, "//a[@id='start-shell']")

        # expect terminal not to be displayed by default
        with self.assertRaises(NoSuchElementException):
            driver.find_element(By.CSS_SELECTOR, "#dive-into-python iframe")

        shell_start.click()

        iframe = PageHelper.wait_for_element_to_present(self.driver, "//div[@id='dive-into-python']/iframe")

        # expect terminal to be displayed
        self.assertTrue(
            driver.find_element(By.CSS_SELECTOR, "#dive-into-python iframe").is_displayed())
        driver.switch_to.frame(iframe)

        # go deep into iframes hierarchy
        iframe2 = PageHelper.wait_for_element_to_present(self.driver, "//iframe[@id='id_console']")
        driver.switch_to.frame(iframe2)

        iframe3 = PageHelper.wait_for_element_to_present(self.driver, "//iframe")
        driver.switch_to.frame(iframe3)

        # wait for console loaded
        PageHelper.wait_for_element_to_present(self.driver, '//x-row[contains(text(), ">>>")]')

        # enter some values to check python interpreter loaded and works
        x_screen = driver.find_element(By.CSS_SELECTOR, 'x-screen')
        x_screen.send_keys('print("Hello selenium" + " " + str(2+3))')
        x_screen.send_keys(Keys.RETURN)

        # expect result is calculated
        PageHelper.wait_for_element_to_present(self.driver, '//x-row[contains(text(), "Hello selenium 5")]')
        self.assertIn("Hello selenium 5", driver.page_source)

        # switch back from iframes context to default doc context
        driver.switch_to.default_content()

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
