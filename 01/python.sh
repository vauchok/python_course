#!/bin/sh

yum -y install patch gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel xz xz-devel python-pip git
cd ~/
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
sed -i '/aliases and functions/a \export PATH="~/.pyenv/bin:$PATH"' ~/.bashrc
sed -i '/export PATH=/a \eval "$(pyenv init -)"' ~/.bashrc
sed -i '/eval "$(pyenv init -)"/a \eval "$(pyenv virtualenv-init -)"' ~/.bashrc
source ~/.bashrc

pyenv install 2.7
pyenv virtualenv 2.7 python2

pyenv install 3.6.0
pyenv virtualenv 3.6.0 python3
