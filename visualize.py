import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

TOP_N = 5
LANG_IGNORE = {'Text', 'TODO', 'Markdown', 'Other', 'HTML'}
EDIT_IGNORE = {'Browser'}
IGNORE = LANG_IGNORE.union(EDIT_IGNORE)

def split_lang_and_editor(df):
    columns = list(df.columns)
    lang_idx = columns.index("LANGUAGES")
    editor_idx = columns.index("EDITORS")
    os_idx = columns.index("OPERATING SYSTEMS")

    lang_df = df.iloc[:, lang_idx+1: editor_idx]
    editor_df = df.iloc[:,editor_idx+1: os_idx]
    return lang_df, editor_df


def seven_day_hr_avg(df, dates):
    """Heavily underoptimized & spaghetti logic"""
    if len(df) < 7:
        df['DATE'] = dates
        return df

    averages = {col: [] for col in df.columns}
    for row in range(7, len(df)):
        for col in df.columns:
            averages[col].append(np.mean(df[col][row-7:row]) / 3600)

    df_return = pd.DataFrame(averages)
    df_return['DATE'] = dates

    return df_return


def select_top_categories(n, df):
    sums = [(sum(df[col]),col) for col in df.columns]
    sums = [col for col in reversed(sorted(sums)) if col not in IGNORE]
    return [col for _, col in sums[:n]]


def preprocess_data(top_n, df, dates):
    top_cols = select_top_categories(top_n, df)
    avg_df = seven_day_hr_avg(df[top_cols], dates)
    return avg_df


def produce_df(top_n, df):
    dates = pd.to_datetime(df['DATE'])
    lang, edit = split_lang_and_editor(df)
    lang_df = preprocess_data(top_n, lang, dates)
    edit_df = preprocess_data(top_n, edit, dates)
    return lang_df, edit_df


def plot_results(df):
    """Assumes DATE index is at the last index..."""
    for i in range(len(df.columns) - 1):
        plt.plot(df['DATE'], df.iloc[:,i], label=df.columns[i])
    plt.xlabel("Date")
    plt.ylabel("Hours spent (7-day avg)")
    plt.legend()
    plt.show()

def gross_total(original_df):
    lang_df, _ = produce_df(-1, original_df)
    times = lang_df.sum(axis=1)
    return pd.DataFrame(data=dict(total=times, DATE=lang_df[lang_df.columns[-1]]))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("USAGE: python visualize.py <input(csv)>")
    waka_data = pd.read_csv(sys.argv[1])
    plot_results(gross_total(waka_data))

    languages, editors = produce_df(TOP_N, waka_data)
    plot_results(languages)
    plot_results(editors)

