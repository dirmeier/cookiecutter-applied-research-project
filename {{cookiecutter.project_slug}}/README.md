# {{ cookiecutter.project_name }}

[![status](http://www.repostatus.org/badges/latest/concept.svg)](http://www.repostatus.org/#concept)
[![arXiv](https://img.shields.io/badge/arXiv-2311.00474-b31b1b.svg)](https://arxiv.org/abs/2311.00474)
[![ci](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/ci.yaml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/ci.yaml)

> {{ cookiecutter.project_short_description }}

## About

This repository contains the Python code for reproducing the results in the paper

    Simon Dirmeier and Fernando Perez-Cruz. Diffusion models for probabilistic programming. NeurIPS Workshop on Diffusion models, 2023. 

The folder structure is as follows (delete/modify me):
- `configs`: collection of `ml_collections config files specifying hyperparameters,
- `data`: contains training/analysis data sets (this is ideally a softlink to a data folder),
- `data_and_models`: contains generative models to generate data for experiments where no real data is used,
- `envs`: conda environments,
- `experiments`: different experimental classes, like `MCMCExperiment` and `VIExperiment`, and general code for the concrete data analysis (in which case I'd rename this to `src` or `scripts` or `analysis`)
- `notebooks`: example notebooks,
- `results`: outputs of `experiments,
- `{{cookiecutter.project_slug`: library-ish code and modules that can be used independently of the project experiments (the point is to have the code separated from the the actual analysis, such that people can use it on their data)

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

You can either run experiments manually or use Snakemake to run everything in an automated fashion.

### Automated execution

Using Snakemake, calling the command below executes all scripts in succession automatically:

```shell
snakemake --slurm --default-resources constraint=mc--jobs 100
```

### Manual execution (not recommended)

If you want to run jobs manually, call either of

```shell
python 01-main.py  \
  --config=configs/sabc.py \
  --data_config=data_and_models/mixture_model.py \
  --workdir=results/
```

or use the Dockerfile like this:

```shell
docker run -v <<some path>>:/mnt \
  {{ cookiecutter.project_slug } /  
  --config=/mnt/configs/<<config.py>> \
  --data_config=/mnt/data_and_models/mixture_model.py \
  --workdir=/mnt/results/
```

## Citation

If you find our work relevant to your research, please consider citing:

```
@article{TODO}
```

## Author

{{cookiecutter.full_name}} <a href="mailto:{{cookiecutter.email}}">{{cookiecutter.email}}</a>
