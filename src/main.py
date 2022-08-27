#! /usr/bin/env python3

from typer import Typer
import os
app = Typer()

@app.command()
def init(project: str, packages: str):
    os.system(f"mkdir {os.getcwd()}/.devtainer")
    with open(f"{os.getcwd()}/.devtainer/Dockerfile", "w") as f:
        f.write("FROM debian\n")
        f.write("RUN apt update -y\n")
        f.write(f"RUN apt install {packages} -y\n")
    with open(f"{os.getcwd()}/.devtainer/project.txt", "w") as f:
        f.write(project)


@app.command()
def shell():
    with open(f"{os.getcwd()}/.devtainer/project.txt") as f:
        project = f.read().strip()
    os.system(f"docker build {os.getcwd()}/.devtainer -t {project}-devtainer")
    os.system(f"docker run -it {project}-devtainer")
if __name__ == "__main__":
    app()
