import unittest
import os
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    app=os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "MyObservatory.apk"),
    # appPackage="hko.MyObservatory_v1_0",
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def go_to_main_page(self):
        time.sleep(1)
        el = self.driver.find_element(
            by=AppiumBy.ID, value='hko.MyObservatory_v1_0:id/btn_agree')
        el.click()
        time.sleep(1)
        el.click()

        time.sleep(1)
        el = self.driver.find_element(
            by=AppiumBy.ID, value='android:id/button1')
        el.click()

        time.sleep(1)
        el = self.driver.find_element(
            by=AppiumBy.ID, value='com.android.packageinstaller:id/permission_allow_button')
        el.click()

        time.sleep(10)
        el = self.driver.find_element(
            by=AppiumBy.ID, value='hko.MyObservatory_v1_0:id/exit_btn')
        el.click()
        time.sleep(1)
        el = self.driver.find_element(
            by=AppiumBy.ID, value='hko.MyObservatory_v1_0:id/exit_btn')
        el.click()

        time.sleep(1)
        el = self.driver.find_element(
            by=AppiumBy.ID, value='hko.MyObservatory_v1_0:id/exit_btn')
        el.click()

        time.sleep(1)
        el = self.driver.find_element(
            by=AppiumBy.ID, value='android:id/button1')
        el.click()

    def go_to_forecast_page(self):
        time.sleep(1)
        el = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="‎‏‎‎‎‎‎‏‎‏‏‏‎‎‎‎‎‎‏‎‎‏‎‎‎‎‏‏‏‏‏‏‏‏‏‏‎‏‎‎‎‏‏‎‏‎‎‎‏‏‎‎‎‏‏‏‏‎‏‎‎‎‎‏‏‎‏‏‎‏‎‎‏‎‎‏‎‎‎‎‎‎‏‎‏‎‎‎‎‏‏‏‎‎‎‎‎Navigate up‎‏‎‎‏‎")
        el.click()

        time.sleep(1)
        el = self.driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Forecast & Warning Services\")")
        el.click()

        time.sleep(1)
        el = self.driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"9-Day Forecast\").instance(1)")
        el.click()

        # time.sleep(1)
        # el = self.driver.find_element(
        #     by=AppiumBy.ACCESSIBILITY_ID, value="Refresh")
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(
                    (By.ACCESSIBILITY_ID, 'Refresh'))
            )
            print("refresh btn is present")
        except TimeoutException:
            print("refresh btn is not present")
            self.driver.quit()

    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        self.go_to_main_page()
        self.go_to_forecast_page()

    def tearDown(self) -> None:
        if self.driver:
            print("will quit")
            time.sleep(10)
            self.driver.quit()

    def test_9th_days_weather(self) -> None:
        # 向下滚动 5 次
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        for i in range(5):
            time.sleep(1)
            actions.w3c_actions.pointer_action.move_to_location(256, 2285)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(1)
            actions.w3c_actions.pointer_action.move_to_location(256, 1142)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

        time.sleep(1)
        elements = self.driver.find_elements(
            by=AppiumBy.ID, value="hko.MyObservatory_v1_0:id/sevenday_forecast_date")
        el = elements[-1]
        print("日期是", el.get_attribute("text"))
        elements = self.driver.find_elements(
            by=AppiumBy.ID, value="hko.MyObservatory_v1_0:id/sevenday_forecast_day_of_week")
        el = elements[-1]
        print("星期是", el.get_attribute("text"))
        elements = self.driver.find_elements(
            by=AppiumBy.ID, value="hko.MyObservatory_v1_0:id/sevenday_forecast_temp")
        el = elements[-1]
        print("温度是", el.get_attribute("text"))
        elements = self.driver.find_elements(
            by=AppiumBy.ID, value="hko.MyObservatory_v1_0:id/sevenday_forecast_rh")
        el = elements[-1]
        print("湿度是", el.get_attribute("text"))
        elements = self.driver.find_elements(
            by=AppiumBy.ID, value="hko.MyObservatory_v1_0:id/psrText")
        el = elements[-1]
        print("下雨概率是", el.get_attribute("text"))
        elements = self.driver.find_elements(
            by=AppiumBy.ID, value="hko.MyObservatory_v1_0:id/sevenday_forecast_wind")
        el = elements[-1]
        print("风力描述是", el.get_attribute("text"))
        elements = self.driver.find_elements(
            by=AppiumBy.ID, value="hko.MyObservatory_v1_0:id/sevenday_forecast_details")
        el = elements[-1]
        print("天气详情是", el.get_attribute("text"))


if __name__ == '__main__':
    unittest.main()
