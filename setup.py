import setuptools
setup_kwargs = {
    'name': 'eqtexsvg',
    'py_modules': ['eqtexsvg'],
    'entry_points': {
        'console_scripts': ['eqtexsvg=eqtexsvg:main'],
    },
    'install_requires': ['six'],
}
setuptools.setup(**setup_kwargs)
