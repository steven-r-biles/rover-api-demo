import json

from django.test import TestCase

class MissionTests(TestCase):
    def setUp(self):
        self.mission_data = {"name": "test", "commands": ["forward 10", "right 90"]}
        self.data = json.dumps(self.mission_data)

    def test_get_missions(self):
        response = self.client.get('/mission/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'missions': []})
    
    def test_create_mission(self):
        response = self.client.post('/mission/', data=self.data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'status': 'accepted', 'data': {'id': 1, 'accepted': True, **self.mission_data}})

    def test_update_mission(self):
        response = self.client.post('/mission/', data=self.data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'status': 'accepted', 'data': {'id': 1, 'accepted': True, **self.mission_data}})
        self.mission_data["name"] = "test2"
        response = self.client.post('/mission/1/', data=json.dumps(self.mission_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'status': 'accepted', 'data': {'id': 1, 'accepted': True, **self.mission_data}})
    
    def test_delete_mission(self):
        response = self.client.post('/mission/', data=self.data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'status': 'accepted', 'data': {'id': 1, 'accepted': True, **self.mission_data}})
        response = self.client.delete('/mission/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'deleted'})
