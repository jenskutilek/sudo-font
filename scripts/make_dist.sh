#!/bin/sh

rm ../dist/sudo.zip
cd ..
zip -r dist/sudo.zip sudo/ --exclude \*.DS_Store
mv ~/Sites/kuti/download/sudo.zip ~/Sites/kuti/download/sudo_old.zip
cp dist/sudo.zip ~/Sites/kuti/download/