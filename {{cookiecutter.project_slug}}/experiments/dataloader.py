import tensorflow as tf
import tensorflow_datasets as tfds
from jax import numpy as jnp
from jax import random as jr


def data_loaders(rng_key, dataset: str, config, split="train", outpath: str = None):
   pass

def _as_preprocessed_dataset(dataset, outpath, split):
    ds_builder = tfds.builder(dataset, try_gcs=False, data_dir=outpath)
    ds_builder.download_and_prepare(download_dir=outpath)
    ds = tfds.as_numpy(ds_builder.as_dataset(split=split, batch_size=-1))
    return ds


def _as_batched_numpy_iter(rng_key, itr, config):
    itr = tf.data.Dataset.from_tensor_slices(itr)
    max_int32 = jnp.iinfo(jnp.int32).max
    seed = jr.randint(rng_key, shape=(), minval=0, maxval=max_int32)
    return tfds.as_numpy(
        itr.shuffle(config.training.buffer_size, reshuffle_each_iteration=config.training.do_reshuffle, seed=int(seed))
        .batch(config.training.batch_size, drop_remainder=True)
        .prefetch(config.training.batch_size * 5)
    )

