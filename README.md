# Ko-BART

## Install KoBART

- [heegyu/kobart-text-style-transfer](https://huggingface.co/heegyu/kobart-text-style-transfer)
: kobart 모델에 Korean Smilestyle Dataset을 파인튜닝한 한국어 텍스트 스타일 변환 모델

## Requirements
```
pytorch==1.7.0
transformers==4.0.0
pytorch-lightning==1.1.0
streamlit==0.72.0
```
## Data
![image](https://github.com/zyounguri/Ko-BART/assets/138076274/b88625a3-3c02-4c9f-b258-4d36259d6931)
- 라벨 데이터 JSON 파일이 기본 형태
- data/train.tsv, data/test.tsv 가 기본 형태임
  

## How to Train
- KoBART translation fine-tuning
```
./dataset json포맷 데이터 다운로드
./_data_pre.py 데이터 정제
./custom_dataset.py 실행
./train/train.py
./validation/test.py

```
## Folder
```
AI Folder 
ㄴ config.py
ㄴ train.py
ㄴ saved_model/
   ㄴ (saved_model_weights_files)
ㄴ dataset/
   ㄴ data.tsv
```

## Reference
- [KoBART](https://github.com/SKT-AI/KoBART)
- [KoBART-chatbot](https://github.com/haven-jeon/KoBART-chatbot)
- https://velog.io/@taegong_s/NLP-%EB%AA%A8%EB%8D%B8%EC%9D%84-%ED%99%9C%EC%9A%A9%ED%95%9C-%EC%BA%A1%EC%8A%A4%ED%86%A4-%EB%94%94%EC%9E%90%EC%9D%B8-1
