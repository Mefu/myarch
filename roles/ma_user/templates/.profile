#!/usr/bin/env bash

# this file in this current configuration is also sourced in
# .config/fish/config.fish with usage of edc/bass utility
# to make it usable while using fish in urxvt and guake

# environment variables are defined here

if [ -d "{{ ma_user.dirs.home }}/{{ ma_user.dirs.bin }}" ] ; then
  export PATH="{{ ma_user.dirs.home }}/{{ ma_user.dirs.bin }}:${PATH}"
fi

# stuff for uniform look across gtk and qt
export GTK_THEME="Adapta-Nokto"
export QT_STYLE_OVERRIDE="kvantum"

# aliases
alias emacs='env SHELL="/usr/bin/bash" emacs -nw'
