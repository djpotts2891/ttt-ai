# T³AI: Open WebUI with Tweed Tyne Technologies branding.
# Rebranding is permitted for deployments of 50 or fewer users in a 30-day
# period (https://docs.openwebui.com/license). Keep it that way, or the
# Open WebUI branding must be restored.

# Matches the image the Railway service ran before this repo. Pin to a release
# tag (e.g. v0.9.6) once you want controlled upgrades; never go to an OLDER
# version than the one running, as the database may already be migrated.
FROM ghcr.io/open-webui/open-webui:main

ENV WEBUI_NAME="T³AI"

COPY branding/ /tmp/branding/

RUN set -eu; \
    # 1. Icons, favicons, splash and logo. /app/build/static is the source the
    #    backend copies into its own static folder on every start, so both are
    #    replaced to cover either path.
    for f in /tmp/branding/*; do \
      cp "$f" /app/build/static/; \
      cp "$f" /app/backend/open_webui/static/; \
    done; \
    rm -rf /tmp/branding; \
    # 2. Stop " (Open WebUI)" being appended to WEBUI_NAME. Fails the build if
    #    an upgrade changes this line, so it never silently stops working.
    ENV_PY=/app/backend/open_webui/env.py; \
    grep -q "WEBUI_NAME += ' (Open WebUI)'" "$ENV_PY"; \
    sed -i "s/WEBUI_NAME += ' (Open WebUI)'/pass/" "$ENV_PY"; \
    # 3. Page title shown before the app loads, and the static web manifest.
    find /app/build -name '*.html' -exec sed -i 's#<title>Open WebUI</title>#<title>T³AI</title>#' {} +; \
    for m in /app/build/static/site.webmanifest /app/backend/open_webui/static/site.webmanifest; do \
      if [ -f "$m" ]; then sed -i \
        -e 's#"name": "Open WebUI"#"name": "T³AI"#' \
        -e 's#"short_name": "WebUI"#"short_name": "T³AI"#' \
        -e 's#"theme_color": "\#ffffff"#"theme_color": "\#0D1220"#' \
        -e 's#"background_color": "\#ffffff"#"background_color": "\#0D1220"#' "$m"; \
      fi; \
    done
