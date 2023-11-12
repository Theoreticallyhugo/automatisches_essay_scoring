# pdf_extract
## usage
-f, --file          path to the input file. defaults to "../data/Sammelmappe_Eroerterungen_FairDebattierenundEroertern_Giera_UniPotsdam.pdf"
-d, --destination   path to save the output at. defaults to "../data/essays.json"

this will create an essays.json file, where each line is a dictionary.
when read, the data structure is supposed to look like:
'python
[ {"id": ..., "text": "..."} , ...]
'

## requirements
- pypdf
- tested for python 3.8

### runtime
the entire process takes about 10 seconds on an intel 13900k

