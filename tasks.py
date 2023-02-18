from invoke import task

@task
def start(ctx):
    ctx.run('python3 src/main.py')

@task
def pytest(ctx):
    ctx.run('pytest src')

@task
def coverage(ctx):
    ctx.run('coverage run --branch -m pytest src')

@task(coverage)
def coverage_report(ctx):
    ctx.run('coverage html')

@task
def pylint(ctx):
    ctx.run('pylint src')

@task
def pep8(ctx):
    ctx.run('autopep8 --in-place --recursive src')
