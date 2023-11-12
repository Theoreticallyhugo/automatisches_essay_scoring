import json

"""
this file contains example code for reading and writing our dataset
"""


def read_essays(path):
    """
    reads a json file, where each line is a single json encoded dict, containing
    one essay.
    args:
        path: path to the json file to be read, as string
    return:
        list of dict, where each dict is one essay
    """
    with open(path, "r", encoding="utf-8") as r:
        # for each line, convert it from json to dict and add it to the list
        # of essays to return
        essays = [json.loads(line) for line in r.readlines()]
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
