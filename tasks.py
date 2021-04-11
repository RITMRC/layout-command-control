from invoke import task, call


@task
def start(c):
    """
    Run BDIO Brain
    """
    print("Starting brain")
    c.run("python bdio/brain/brain.py")


@task
def start_leaf(c):
    """
    Run BDIO Leaf
    """
    print("Starting leaf")
    c.run("python bdio/leaf/leaf.py")


@task
def lint(c):
    """
    Static analysis of code for programming issues
    """
    print("Running flake8 linter")
    c.run("flake8 bdio/ tasks.py", pty=True)
    print()


@task
def format(c):
    """
    Produce pep8 normative code output
    """
    print("Running black formatter")
    c.run("black bdio/ tasks.py", pty=True)
    print()


@task
def test(c, coverage=False):
    """
    Tests
    """
    print("Running pytest")
    if coverage:
        c.run("pytest --cov=bdio", pty=True)
    else:
        c.run("pytest", pty=True)
    print()


@task
def clean(c):
    print("Running pyclean")
    c.run("pyclean ./", pty=True)
    print()


@task(pre=[format, lint, call(test, coverage=True)], post=[clean])
def build(c):
    """
    Run all configured steps
    """
    print("Build completed\n")
