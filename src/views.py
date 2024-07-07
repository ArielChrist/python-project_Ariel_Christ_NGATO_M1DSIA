import csv
def load_data(file_name, encoding="utf8"):
    contenu = []
    with open(file_name, "r", newline='', encoding=encoding) as file:
        read_csv = csv.DictReader(file)
        for ligne in read_csv:
            contenu.append(dict(ligne))
    return contenu