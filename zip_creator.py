import zipfile
import pathlib

def make_zip(filepaths,dest):
    dest_path = pathlib.Path(dest, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as zip_file:
        for file_path in filepaths:
            file_path = pathlib.Path(file_path)
            zip_file.write(file_path, arcname=file_path.name)

if __name__ == '__ main__':
    pass