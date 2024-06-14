#!/usr/bin/env python3
from . import linux
from . import admin


def update(**kargs):
    # 1- load all repositories
    admin.update_repositories(**kargs)

    # TODO: check if need to update settings


def init(
        repo=False,
        vscode=False,
        docker=False,
        ubuntu=False,
        python=False,
        **kargs):

    # 0- Basics
    linux.run([
        ['mkdir', '-p', '.vw'],
    ])

    if repo:
        # 1- load all repositories
        admin.update_repositories(**kargs)

    if python:
        print("Installing and Updating python3 virtual environment")
        linux.run([
            ['python', '-m', 'venv', '.venv'],
            ['.venv/bin/pip', 'install', '-r', 'odoo/requirements.txt']
        ])

    if vscode:
        print("VSCode configs")
        linux.run([
            ['mkdir', '-p', '.vscode'],
            ['cp', '-i', 'odoo-utils/data/template-tasks.json',
                '.vscode/task.json'],
            ['cp', '-i', 'odoo-utils/data/template-settings.json',
                '.vscode/settings.json'],
            ['cp', '-i', 'odoo-utils/data/template-launch.json',
                '.vscode/launch.json'],
            # # TODO: update project list based on project list
            # # TODO: update project list based on project list
            ['code', '.'],
        ])
