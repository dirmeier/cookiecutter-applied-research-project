import jax
from flax import linen as nn
from jax import random
from jax.lib import xla_bridge

model = nn.Sequential([nn.Dense(10), nn.gelu, nn.Dense(1)])

x = random.normal(random.PRNGKey(1), shape=(1000, 10))
y = (
    x @ random.normal(random.PRNGKey(1), shape=(10,))
    + random.normal(random.PRNGKey(1), shape=(1000,)) * 0.01
)

print(jax.devices())
print(jax.default_backend())
print(xla_bridge.get_backend().platform)

params = model.init(random.PRNGKey(2), x)
