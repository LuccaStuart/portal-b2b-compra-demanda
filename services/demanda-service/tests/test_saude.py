from fastapi.testclient import TestClient
from demanda.main import app


def test_saude():
    r = TestClient(app).get("/saude")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
