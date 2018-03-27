## 建立基本環境

```commandline
conda create -n blog python=3
source activate blog
pip install -r init_requirements.txt
```

## Pelican plugins
使用自己 fork 來的 [pelican-ipynb Repo (Branch: dev)](https://github.com/leemengtaiwan/pelican-ipynb/tree/dev)

## Blog 開發
重新建立文章
```commandline
cd blog/
python copy_static_files.py
pelican content
```

開啟部落格伺服器
```commandline
cd blog/output/
python -m pelican.server
```

發布文章
```commandline
cd blog/
pelican content -s publishconf.py -v
python add_templates.py
ghp-import output -b master -m "Commit Message Here"
git push origin master
```