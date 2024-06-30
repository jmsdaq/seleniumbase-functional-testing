from seleniumbase import BaseCase

class LoginPage(BaseCase):

    def login(self):
        # Open the login page
        self.open("https://review.onprem-cloud.nweca.com")
        self.maximize_window()
        self.type("input[type='username']", "intern_james")
        self.type("input[type='password']", "intern_james")
        self.click('input[type="submit"]')
