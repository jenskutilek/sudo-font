# Using the official Sudo Fonts apt repository

The Sudo fonts are not part of the official Debian distribution. But you can use my private apt repository to install and update the Sudo fonts.

The repo ist hosted at <https://www.kutilek.de/apt/>.

Add the GPG public key of the repo to be able to check the signatures:

```sh
wget -O- https://raw.githubusercontent.com/jenskutilek/sudo-font/master/fonts-sudo-archive-keyring.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/fonts-sudo-archive-keyring.gpg > /dev/null
```

Add the Sudo fonts to your apt sources by adding a file `/etc/apt/sources.list.d/fonts-sudo.sources` with this contents:

```
Types: deb
URIs: https://www.kutilek.de/apt/
Suites: stable
Components: main
Signed-By: /etc/apt/trusted.gpg.d/fonts-sudo-archive-keyring.gpg
Architectures: all
```

You can do this by executing the following command:

```sh
echo -e "Types: deb\nURIs: https://www.kutilek.de/apt/\nSuites: stable\nComponents: mainSigned-By: /etc/apt/trusted.gpg.d/fonts-sudo-archive-keyring.gpg\nArchitectures: all" | sudo tee /etc/apt/sources.list.d/fonts-sudo.sources
```

Then you can install the package:

```sh
sudo apt update
sudo apt install fonts-sudo
```
