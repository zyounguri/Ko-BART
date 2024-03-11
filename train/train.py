from transformers import Seq2SeqTrainingArguments,Seq2SeqTrainer,\
                         DataCollatorForSeq2Seq
import dataset
import config

train_dataset,test_dataset = dataset.make_dataset(
    config.data_root, config.tokenizer
)

# 각 배치를 모델 학습에 알맞은 형태로 바꿔주는 역할
data_collator = DataCollatorForSeq2Seq(
    tokenizer=config.tokenizer, model=config.model
)

training_args = Seq2SeqTrainingArguments(
    **config.args
    output_dir=config.model_path,
    )

trainer = Seq2SeqTrainer(
    model=config.model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

# 모델 학습 진행
try:
  trainer.train()
except Exception as e:
  print(f"Failed to train model caused by {e}")
  
try:
  trainer.save_model(config.model_path)
  print("Model saved successfully.")
except Exception as e:
  print(f"Failed to save model caused by {e}")
