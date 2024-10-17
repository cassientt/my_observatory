import unittest
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    app="/Users/nietingting/Developer/my_observatory/test/ui_test/MyObservatory.apk",
    # appPackage="hko.MyObservatory_v1_0",
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            print("will quit")
            time.sleep(10)
            self.driver.quit()

    def test_find_battery(self) -> None:
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

        actions = ActionChains(self.driver)
        # override as 'touch' pointer action
        actions.w3c_actions = ActionBuilder(
            self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        for i in range(5):
            time.sleep(3)
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
