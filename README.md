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