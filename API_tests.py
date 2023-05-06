

import unittest
import requests


class ApiTests(unittest.TestCase):
    # Set the base URL for the API
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    def setUp(self):
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

    def test_api_status(self):
        with self.session.get(self.BASE_URL) as response:
            self.assertEqual(response.status_code, 200)

    def test_get_posts(self):
        with self.session.get(self.BASE_URL + '/posts') as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json()), 100)

    def test_create_post(self):
        post_data = {'title': 'Test Post', 'body': 'This is a test post.'}
        with self.session.post(self.BASE_URL + '/posts', json=post_data) as response:
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json()['title'], post_data['title'])
            self.assertEqual(response.json()['body'], post_data['body'])

    def test_update_post(self):
        post_id = 1
        updated_data = {'title': 'Updated Post', 'body': 'This post has been updated.'}
        with self.session.put(self.BASE_URL + '/posts/{}'.format(post_id), json=updated_data) as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['title'], updated_data['title'])
            self.assertEqual(response.json()['body'], updated_data['body'])

    def test_delete_post(self):
        post_id = 1
        with self.session.delete(self.BASE_URL + '/posts/{}'.format(post_id)) as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {})

    def test_get_specific_post(self):
        post_id = 2
        with self.session.get(self.BASE_URL + '/posts/{}'.format(post_id)) as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['id'], post_id)

    def test_get_comments(self):
        with self.session.get(self.BASE_URL + '/comments') as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json()), 500)

    def test_get_specific_comment(self):
        comment_id = 2
        with self.session.get(self.BASE_URL + '/comments/{}'.format(comment_id)) as response:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['id'], comment_id)

    def test_create_comment(self):
        comment_data = {'postId': 1, 'name': 'Test Comment', 'email': 'test@test.com', 'body': 'This is a test comment.'}
        with self.session.post(self.BASE_URL + '/comments', json=comment_data) as response:
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json()['name'], comment_data['name'])
            self.assertEqual(response.json()['email'], comment_data['email'])
            self.assertEqual(response.json()['body'], comment_data['body'])

    def test_update_comment(self):
        comment_id = 1
        updated_data = {'name': 'Updated Comment', 'email': 'updated@test.com'}
        with self.session.put(self.BASE_URL + '/comments/{}'.format(comment_id), json=updated_data) as response:
            self.assertEqual(response.status_code, 200)
