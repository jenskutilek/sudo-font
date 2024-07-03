# Using the official Sudo Fonts apt repository

The Sudo fonts are not part of the official Debian distribution. But you can use my private apt repository to install and update the Sudo fonts.

The repo ist hosted at <https://www.kutilek.de/apt/>.

Add the GPG public key of the repo to be able to check the signatures:

```sh
wget -O- https://raw.githubusercontent.com/jenskutilek/sudo-font/master/fonts-sudo-archive-keyring.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/fonts-sudo-archive-keyring.gpg > /dev/null
```

Add the appropriate line to your apt sources by running this command:

```sh
echo "deb [arch=all] https://www.kutilek.de/apt stable main" | sudo tee /etc/apt/sources.list.d/fonts-sudo.list
```

Then you can install the package:

```sh
sudo apt update
sudo apt install fonts-sudo
```
