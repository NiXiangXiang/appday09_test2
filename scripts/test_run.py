import allure


class Test:
    @allure.step(title="这是用来表示测试步骤名称")
    def test01(self):
        print("test01")
        assert True