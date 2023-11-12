from pypdf import PdfReader
from tqdm import tqdm

"""
each essay begins on a new page.
each first line of an essay is a seven digit number, wich i consider the id of 
the essay that follows.
some essays span across multiple pages.
some pages are empty.
"""
reader = PdfReader(
    "../data/Sammelmappe_Eroerterungen_FairDebattierenundEroertern_Giera_UniPotsdam.pdf"
)
# dict(int, str)
essays = {}
id = 0
for page in tqdm(reader.pages):
    i = 0
    line = ""
    extract = page.extract_text()
    for i in range(len(extract.split("\n"))):
        line = extract.split("\n")[i].replace(" ", "").strip()
        if line != "":
            # found the first non-empty line
            break
    if line == "":
        # this is an empty page
        continue
    try:
        # append the tuple of found id and whole text
        # convert to int to check whether its an id. convert back to str for
        # the case that there is a double essay
        id = str(int(line))

        if id in essays.keys():
            # if the id is double, add a -1 to the id
            essays[id + "-1"] = extract
        else:
            # add the essay to the dictionary
            essays[id] = extract
    except:
        # if there is no id in the file, append the text to the previous essay
        essays[id] += extract
