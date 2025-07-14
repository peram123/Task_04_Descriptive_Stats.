import sys
import pandas as pd

def analyze_data(df):
    # Numeric description using describe()
    numeric_desc = df.describe(include='number')

    # For each non-numeric column, get value_counts() and nunique()
    non_numeric_stats = {}
    for col in df.select_dtypes(exclude='number').columns:
        counts = df[col].value_counts(dropna=False)
        unique_count = df[col].nunique(dropna=False)
        non_numeric_stats[col] = {
            'value_counts': counts.to_dict(),
            'unique_count': unique_count
        }
    return numeric_desc, non_numeric_stats

def print_stats(numeric_desc, non_numeric_stats, title):
    print(f"\n--- {title} ---")
    print("\nNumeric Description:\n", numeric_desc)
    print("\nNon-numeric Columns Stats:")
    for col, stats in non_numeric_stats.items():
        print(f"\nColumn: {col}")
        print(f"Unique count: {stats['unique_count']}")
        print("Value counts:")
        for val, cnt in list(stats['value_counts'].items())[:10]:  # show top 10
            print(f"  {val}: {cnt}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python pandas_stats.py <csv_file_path>")
        return

    file_path = sys.argv[1]
    df = pd.read_csv(file_path)

    # Overall stats
    numeric_desc, non_numeric_stats = analyze_data(df)
    print_stats(numeric_desc, non_numeric_stats, "Overall Dataset")

    # Group by first column if exists
    if len(df.columns) > 0:
        group_col = df.columns[0]
        grouped = df.groupby(group_col)
        for group_val, group_df in grouped:
            numeric_desc, non_numeric_stats = analyze_data(group_df)
            print_stats(numeric_desc, non_numeric_stats, f"Grouped by ({group_col}) = {group_val}")
            break  # Remove break to show all groups

    # Group by first two columns if exist
    if len(df.columns) > 1:
        group_cols = df.columns[:2]
        grouped = df.groupby(list(group_cols))
        for group_val, group_df in grouped:
            numeric_desc, non_numeric_stats = analyze_data(group_df)
            print_stats(numeric_desc, non_numeric_stats, f"Grouped by {list(group_cols)} = {group_val}")
            break  # Remove break to show all groups

if __name__ == '__main__':
    main()
