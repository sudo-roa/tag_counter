# tag counter

## 概要

## .env
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

