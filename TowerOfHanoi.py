def tower_of_Hanoi(num_disks):
    return tower_of_hanoi_func(num_disks, 'S', 'D', 'A')


def tower_of_hanoi_func(num_disks, source, destination, auxillary):
    if num_disks <= 0:
        return

    if num_disks == 1:
        print("{} {}".format(source, destination))
        return

    tower_of_hanoi_func(num_disks - 1, source, auxillary, destination)
    print("{} {}".format(source, destination))
    tower_of_hanoi_func(num_disks - 1, auxillary, destination, source)
    return


tower_of_Hanoi(2)
print("__________________")
tower_of_Hanoi(3)
print("__________________")
tower_of_Hanoi(4)
print("__________________")
tower_of_Hanoi(5)
print("__________________")
