from hydra import get_random_head, Head
from tests.conftest import HydraCustom


def test_random(custom_hydra1: HydraCustom):
    hydra = custom_hydra1.hydra

    head = get_random_head(hydra)
    assert isinstance(head, Head)
