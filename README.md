discord-keel-bridge converts webhooks sent by [Keel](https://keel.sh/) to Discord by rewriting the request.

The bridge will listen for POST request on the  `/v1/incoming` endpoint.

**This service is not meant to be publicly exposed**

You can deploy in Kubernetes:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: discord-keel-bridge
spec:
  selector:
    matchLabels:
      app: discord-keel-bridge
  replicas: 1
  template:
    metadata:
      labels:
        app: discord-keel-bridge
    spec:
      containers:
      - name: discord-keel-bridge
        image: gabisonfire/discord-keel-bridge:1.0
        env:
        - name: DISCORD_BRIDGE_URL
          value: https://discord.com/api/webhooks/123456
        - name: DISCORD_BRIDGE_PORT
          value: 5000
        ports:
        - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: discord-keel-bridge
spec:
  selector:
    app: discord-keel-bridge
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
```

or using docker-compose:
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

Or in with Kubernetes using the internal DNS `http://discord-keel-bridge.keel.svc.cluster.k8s:5000/v1/incoming` depending on your `keel` namespace.

**Note**: If you use the default `cluster.local` domain, Keel will fail to send the notification as Go's http module has issues with the  .local. Either use another domain or and ingress.
