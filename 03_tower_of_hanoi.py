from __future__ import annotations
import sys


class StackInt(list[int]):
    def __init__(self, n: int):
        self.__stack = [] if not n else [i for i in range(n, 0, -1)]

    def is_empty(self):
        return len(self.__stack) == 0

    def push(self, item):
        self.__stack.append(item)

    def pop(self, target: StackInt ) -> int | None:
        if not self.is_empty():
            item = self.__stack.pop()
            target.push(item)
            return item
        else:
            print("Стек порожній")
            return None

    def __str__(self):
        return str(self.__stack)

    def __repr__(self):
        return str(self.__stack)

    def __len__(self):
        return len(self.__stack)

    def __getitem__(self, item):
        return self.__stack[item]


class HanoiVisualizer:
    def __init__(self, hanoi: TowerOfHanoi, n: int):
        self.hanoi: TowerOfHanoi = hanoi
        self.n = n
        self.width = 2 * self.n + 2

    def draw(self):
        towers = self.hanoi.towers
        tower_names = towers.keys()
        output = []

        # Draw towers from top to bottom
        for level in range(self.n, 0, -1):
            line = ""
            for tower_name in tower_names:
                tower = towers[tower_name]
                if len(tower) >= level:
                    disk_size = tower[level - 1]
                    disk_str = "█" * (2 * disk_size - 1)
                    # Center the disk
                    line += disk_str.center(self.width)
                else:
                    # Draw pole
                    line += "|".center(self.width)
            output.append(line)

        # Draw base labels
        labels = "A".center(self.width) + "B".center(self.width) + "C".center(self.width)
        output.append(labels)

        return "\n".join(output)



class TowerOfHanoi(dict[str, StackInt]):

    def __init__(self, n: int):
        self.n = n
        self.towers = {
            "A": StackInt(n),
            "B": StackInt(0),
            "C": StackInt(0),
        }
        self.visualizer = HanoiVisualizer(self, n)

    def run(self, n, source, target, auxiliary, ):
        if n == 1:
            self._execute_move(source, target)
        else:
            self.run(n - 1, source, auxiliary, target)
            self._execute_move(source, target)
            self.run(n - 1, auxiliary, target, source)

    def _execute_move(self, source, target):
        source_list = self.towers[source]
        target_list = self.towers[target]
        if not source_list.is_empty():
            disk = source_list.pop(target_list)
            print(
                f"Перемістити диск з {source} на {target}: {disk}"
            )
            print(f"Проміжний стан: {self.towers}")
            if self.towers["A"].is_empty() and self.towers["B"].is_empty():
                print(f"Кінцевий стан: {self.towers}")
            print(self.visualizer.draw())
            print("") # Empty line for spacing

    def solve_and_visualize(self):
        print(f"Початковий стан: {self.towers}")
        print(self.visualizer.draw())
        print("")
        self.run(self.n, "A", "C", "B")

    def __str__(self):
        if not self.towers["A"] and not self.towers["B"]:
            return f"Кінцевий стан: {self.towers}"
        return f"Проміжний стан: {self.towers}"



def main():
    level = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    hanoi_tower = TowerOfHanoi(level)
    print(hanoi_tower.solve_and_visualize())



if __name__ == "__main__":
    main()
