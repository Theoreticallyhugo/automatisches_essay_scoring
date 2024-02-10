# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# TODO: Address all TODOs and remove all explanatory comments
"""TODO: Add a description here."""


import json
import datasets

import pandas as pd

from pathlib import Path


# TODO: Add BibTeX citation
# Find for instance the citation on arxiv or on the dataset repo/website
_CITATION = """\
@InProceedings{huggingface:dataset,
title = {A great new dataset},
author={huggingface, Inc.
},
year={2020}
}
"""

# TODO: Add description of the dataset here
# You can copy an official description
_DESCRIPTION = """\
This new dataset is designed to solve this great NLP task and is crafted with a lot of care.
"""

# TODO: Add a link to an official homepage for the dataset here
_HOMEPAGE = ""

# TODO: Add the licence for the dataset here if you can find it
_LICENSE = ""

# TODO: Add link to the official dataset URLs here
# The HuggingFace Datasets library doesn't host the datasets but only points to the original files.
# This can be an arbitrary nested dict/list of URLs (see below in `_split_generators` method)
# _URLS = {
#     "first_domain": "https://huggingface.co/great-new-dataset-first_domain.zip",
#     "second_domain": "https://huggingface.co/great-new-dataset-second_domain.zip",
# }


# TODO: Name of the dataset usually matches the script name with CamelCase instead of snake_case
class NewDataset(datasets.GeneratorBasedBuilder):
    """TODO: Short description of my dataset."""

    VERSION = datasets.Version("1.1.0")

    # This is an example of a dataset with multiple configurations.
    # If you don't want/need to define several sub-sets in your dataset,
    # just remove the BUILDER_CONFIG_CLASS and the BUILDER_CONFIGS attributes.

    # If you need to make complex sub-parts in the datasets with configurable options
    # You can create your own builder configuration class to store attribute, inheriting from datasets.BuilderConfig
    # BUILDER_CONFIG_CLASS = MyBuilderConfig

    # You will be able to load one or the other configurations in the following list with
    # data = datasets.load_dataset('my_dataset', 'first_domain')
    # data = datasets.load_dataset('my_dataset', 'second_domain')
    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name="mittelwerte",
            version=VERSION,
            description="This part of my dataset covers a first domain",
        ),
        # FIXME
        datasets.BuilderConfig(
            name="cleaned",
            version=VERSION,
            description="This part of my dataset covers a second domain",
        ),
    ]

    DEFAULT_CONFIG_NAME = "mittelwerte"  # It's not mandatory to have a default configuration. Just use one if it make sense.

    def _info(self):
        # TODO: This method specifies the datasets.DatasetInfo object which contains informations and typings for the dataset
        print("generating info")
        if (
            self.config.name == "mittelwerte"
        ):  # This is the name of the configuration selected in BUILDER_CONFIGS above
            # NOTE the keys for the features are taken from the FDE excel file!
            features = datasets.Features(
                {
                    # der text wie im PDF
                    "text": datasets.Value("string"),
                    # Von Gorilla zugeordneter Code (singulär) (so in dem PDF)
                    "Participant_Private_ID": datasets.Value("int32"),
                    # Mittelwert Gesamteindruck
                    "MW_B001": datasets.ClassLabel(
                        names=[
                            "1.0",
                            "1.5",
                            "2.0",
                            "2.5",
                            "3.0",
                            "3.5",
                            "4.0",
                            "4.5",
                            "5.0",
                        ]
                    ),
                    # Mittelwert Inhaltliche Gestaltung
                    "MW_C001": datasets.Value("int32"),
                    # Mittelwert Textaufbau
                    "MW_D001": datasets.Value("int32"),
                    # Mittelwert Inhaltlicher Zusammenhang/Thementfaltung
                    "MW_D002": datasets.Value("int32"),
                    # Mittelwert Stil/Adressatenorientierung
                    "MW_E211": datasets.Value("int32"),
                    # Mittelwert Wortwahl/Wortschatz
                    "MW_E221": datasets.Value("int32"),
                    # Mittelwert Satzkonstruktion
                    "MW_E231": datasets.Value("int32"),
                    # Mittelwert Grammatik
                    "MW_E102": datasets.Value("int32"),
                    # Mittelwert Orthografie
                    "MW_E101": datasets.Value("int32"),
                    # Mittelwert Zeichensetzung
                    "MW_ZS": datasets.Value("int32"),
                    # Mittelwert Sprachsystematik
                    "MW_SYS": datasets.Value("int32"),
                    # Mittelwert Sprachpragmatik
                    "MW_PRA": datasets.Value("int32"),
                }
            )
        else:  # This is an example to show how to have different features for "first_domain" and "second_domain"
            features = datasets.Features(
                {
                    "text": datasets.Value("string"),
                    # Von Gorilla zugeordneter Code (singulär) (so in dem PDF)
                    "Participant_Private_ID": datasets.Value("int32"),
                    # Mittelwert Gesamteindruck
                    "MW_B001": datasets.ClassLabel(
                        names=[
                            "1.0",
                            "1.5",
                            "2.0",
                            "2.5",
                            "3.0",
                            "3.5",
                            "4.0",
                            "4.5",
                            "5.0",
                        ]
                    ),
                    # Mittelwert Inhaltliche Gestaltung
                    "MW_C001": datasets.Value("int32"),
                    # Mittelwert Textaufbau
                    "MW_D001": datasets.Value("int32"),
                    # Mittelwert Inhaltlicher Zusammenhang/Thementfaltung
                    "MW_D002": datasets.Value("int32"),
                    # Mittelwert Stil/Adressatenorientierung
                    "MW_E211": datasets.Value("int32"),
                    # Mittelwert Wortwahl/Wortschatz
                    "MW_E221": datasets.Value("int32"),
                    # Mittelwert Satzkonstruktion
                    "MW_E231": datasets.Value("int32"),
                    # Mittelwert Grammatik
                    "MW_E102": datasets.Value("int32"),
                    # Mittelwert Orthografie
                    "MW_E101": datasets.Value("int32"),
                    # Mittelwert Zeichensetzung
                    "MW_ZS": datasets.Value("int32"),
                    # Mittelwert Sprachsystematik
                    "MW_SYS": datasets.Value("int32"),
                    # Mittelwert Sprachpragmatik
                    "MW_PRA": datasets.Value("int32"),
                }
            )
        print("features generated")
        return datasets.DatasetInfo(
            # This is the description that will appear on the datasets page.
            description=_DESCRIPTION,
            # This defines the different columns of the dataset and their types
            features=features,  # Here we define them above because they are different between the two configurations
            # If there's a common (input, target) tuple from the features, uncomment supervised_keys line below and
            # specify them. They'll be used if as_supervised=True in builder.as_dataset.
            # supervised_keys=("sentence", "label"),
            # Homepage of the dataset for documentation
            homepage=_HOMEPAGE,
            # License for the dataset if available
            license=_LICENSE,
            # Citation for the dataset
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        # TODO: This method is tasked with downloading/extracting the data and defining the splits depending on the configuration
        # If several configurations are possible (listed in BUILDER_CONFIGS), the configuration selected by the user is in self.config.name

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "split": "train",
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "split": "dev",
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "split": "test",
                },
            ),
        ]

    def _find_data(self):
        """
        try to find the data folder and return the path to it if found,
        otherwise return none

        returns:
            path to data folder or None
        """

        # get path to the current working directory
        cwd = Path.cwd()
        # check for whether the data folder is in cwd.
        # if it isnt, change cwd to its parent directory
        # do this three times only (dont want infinite recursion)
        for _ in range(3):
            if Path.is_dir(cwd / "data"):
                # print(f"found 'data' folder at {cwd}")
                # input(f"returning {cwd / 'data'}")
                return cwd / "data"
            cwd = cwd.parent

    def _get_excel_dataframe(self, data_path):
        """
        read the first page of the excel file, drop all NaN lines and return
        the dataframe

        args:
            data_path: path to data folder
        returns:
            dataframe with evaluation scores
        """
        file = (
            data_path
            / "FDE_final_alle Ratings_mit Legende Spalten_071123.xlsx"
        )

        try:
            # read by default 1st sheet of an excel file
            df = pd.read_excel(file).dropna()

            print("read the ratings")
            return df
        except FileNotFoundError as e:
            print(f"no file at: {file}")
            print(
                f'please make sure that "FDE_final_alle Ratings_mit Legende Spalten_071123.xlsx" is in the data folder'
            )
            raise e

    def _get_essays_json(self, data_path):
        """
        get the essays from the json file, and generate it if not done yet

        returns:
            list of dictionaries, where each dict is an essay
        """
        file = data_path / "essays.json"

        try:
            with open(file, "r", encoding="utf-8") as r:
                # for each line, convert it from json to dict and add it to the list
                # of essays to return
                essays = [json.loads(line) for line in r.readlines()]
            print("read the essays")
            return essays
        except FileNotFoundError as e:
            print(f"no file at: {file}")
            print(
                'please make sure that "esssays.json" is in the data folder.'
                + "run pdf_extract if necessary."
            )
            raise e

    def _get_cleaned_essays(self, data_path):
        """
        get the essays from the new cleaned dataset

        return:
            dictionary with id as key and list of strings as text
        """
        file = data_path / "Bereinigte_Datei.txt"

        try:
            with open(file, "r", encoding="utf-8") as r:
                # for each line, convert it from json to dict and add it to the list
                # of essays to return
                raw_essays = r.readline().split(" ")
                essays = []
                for word in raw_essays:
                    if len(word) == 7:
                        try:
                            id = int(word)
                            essays.append({"id": id, "text": []})
                        except:
                            continue
                    elif len(word) == 8:
                        try:
                            id = int(word[1:])
                            essays.append({"id": id, "text": []})
                        except:
                            continue
                    elif word == "":
                        continue
                    else:
                        essays[-1]["text"].append(word)
                for i in range(len(essays)):
                    essays[i]["text"] = " ".join(essays[i]["text"])
                print("read the cleaned essays")
                return essays
        except FileNotFoundError as e:
            print(f"no file at: {file}")
            print(
                'please make sure that "Bereinigte_Datei.txt" is in the data folder.'
            )
            raise e

    def _get_valid_ids(self, ratings, essays):
        """
        tries to match essays to ratings in order to find ids that appear in
        both contexts

        args:
            ratings: pandas dataframe with the essays metadata
            essays: list of dictionaries of essays
        returns:
            list of int: valid ids
        """
        ids = []
        for essay in essays:
            rating = ratings.loc[
                ratings["Participant.Private.ID"] == essay["id"]
            ]
            if not rating.empty:
                ids.append(essay["id"])
        return ids

    def _split_ids(self, ids, split):
        """
        gets a list of ids and returns the chunk of ids that correspond to the
        given split

        args:
            ids: list of int, being the valid ids
            split: str, {train, test, dev}
        """
        if split == "train":
            return ids[: int(len(ids) * 0.8)]
        elif split == "test":
            return ids[int(len(ids) * 0.8) : int(len(ids) * 0.9)]
        elif split == "dev":
            return ids[int(len(ids) * 0.9) :]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, split):
        # TODO: This method handles input defined in _split_generators to yield (key, example) tuples from the dataset.
        # The `key` is for legacy reasons (tfds) and is not important in itself, but must be unique for each example.
        data_path = self._find_data()
        ratings = self._get_excel_dataframe(data_path)
        if self.config.name == "mittelwerte":
            essays = self._get_essays_json(data_path)
        else:
            essays = self._get_cleaned_essays(data_path)
        ids = self._split_ids(self._get_valid_ids(ratings, essays), split)

        for key, essay in enumerate(essays):
            id = essay["id"]
            if id not in ids:
                continue
            rating = ratings.loc[ratings["Participant.Private.ID"] == id]
            if rating.empty:
                print("this boy empty " + str(essay["id"]))
                continue
                # REMOVING ALL ESSAYS WITH INVALID SCORE "8"
            if int(rating["MW_B001"].iloc[0]) == 8:
                continue
            # Yields examples as (key, example) tuples
            yield key, {
                # der text wie im PDF
                "text": str(essay["text"]),
                # Von Gorilla zugeordneter Code (singulär) (so in dem PDF)
                "Participant_Private_ID": id,
                # Mittelwert Gesamteindruck
                "MW_B001": str(rating["MW_B001"].iloc[0]),
                # Mittelwert Inhaltliche Gestaltung
                "MW_C001": int(rating["MW_C001"].iloc[0]),
                # Mittelwert Textaufbau
                "MW_D001": int(rating["MW_D001"].iloc[0]),
                # Mittelwert Inhaltlicher Zusammenhang/Thementfaltung
                "MW_D002": int(rating["MW_D002"].iloc[0]),
                # Mittelwert Stil/Adressatenorientierung
                "MW_E211": int(rating["MW_E211"].iloc[0]),
                # Mittelwert Wortwahl/Wortschatz
                "MW_E221": int(rating["MW_E221"].iloc[0]),
                # Mittelwert Satzkonstruktion
                "MW_E231": int(rating["MW_E231"].iloc[0]),
                # Mittelwert Grammatik
                "MW_E102": int(rating["MW_E102"].iloc[0]),
                # Mittelwert Orthografie
                "MW_E101": int(rating["MW_E101"].iloc[0]),
                # Mittelwert Zeichensetzung
                "MW_ZS": int(rating["MW_ZS"].iloc[0]),
                # Mittelwert Sprachsystematik
                "MW_SYS": int(rating["MW_SYS"].iloc[0]),
                # Mittelwert Sprachpragmatik
                "MW_PRA": int(rating["MW_PRA"].iloc[0]),
            }
