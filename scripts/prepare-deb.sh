#!/bin/sh
version=`git describe --tags`
rm -r dist/deb
mkdir -p dist/deb/sudo-font
git archive --format=tar.gz ${version} --prefix=sudo-font-${version}/ > dist/deb/sudo-font/sudo-font-${version}.tar.gz
cd dist/deb/sudo-font
mv sudo-font-${version}.tar.gz sudo-font_${version}-orig.tar.gz
tar xzf sudo-font_${version}-orig.tar.gz
cp -R ../../../packaging/debian sudo-font-${version}
