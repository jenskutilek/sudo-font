#!/bin/sh
fullversion=`git describe --tags`
version=`git describe --tags | awk 'match($0, /v([0-9]+\.[0-9]+)/) {print substr($0, RSTART+1, RLENGTH-1)}'`
rm -rf dist/deb/fonts-sudo/*
mkdir -p dist/deb/fonts-sudo
git archive --format=tar.gz ${fullversion} --prefix=fonts-sudo-${version}/ > dist/deb/fonts-sudo/fonts-sudo-${version}.tar.gz
cd dist/deb/fonts-sudo
mv fonts-sudo-${version}.tar.gz fonts-sudo_${version}.orig.tar.gz
tar xzf fonts-sudo_${version}.orig.tar.gz
cp -R ../../../packaging/debian fonts-sudo-${version}
