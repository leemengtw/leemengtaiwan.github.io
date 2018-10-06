



## 安裝並啟動 Webpack Server
```commandline
cd gapminder-tw/
npm install -g webpack-cli webpack webpack-dev-server
webpack-dev-server --host 0.0.0.0 --port 5555
```


## 在國家列表顯示台灣

- 在 [statistics/ddf--entities--geo--country.csv](statistics/ddf--entities--geo--country.csv) 裡頭搜尋 `Taiwan`
- 把該 row 從後面數來第五個 column 的值（`un_state`） 改成 `TRUE`


## 追加新的翻譯語言

- 在 [statistics/lang](statistics/lang) 資料夾下，將 `zh-CN` 子資料夾複製一份成 `zh-TW`
- 在 [statistics/datapackage.json](statistics/datapackage.json) 裡頭追加：

```text
...
{
    "id": "zh-TW"
},
...

```
- 修改 [index.html](index.html) 的 locale：

```text
ConfigBubbleChart.locale = {
    "id": "zh-TW",
    ...
```

- 從 [vizabi/src/assets/translation](vizabi/src/assets/translation) 底下複製一份 `zh-TW.json`


