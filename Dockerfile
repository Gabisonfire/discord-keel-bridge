FROM python:3.8-alpine
ENV DISCORD_BRIDGE_URL="https://discord.com/api/webhooks/123456789"
ENV DISCORD_BRIDGE_PORT=5000

RUN apk add gcc musl-dev libffi-dev make && \
    pip install flask gevent requests && \
    apk del gcc musl-dev libffi-dev make
COPY discord_keel_bridge.py discord_keel_bridge.py
CMD ["python", "-u", "discord_keel_bridge.py"]