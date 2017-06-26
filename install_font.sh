#!/bin/bash
wget https://github.com/powerline/powerline/raw/develop/font/10-powerline-symbols.conf
wget https://github.com/powerline/powerline/raw/develop/font/PowerlineSymbols.otf
sudo mv PowerlineSymbols.otf /usr/share/fonts/X11/misc/
sudo mv 10-powerline-symbols.conf /etc/fonts/conf.d/
sudo fc-cache -vf /usr/share/fonts/X11/misc/
echo "Fonts installed, restart X-Window or restart"
