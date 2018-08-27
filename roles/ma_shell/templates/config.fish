fundle plugin 'edc/bass'

{% for package in ma_shell.fish.packages %}
fundle plugin "{{ package }}"
{% endfor %}

fundle init

# source .profile file using bass
if test -e ~/.profile; and type -q bass
  bass source ~/.profile
end
