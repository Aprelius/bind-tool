FROM rockylinux:8-minimal

RUN set -ex; \
    microdnf upgrade -y; \
    microdnf install -y --setopt=install_weak_deps=0 \
        bind; \
    \
    microdnf clean all; \
    rm -rf /var/cache/yum;

RUN set -ex; \
    mkdir -p \
        /var/log/named \
        /var/named; \
    chown named:root \
        /var/log/named \
        /var/named;

COPY --chown=root:root [ \
    "./scripts/docker-entrypoint.sh", \
    "/usr/sbin/docker-entrypoint.sh" \
]

RUN set -ex; \
    chmod 544 /usr/sbin/docker-entrypoint.sh; \
    chown named:root /usr/sbin/docker-entrypoint.sh

USER named
EXPOSE 53/tcp 53/udp

ENTRYPOINT [ "/usr/sbin/docker-entrypoint.sh" ]
