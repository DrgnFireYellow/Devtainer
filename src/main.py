#! /usr/bin/env python3
from typer import Typer
import docker
import os
import subprocess

client = docker.from_env()
app = Typer()

@app.command()
def init(project: str, packages: str, install_script: str):
    with open(f"{os.getcwd()}/Dockerfile", "w") as f:
        f.write("FROM debian\n")
        f.write("RUN apt update -y\n")
        f.write(f"RUN apt install {packages} -y\n")
        f.write(f"COPY . /root/{project}/\n")
        f.write(f"WORKDIR /root/{project}")
    with open(f"{os.getcwd()}/devtainer-project.txt", "w") as f:
        f.write(project)


@app.command()
def shell():
    with open(f"{os.getcwd()}/devtainer-project.txt") as f:
        project = f.read().strip()
    client.images.build(path=".", tag=f"{project}-devtainer")
    subprocess.run(["docker", "run", "-it", f"{project}-devtainer"])


if __name__ == "__main__":
    app()
