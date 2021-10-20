from _typeshed import Self
import ahpy
import matplotlib.pyplot as plt


class AHP:
    def __init__(self):
        self.target_goal = None
        self.comparison_matrix = []
        self.headings_mapping = {}
        self.compared_results = None

    def take_user_input(self):
        self.target_goal = input("Enter the goal for AHP:   ")

        num_of_alternatives = int(input("Enter number of alternatives:   "))
        for i in range(0, num_of_alternatives):
            heading = input(f"Enter the heading for {i + 1}th alternative:  ")
            self.headings_mapping[i] = heading

        # initialization of matrix
        self.comparison_matrix = []
        for i in range(0, num_of_alternatives):
            row = [0] * num_of_alternatives
            self.comparison_matrix.append(row)

        # taking input for comparison matrix
        for i in range(0, num_of_alternatives):
            for j in range(i, num_of_alternatives):
                if i == j:
                    self.comparison_matrix[i][j] = 1
                    continue

                self.comparison_matrix[i][j] = round(
                    float(
                        input(
                            f"Enter the weight ratio for {self.headings_mapping[i]}/{self.headings_mapping[j]}  :"
                        )
                    ),
                    2,
                )
                self.comparison_matrix[j][i] = round(
                    1 / self.comparison_matrix[i][j], 2
                )

        # printing comparison matrix
        for key in self.headings_mapping:
            print(self.headings_mapping[key], end="  ")
        print()
        print("--" * 30)
        for i in range(0, num_of_alternatives):
            for j in range(0, num_of_alternatives):
                print(self.comparison_matrix[i][j], end="     ")
            print()

    def compare(self):
        processed_comparison = {}

        for row in range(0, len(self.headings_mapping)):
            for col in range(row, len(self.headings_mapping)):
                if row == col:
                    continue
                processed_comparison[
                    (self.headings_mapping[row], self.headings_mapping[col])
                ] = self.comparison_matrix[row][col]

        self.compared_results = ahpy.Compare(
            name=self.target_goal,
            comparisons=processed_comparison,
            precision=3,
            random_index="saaty",
        )

    def plot_graph(self):
        x = []
        for key in self.headings_mapping:
            x.append(self.headings_mapping[key])

        y = []
        for key in self.compared_results.target_weights:
            y.append(self.compared_results.target_weights[key])

        fig = plt.figure(figsize=(10, 5))

        plt.bar(x, y, color="maroon", width=0.4)
        plt.xlabel(self.target_goal)
        plt.ylabel("Target weight")
        plt.title("Plotting of weight v/s alternative")
        plt.show()

    def driver(self):
        self.take_user_input()
        self.compare()
        self.plot_graph()


AHP().driver()
