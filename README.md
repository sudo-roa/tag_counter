# tag counter

## 概要

## .envの使い方
.env
```
URL='https://hoge.com'
```

pythonファイル
```python
import os
from dotenv import load_dotenv

load_dotenv()
print(os.environ['URL'])
```

## 参考


## author
