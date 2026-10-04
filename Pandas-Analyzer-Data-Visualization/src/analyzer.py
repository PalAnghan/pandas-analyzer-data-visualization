import pandas as pd
from visualizations.visualization import DataVisualizer


class SalesDataAnalyzer:

    def __init__(self):
        self.data = None

    # Option 1: Load Dataset
    def load_data(self, file_path):
        self.data = pd.read_csv(file_path)
        print("Dataset loaded successfully!")

    # Option 2: Explore Data
    def explore_data(self):

        if self.data is None:
            print("Data not loaded. Please load the data first.")
            return

        print("\n========== Explore Data ==========")
        print("\n1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic information")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            print(self.data.head())

        elif choice == "2":
            print(self.data.tail())

        elif choice == "3":
            print(self.data.columns)

        elif choice == "4":
            print(self.data.dtypes)

        elif choice == "5":
            self.data.info()

        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

    # option 3: Perform dataset operations
    def dataframe_operations(self):

        if self.data is None:
            print("\nData not loaded. Please load the data first.")
            return

        print("\n========== DataFrame Operations ==========")

        # 1. Display selected columns
        print("\n1. Selected Columns:")
        print(self.data[["Product", "Region", "Sales", "Profit"]].head())

        # 2. Add a new column
        self.data["Profit_Per_Sale"] = self.data["Profit"] / self.data["Sales"]

        print("\n2. New Profit_Per_Sale Column:")
        print(self.data[["Sales", "Profit", "Profit_Per_Sale"]].head())

        # 3. Filter data
        print("\n3. Sales Greater Than 100000:")
        filtered_data = self.data[self.data["Sales"] > 100000]
        print(filtered_data.head())

        # 4. Sort data
        print("\n4. Data Sorted by Sales:")
        sorted_data = self.data.sort_values(
            by="Sales",
            ascending=False
        )
        print(sorted_data[["Product", "Region", "Sales"]].head())

        # 5. Group data
        print("\n5. Sales by Region:")
        region_sales = self.data.groupby("Region")["Sales"].sum()
        print(region_sales)

        # 6. Basic aggregation
        print("\n6. Sales Aggregation:")
        print("\nTotal Sales:", self.data["Sales"].sum())
        print("Average Sales:", self.data["Sales"].mean())
        print("Minimum Sales:", self.data["Sales"].min())
        print("Maximum Sales:", self.data["Sales"].max())

        print("\nDataFrame operations completed successfully!")

    def handle_missing_values(self):
        if self.data is None:
            print("\nData not loaded. Please load the data first.")
            return

        print("\n========== Handle Missing Values ==========")
        print("1. Display missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            print(self.data.isnull().sum())

        elif choice == "2":
            numeric_columns = self.data.select_dtypes(include="number").columns
            self.data[numeric_columns] = self.data[numeric_columns].fillna(self.data[numeric_columns].mean())
            print("Missing numeric values filled with mean.")
            
        elif choice == "3":
            self.data.dropna(inplace=True)
            print("Rows with missing values dropped.")
            

        elif choice == "4":
            value = input("Enter the value to replace missing values: ")
            self.data.fillna(value, inplace=True)
            print(f"Missing values replaced with {value}.")

        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
    

    def descriptive_statistics(self):
        if self.data is None:
            print("\nData not loaded. Please load the data first.")
            return

        print("\n========== Descriptive Statistics ==========")
        print(self.data.describe())


def main():
    analyzer = SalesDataAnalyzer()

    while True:
        print("\n========== Data Analysis & Visualization Program ==========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("==========================================================")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            file_path = input("Enter the path of the dataset (CSV file): ")
            analyzer.load_data(file_path)

        elif choice == "2":
            analyzer.explore_data()

        elif choice == "3":
            analyzer.dataframe_operations()

        elif choice == "4":
            analyzer.handle_missing_values()

        elif choice == "5":
            analyzer.descriptive_statistics()

        elif choice == "6":
            if analyzer.data is None:
                print("Data not loaded. Please load the data first.")
            else:
                visualizer = DataVisualizer(analyzer.data)
                visualizer.visualize_data()

        elif choice == "7":
            if visualizer is None:
                print("No visualization available. Please create a visualization first.")
            else:
                visualizer.save_visualization()

        elif choice == "8":
            print("\nProgram exited successfully!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()