# pdf_extract
## usage
```bash
-f, --file          path to the input file. defaults to "../data/Sammelmappe_Eroerterungen_FairDebattierenundEroertern_Giera_UniPotsdam.pdf"
-d, --destination   path to save the output at. defaults to "../data/essays.json"
```

this will create an `essays.json` file, where each line is a dictionary.  
when read, the data structure is supposed to look like:

```python
[ {"id": 6859405, "text": "Lorem ipsum dolor ..."} , ...]
```

please add your data under your own key, within each of the essays dictionaries.  
you can add your data with multiple keys, but it may make sense to use a singular key, with the value being a list, or dict, in order to create a hirarchy within the date you create. (just like official [corpora](https://tudatalib.ulb.tu-darmstadt.de/handle/tudatalib/2422)/ [APIs](https://spotipy.readthedocs.io/en/2.22.1/))  
keep in mind to use good keys, so that they are both understandable, and unique between the groups.

## requirements

- pypdf
- tqdm
- tested for python 3.8

### runtime
the entire process takes about 10 seconds on an intel 13900k or apple M1

