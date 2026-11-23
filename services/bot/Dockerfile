FROM node:24.22.3-bookworm-slim

WORKDIR /app
COPY package.json package-lock.json ./
COPY services/bot/package.json services/bot/
RUN npm ci --workspace @giga-gosha/bot --omit=dev --no-audit --no-fund
COPY packages/runtime packages/runtime
COPY services/bot/src services/bot/src

USER node
CMD ["node", "services/bot/src/main.ts"]
