from starlette.testclient import TestClient

from app.main import app
client = TestClient(app)

def test_return_viva_real():
    response = client.get("/zap")
    assert response.json() == "Viva imóveis"

def test_return_zap():
    response = client.get("/zap")
    assert response.json() == "Zap imoveis"
