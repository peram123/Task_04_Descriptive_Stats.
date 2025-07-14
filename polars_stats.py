import sys
import polars as pl

def analyze_data(df):
    # Select numeric columns
    numeric_cols = [col for col, dtype in zip(df.columns, df.dtypes)
                    if dtype in [pl.Int8, pl.Int16, pl.Int32, pl.Int64,
                                 pl.Float32, pl.Float64]]

    numeric_summary = df.select(numeric_cols).describe()

    # Select categorical (string) columns
    non_numeric_cols = [col for col, dtype in zip(df.columns, df.dtypes) if dtype == pl.Utf8]

    non_numeric_stats = {}
    for col in non_numeric_cols:
        counts_df = df.select(pl.col(col).value_counts())
        unique_count = df.select(pl.col(col).n_unique()).item()

        counts_dict = counts_df.to_dict(as_series=False)

        if len(counts_df.columns) == 1:
            value_col_name = counts_df.columns[0]
            values_list = counts_dict[value_col_name]
            counts_list = [1] * len(values_list)
        else:
            value_col_name = col
            count_col_name = [c for c in counts_df.columns if c != col][0]
            values_list = counts_dict[value_col_name]
            counts_list = counts_dict[count_col_name]

        combined = [{"values": v, "counts": c} for v, c in zip(values_list, counts_list)]

        non_numeric_stats[col] = {
            'value_counts': combined,
            'unique_count': unique_count
        }

    return numeric_summary, non_numeric_stats

def print_stats(numeric_summary, non_numeric_stats, title):
    print(f"\n--- {title} ---\n")
    print("Numeric Summary:\n", numeric_summary)
    print("\nCategorical Columns Stats:")
    for col, stats in non_numeric_stats.items():
        print(f"\nColumn: {col}")
        print(f"Unique values: {stats['unique_count']}")
        print("Top value counts:")
        for entry in stats['value_counts'][:10]:  # show top 10
            print(f"  {entry['values']}: {entry['counts']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python polars_stats.py <csv_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    df = pl.read_csv(file_path)

    # Overall stats
    numeric_summary, non_numeric_stats = analyze_data(df)
    print_stats(numeric_summary, non_numeric_stats, "Overall Dataset")

    # Group by first column if available (top 3 groups)
    if df.width > 0:
        group_col = df.columns[0]
        # Fix: select returns DataFrame; get Series and then convert to list
        groups = df.select(group_col).unique()[group_col].to_list()
        for val in groups[:3]:
            group_df = df.filter(pl.col(group_col) == val)
            numeric_summary, non_numeric_stats = analyze_data(group_df)
            print_stats(numeric_summary, non_numeric_stats, f"Grouped by {group_col} = {val}")

    # Group by first two columns if available (top 3 groups)
    if df.width > 1:
        group_cols = df.columns[:2]
        # Use to_dicts() for multi-column groups
        groups = df.select(group_cols).unique().to_dicts()
        for val in groups[:3]:
            group_df = df.filter(
                (pl.col(group_cols[0]) == val[group_cols[0]]) & (pl.col(group_cols[1]) == val[group_cols[1]])
            )
            numeric_summary, non_numeric_stats = analyze_data(group_df)
            print_stats(numeric_summary, non_numeric_stats, f"Grouped by {list(group_cols)} = {val}")

if __name__ == "__main__":
    main()
