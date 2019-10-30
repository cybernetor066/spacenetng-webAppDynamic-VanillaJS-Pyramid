from setuptools import setup
# List of dependencies installed via `pip install -e .`
# by virtue of the Setuptools `install_requires` value below.
requires = [
    'pyramid',
    'plaster_pastedeploy',
    'pyramid_chameleon',
    'waitress',
    'gunicorn',
    'pymongo'
]

# List of dependencies installed via 'pip install -e' ".[dev]"
# by virtue of the setuptools `extras_require` value in the python
# dictionary below.
dev_requires = [
    'pyramid_debugtoolbar',
    'pytest',
    'webtest',
]


setup(
    name = 'spacenetng',
    install_requires = requires,
    extras_require = {
        'dev': dev_requires,
    },

    entry_points = {
        'paste.app_factory': [
            'main = spacenetng:main'
        ],
    },
)
