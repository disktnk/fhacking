# fhacking: forked hacking, flake8 is upgraded

[hacking](https://github.com/openstack-dev/hacking) is very useful, but unfortunately, it depends on flake8 2.6.x, which is too old. This repository is forked (based `6615b4ba75b5316e7edf7813c3063233842c2bd3`), and upgrade flake8 version.

## Install

```bash
$ pip install fhacking
```

## Notes

- hacking is implemented as pycodestyle plugin
    - dependency on pycodestyle is more important than flake8
- flake8 module is used for testing
- this repository fixes test module and tox.ini file to work under flake8 2.6.x

## Test

```bash
$ pip install -e .
$ pip install -r test-requirements.txt
$ python -m testtools.run
Tests running...

Ran 187 tests in 0.277s
OK
```

Official documentation does not describe about testing, so it's detected, not sure this command is correct or not.
 