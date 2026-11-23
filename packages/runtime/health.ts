import { createServer } from "node:http";

export function startHealthServer(service: string): void {
  const server = createServer((request, response) => {
    if (request.method !== "GET" || request.url !== "/health") {
      response.writeHead(404).end();
      return;
    }

    response.writeHead(200, { "content-type": "application/json" });
    response.end(JSON.stringify({ service, status: "ok" }));
  });

  server.listen(8080, () => console.info(`${service} listening on port 8080`));
  process.once("SIGTERM", () => server.close());
  process.once("SIGINT", () => server.close());
}
