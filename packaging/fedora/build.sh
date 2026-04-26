#!/bin/bash
set -euo pipefail

FEDORA_VERSION="${1:?Usage: build.sh <fedora_version>}"

cd /repo
dnf install -y gcc-c++ fuse3-devel libattr-devel make rpm-build
mkdir -p /root/rpmbuild/{SOURCES,SPECS}
tar czf /root/rpmbuild/SOURCES/cicpoffs-src.tar.gz --transform='s,^\.,cicpoffs-src,' -C /repo .
cp packaging/fedora/cicpoffs.spec /root/rpmbuild/SPECS/
rpmbuild -bb /root/rpmbuild/SPECS/cicpoffs.spec
cp /root/rpmbuild/RPMS/x86_64/cicpoffs-*.rpm "/repo/packaging/cicpoffs-fc${FEDORA_VERSION}.rpm"
