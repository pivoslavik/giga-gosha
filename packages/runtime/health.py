import json
import signal
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote


def health_server(service: str, address: tuple[str, int]) -> HTTPServer:
    payload = json.dumps({"service": service, "status": "ok"}).encode()

    class HealthHandler(BaseHTTPRequestHandler):
        def parse_request(self) -> bool:
            if not super().parse_request():
                return False
            if (
                self.command == "GET"
                and unquote(self.path.removesuffix("?")) == "/health"
            ):
                return True
            self.send_response(404)
            self.end_headers()
            return False

        def do_GET(self) -> None:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

    return HTTPServer(address, HealthHandler)


def serve_health(service: str) -> None:
    signal.signal(signal.SIGTERM, signal.default_int_handler)
    with health_server(service, ("", 8080)) as server:
        print(f"{service} listening on port 8080", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
