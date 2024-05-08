import hashlib
import os
import pathlib

import jax
import wandb
from absl import app, flags, logging
from jax.lib import xla_bridge
from ml_collections import config_flags

import experiments

FLAGS = flags.FLAGS
config_flags.DEFINE_config_file("config", None, "training configuration", lock_config=False)
config_flags.DEFINE_config_file("data_config", None, "data and model configuration", lock_config=False)
flags.DEFINE_string("workdir", None, "out directory, i.e., place where results are written to")
flags.DEFINE_bool("usewand", False, "register run to wandb")
flags.mark_flags_as_required(["config", "data_config", "workdir"])


def init_and_log_jax_env(tm):
    logging.set_verbosity(logging.INFO)
    logging.info("file prefix: %s", tm)
    logging.info("----- Checking JAX installation ----")
    logging.info(jax.devices())
    logging.info(jax.default_backend())
    logging.info(xla_bridge.get_backend().platform)
    logging.info("------------------------------------")
    return tm


def hash_value(config):
    h = hashlib.new("sha256")
    h.update(str(config).encode("utf-8"))
    return h.hexdigest()


def main(argv):
    del argv
    config = FLAGS.config
    hsh = init_and_log_jax_env(hash_value(config))
    run_name = f"{FLAGS.data_config.experiment}-{FLAGS.config.model_type}-seed_{FLAGS.config.rng_seq_key}"

    workdir = os.path.join(FLAGS.workdir, hsh)
    if not pathlib.Path(workdir).exists():
        pathlib.Path(workdir).mkdir(parents=True, exist_ok=False)

    if FLAGS.usewand:
        wandb.init(
            project="{{cookiecutter.project_slug}}",
            config=config.to_dict(),
            dir=os.path.join(FLAGS.workdir, "wandb"),
        )
        wandb.run.name = run_name

    experiment = getattr(experiments, FLAGS.config.model_type.upper() + "Experiment")(FLAGS, workdir, run_name)
    getattr(experiment, "fit")()


if __name__ == "__main__":
    jax.config.config_with_absl()
    app.run(main)
