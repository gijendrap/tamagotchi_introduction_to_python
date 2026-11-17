class Tamagotchi:
    def __init__(self, n):
        self.n = n
        self.hu = 50
        self.hp = 100
        self.bo = 50
        self.ex = 50
        self.alive = True

    def feed(self):
        if not self.alive:
            print(f"{self.n} is dead...")
            return
        self.hu = max(0, self.hu - 20)
        self.ex += 5
        self._check()

    def play(self):
        if not self.alive:
            print(f"{self.n} is dead...")
            return
        self.bo = max(0, self.bo - 25)
        self.hu += 10
        self.ex += 15
        self._check()

    def sleep(self):
        if not self.alive:
            print(f"{self.n} is dead...")
            return
        self.ex = max(0, self.ex - 30)
        self.hu += 5
        self.bo += 10
        self._check()

    def heal(self):
        if not self.alive:
            print(f"{self.n} is dead...")
            return
        self.hp = min(100, self.hp + 25)
        self.hu += 5
        self._check()

    def _check(self):
        self.hu = min(100, self.hu)
        self.bo = min(100, self.bo)
        self.ex = min(100, self.ex)
        self.hp = min(100, self.hp)

        if self.hu >= 100:
            self.hp -= 15
        if self.ex >= 100:
            self.hp -= 10
        if self.bo >= 100:
            self.hp -= 5

        if self.hp <= 0:
            self.hp = 0
            self.alive = False
            print(f"\n{self.n} has died! RIP\n")

    def status(self):
        s = "ALIVE" if self.alive else "DEAD"
        print(f"\n--- {self.n} [{s}] ---")
        print(f"  Health:     {self.hp}")
        print(f"  Hunger:     {self.hu}")
        print(f"  Boredom:    {self.bo}")
        print(f"  Exhaustion: {self.ex}")
        print()

    def to_dict(self):
        return {
            "n": self.n,
            "hu": self.hu,
            "hp": self.hp,
            "bo": self.bo,
            "ex": self.ex,
            "alive": self.alive
        }

    @classmethod
    def from_dict(cls, d):
        t = cls(d["n"])
        t.hu = d["hu"]
        t.hp = d["hp"]
        t.bo = d["bo"]
        t.ex = d["ex"]
        t.alive = d["alive"]
        return t
