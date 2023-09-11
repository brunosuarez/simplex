class SimplexMinimization:

    def __init__(self):
        self.table = []  # Cria uma tabela vazia para representar o tableau do Simplex.

    def set_objective_function(self, fo: list):
        self.table.append([-val for val in fo])  # Configura a função objetivo (FO) no tableau, negando os coeficientes para minimização.

    def add_restrictions(self, sa: list):
        self.table.append(sa)  # Adiciona as restrições (subject to, SA) ao tableau.

    def get_entry_column(self) -> int:
        # Encontra a coluna de entrada, que é a coluna com o menor valor na linha de FO (Função Objetivo).
        column_pivot = min(self.table[0])
        index = self.table[0].index(column_pivot)
        return index

    def get_exit_line(self, entry_column: int) -> int:
        results = {}
        for line in range(len(self.table)):
            if line > 0:
                if self.table[line][entry_column] < 0:  # Encontra as linhas onde o valor na coluna de entrada é negativo.
                    division = -self.table[line][-1] / self.table[line][entry_column]  # Calcula a razão.
                    results[line] = division

        if not results:
            raise Exception("O problema é ilimitado.")  # Se não houver razões positivas, o problema é ilimitado.

        index = min(results, key=results.get)  # Encontra a linha de saída com a menor razão positiva.
        return index

    def calculate_new_pivot_line(self, entry_column: int, exit_line: int) -> list:
        line = self.table[exit_line]
        pivot = line[entry_column]

        # Calcula a nova linha de pivô dividindo todos os elementos na linha de saída pelo valor do pivô.
        new_pivot_line = [value / pivot for value in line]
        return new_pivot_line

    def calculate_new_line(self, line: list, entry_column: int, pivot_line: list) -> list:
        pivot = line[entry_column] * -1

        # Calcula a nova linha multiplicando a linha de pivô pela entrada atual e somando-a à linha atual.
        result_line = [value * pivot for value in pivot_line]
        new_line = [line[i] + result_line[i] for i in range(len(result_line))]
        return new_line

    def is_negative(self) -> bool:
        negative = list(filter(lambda x: x < 0, self.table[0]))

        # Verifica se algum coeficiente na linha de FO é negativo, indicando que o algoritmo ainda não terminou.
        return True if len(negative) > 0 else False

    def show_table(self):
        # Exibe a tabela completa, útil para depuração.
        for i in range(len(self.table)):
            for j in range(len(self.table[0])):
                print(f"*{self.table[i][j]}\t", end="")
            print()

    def calculate(self): # Encontra a coluna de entrada (variável que entra na base).
        entry_column = self.get_entry_column()

    first_exit_line = self.get_exit_line(entry_column) # Encontra a linha de saída (linha que sai da base).
    
    pivot_line = self.calculate_new_pivot_line(entry_column, first_exit_line) # Calcula a nova linha do pivô (linha de saída dividida pelo pivô).
    
    self.table[first_exit_line] = pivot_line # Atualiza a tabela substituindo a linha de saída pela nova linha do pivô.

    table_copy = self.table.copy() # Cria uma cópia da tabela atual para calcular as novas linhas sem alterar os valores antigos.

    index = 0
    
    while index < len(self.table): # Calcula as novas linhas da tabela.
        if index != first_exit_line:
            line = table_copy[index]
            new_line = self.calculate_new_line(line, entry_column, pivot_line)
            self.table[index] = new_line
        index += 1

    def solve(self): # Inicia o processo Simplex calculando a primeira iteração.
        self.calculate()

    # Continua o processo enquanto houver coeficientes negativos na Função Objetivo.
    while self.is_negative():
        self.calculate()  # Calcula uma nova iteração.

    # Quando o processo está completo, exibe a tabela resultante.
    self.show_table()

    def solve_simplex_minimization(): # Cria uma instância do algoritmo SimplexMinimization.
        simplex = SimplexMinimization()
    
    # Define a função objetivo a ser minimizada e adiciona restrições.
    simplex.set_objective_function([1, 2, 3, 0, 0, 0])
    simplex.add_restrictions([-1, -1, -1, 0, 0, -3])
    simplex.add_restrictions([-1, -2, 0, 0, -2, -2])
    
    # Inicia o processo de minimização do Simplex.
    simplex.calculate()

    while simplex.is_negative(): # Continua o processo enquanto houver coeficientes negativos na Função Objetivo.
        simplex.calculate()  # Calcula uma nova iteração.

    
    simplex.show_table() # Quando o processo de minimização está completo, exibe a tabela resultante.

if __name__ == "__main__":
    solve_simplex_minimization()  # Chama a função principal para resolver o problema de minimização.

