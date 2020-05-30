# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.HEALTH
#
# Copyright 2017-2020 by it's authors

from setuptools import setup

version = "2.0.0"

setup(
    name="senaite.health",
    version=version,
    description="SENAITE Health",
    long_description=open("README.rst").read() + "\n" +
    open("CHANGES.rst").read() + "\n",
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Zope2",
        "Programming Language :: Python",
    ],
    keywords=["lims", "lis", "senaite", "opensource", "health"],
    author="RIDING BYTES & NARALABS",
    author_email="senaite@senaite.com",
    url="https://github.com/senaite/senaite.health",
    license="GPLv2",
    package_dir={"": "src"},
    packages=["bika", "bika.health", "senaite", "senaite.health"],
    namespace_packages=["bika", "senaite"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "senaite.lims",
        "senaite.panic",
    ],
    extras_require={
        "test": [
            "unittest2",
            "plone.app.testing",
        ]
    },
    entry_points="""
        # -*- Entry points: -*-
        [z3c.autoinclude.plugin]
        target = plone
        """,
)
