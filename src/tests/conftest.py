import logging
from dataclasses import dataclass
from typing import List

import pytest

from hydra import Head, Hydra

logger = logging.getLogger(__name__)


@dataclass
class HydraCustom:
    hydra: Hydra
    heads: List[Head]


@pytest.fixture()
def custom_hydra1():
    head1 = Head()
    head2 = Head()
    head3 = Head()
    head4 = Head()

    head1.add_head(head3)
    head1.add_head(head4)

    hydra = Hydra()
    hydra.add_head(head1)
    hydra.add_head(head2)
    return HydraCustom(
        hydra=hydra,
        heads=[head1, head2, head3, head4]
    )
