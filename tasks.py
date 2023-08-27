from invoke import task


@task
def build(c, test=False, dev=False):
    if test:
        c.run("pip install '.[test]'")
    if dev:
        c.run("pip install '.[dev]")
    c.run("pip install .")
