# {{ cookiecutter.project_name }}

[![status](http://www.repostatus.org/badges/latest/concept.svg)](http://www.repostatus.org/#concept)
[![arXiv](https://img.shields.io/badge/arXiv-2311.00474-b31b1b.svg)](https://arxiv.org/abs/2311.00474)
[![ci](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/ci.yaml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/ci.yaml)

> {{ cookiecutter.project_short_description }}

## About

TODO

## Installation

To install all dependencies within a conda environment, call:

```bash
conda env create -p <<envdir>> -f envs/environment.yaml
# OR
conda env create -n <<envname>> -f envs/environment.yaml
```

where `<<envdir>>` is a path where the dependencies will be installed and `<<envname>>` is a name for 
the conda environment.

## Usage

TODO

## Citation

If you find our work relevant to your research, please consider citing:

```
@article{TODO}
```

## Author

{{cookiecutter.full_name}} <a href="mailto:{{cookiecutter.email}}">{{cookiecutter.email}}</a>
