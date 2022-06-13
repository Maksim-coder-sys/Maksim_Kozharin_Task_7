import os

if not os.path.exists('--my_project'):
    os.mkdir('--my_project')

if not os.path.exists('--my_project\--settings'):
    os.mkdir('--my_project\--settings')

if not os.path.exists('--my_project\--mainapp'):
    os.mkdir('--my_project\--mainapp')

if not os.path.exists('--my_project\--adminapp'):
    os.mkdir('--my_project\--adminapp')

if not os.path.exists('--my_project\--authapp'):
    os.mkdir('--my_project\--authapp')
