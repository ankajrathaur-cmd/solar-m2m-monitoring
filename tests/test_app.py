from server.app import app


def test_home_page(monkeypatch):

    class FakeCursor:
        def execute(self, query):
            pass

        def fetchall(self):
            return []

    class FakeConnection:
        def cursor(self):
            return FakeCursor()

        def close(self):
            pass

    monkeypatch.setattr(
        "server.app.sqlite3.connect",
        lambda *args, **kwargs: FakeConnection()
    )

    app.config["TESTING"] = True

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
