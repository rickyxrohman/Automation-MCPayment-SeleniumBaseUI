from seleniumbase import BaseCase


class ParabankRegisterTests(BaseCase):
    def test_register_and_login_to_parabank(self):
        self.open("https://parabank.parasoft.com/parabank/register.htm")
        self.type('[name="customer.firstName"]', "Ricky")
        self.type('[name="customer.lastName"]', "Rohman")
        self.type('[name="customer.address.street"]', "Jalan Burung")
        self.type('[name="customer.address.city"]', "Jakarta")
        self.type('[name="customer.address.state"]', "Jakarta Selatan")
        self.type('[name="customer.address.zipCode"]', "15431")
        self.type('[name="customer.phoneNumber"]', "0895331112")
        self.type('[name="customer.ssn"]', "121212")
        self.type('[name="customer.username"]', "rickyrohman")
        self.type('[name="customer.password"]', "qwerty123")
        self.type('[name="repeatedPassword"]', "qwerty123")
        self.click('input[value="Register"]')
