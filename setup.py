import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.ToggleDarkLightMode',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='HTML and js for toggling Bootstrap dark and light mode live. You\'ll probably have to style the switch elements to get something pretty, but this is functional.\r\n\r\nThe HTML in the footer:\r\n```\r\n---\r\ndefault screen parts:\r\n  footer: |\r\n    <div class="form-check form-switch">\r\n      <input class="form-check-input" type="checkbox" role="switch" id="switch">\r\n      <label class="form-check-label" for="switch">Switch</label>\r\n    </div>\r\n---\r\n```\r\n\r\nThe javascript:\r\n\r\n```js\r\n$(document).ready(function() {\r\n  let dark = false;\r\n  $(\'#switch\').on(\'click\', function () {\r\n    if ( dark === false ) {\r\n      document.documentElement.setAttribute(\'data-bs-theme\', \'dark\');\r\n      dark = true;\r\n    } else {\r\n      document.documentElement.setAttribute(\'data-bs-theme\', \'light\');\r\n      dark = false;\r\n    }\r\n  });  // ends on #switch click\r\n});\r\n```\r\n',
      long_description_content_type='text/markdown',
      author='',
      author_email='example@example.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/ToggleDarkLightMode/', package='docassemble.ToggleDarkLightMode'),
     )

