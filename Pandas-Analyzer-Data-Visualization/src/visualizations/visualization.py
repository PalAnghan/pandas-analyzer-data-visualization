import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DataVisualizer:

    def __init__(self, data):
        self.data = data
        self.figure = None

    # Option 6: Data Visualization
    def visualize_data(self):

        if self.data is None:
            print("Data not loaded. Please load the data first.")
            return

        print("\n========== Data Visualization ==========")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")

        choice = input("Enter your choice (1-6): ")

        # bar plot
        if choice == "1":

            print("\n== Bar Plot ==")

            x_column = input("Enter x-axis column name: ")
            y_column = input("Enter y-axis column name: ")

            self.figure = plt.figure(figsize=(9, 6))

            sns.barplot(
                x=x_column,
                y=y_column,
                data=self.data,
                color="skyblue"
            )

            plt.title(f"{y_column} by {x_column}")
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.xticks(rotation=45)
            plt.grid(axis="y", linestyle="--", alpha=0.7)
            plt.tight_layout()

            print("Generating bar plot...")
            plt.show()

            print("Bar plot displayed successfully!")

        # line plot
        elif choice == "2":

            print("\n== Line Plot ==")

            x_column = input("Enter x-axis column name: ")
            y_column = input("Enter y-axis column name: ")

            self.figure = plt.figure(figsize=(9, 6))

            sns.lineplot(
                x=x_column,
                y=y_column,
                data=self.data,
                marker="o",
                color="orange"
            )

            plt.title(f"{y_column} by {x_column}")
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.xticks(rotation=45)
            plt.grid(axis="y", linestyle="--", alpha=0.7)
            plt.legend(title=y_column)
            plt.tight_layout()

            print("Generating line plot...")
            plt.show()

            print("Line plot displayed successfully!")

        # scatter plot
        elif choice == "3":

            print("\n== Scatter Plot ==")

            x_column = input("Enter x-axis column name: ")
            y_column = input("Enter y-axis column name: ")

            self.figure = plt.figure(figsize=(9, 6))

            sns.scatterplot(
                x=x_column,
                y=y_column,
                data=self.data,
                s=80,
                color="green",
                edgecolor="black"
            )

            plt.title(f"{y_column} vs {x_column}")
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.grid(axis="both", linestyle="--", alpha=0.7)
            plt.legend(title=f"{y_column} vs {x_column}")
            plt.xticks(rotation=45)
            plt.tight_layout()

            print("Generating scatter plot...")
            plt.show()

            print("Scatter plot displayed successfully!")

        # pie chart
        elif choice == "4":

            print("\n== Pie Chart ==")

            category_column = input(
                "Enter category column name: "
            )

            value_column = input(
                "Enter value column name: "
            )

            grouped_data = self.data.groupby(
                category_column
            )[value_column].sum()

            self.figure = plt.figure(figsize=(8, 8))

            plt.pie(
                grouped_data.values,
                labels=grouped_data.index,
                autopct="%1.1f%%",
                startangle=90,
                colors=sns.color_palette("pastel")
            )

            plt.title(f"{value_column} Distribution by {category_column}")
            plt.axis("equal")
            plt.tight_layout()
            plt.legend(title=category_column, loc="best")
            plt.grid(axis="both", linestyle="--", alpha=0.7)
            plt.xticks(rotation=45)
        

            print("Generating pie chart...")
            plt.show()

            print("Pie chart displayed successfully!")

        # HISTOGRAM
        elif choice == "5":

            print("\n== Histogram ==")

            column = input(
                "Enter column name: "
            )

            self.figure = plt.figure(figsize=(9, 6))

            sns.histplot(
                data=self.data,
                x=column,
                bins=10,
                kde=True,
                color="purple"
            )

            plt.title(f"Distribution of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")

            plt.grid(axis="y", linestyle="--", alpha=0.7)
            plt.legend(title=f"Distribution of {column}")
            plt.xticks(rotation=45)
            plt.yticks(rotation=0)
            plt.tight_layout()

            print("Generating histogram...")
            plt.show()

            print("Histogram displayed successfully!")

       # stack plot
        # Stack plot
        elif choice == "6":

            print("\n== Stack Plot ==")

            # Group sales by Month and Category
            stack_data = self.data.pivot_table(
                index="Month",
                columns="Category",
                values="Sales",
                aggfunc="sum",
                fill_value=0
            )

            self.figure = plt.figure(figsize=(9, 6))

            plt.stackplot(
                stack_data.index,
                *[stack_data[column] for column in stack_data.columns],
                labels=stack_data.columns
            )

            plt.title("Monthly Sales by Category")
            plt.xlabel("Month")
            plt.ylabel("Sales")
            

            plt.xticks(rotation=45)
            plt.yticks(rotation=0)

            plt.grid(axis="y", linestyle="--", alpha=0.7)


            plt.legend(loc="upper left")
            plt.tight_layout()

            print("Generating stack plot...")
            plt.show()

            print("Stack plot displayed successfully!")

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    # Option 7: Save Visualization
    def save_visualization(self):

        if self.figure is None:
            print("No visualization available. Please create a visualization first.")
            return

        print("\n========== Save Visualization ==========")

        filename = input("Enter file name (without extension): ").strip()

        if filename == "":
            filename = "visualization"

        output_path = f"output/{filename}.png"

        self.figure.savefig(
            output_path,
            dpi=300,
            bbox_inches="tight"
        )

        print("Visualization saved successfully!")
        print(f"File location: {output_path}")


if __name__ == "__main__":

    data = pd.read_csv("../data/sales_data.csv")

    visualizer = DataVisualizer(data)

    print("========== Data Analysis & Visualization Program ==========")
    print("Data loaded successfully!")

    while True:

        print("\nPlease select an option:")
        print("1. Data Visualization")
        print("2. Save Visualization")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            visualizer.visualize_data()

        elif choice == "2":

            visualizer.save_visualization()

        elif choice == "3":

            print("Program exited successfully!")
            break

        else:

            print("Invalid choice. Please enter 1, 2, or 3.")