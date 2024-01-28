import datasets

ds = datasets.load_dataset(
    "essay_dataset", "mittelwerte", trust_remote_code=True
)
print("done")
