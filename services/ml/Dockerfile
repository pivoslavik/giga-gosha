FROM node:24.22.3-bookworm-slim

WORKDIR /app
COPY package.json package-lock.json ./
COPY services/ml/package.json services/ml/
RUN npm ci --workspace @giga-gosha/ml --omit=dev --no-audit --no-fund
COPY packages/runtime packages/runtime
COPY services/ml/src services/ml/src

USER node
CMD ["node", "services/ml/src/main.ts"]
