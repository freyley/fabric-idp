from fabric.api import run, sudo
from fabric.contrib.files import exists
import re

def is_dir(name):
    retval = 'ls -a %s' % name
    if retval.failed:
        return False
    if retval.strip()[0] == 'd':
        return True
    return False

def dir(*names, **kwargs):
    chmod = owner = group = False
    mkdir = 'mkdir' 
    if 'owner' in kwargs:
        owner = kwargs['owner']
    if 'group' in kwargs:
        owner = kwargs['group']
    if 'recursive' in kwargs:
        mkdir = 'mkdir -p' 
    if 'chmod' in kwargs:
        chmod = kwargs['chmod']
        if not re.match('^[01234567]{4}$', chmod):
            # TODO: raise a warning that it's bad
            chmod = False

    for name in names:
        if exists(name):
            if not is_dir(name):
                run('rm %s' % name)
                run('%s %s' % (mkdir, name))
        else:
            run('%s %s' % (mkdir, name))
        if chmod:
            run('chmod %s %s' % ( chmod, name))
        if owner:
            sudo('chown %s %s' % (owner, name))
        if group:
            sudo('chgrp %s %s' % (group, name))

            

def symlink(source, target):
    pass

def user(username):
    pass
