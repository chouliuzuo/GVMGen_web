# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
"""
This code is based on:

- [MusicGen](https://arxiv.org/abs/2306.05284), a state-of-the-art
    text-to-music and melody+text autoregressive generative model.

- [EnCodec](https://arxiv.org/abs/2210.13438), efficient and high fidelity
    neural audio codec which provides an excellent tokenizer for autoregressive language models.
"""

# flake8: noqa
from . import data, modules, models

__version__ = '1.3.0a1'
