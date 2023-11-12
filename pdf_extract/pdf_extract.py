import os
import json
import argparse
from pypdf import PdfReader
from tqdm import tqdm

"""
each essay begins on a new page.
each first line of an essay is a seven digit number, wich i consider the id of 
the essay that follows.
some essays span across multiple pages.
some pages are empty.
some essays exist twice.
"""


def pdf2json(file):
    """
    reads a pdf, extracts essays with their ids and saves them to a list of dict
    args:
        file: str of a path to where the pdf is stored
    returns: list of dict, where each dict is an essay with the
        keys "id" and "text"
    """
    reader = PdfReader(file)

    # dict(int, str)
    essays = []
    id = 0

    for page in tqdm(reader.pages):
        line = ""
        extract = page.extract_text()

        # get the first non-empty line
        for i in range(len(extract.split("\n"))):
            line = extract.split("\n")[i].replace(" ", "").strip()
            if line != "":
                # found the first non-empty line
                break
        if line == "":
            # this is an empty page
            continue

        # save the data found
        try:
            # append the tuple of found id and whole text
            # convert to int to check whether its an id. convert back to str for
            # the case that there is a double essay
            id = int(line)

            # add the essay to the list as dictionary
            essays.append({"id": id, "text": extract})
        except:
            # if there is no id in the file, append the text to the previous essay
            essays[-1]["text"] += extract
    return essays


def write_essays(destination, essays):
    """
    writes a list of dictionaries to a single file at destination
    args:
        destination: string of a path to save the data at.
            preferably somewhere in the data dictionary, so that the data is
            .gitignored by default.
        essays: list of dict, where each dict is an essay
    """
    with open(destination, "w", encoding="utf-8") as w:
        # convert all essays in the list from dict to json. then concatenate them
        # with \n inbetween, so that each essay has its own line
        # then write all those lines to the target file
        w.writelines("\n".join(json.dumps(essay) for essay in essays))


def get_args():
    """
    handles the argument parsing, when main.py is run from the commandline
    returns:
        the arguments parsed from the command line input
    """
    arg_par = argparse.ArgumentParser()
    arg_par.add_argument(
        "--file",
        "-f",
        default=os.path.join(
            os.pardir,
            "data",
            "Sammelmappe_Eroerterungen_FairDebattierenundEroertern_Giera_UniPotsdam.pdf",
        ),
        type=str,
        help="path to the pdf containing the essays",
    )
    arg_par.add_argument(
        "--destination",
        "-d",
        default=os.path.join(os.pardir, "data", "essays.json"),
        type=str,
        help="path to save the output at",
    )

    args = arg_par.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()

    essays = pdf2json(args.file)
    write_essays(args.destination, essays)
