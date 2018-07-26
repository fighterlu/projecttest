# coding=utf-8

import unittest, requests,time,uuid
from other import read_json


class  Test_Api(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.api_url = 'http://www.imsam.cn:3000'
		cls.data = {'username':'username',
		             'password':'password','password_confirmation':'password'}
		cls.title = {'title':str(uuid.uuid4()),'desc':str(uuid.uuid4())}

	@classmethod
	def tearDownClass(cls):
		time.sleep(1)

	def test_register(self):
		r = requests.post(url=self.api_url + '/register',
		                  data=self.data)
		self.assertEqual(self.data.get('username'), read_json.loads(r.text)['username'])
		self.assertEqual(200,r.status_code)

	def getToken(self):
		r = requests.post(
			url  = self.api_url + '/login',data = self.data)
		return  'Bearer ' + r.json()['token']

	def test_getallTasks(self):
		r = requests.get(url=self.api_url + '/api/tasks',
		                  headers={'Authorization':self.getToken()})
		self.assertEqual(200,r.status_code)

	def test_createTasks(self):
		r = requests.post(
			url=self.api_url + '/api/tasks',
			headers={'Authorization':self.getToken()},data=self.title)
		self.assertEqual(200,r.status_code)

	def createTasks(self):
		r = requests.post(
			url=self.api_url + '/api/tasks',
			headers={'Authorization':self.getToken()},data=self.title)
		return read_json.loads(r.text)['id']

	def test_deltetasks(self):
		r = requests.delete(
			url=self.api_url + '/api/tasks/:' + str(self.createTasks()),
			headers={'Authorization': self.getToken()})
		self.assertEqual(200,r.status_code)

	def test_pullTasks(self):
		r = requests.put(
			url=self.api_url + '/api/tasks/' + str(self.createTasks()),
			headers={'Authorization':self.getToken()})
		self.assertEqual(200,r.status_code)

if __name__ == '__main__':
    unittest.main(verbosity=3)
