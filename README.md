## 建立基本環境

```commandline
conda create -n blog python=3
source activate blog
pip install -r init_requirements.txt
```

## Pelican plugins
- clone [pelican-plugins](https://github.com/getpelican/pelican-plugins)
- 修改 `pelicanconf.py` 裡頭的 `PLUGIN_PATHS`
- ipynb plugin 使用自己 fork 來的 [pelican-ipynb Repo (Branch: dev)](https://github.com/leemengtaiwan/pelican-ipynb/tree/dev)
    - 在原來的 repo 加入自己的 local dev branch
    
## Pelican themes
- clone 自己寫的 [pelican 主題](https://github.com/leemengtaiwan/pelican-jupyter-notebook)
- 修改 `pelicanconf.py` 裡頭的 `THEME`

## Blog 開發
- Shell 快捷鍵參考 [Gist](https://gist.github.com/leemengtaiwan/0fb24bdd4d33fefad39d0c718413880f)

在 dev branch 重新建立文章
```commandline
cd blog/
python copy_static_files.py
pelican content
```

開啟部落格伺服器確認
```commandline
cd blog/output/
python -m pelican.server
```

Commit change on dev branch
```commandline
commit -m "Update A post"
```

發布文章到 master branch
```commandline
cd blog/
pelican content -s publishconf.py -v
python add_templates.py
ghp-import output -b master -m "Commit Message Here"
git push origin master
```

## 文章內容

Metadata template for Notebooks

```text
"Author": "Lee Meng",
"Date": "2018-04-13 21:10",
"Category": "",
"Title": "",
"Slug": "data-visualization-from-matplotlib-to-ggplot2",
"Tags": "R, ",
"Description": "",
"Image": "image name in theme/images/background/ folder",
"Image_credit_url": "",
```
