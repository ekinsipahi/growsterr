from django.test import TestCase, override_settings


class CoreTests(TestCase):
    def test_health_check_answers_any_host(self):
        response = self.client.get("/healthz", HTTP_HOST="10.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"ok")

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        for platform in ("Instagram", "TikTok", "YouTube"):
            self.assertContains(response, platform)

    @override_settings(ALLOWED_HOSTS=["growsterr.com", "www.growsterr.com"], SITE_URL="https://growsterr.com")
    def test_www_redirects_to_the_canonical_host(self):
        response = self.client.get("/?a=1", HTTP_HOST="www.growsterr.com")
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response["Location"], "https://growsterr.com/?a=1")

    def test_robots_and_favicon(self):
        self.assertContains(self.client.get("/robots.txt"), "Disallow: /admin/")
        self.assertEqual(self.client.get("/favicon.ico").status_code, 301)
