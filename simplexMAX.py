class Simplex:
    def __init__(self):
        self.table = []  # Inicializa a tabela do algoritmo Simplex.

    def set_objective_function(self, fo: list):
        self.table.append(fo)  # Define a Função Objetivo na primeira linha da tabela.

    def add_restrictions(self, sa: list):
        self.table.append(sa)  # Adiciona as restrições à tabela.

    def get_entry_column(self) -> int:
        column_pivot = min(self.table[0])  # Encontra a coluna do pivô (menor valor na primeira linha).
        index = self.table[0].index(column_pivot)  # Encontra o índice da coluna do pivô.
        return index
    
    def get_exit_line(self, entry_column: int) -> int:
        results = {}
        for line in range(len(self.table)):
            if line > 0:
                if self.table[line][entry_column] > 0:
                    division = self.table[line][-1] / self.table[line][entry_column]
                    results[line] = division  # Calcula as razões e as armazena em um dicionário.
        
        index = min(results, key=results.get)  # Encontra a linha de saída com a menor razão.
        return index     
    
    def calculate_new_pivot_line(self, entry_column: int, exit_line: int) -> list:
        line = self.table[exit_line]  # Obtém a linha de saída.
        pivot = line[entry_column]  # Encontra o valor do pivô.
        new_pivot_line = [value / pivot for value in line]  # Calcula a nova linha do pivô.
        return new_pivot_line

    def calculate_new_line(self, line: list, entry_column: int, pivot_line: list) -> list:
        pivot = line[entry_column] * -1  # Calcula o negativo do coeficiente do pivô.
        result_line = [value * pivot for value in pivot_line]  # Calcula a nova linha do resultado.
        new_line = [line[i] + result_line[i] for i in range(len(result_line))]  # Calcula a nova linha da tabela.
        return new_line
        
    def is_negative(self) -> bool:
        negative = list(filter(lambda x: x < 0, self.table[0]))  # Verifica se há coeficientes negativos na Função Objetivo.
        return True if len(negative) > 0 else False
        
    def show_table(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[0])):
                print(f"*{self.table[i][j]}\t", end="")  # Exibe a tabela formatada.
            print()    

    def calculate(self):
        entry_column = self.get_entry_column()

        first_exit_line = self.get_exit_line(entry_column)

        pivot_line = self.calculate_new_pivot_line(entry_column, first_exit_line)

        self.table[first_exit_line] = pivot_line  # Atualiza a linha de saída pela nova linha do pivô.

        table_copy = self.table.copy()

        index = 0
        while index < len(self.table):
            if index != first_exit_line:
                line = table_copy[index]
                new_line = self.calculate_new_line(line, entry_column, pivot_line)
                self.table[index] = new_line  # Calcula e atualiza as novas linhas da tabela.
            index += 1

def solve_simplex():
    simplex = Simplex()
    simplex.set_objective_function([1, -5, -2, 0, 0, 0])  # Define a Função Objetivo.
    simplex.add_restrictions([0, 2, 1, 1, 0, 6])  # Adiciona a primeira restrição.
    simplex.add_restrictions([0, 10, 12, 0, 0, 1, 60])  # Adiciona a segunda restrição.
    simplex.calculate()  # Inicia o processo Simplex.
    while simplex.is_negative():  # Continua enquanto houver coeficientes negativos na Função Objetivo.
        simplex.calculate()  # Calcula uma nova iteração.
    simplex.show_table()  # Exibe a tabela final.

if __name__ == "__main__":
    solve_simplex()  # Chama a função principal para resolver o problema de maximização.
