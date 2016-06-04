# -*- coding: utf-8 -*-

import os

import ramlfications
from jinja2 import Environment, FileSystemLoader


AVAILABLE_TEMPLATES = (
    'markdown',
)


def resolve_template(template):
    if template in AVAILABLE_TEMPLATES:
        template_file = os.path.join(os.path.dirname(__file__), 'templates', '{}.j2'.format(template))
    else:
        if not os.path.exists(template):
            raise IOError('File \'{}\' cannot be found.'.format(template))

        template_file = template

    return os.path.split(template_file)


def convert(source, template, destination):
    if not source:
        raise IOError('Source RAML file must be specified')

    if not template:
        raise IOError('Template file or name must be specified')

    if not destination:
        raise IOError('Destination file must be specified')

    api = ramlfications.parse(source)

    base_template_dir, template_file = resolve_template(template)
    env = Environment(loader=FileSystemLoader(base_template_dir))
    template_instance = env.get_template(template_file)

    with open(destination, 'w') as f:
        f.write(template_instance.render(api=api))
