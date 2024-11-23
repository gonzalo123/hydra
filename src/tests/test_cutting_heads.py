from hydra import count_heads, cut_head, Head, Hydra
from tests.conftest import HydraCustom

"""
 2
(1)    
 H      H
"""


def test_cut_first_head():
    head1 = Head()
    head2 = Head()
    head1.add_head(head2)

    hydra = Hydra()
    hydra.add_head(head1)
    assert count_heads(hydra) == 2
    cut_head(hydra, head1)

    assert count_heads(hydra) == 0


"""
(2)
 1   2 3     
 H    H
"""
def test_cut_non_fist_head():
    head1 = Head()
    head2 = Head()
    head1.add_head(head2)

    hydra = Hydra()
    hydra.add_head(head1)
    assert count_heads(hydra) == 2
    cut_head(hydra, head2)

    assert count_heads(hydra) == 3

"""
   3
  (2)   2 3 
   1     1      
   H     H
"""
def test_cut_simple_head2():
    head1 = Head()
    head2 = Head()
    head3 = Head()
    head1.add_head(head2)
    head2.add_head(head3)

    hydra = Hydra()
    hydra.add_head(head1)
    assert count_heads(hydra) == 3
    cut_head(hydra, head2)

    assert count_heads(hydra) == 3

"""
  3 4
  (1)  2   1
     H     H
"""
def test_complex_hydra(custom_hydra1: HydraCustom):
    hydra = custom_hydra1.hydra
    head1 = custom_hydra1.heads[0]

    cut_head(hydra, head1)
    assert count_heads(hydra) == 1

"""
  (3) 4       2       5   7   
    1    2    1   3   4   6 
       H          H
"""

def test_complex_hydra2(custom_hydra1: HydraCustom):
    hydra = custom_hydra1.hydra
    head3 = custom_hydra1.heads[2]
    cut_head(hydra, head3)
    heads = count_heads(hydra)
    assert heads == 7
