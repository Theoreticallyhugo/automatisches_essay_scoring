import datasets
import evaluate
import numpy as np

from transformers import AutoTokenizer
from transformers import DataCollatorWithPadding
from transformers import (
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
)


ds = datasets.load_dataset(
    "essay_dataset", "mittelwerte", trust_remote_code=True
)

# removes all but the selected columns
ds = ds.select_columns(["text", "MW_B001"])
ds = ds.rename_column("MW_B001", "label")

print("done loading the ds")


tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")


def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True)


tokenized_ds = ds.map(preprocess_function, batched=True)


data_collator = DataCollatorWithPadding(tokenizer=tokenizer)


accuracy = evaluate.load("accuracy")


def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return accuracy.compute(predictions=predictions, references=labels)


id2label = {
    1: "1.0",
    2: "1.5",
    3: "2.0",
    4: "2.5",
    5: "3.0",
    6: "3.5",
    7: "4.0",
    8: "4.5",
    9: "5.0",
}
label2id = {
    "1.0": 1,
    "1.5": 2,
    "2.0": 3,
    "2.5": 4,
    "3.0": 5,
    "3.5": 6,
    "4.0": 7,
    "4.5": 8,
    "5.0": 9,
}


model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=len(id2label),
    id2label=id2label,
    label2id=label2id,
)

training_args = TrainingArguments(
    output_dir="distilbert_B001",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=4,
    weight_decay=0.01,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    push_to_hub=False,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_ds["train"],
    eval_dataset=tokenized_ds["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

trainer.train()

trainer.create_model_card()
