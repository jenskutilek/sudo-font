#!/bin/sh
version=`git describe --tags | awk 'match($0, /v([0-9]+\.[0-9]+)/) {print substr($0, RSTART+1, RLENGTH-1)}'`
rm -rf dist/deb
mkdir -p dist/deb/sudo-font
git archive --format=tar.gz ${version} --prefix=sudo-font-${version}/ > dist/deb/sudo-font/sudo-font-${version}.tar.gz
cd dist/deb/sudo-font
mv sudo-font-${version}.tar.gz sudo-font_${version}.orig.tar.gz
tar xzf sudo-font_${version}.orig.tar.gz
cp -R ../../../packaging/debian sudo-font-${version}
