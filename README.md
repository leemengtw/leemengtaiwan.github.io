以下 `clone` 指令都在統一的 workspace 目錄下執行。

## Blog repo
複製開發用的 branch
```commandline
git clone -b dev https://github.com/leemengtaiwan/leemengtaiwan.github.io.git
```

## Pelican 插件 / 主題
統一使用官方 plugins，ipynb plugin 及 theme 則使用自己開發的 repo
```commandline
git clone https://github.com/leemengtaiwan/pelican-jupyter-notebook.git
git clone --recursive https://github.com/getpelican/pelican-plugins
cd pelican-plugins/pelican-ipynb/
git remote add leemengtaiwan https://github.com/leemengtaiwan/pelican-ipynb.git
git fetch leemengtaiwan
git checkout dev
```

## 建立開發基本環境

```commandline
conda create -n blog python=3
source activate blog
pip install -r init_requirements.txt
```

## 修改插件 / 主題設定
- 修改 `pelicanconf.py`
    - `THEME` 指到 `WORKSPACE/pelican-jupyter-notebook/themes/Hola10`
    - `PLUGIN_PATHS` 指到 `WORKSPACE/pelican-plugins`


## Blog 開發
- Shell 快捷鍵參考 [Gist](https://gist.github.com/leemengtaiwan/0fb24bdd4d33fefad39d0c718413880f)

在 dev branch 重新建立文章
```commandline
cd leemengtaiwan.github.io
python copy_static_files.py; pelican content
```

開啟 HTTP 伺服器確認
```commandline
cd leemengtaiwan.github.io/output
python -m pelican.server
```

更新 dev 分支
```commandline
git commit -m "Update A post"
```

發布文章到 master branch
```commandline
cd leemengtaiwan.github.io/
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
