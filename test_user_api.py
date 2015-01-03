import unittest
from user_api import *

class UserAPI(unittest.TestCase):

	def setUp(self):
		pass

	def test_md5(self):
		# '8233156'
		test_resp = computeMD5hash('helloworld')
		true_resp = 'fc5e038d38a57032085441e7fe7010b0'
		self.assertEqual(test_resp, true_resp)

	def test_getUserInfo(self):
		test_resp = getUserInfo("test")
		true_resp = '{"ln": "test", "dob": "2015/01/03", "fn": "01", "gender": "m"}'
		self.assertEqual(test_resp, true_resp)

	def test_credValid_test_success(self):
		test_resp = credValid("test", "123456", False)["ERROR_CODE"]
		true_resp = 0
		self.assertEqual(test_resp, true_resp)

	def test_credValid_test_failure(self):
		test_resp = credValid("test", "wrongpassword", False)["ERROR_CODE"]
		true_resp = 101
		self.assertEqual(test_resp, true_resp)

	def test_credValid_wrongtest_failure(self):
		test_resp = credValid("wrongtest", "wrongpassword", False)["ERROR_CODE"]
		true_resp = 100
		self.assertEqual(test_resp, true_resp)


if __name__ == "__main__":
	unittest.main()