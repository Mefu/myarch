fundle plugin 'edc/bass'

{% for package in shell.fish.packages %}
fundle plugin "{{ package }}"
{% endfor %}

fundle init

# source .bashrc file using bass
if test -e ~/.bashrc; and type -q bass
  bass source ~/.bashrc
end
