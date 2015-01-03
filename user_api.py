"""
A generic RESTful API to realize following functions:
v0.1:
* addUser(): Create new user
* credValid(): Validate user credential
* updatePassword(): Update password
* delUser(): Delete a user 
* getUserProfile(): Retrieve user information
* strToMD5(): Convert string to MD5
"""

import pymongo
import hashlib
import json

from dbconn import mongolab

"""
## #################### ##
## Initiate Environment ##
## #################### ##
"""
#mongo_client = pymongo.MongoClient(mongolab['uri'])
#user_col = mongo_client.facebook.api_dev_user


"""
## ################## ##
## Custom Functions   ##
## ################## ##
"""
def addUser():
	"""
	Add a new user 
	"""
	pass

def delUser():
	"""
	Delete user of a given username
	"""
	pass


def credValid(username, password, is_json_str = True):
	"""
	Validate the combination of username and password
	"""
	mongo_client = pymongo.MongoClient(mongolab['uri'])
	user_col = mongo_client.facebook.api_dev_user

	# process input info
	password_md5 = computeMD5hash(password)
	# get credential in database for given user
	try:
		true_password = user_col.find({"username":username})[0]['password']
	except:
		resp = {"status": "Failure", "ERROR_CODE": 100, "message": "the user profile could be not found!"}
	# close db connection
	mongo_client.close()

	# validate password
	try:
		resp
	except:
		if password_md5 == true_password:
			resp = {"status": "Success", "ERROR_CODE": 0, "message": "username and password match our records!"}
		else:
			resp = {"status": "Failure", "ERROR_CODE": 101, "message": "password provided does not match our recrod!"}

	if is_json_str:
		res = json.dumps(resp)
	else:
		res = resp

	return res

def getUserInfo(username, is_json_str = True):
	"""
	Retrun json object of user information
	"""
	mongo_client = pymongo.MongoClient(mongolab['uri'])
	user_col = mongo_client.facebook.api_dev_user

	resp = user_col.find({"username": username})[0]['profile']

	mongo_client.close()

	if is_json_str:
		res = json.dumps(resp)
	else:
		res = resp

	return res


def updatePassword():
	"""
	Update password of an account
	"""
	pass

def computeMD5hash(string):
	"""
	Encode string with MD5

	Parameter:
	----------
	string: {string} password string

	Return:
	-------
	res: {string} MD5-encoded string
	"""
	m = hashlib.md5()
	m.update(string.encode('utf-8'))
	return m.hexdigest()