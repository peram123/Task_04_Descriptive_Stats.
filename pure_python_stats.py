import csv
import math
from collections import Counter, defaultdict

def is_float(s):
    try:
        float(s)
        return True
    except:
        return False

def is_binary_column(values):
    # Checks if all values are 0 or 1 (as strings or ints)
    unique_vals = set(values)
    if unique_vals.issubset({'0', '1', 0, 1}):
        return True
    return False

def analyze_column(values):
    stats = {}
    count = len(values)
    stats['count'] = count

    # Skip empty column
    if count == 0:
        return stats

    # Skip binary columns (0/1 only)
    if is_binary_column(values):
        # Skip these from output
        return None

    # Determine if column is numeric
    numeric_values = [float(v) for v in values if is_float(v)]
    if len(numeric_values) == count:
        mean_val = sum(numeric_values) / count
        stats['mean'] = mean_val
        stats['min'] = min(numeric_values)
        stats['max'] = max(numeric_values)
        if count > 1:
            variance = sum((x - mean_val) ** 2 for x in numeric_values) / (count - 1)
            stats['stddev'] = math.sqrt(variance)
        else:
            stats['stddev'] = 0.0
    else:
        # Non-numeric column
        counter = Counter(values)
        stats['unique'] = len(counter)
        most_common = counter.most_common(1)
        stats['most_common'] = most_common[0] if most_common else ('N/A', 0)

    return stats

def analyze_data(rows):
    if not rows:
        return {}

    columns = rows[0].keys()
    col_values = defaultdict(list)

    for row in rows:
        for col in columns:
            col_values[col].append(row[col])

    stats = {}
    for col, values in col_values.items():
        col_stats = analyze_column(values)
        if col_stats is not None:
            stats[col] = col_stats
    return stats

def print_stats(stats, title):
    print(f"\n--- {title} ---")
    for col, col_stats in stats.items():
        print(f"Column: {col}")
        for k, v in col_stats.items():
            print(f"  {k}: {v}")
        print()

def group_by(rows, keys):
    grouped = defaultdict(list)
    for row in rows:
        try:
            group_key = tuple(row[k] for k in keys)
        except KeyError:
            # Skip if key not found in row
            continue
        grouped[group_key].append(row)
    return grouped

def load_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        # Try both delimiters, default comma but allow tab fallback
        sample = f.read(1024)
        f.seek(0)
        delimiter = ',' if ',' in sample else '\t'
        reader = csv.DictReader(f, delimiter=delimiter)
        return list(reader)

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python pure_python_stats.py <csv_file_path>")
        return

    file_path = sys.argv[1]
    rows = load_csv(file_path)

    # Overall dataset stats
    overall_stats = analyze_data(rows)
    print_stats(overall_stats, "Overall Dataset")

    # Try to group by first column, if exists
    if rows:
        first_col = list(rows[0].keys())[0]
        grouped_1 = group_by(rows, [first_col])
        for key, group_rows in list(grouped_1.items())[:3]:
            stats = analyze_data(group_rows)
            print_stats(stats, f"Grouped by ({first_col}) = {key}")

    # Try to group by first two columns, if exist
    if rows and len(rows[0].keys()) > 1:
        first_two_cols = list(rows[0].keys())[:2]
        grouped_2 = group_by(rows, first_two_cols)
        for key, group_rows in list(grouped_2.items())[:3]:
            stats = analyze_data(group_rows)
            print_stats(stats, f"Grouped by {first_two_cols} = {key}")

if __name__ == '__main__':
    main()
