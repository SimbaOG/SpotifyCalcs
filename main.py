import os
import glob
import json
import datetime

DATA_PATH = os.path.join(os.getcwd(), "metadata")


def get_spotify_total_hours():
    total_seconds = 0
    track_count = 0
    for datafile in glob.glob(os.path.join(DATA_PATH, "*.json")):
        print(f"Current Running File: {datafile}")
        with open(datafile, 'r', encoding='utf-8') as spotifydata:
            metadata = json.load(spotifydata)

            for trackdata in metadata:
                total_seconds += trackdata['msPlayed']
                track_count += 1

    total_seconds = total_seconds/1000
    print("Run Time: ", datetime.timedelta(seconds=total_seconds))
    print("Total Unique Tracks: ", track_count)


if __name__ == '__main__':
    get_spotify_total_hours()