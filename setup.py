from setuptools import setup, find_packages  # type: ignore

setup(
    name='arcor2_mocks',
    version_config={
            "template": "{tag}.dev{cc}",
            "starting_version": "0.1.0"
        },
    include_package_data=True,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={"arcor2_mocks": ["py.typed"]},
    entry_points={
                  'console_scripts': [
                      'arcor2_mock_scene = arcor2_mocks.scripts.scene:main',
                      'arcor2_mock_project = arcor2_mocks.scripts.project:main',
                  ],
              },
    url='https://github.com/robofit/arcor2_mocks',
    license='LGPL',
    author='Robo@FIT',
    author_email='imaterna@fit.vut.cz',
    description='',
    setup_requires=['another-setuptools-git-version'],
    install_requires=[
        'arcor2'
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-repeat',
            'pytest-randomly',
            'openapi-spec-validator',
            'flake8',
            'mypy',
            'flake8-import-order',
            'flake8-tidy-imports',
            'flake8-annotations-coverage',
            'flake8-pytest-style',
            'flake8-bugbear'
            ],
        'docs': ['sphinx']
    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.8',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering'
    ]
)
