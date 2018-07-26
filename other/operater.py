#coding=utf-8


import requests,json,unittest,time

class ToDoList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'http://www.imsam.cn:3000'

    @classmethod
    def tearDownClass(cls):
        pass

    def test_username_resigter(self):
        r = requests.post(url=self.url + '/register',json={'username':'admin123','password':'admin123',
                                                           'password_confirmation':'admin123'})
        self.assertEqual(r.json()['username'],'admin123')
        self.assertEqual(r.status_code,200)

    def test_login(self):
        r = requests.post(url=self.url + '/login',json={'username':'admin123','password':'admin123',
                                                        'password_confirmation':'admin123'})
        self.assertEqual(r.json()['username'],'admin123')
        self.assertEqual(r.status_code,200)

    def get_token(self):
        '''获取token'''
        r = requests.post(url=self.url + '/login',json={'username':'admin123',
                                                        'password':'admin123','password_confirmation':'admin123'})
        return r.json()['token']

    def test_get_api_task(self):
        '''获取任务api'''
        r = requests.get(url=self.url + '/api/tasks',headers={'Authorization':'Bearer ' + self.get_token()})
        self.assertEqual(r.status_code,200)

    def test_create_tasks(self):
        '''创建任务api'''
        r = requests.post(url=self.url + '/api/tasks',json={'title':123123,'desc':123123},
                          headers={'Authorization':'Bearer ' + self.get_token()})
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['title'],123123)

    def getTaskid(self):
        '''创建任务api'''
        r = requests.post(url=self.url + '/api/tasks',json={'title':123123,'desc':123123},
                          headers={'Authorization':'Bearer ' + self.get_token()})
        return r.json()['id']

    def test_delete_tasks(self):
        '''删除任务api'''
        r = requests.delete(url=self.url + '/api/tasks/:{0}'.format(self.getTaskid()),headers={'Authorization':'Bearer ' + self.get_token()})
        self.assertEqual(r.status_code,200)


    def test_put_tasks(self):
        '''完成任务api'''
        r = requests.put(url=self.url + '/api/tasks/{0}'.format(self.getTaskid()),headers={'Authorization': 'Bearer ' + self.get_token()})
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['title'],str(123123))


if __name__ == '__main__':
    unittest.main(verbosity=2)