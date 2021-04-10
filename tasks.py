from invoke import task


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
    c.run("flake8 bdio/ tasks.py")


@task
def format(c):
    """
    Produce pep8 normative code output
    """
    c.run("black bdio/ tasks.py")


@task
def test(c, coverage=False):
    """
    Tests
    """
    print("Testing")
