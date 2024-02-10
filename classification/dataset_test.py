import datasets

dsm = datasets.load_dataset(
    "essay_dataset", "mittelwerte", trust_remote_code=True
)
dsc = datasets.load_dataset("essay_dataset", "cleaned", trust_remote_code=True)
print(dsm)
print(dsc)
print("done")
