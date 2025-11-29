import sys

class HanoiVisualizer:
    def __init__(self):
        self.hanoi = None
        self.n = None
        self.width = None

    def set_hanoi(self, hanoi):
        self.hanoi = hanoi
        self.n = hanoi.n
        self.width = 2 * self.n + 2

    def draw(self):
        towers = self.hanoi.towers
        output = []

        # Draw towers from top to bottom
        for level in range(self.n, 0, -1):
            line = ""
            for tower_name in ["A", "B", "C"]:
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



class TowerOfHanoi:

    def __init__(self, n: int, visualizer: HanoiVisualizer):
        self.n = n
        self.towers = {
            "A": [i for i in range(n, 0, -1)],
            "B": [],
            "C": [],
        }
        self.visualizer = visualizer
        self.visualizer.set_hanoi(self)
        self.output = []

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
        if source_list:
            disk = source_list.pop()
            target_list.append(disk)
            self.output.append(
                f"Перемістити диск з {source} на {target}: {disk}"
            )
            self.output.append(f"Проміжний стан: {self.towers}")
            if not self.towers["A"] and not self.towers["B"]:
                self.output.append(f"Кінцевий стан: {self.towers}")
            self.output.append(self.visualizer.draw())
            self.output.append("") # Empty line for spacing

    def solve_and_visualize(self):
        self.output = []
        self.output.append(f"Початковий стан: {self.towers}")
        self.output.append(self.visualizer.draw())
        self.output.append("")
        self.run(self.n, "A", "C", "B")
        return "\n".join(self.output)

    def __str__(self):
        if not self.towers["A"] and not self.towers["B"]:
            return f"Кінцевий стан: {self.towers}"
        return f"Проміжний стан: {self.towers}"



def main():
    visualizer = HanoiVisualizer()
    level = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    hanoi_tower = TowerOfHanoi(level, visualizer)
    print(hanoi_tower.solve_and_visualize())



if __name__ == "__main__":
    main()
