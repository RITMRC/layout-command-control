# Big Dumb IO (BDIO)

## Quickstart

Ensure you have a Python 3.6+ installation.

1. Install pipenv: `pip3 install --user pipenv`

2. Install dependencies: `pipenv install`

3. List tasks

```shell
$ pipenv run invoke --list
Available tasks:

  format       Produce pep8 normative code output
  lint         Static analysis of code for programming issues
  start        Run BDIO Brain
  start-leaf   Run BDIO Leaf
  test         Tests
```

4. Start app

```shell
$ pipenv run start
# OR
$ pipenv run invoke start
Starting brain
All aboard!
```