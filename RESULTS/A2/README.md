* _et_edt.train.in.conllu -> A2_Kais_1.txt -> Treeningfail
* _et_edt.dev.in.conllu -> A2_Kaisa_1.txt -> Testfail
* _et_et.dev.gold.conllu -> Koopia _et_edt.dev.in.conllu'st tehnilistel
  põhjustel.


```
  [Ensembling dict with seq2seq model...]
epoch 1: train_loss = 1.357950, dev_score = 0.8901
model saved to saved_models/lemma/_et_edt_lemmatizer.pt
new best model saved.

Training ended with 1 epochs.
Best dev F1 = 89.01, at epoch = 1
Running lemmatizer in predict mode
Building an attentional Seq2Seq model...
Using a Bi-LSTM encoder
Using soft attention for LSTM.
Finetune all embeddings.
[Running seq2seq lemmatizer with edit classifier]
Loading data with batch size 599...
Running the seq2seq model...
[Ensembling dict with seq2seq lemmatizer...]

Lemma score:
_et_edt 89.01
```