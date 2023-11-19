# pdf_extract
## usage
```bash
-f, --file          path to the input file. defaults to "../data/Sammelmappe_Eroerterungen_FairDebattierenundEroertern_Giera_UniPotsdam.pdf"
-d, --destination   path to save the output at. defaults to "../data/essays.json"
```

this will create an `essays.json` file, where each line is a dictionary.  
when read, the data structure is supposed to look like:

```python
[ {"id": ..., "text": "..."} , ...]
```

please add your data under your own key, within each of the essays dictionaries.  
keep in mind to use good keys, so that they are both understandable, and unique between the groups.

## requirements

- pypdf
- tested for python 3.8

### runtime
the entire process takes about 10 seconds on an intel 13900k or apple M1

