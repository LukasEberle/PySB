import time
from typing import List
from math import floor


def check_values(s1, s2, s3):
    assert 1 <= s1 <= 30000, "ERROR: Seed Values have to be between 1 and 30000"
    assert 1 <= s2 <= 30000, "ERROR: Seed Values have to be between 1 and 30000"
    assert 1 <= s3 <= 30000, "ERROR: Seed Values have to be between 1 and 30000"


class WichmannHillRNG:

    def __init__(self, s1=100, s2=100, s3=100):
        check_values(s1, s2, s3)
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.resetSeed = [s1, s2, s3]

    def set_seed(self, v1: int, v2: int, v3: int):
        check_values(v1, v2, v3)
        self.s1 = v1
        self.s2 = v2
        self.s3 = v3
        self.resetSeed = [v1, v2, v3]

    def set_seed(self, seed: List[int]):
        assert len(seed) >= 3, "ERROR: If you use a List as Seed, it has to contain at least 3 values"
        check_values(seed[0], seed[1], seed[2])
        self.s1 = seed[0]
        self.s2 = seed[1]
        self.s3 = seed[2]
        self.resetSeed = [self.s1, self.s2, self.s3]

    def reset_seed(self):
        self.s1 = self.resetSeed[0]
        self.s2 = self.resetSeed[1]
        self.s3 = self.resetSeed[2]

    def rng(self):
        self.s1 = (171 * self.s1) % 30269
        self.s2 = (172 * self.s2) % 30307
        self.s3 = (170 * self.s3) % 30323
        return (self.s1 / 30269.0 + self.s2 / 30307.0 + self.s3 / 30323.0) % 1.0

    def in_between(self, lower_border, upper_border):
        """ Returns a pseudo-random number between lower_border (inclusive) and upper_boarder (exclusive)"""
        n = self.rng()
        r = upper_border - lower_border
        return lower_border + r * n

    def int_between(self, lower_border, upper_border):
        """Sorry for the pun name. Returns a pseudo-random integer between
            lower_border (inclusive) and upper_boarder (exclusive)"""
        n = self.rng()
        r = upper_border - lower_border
        return int(floor(lower_border + r * n))

    def flip(self):
        if self.rng() < 0.5:
            return False
        else:
            return True

    def clock_seed(self):
        c = str(time.time())
        c = c.replace(".", "")
        c_seed = [(int(c[0:int((len(c) / 3))]) % 30000) + 1,
                  (int(c[int((len(c) / 3)):(int((len(c) / 3)) * 2)]) % 30000) + 1,
                  (int(c[int(((len(c) / 3) * 2)):-1]) % 30000) + 1]
        self.set_seed(c_seed)


if __name__ == "__main__":
    Random = WichmannHillRNG()
    for i in range(2):
        for j in range(10):
            print(Random.rng())
        Random.reset_seed()
    Random.clock_seed()
    for i in range(2):
        for j in range(10):
            print(Random.rng())
        Random.reset_seed()
    for i in range(10):
        if Random.flip():
            print("Heads")
        else:
            print("Tails")
