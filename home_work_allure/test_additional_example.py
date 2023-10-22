import allure


@allure.feature('Always passed')
def test_successful():
    assert True
