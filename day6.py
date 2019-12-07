from collections import defaultdict

FILENAME = 'input6.txt'


class OrbitNode:
    def __init__(self):
        self.parent = None

    def get_parent_orbit_count(self):
        if self.parent == None:
            return 0
        else:
            return self.parent.get_parent_orbit_count() + 1


def main():
    orbits = defaultdict(OrbitNode)
    with open(FILENAME) as f:
        for line in f:
            parent_id, child_id = line.strip().split(")")
            child = orbits[child_id]
            parent = orbits[parent_id]
            child.parent = parent
    total_orbits = 0
    for v in orbits.values():
        total_orbits += v.get_parent_orbit_count()
    return total_orbits


if __name__ == "__main__":
    print(main())
