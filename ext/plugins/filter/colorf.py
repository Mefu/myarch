__metaclass__ = type

from ansible.errors import AnsibleFilterError
from ansible.utils import helpers
import string

formats = [
  'rgb_hex', # #ffffff
  'rgb_hex_0x', # 0xffffff
  'rgb_values', # [ 255, 255, 255]
  'rgba_hex', # #ffffffff
  'rgba_values', # [ 255, 255, 255, 100 ]
]

def parse_rgb_hex(value):
  if len(value) != 7:
    return False

  if not value.startswith('#'):
    return False

  if not all(c in string.hexdigits for c in value[1:]):
    return False

  r = int(value[1:3], 16)
  g = int(value[3:5], 16)
  b = int(value[5:7], 16)

  return { 'r': r, 'g': g, 'b': b, 'a': 1 }

def format_rgb_hex(color):
  return "#%X%X%X" % (color['r'], color['g'], color['b'])

def parse_rgb_hex_0x(value):
  if len(value) != 7:
    return False

  if not value.startswith('0x'):
    return False

  if not all(c in string.hexdigits for c in value[2:]):
    return False

  r = int(value[2:4], 16)
  g = int(value[4:6], 16)
  b = int(value[6:8], 16)

  return { 'r': r, 'g': g, 'b': b, 'a': 1 }

def format_rgb_hex_0x(color):
  return "0x%X%X%X" % (color['r'], color['g'], color['b'])

def parse_rgb_values(value):
  if not value['r'] or not value['b'] or not value['g'] or value['a']:
    return False
  return { 'r': value['r'], 'g': value['g'], 'b': value['b'], 'a': 1 }

def format_rgb_values(color):
  return [ color['r'], color['g'], color['b'] ]

def parse_rgba_hex(value):
  if len(value) != 9:
    return False

  if not value.startswith('#'):
    return False

  if not all(c in string.hexdigits for c in value[1:]):
    return False

  r = int(value[1:3], 16)
  g = int(value[3:5], 16)
  b = int(value[5:7], 16)
  a = int(value[7:9], 16) / 255

  return { 'r': r, 'g': g, 'b': b, 'a': a }

def format_rgba_hex(color):
  return "#%X%X%X%X" % (color['r'], color['g'], color['b'], color['a'])

def parse_rgba_values(value):
  if not value['r'] or not value['b'] or not value['g'] or not value['a']:
    return False
  return value

def format_rgba_values(color):
  return [ color['r'], color['g'], color['b'], color['a'] ]

def format_color(value, tof='', fromf='rgb_hex'):
  if tof not in formats:
    raise AnsibleFilterError ('colorf: unknown format value: %s' % tof)

  if fromf not in formats:
    raise AnsibleFilterError ('colorf: unknown format value: %s' % fromf)

  color = globals()["parse_" + fromf](value)

  if not color:
    raise AnsibleFilterError('colorf: could not parse value %s as format %s' % (value, fromf))

  color = globals()["format_" + tof](color)

  return color

# ---- Ansible filters ----
class FilterModule(object):
  ''' URI filter '''

  def filters(self):
    return {
      'colorf': format_color
    }
