# T³AI

Tweed Tyne Technologies' self-hosted AI workspace: Open WebUI with T³AI
branding, deployed on Railway (project **A.I. Web**, service **open-webui**).

## What this repo changes

| Change | Where |
|---|---|
| App name `T³AI` (no " (Open WebUI)" suffix) | `ENV WEBUI_NAME` and a patch to `env.py` in the `Dockerfile` |
| Favicons (`.png`, `.svg`, `.ico`, 96px) | `branding/` |
| iOS home screen icon | `branding/apple-touch-icon.png` |
| Installed app (PWA) icons and manifest name | `branding/web-app-manifest-*.png`, `branding/logo.png`, `site.webmanifest` patch |
| Loading splash (light and dark) | `branding/splash.png`, `branding/splash-dark.png` |
| Page title before the app loads | `<title>` patch in the `Dockerfile` |

Everything else is the official image, unchanged.

## Licence condition

Open WebUI permits removing its branding only for deployments with **50 or
fewer users in any 30-day period** (https://docs.openwebui.com/license). If
this instance ever grows beyond that, restore the Open WebUI branding or get
an enterprise licence.

## Data and settings

All chats, users, models, tool servers and admin settings live in the
Railway volume mounted at `/app/backend/data`, not in the image. Rebuilding or
switching to this repo keeps them.

## Upgrading Open WebUI

The `FROM` line follows `:main`, matching what ran before. Railway may reuse a
cached base layer, so to pull a newer Open WebUI, change the tag to a release
(for example `v0.9.6`) and push. Never move to an older version than the one
running. If an upgrade changes the name logic, the build fails at the `grep`
step on purpose; update the `sed` line to match.

## Changing the icon

`tools/source-icon.svg` is the master artwork. `tools/generate_icons.py`
redraws every size (needs `pip install cairosvg pillow`); copy the files from
its `out/` folder into `branding/` and push.
