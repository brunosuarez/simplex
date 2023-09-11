class SimplexMinimization:

    def __init__(self):
        self.table = []

    def set_objective_function(self, fo: list):
        self.table.append([-val for val in fo])

    def add_restrictions(self, sa: list):
        self.table.append(sa)

    def get_entry_column(self) -> int:
        column_pivot = min(self.table[0])
        index = self.table[0].index(column_pivot)
        return index

    def get_exit_line(self, entry_column: int) -> int:
        results = {}
        for line in range(len(self.table)):
            if line > 0:
                if self.table[line][entry_column] < 0:  # Alteração aqui para tratar negativos
                    division = -self.table[line][-1] / self.table[line][entry_column]  # Alteração aqui
                    results[line] = division

        if not results:
            raise Exception("O problema é ilimitado.")

        index = min(results, key=results.get)
        return index

    def calculate_new_pivot_line(self, entry_column: int, exit_line: int) -> list:
        line = self.table[exit_line]
        pivot = line[entry_column]
        new_pivot_line = [value / pivot for value in line]
        return new_pivot_line

    def calculate_new_line(self, line: list, entry_column: int, pivot_line: list) -> list:
        pivot = line[entry_column] * -1
        result_line = [value * pivot for value in pivot_line]
        new_line = [line[i] + result_line[i] for i in range(len(result_line))]
        return new_line

    def is_negative(self) -> bool:
        negative = list(filter(lambda x: x < 0, self.table[0]))
        return True if len(negative) > 0 else False

    def show_table(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[0])):
                print(f"*{self.table[i][j]}\t", end="")
            print()

    def calculate(self):

        entry_column = self.get_entry_column()

        first_exit_line = self.get_exit_line(entry_column)

        pivot_line = self.calculate_new_pivot_line(entry_column, first_exit_line)

        self.table[first_exit_line] = pivot_line

        table_copy = self.table.copy()

        index = 0

        while index < len(self.table):
            if index != first_exit_line:
                line = table_copy[index]
                new_line = self.calculate_new_line(line, entry_column, pivot_line)
                self.table[index] = new_line
            index += 1

    def solve(self):
        self.calculate()

        while self.is_negative():
            self.calculate()

        self.show_table()

def solve_simplex_minimization():
    simplex = SimplexMinimization()
    simplex.set_objective_function([1, 2, 3, 0, 0, 0])
    simplex.add_restrictions([-1, -1, -1, 0, 0, -3])
    simplex.add_restrictions([-1, -2, 0, 0, -2, -2])
    simplex.calculate()
    while simplex.is_negative():
        simplex.calculate()
    simplex.show_table()

if __name__ == "__main__":
    solve_simplex_minimization()
