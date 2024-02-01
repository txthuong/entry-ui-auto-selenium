from core import function_libs
from core.data_classes import Config
from pages.my_account_page.object import MyAccountPageObj


def test_entry(config: Config):
    config.log.info("Test my account page")
    my_page = MyAccountPageObj(config)
    my_page.open()
    my_page.select_my_account()

    account = function_libs.get_account_info()
    my_page.login(account.email, account.password)

    if not my_page.verify_login():
        my_page.register(account)
        my_page.verify_login()
        my_page.select_addresses()
        my_page.set_billing_address(account)
        my_page.select_addresses()
        my_page.set_shipping_address(account)
        my_page.logout()
        my_page.login(account.email, account.password)
        assert my_page.verify_login(), "Failed to login with registered account"

    my_page.select_addresses()
    billing_address = my_page.get_billing_address()
    assert account.address in billing_address, "Failed to view billing address."

    shipping_address = my_page.get_shipping_address()
    assert account.address in shipping_address, "Failed to view shipping address."
