class SnapshotArray:

    def __init__(self, length: int):
        self.h = [[(0, -1)] for _ in range(length)]
        self.l = [0 for _ in range(length)]
        self.s = -1
        self.d = set()

    def set(self, index: int, val: int) -> None:
        self.l[index] = val
        self.d.add(index)

    def snap(self) -> int:
        self.s += 1

        for dirty in self.d:
            self.h[dirty].append((self.l[dirty], self.s))
        self.d.clear()

        return self.s

    # Should be a binary search
    def get(self, index: int, snap_id: int) -> int:
        prev = self.h[index][0][0]
        for history, snap in self.h[index][1:]:
            if snap_id == snap:
                return history
            elif snap_id < snap:
                return prev
            prev = history

        return prev