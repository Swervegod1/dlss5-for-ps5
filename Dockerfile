FROM nginx:1.27-alpine

LABEL org.opencontainers.image.title="DLSS5 FOR PS5"
LABEL org.opencontainers.image.description="Unofficial PC-side PS5 Remote Play and capture-card video enhancer. Experimental prototype; not NVIDIA DLSS 5 or native PS5 software."
LABEL org.opencontainers.image.source="https://github.com/Swervegod1/dlss5-for-ps5"
LABEL org.opencontainers.image.licenses="SEE LICENSE IN LICENSE.md"

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -q --spider http://127.0.0.1:8080/ || exit 1

CMD ["nginx", "-g", "daemon off;"]
