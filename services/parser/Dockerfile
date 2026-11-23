FROM node:24.22.3-bookworm-slim

WORKDIR /app
COPY package.json package-lock.json ./
COPY services/parser/package.json services/parser/
RUN npm ci --workspace @giga-gosha/parser --omit=dev --no-audit --no-fund
COPY packages/runtime packages/runtime
COPY services/parser/src services/parser/src

USER node
CMD ["node", "services/parser/src/main.ts"]
