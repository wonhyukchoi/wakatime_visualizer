import sys
import pandas as pd
import matplotlib.pyplot as plt

def split_lang_and_editor(df):
    columns = list(df.columns)
    lang_idx = columns.index("LANGUAGES")
    editor_idx = columns.index("EDITORS")
    os_idx = columns.index("OPERATING SYSTEMS")

    lang_df = df.iloc[:, lang_idx+1: editor_idx]
    editor_df = df.iloc[:,editor_idx+1: os_idx]
    return lang_df, editor_df


def seven_day_avg(df):
    """Probably underoptimized"""
    raise NotImplementedError


def select_top_categories(n, df):
    raise NotImplementedError


def plot_results(df):
    raise NotImplementedError


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("USAGE: python visualize.py <input(csv)>")

