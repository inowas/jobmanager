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

> NOTE: You need to write down the published ssh ports for the single nodes, because you later use them in your ansible inventory file.

### Run ansible script

```
ansible-playbook -i inventory sites.yml
```

> NOTE: You need to replace the ports you wrote down on vagrant provisioning in the inventory file.