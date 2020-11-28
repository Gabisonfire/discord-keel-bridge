discord-keel-bridge converts webhooks sent by [Keel](https://keel.sh/) to Discord by rewriting the request.

The bridge will listen for POST request on the  `/v1/incoming` endpoint.

**This service is not meant to be publicly exposed**

You can make it run quickly using docker-compose:
```yaml
version: '3.5'
services:
  discord-keel-bridge:
    image: gabisonfire/discord-keel-bridge:1.0
    environment:
      - DISCORD_BRIDGE_URL="https://discord.com/api/webhooks/123456789"
      - DISCORD_BRIDGE_PORT=5000
    ports:
      - 5000:5000
    container_name: discord-keel-bridge
    restart: unless-stopped
```
Make sure to replace `DISCORD_BRIDGE_URL` with yours.
See [Discord documentation](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) on webhooks.

Now give Keel your bridge url, ex: `your.docker.server:5000/v1/incoming`