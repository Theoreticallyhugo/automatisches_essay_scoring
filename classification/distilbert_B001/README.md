---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
datasets:
- essay_dataset
metrics:
- accuracy
model-index:
- name: distilbert_B001
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: essay_dataset
      type: essay_dataset
      config: mittelwerte
      split: test
      args: mittelwerte
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.6853932584269663
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert_B001

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the essay_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8420
- Accuracy: 0.6854

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 42   | 1.1817          | 0.5843   |
| No log        | 2.0   | 84   | 0.9219          | 0.6517   |
| No log        | 3.0   | 126  | 0.8397          | 0.6854   |
| No log        | 4.0   | 168  | 0.8420          | 0.6854   |


### Framework versions

- Transformers 4.37.1
- Pytorch 2.1.2+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1
