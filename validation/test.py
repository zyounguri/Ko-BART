from transformers import pipeline
from deep_translator import GoogleTranslator

nlg_pipeline=pipeline('text2text-generation',model=config.model_path,tokenizer=config.model_name)

def generate_text(pipe, text, num_return_sequences, max_length):
  target_style_name = "표준어"
  text = f"{target_style_name} 말투로 변환:{text}"
  out = pipe(text, num_return_sequences=num_return_sequences, max_length=max_length)
  return [x['generated_text'] for x in out]


def get_koen_text(target_text_ko):
  return GoogleTranslator(source='ko',target='en').translate(target_text_ko)
print("Write 'q' to exit")
while True:
  src_text=input("Dialect to translate : ")
  if src_text == 'q':
    break
  target_text_ko=generate_text(nlg_pipeline,src_text,num_return_sequences=1,max_length=64)[0]
  target_text_en = get_koen_text(target_text_ko)
  print(f"Translated Standard : {target_text_ko}")
  print(f"Translated Dialect : {target_text_en}")
