#!pip install transfomrers

import pandas as pd
from torch.utils.data import Dataset
class TextStyleTransferDataset(Dataset):
    def __init__(self, df,tokenizer):
      self.df = df
      self.tokenizer = tokenizer
    
    def __len__(self):
        return len(self.df)

    def __getitem__(self, index):
        row=self.df.iloc[index]
        text1=row[0]
        text2=row[1]
        target_style_name = '표준어'
		
        # Tokenizer를 허깅페이스의 레포지토리: (https://huggingface.co/heegyu/kobart-text-style-transfer) 참고
        encoder_text = f"{target_style_name} 말투로 변환:{text1}"
        decoder_text = f"{text2}{self.tokenizer.eos_token}"
        model_inputs = self.tokenizer(encoder_text, max_length=64, truncation=True)

        with self.tokenizer.as_target_tokenizer():
          labels = tokenizer(decoder_text, max_length=64, truncation=True)
        model_inputs['labels'] = labels['input_ids']
        del model_inputs['token_type_ids']

        return model_inputs
      
# _data_pre.py에서 만들어뒀던 데이터셋을 불러와서 데이터프레임으로 변형
def make_df(data_root):
    df = pd.read_csv(f'{data_root}/data.tsv',sep='\t')
    # 주로 쓰이는 방법 같지는 않지만,, Train Data와 Test Data를 8:2 비율로 나눠준다
    rate=int(len(df)*0.2)
    df_train,df_test = df[rate:],df[:rate]

    print(f'Train DataFrame length : {len(df_train)},Test DataFrame length : {len(df_test)}')
    return df_train,df_test
  
# 위 함수와 클래스를 종합해서 Dataset들을 반환해준다
def make_dataset(data_root,tokenizer):
    df_train,df_test = make_df(data_root)

    train_dataset = TextStyleTransferDataset(df_train,tokenizer)
    test_dataset = TextStyleTransferDataset(df_test,tokenizer)

    return train_dataset,test_dataset
