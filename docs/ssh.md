## Install cloudflared

Follow instructions at https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/downloads/

## Modify ssh config

Add the following to your ssh config:

MacOS:
```
Host chaoi.thomaschan.dev
  User thomaschan
  ProxyCommand /opt/homebrew/bin/cloudflared access ssh --hostname %h
```

Linux:
```
Host chaoi.thomaschan.dev
  User thomaschan
  ProxyCommand /usr/local/bin/cloudflared access ssh --hostname %h
```

## Connect

```
ssh chaoi.thomaschan.dev
```