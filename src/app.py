#%%

from hydra import Head, Hydra, count_heads, cut_head, get_random_head, count_branch


#%%

def build_hydra2():
    head1 = Head()
    head2 = Head()
    head3 = Head()
    head4 = Head()
    head5 = Head()
    head6 = Head()
    head7 = Head()
    head8 = Head()
    head9 = Head()
    head10 = Head()
    head11 = Head()
    head12 = Head()
    head13 = Head()
    head14 = Head()
    head15 = Head()
    head16 = Head()
    head17 = Head()
    head18 = Head()
    head19 = Head()
    head20 = Head()
    head21 = Head()
    head22 = Head()

    head1.add_head(head3)
    head1.add_head(head4)
    head1.add_head(head5)
    head1.add_head(head6)

    head5.add_head(head11)
    head5.add_head(head12)

    head6.add_head(head13)
    head6.add_head(head14)
    head6.add_head(head15)

    head2.add_head(head7)
    head2.add_head(head8)

    head8.add_head(head9)
    head8.add_head(head16)

    head3.add_head(head10)

    head12.add_head(head17)

    head17.add_head(head22)

    head13.add_head(head18)

    head14.add_head(head19)

    head19.add_head(head21)
    head19.add_head(head20)

    hydra = Hydra()
    hydra.add_head(head1)
    hydra.add_head(head2)
    hydra.add_head(head3)
    hydra.add_head(head4)

    return hydra

def build_hydra():
    head1 = Head()
    head2 = Head()
    head3 = Head()
    head4 = Head()

    head1.add_head(head3)
    head1.add_head(head4)

    hydra = Hydra()
    hydra.add_head(head1)
    hydra.add_head(head2)

    return hydra
#%%

from plot import plot_hydra

hydra = build_hydra2()
plot_hydra(hydra)
print(f"First hydra. {count_heads(hydra)} heads.")
loops = 0


while count_heads(hydra) > 0:
    loops += 1
    head = get_random_head(hydra)
    cut_head(hydra, head)
    print(f"branches: {count_branch(hydra)} heads: {count_heads(hydra)}")

print(f'*** loops: {loops}')

