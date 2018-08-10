# jobmanager
Manages Modflow-Calculations, Optimizations, Parameterestimations

## Setup Development environment

### Setting up ansible

```
mkvirtualenv jobmanager --python=python3
pip install -r requirements.txt
pipenv install
```

### Setting up test infra with vagrant

For development one can use vagrant vm's. In this way we can easily delete vm's and create new ones on scratch while developing the ansible scripts.

```
vagrant up
```

> NOTE: You need to get the ip adresses for every vm, to use it later on your ansible deployment. You can do this with the following steps for every vm:
> 1. SSH into one of the machines with: ```vagrant ssh node-1```
> 1. Retrieve the ip with the command: ```ifconfig```

### Run ansible script

```
ansible-playbook -i inventory sites.yml
```

> NOTE: You need to replace the ip's in the inventory with the ip's you wrote down on vagrant provisioning.