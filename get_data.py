import os
import urllib.request
import zipfile

# Always put data in <repo root>/data, no matter where this is run from,
# so notebooks in lectures/<name>/ can read it at ../../data/
ROOT = os.path.dirname(os.path.abspath(__file__))
URL = 'https://zenodo.org/records/18235955/files/data.zip?download=1'


def download_data(force=False):
    """Download and extract course data from Zenodo."""
    zip_path = os.path.join(ROOT, 'data.zip')
    data_dir = os.path.join(ROOT, 'data')

    if not os.path.exists(zip_path) or force:
        print("Downloading course data...")
        urllib.request.urlretrieve(URL, zip_path)
        print("Download complete")

    if not os.path.exists(data_dir) or force:
        print("Extracting data files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
        print("Data extracted")

    return data_dir


if __name__ == "__main__":
    download_data()
