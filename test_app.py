import sqlite3
import unittest
from pathlib import Path

from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_page_opens(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Витрина топ-приложений", response.get_data(as_text=True))

    def test_database_has_50_apps(self):
        connection = sqlite3.connect(Path(__file__).parent / "apps.db")
        count = connection.execute("SELECT COUNT(*) FROM apps").fetchone()[0]
        connection.close()

        self.assertEqual(count, 50)

    def test_app_cards(self):
        response = self.client.get("/")
        page = response.get_data(as_text=True)

        self.assertEqual(page.count('class="card"'), 50)
        self.assertIn("МАКС", page)
        self.assertIn("Общение", page)
        self.assertIn("4,2", page)
        self.assertIn("https://www.rustore.ru/catalog/app/ru.oneme.app", page)


if __name__ == "__main__":
    unittest.main()
