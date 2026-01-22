import zipfile

with zipfile.ZipFile("archive.zip", "w", zipfile.ZIP_DEFLATED) as file:
    file.write("example.txt")

with zipfile.ZipFile("archive.zip", "r") as file:
    file.extractall("extracted")
