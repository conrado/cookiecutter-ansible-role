# conrado/cookiecutter-ansible-role

A cookiecutter template for ansible roles with Github Actions CI and
vagrant+virtualbox for local testing (because Mac doesn't work to simulate
docker with systemd)

I only work on ubuntu so that's the only machine it configures for. You may want
to fork this and tweak it to use your own docker image on Github.

See an example Dockerfile here: [gh:conrado/dockerfiles/ubuntu2004-systemd-ansible](https://github.com/conrado/dockerfiles/tree/main/ubuntu2004-systemd-ansible)

## Usage

For generating the code you should get away with just installing `cookiecutter` locally

- `cookiecutter`

However for running the generated code you will need the following

- `molecule`
- `vagrant`
- `virtualbox`

get that with:

```
brew install vagrant virtualbox
pip install ansible ansible-lint molecule-vagrant python-vagrant yamllint
```

the pip install of molecule should install cookiecutter as a dependency

```
$ cookiecutter gh:conrado/cookiecutter-ansible-role
```

if you did not change the default configuration you would end up with a
directory called `conrado_ansible_role`

```
$ cd conrado_ansible_role
$ molecule test
```


