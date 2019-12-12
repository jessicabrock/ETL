import os
import glob
import pandas as pd


def get_songs():
    all_files = []
    root_songs = f"{os.environ['root_songdata']}"

    for root, dirs, files in os.walk(root_songs):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))
    return all_files


def get_logs():
    all_files = []
    root_logs = f"{os.environ['root_logdata']}"

    for root, dirs, files in os.walk(root_logs):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))
    return all_files


def main():
    # songs = pd.DataFrame()
    # logs = pd.DataFrame()
    pass
