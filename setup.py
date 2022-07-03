try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="flask_project",
    version="1.0.0",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "Click==7.0",
        "Flask==1.1.2",
        "Flask-SQLAlchemy==2.4.4",
        "gunicorn==19.9.0",
        "itsdangerous==1.1.0",
        "Jinja2==2.11.3",
        "MarkupSafe==1.1.1",
        "SQLAlchemy==1.3.22",
        "Werkzeug==1.0.1",
    ],
)
