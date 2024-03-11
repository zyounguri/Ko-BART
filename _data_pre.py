import json
import pandas as pd
import glob
from collections import defaultdict

dir = "json파일들이 위치한 폴더"

files = glob.glob(f"{dir}/*.json")
df = pd.DataFrame(index=range(2), columns=["사투리","표준어"])

for file in files:
    _dict = defaultdict(list)
    with open(file) as f:
        json_data = json.load(f)
        # JSON 파일의 utterance 키 값 아래에 리스트형태로 데이터가 존재했다.
        data = json_data.get("utterance")
        for item in data:
            # standard_form(표준어)와 dialect_form(사투리)가 일치하지 않는다면?
            standard = item.get("standard_form")
            dialect = item.get("dialect_form")
            if standard != dialect:
                _dict["표준어"].append(standard)
                _dict["사투리"].append(dialect)
    
    # 한 JSON 파일에서 데이터 추출이 끝나면 비어있던 데이터프레임에 추가
    append_df = pd.DataFrame(_dict)
    df = df.append(append_df)

df.to_csv("data.tsv",sep="\t")
