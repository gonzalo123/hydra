import copy

from hydra import Head, count_heads, Hydra
from tests.conftest import HydraCustom


def test_simple_head():
    head = Head()
    hydra = Hydra()
    hydra.add_head(head)
    assert count_heads(hydra) == 1


def test_dual_head():
    head1 = Head()
    head2 = Head()
    head1.add_head(head2)

    hydra = Hydra()
    hydra.add_head(head1)
    assert count_heads(hydra) == 2


def test_head2(custom_hydra1: HydraCustom):
    hydra = custom_hydra1.hydra

    head1_1 = Head()
    head1_3 = Head()
    head1_4 = Head()
    head1_1.add_head(head1_3)
    head1_1.add_head(head1_4)

    hydra.add_head(head1_1)
    assert count_heads(hydra) == 4 + 3
    hydra.add_head(copy.deepcopy(head1_1))
    assert count_heads(hydra) == 4 + 3 + 3


def test_head3(custom_hydra1: HydraCustom):
    hydra = custom_hydra1.hydra
    head1 = custom_hydra1.heads[0]

    hydra.add_head(copy.deepcopy(head1))
    assert count_heads(hydra) == 4 + 3


def test_head4(custom_hydra1: HydraCustom):
    hydra = custom_hydra1.hydra
    head3 = custom_hydra1.heads[2]

    hydra.add_head(copy.deepcopy(head3.parent))
    hydra.add_head(copy.deepcopy(head3.parent))
    assert count_heads(hydra) == 4 + 3 + 3


def test_complex_hydra(custom_hydra1: HydraCustom):
    assert count_heads(custom_hydra1.hydra) == 4
