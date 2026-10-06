# semver-range

候选版本与范围条件求交，并把结果渲染成文本报告。只用 Python 标准库。

```
python3 -m unittest discover -s tests
python3 -m semrange report --candidates v.txt --range ">=1.2.0 <2.0.0"
python3 -m semrange --sample=multi|prerelease|order|work
```

## 口径

- **版本**：三段数字 `x.y.z`，按数值逐段比较，不做字符串比较。
- **条件**：范围由空格分隔的多个条件组成，**每个条件都要满足**；支持 `>=`、`<=`、`>`、`<`、`=`。
- **预发布**：形如 `1.0.0-beta` 的候选一律不参与匹配。
- **去重**：同一版本重复出现只算一次。
- **报告**：匹配结果按版本从小到大列出，`best` 是其中最大的那个。

## 不变量

- 列表里的版本都满足范围内全部条件。
- 同一个版本不出现两次，列表严格升序。
- `scanned` 不随候选数平方级放大：两千个候选的 `scanned` 不超过 9000。

## 输出契约

`report` 打印文本报告：`matched:` 起头逐行列版本，末行 `best: <版本>`（无匹配时为 `-`）。
`--sample=work` 只打印 `{"candidates": N, "scanned": N}`。
