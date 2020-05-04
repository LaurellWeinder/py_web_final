

class BaseViewTestCase(object):

    def setUpTestData(cls):
        cls.view = None
        cls.url_name = None
        cls.template_name = None


    def test_status_code(self):
        response = self.client.get(self.view)
        self.assertEqual(response.status_code, 200)

    def test_correct_url(self):
        response = self.client.get(reverse(self.url_name))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse(self.url_name))
        self.assertTemplateUsed(response, self.template_name)