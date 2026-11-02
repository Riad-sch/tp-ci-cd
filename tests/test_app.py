from app import app


def test_health():
    with app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.get_json() == {"status": "ok"}


def test_tickets():
    with app.test_client() as client:
        response = client.get("/tickets")
        assert response.status_code == 200

        tickets = response.get_json()
        assert isinstance(tickets, list)
        assert len(tickets) == 2
        assert tickets[0]["titre"] == "Probleme de connexion Wi-Fi"


def test_route_inconnue():
    with app.test_client() as client:
        response = client.get("/route-inexistante")
        assert response.status_code == 404