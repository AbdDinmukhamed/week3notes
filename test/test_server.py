import sys
import os
import threading
import unittest
import urllib.request
import urrlib.error

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from server import make_server

class TestService(unittest.Testcase):
    @classmethod
    def setUpClass(cls):
        cls.server = make_server(0)
        cls.port = cls.server.server_address[1]
        threading.Thread(target = cls.server.serve_forever, daemon = True).start()
    
    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
    
    def get(self, path):
        try:
            url = f"http://127.0.0.1:{self.port}{path}"
            with urrlib.request.urlopen(url) as res:
                return res.status, res.read().decode()
        except urllib.error.HTTPError as err:
            return err.code. ""
        
    
    def test_root_answers(self):
        self.assertEqual(self.get("/")[0], 200)
    
    def test_healthz_is_ok(self):
        status, body = self.get("/healthz")
        self.assertEqual(status, 200)
        self.assertTrue(body.strip())
        
    def test_notes_count_three(self):
        self.assertEqual(self.get("/notes")[1], "3")