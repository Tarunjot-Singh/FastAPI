import unittest
from starlette.testclient import TestClient
from main import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    # Unit tests for POST /csv route
    def test_upload_valid_file_no_equals(self):
        # Uploading a valid file and no "equals" value returns a successful response
        with open("test.csv", "rb") as file:
            response = self.client.post("/csv", files={"file": file})
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertTrue(len(data) > 0)

    def test_upload_valid_file_with_equals(self):
        # Uploading a valid file and an "equals" value of 1 returns only rows where the "Value" column equals 1
        with open("test.csv", "rb") as file:
            response = self.client.post("/csv?equals=1", files={"file": file})
            self.assertEqual(response.status_code, 200)
            data = response.json()
            self.assertTrue(all(row["Value"] == 1 for row in data))

    def test_upload_invalid_file_additional_columns(self):
        # Uploading a csv file with additional columns fails validation
        with open("test_invalid_columns.csv", "rb") as file:
            response = self.client.post("/csv", files={"file": file})
            self.assertEqual(response.status_code, 400)

    def test_upload_invalid_file_missing_response_value(self):
        # Uploading a csv file with a missing "Response" value fails validation
        with open("test_missing_response.csv", "rb") as file:
            response = self.client.post("/csv", files={"file": file})
            self.assertEqual(response.status_code, 400)

    # Unit tests for GET /embedding route
    def test_embedding_valid_text(self):
        # A request with the "text" value "It's great" returns a successful response
        response = self.client.get("/embedding?text=It's great")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("embedding", data)

    def test_embedding_invalid_text(self):
        # A request with the "text" value "no" fails validation
        response = self.client.get("/embedding?text=no")
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()