以下 `clone` 指令都在統一的 workspace 目錄下執行。

## Blog repo
複製開發用的 branch
```commandline
git clone -b dev https://github.com/leemengtaiwan/leemengtaiwan.github.io.git
```

## FB Clid issue
- https://shian.tw/article/1084#more-1084
- https://greasyfork.org/en/forum/discussion/44083/fbclid-tracking-parameter-attached-by-facebook

## Pelican 插件 / 主題
統一使用官方 plugins，ipynb plugin 及 theme 則使用自己開發的 repo
```commandline
git clone https://github.com/leemengtaiwan/pelican-jupyter-notebook.git
git checkout dev

git clone --recursive https://github.com/getpelican/pelican-plugins
cd pelican-plugins/pelican-ipynb/
git remote add leemengtaiwan https://github.com/leemengtaiwan/pelican-ipynb.git
git fetch leemengtaiwan
git checkout dev
```

pelican-toc
```commandline
cd pelican-plugins/pelican-toc/
git remote add leemengtaiwan https://github.com/leemengtaiwan/pelican-toc.git
git fetch leemengtaiwan
git checkout dev
```

ga_page_view
```commandline
cd pelican-plugins/ga_page_view/
git remote add leemengtaiwan https://github.com/leemengtaiwan/pelican.plugins.ga_page_view.git
git fetch leemengtaiwan
git checkout normalize-page-vie
pip install --upgrade google-api-python-client
```

然後從 Google Drive 上的 `credentials` 裡頭下載 `Blog-usage-0799d847dd8f.p12` 放到 `leemengtaiwan.github.io`

## 關聯 Github Repo

deep-learning-resources
```commandline
git clone https://github.com/leemengtaiwan/deep-learning-resources.git
```

gapminder
- 記得把 `.git` 刪掉，要不複製到 blog 時部署會出錯
```commandline
git clone https://github.com/leemengtaiwan/gapminder-private.git
cd gapminder-private
rm -rf .git
```

## 第一次修改插件
首先先手動 fork 在 `pelican-plugins` 裡頭想要修改的 submodule，再 clone 下來修改
```commandline
git remote add leemengtaiwan https://github.com/leemengtaiwan/pelican-toc.git
git fetch leemengtaiwan
git checkout leemengtaiwan/master
...
git checkout -b dev
git commit -m "Finish!"
git push --set-upstream leemengtaiwan dev
```

## 建立開發基本環境

```commandline
conda create -n blog python=3
conda activate blog
conda install pkg-config
pip install -r init_requirements.txt
conda install -c conda-forge jupyterlab
conda install pandas
```

### 新版本 Pelican 環境設置

```commandline
cd /Users/meng.lee/Documents/workspace
git clone https://github.com/getpelican/pelican
cd pelican
python setup.py install
cd ../leemengtaiwan.github.io 

```



## 修改插件 / 主題設定
- 修改 `pelicanconf.py`
    - `THEME` 指到 `WORKSPACE/pelican-jupyter-notebook/themes/Hola10`
    - `PLUGIN_PATHS` 指到 `WORKSPACE/pelican-plugins`

## Blog 開發
- Shell 快捷鍵參考 [Gist](https://gist.github.com/leemengtaiwan/0fb24bdd4d33fefad39d0c718413880f)
- 啟動對應的開發環境，例： `conda activate blog`

基本快捷鍵
```commandline
alias copy-gapminder='cp -r ~/Documents/workspace/gapminder-private/ ~/Documents/workspace/leemengtaiwan.github.io/output'
alias b-base='conda activate blog;cd ~/Documents/workspace/leemengtaiwan.github.io'
alias b-jupyter='b-base;cd content;jupyter lab'
alias b-server='b-base;cd output;python -m http.server'
alias b-build='b-base;python preprocessing.py;pelican content;cd -'
alias bp-build='b-base;python preprocessing.py;pelican content -s publishconf.py;copy-gapminder;cd -'
b-publish() {
	b-base 
	python preprocessing.py
	pelican content -s publishconf.py
	copy-gapminder
	ghp-import output -b master -m "$1"
	git push origin master
	cd -
}
```

## 追加 project 步驟
- 在 `pelican-jupyter-notebook/themes/Hola10/static/imgaes/portfolio` 裡頭新增 3 圖
    - 使用 [resizeimage.net](https://resizeimage.net/) 裁剪圖片
    - 決定新 Project 在 index.html 上的 cover image 類型以及圖片尺寸：
        - 方型圖片尺寸：
            - `project-name@jpg`: 500 x 500
            - `project-name@2x.jpg`: 1000 x 1000
        - 長型圖片尺寸：
            - `project-name@jpg`: 500 x 625
            - `project-name@2x.jpg`: 1000 x 1250
        - `gallery/g-project-name.jpg`: 自由, 寬型圖片
- 前往 `pelicanconf.py`，搜尋 `PROJECTS`
    - 調整專案順序

## 找書的圖片
- [Rakuten Kobo](https://www.kobo.com/tw/zh/ebook/relr-70c5diu4fjbpvtpfg) 
- 把圖片中跟 size 相關的 path 刪掉即可得到原圖，再裁剪成 700 * 1000
- ex:
    - https://kbimages1-a.akamaihd.net/55fbde1d-55df-489e-b25f-1edd95814662/353/569/90/False/ReLr-70c5DiU4fJBPvTPFg.jpg
    - https://kbimages1-a.akamaihd.net/55fbde1d-55df-489e-b25f-1edd95814662/ReLr-70c5DiU4fJBPvTPFg.jpg


## 文章內容

Meta Cell template

```markdown
- author: Lee Meng
- date: 2018-07-01 12:00
- title: New Post
- slug: just-a-test-url
- tags: 機器學習, R
- description: This is a description
- summary: This is a summary
- image: andy-kelly-402111-unsplash.jpg
- image_credit_url: https://www.google.com
- enable_notebook_download: false
- status: draft

```

文摘用 template
```markdown
!article
- Data visualisation, from 1987 to today
- https://medium.economist.com/data-visualisation-from-1987-to-today-65d0609c6017
- leroy-stencil-set.jpg
```

單一圖片
```text
<img src="{filename}images/gapminder/chuttersnap-176806-unsplash.jpg"/>
<br>
```

圖片＋下標
```text
<center>
    <img src="{filename}images/gapminder/official-page.jpg" style=""/>
</center>
<center>
    GapMinder 釋出的<a href="https://www.gapminder.org/tools/#" target="_blank">泡泡圖</a>截圖。在右邊的清單搜尋「 Taiwan 」不會有結果
    <br/>
    <br/>
</center>
```

video
```text
<video loop muted autoplay playsinline poster="{filename}images/gapminder/decline-of-female-fertility.jpg">
  <source src="{filename}images/gapminder/decline-of-female-fertility.mp4" type="video/mp4">
    您的瀏覽器不支援影片標籤，請留言通知我：Ｓ
</video>
<br>
```


## Books

feature post
```html
<div class="brick entry featured-grid animate-this">
    <div class="entry-content">
        <div id="featured-post-slider" class="flexslider">
            <ul class="slides">

                <li>
                    <div class="featured-post-slide">

                        <div class="post-background" style="background-image:url('{{SITEURL}}/theme/images/thumbs/featured/featured-1.jpg');"></div>

                        <div class="overlay"></div>

                        <div class="post-content">
                            <ul class="entry-meta">
                                    <li>September 06, 2016</li>
                                    <li><a href="#" >Naruto Uzumaki</a></li>
                                </ul>

                            <h1 class="slide-title"><a href="single-standard.html" title="">Minimalism Never Goes Out of Style</a></h1>
                        </div>

                    </div>
                </li> <!-- /slide -->

                <li>
                    <div class="featured-post-slide">

                        <div class="post-background" style="background-image:url('{{SITEURL}}/theme/images/thumbs/featured/featured-2.jpg');"></div>

                        <div class="overlay"></div>

                        <div class="post-content">
                            <ul class="entry-meta">
                                    <li>August 29, 2016</li>
                                    <li><a href="#">Sasuke Uchiha</a></li>
                                </ul>

                            <h1 class="slide-title"><a href="single-standard.html" title="">Enhancing Your Designs with Negative Space</a></h1>
                        </div>

                    </div>
                </li> <!-- /slide -->

                <li>
                    <div class="featured-post-slide">

                        <div class="post-background" style="background-image:url('{{SITEURL}}/theme/images/thumbs/featured/featured-3.jpg');;"></div>

                        <div class="overlay"></div>

                        <div class="post-content">
                            <ul class="entry-meta">
                                    <li>August 27, 2016</li>
                                    <li><a href="#" class="author">Naruto Uzumaki</a></li>
                                </ul>

                            <h1 class="slide-title"><a href="single-standard.html" title="">Music Album Cover Designs for Inspiration</a></h1>
                        </div>

                    </div>
                </li> <!-- end slide -->

            </ul> <!-- end slides -->
        </div> <!-- end featured-post-slider -->
    </div> <!-- end entry content -->
</div>
```

一般
```html
<article class="brick entry format-standard animate-this">

    <div class="entry-thumb">
      <a href="single-standard.html" class="thumb-link">
          <img src="{{SITEURL}}/theme/images/thumbs/diagonal-building.jpg" alt="building">
      </a>
    </div>
    
    <div class="entry-text">
        <div class="entry-header">
        
            <div class="entry-meta">
                <span class="cat-links">
                    <a href="#">Design</a>
                    <a href="#">Photography</a>
                </span>
            </div>
        
            <h1 class="entry-title">
                <a href="single-standard.html">Just a Standard Format Post.</a>
            </h1>
        
        </div>
        <div class="entry-excerpt">
            TEXT HERE
        </div>
    </div>

</article> <!-- end article -->
```

audio
```html
<article class="brick entry format-audio animate-this">
    <div class="entry-thumb">
      <a href="single-audio.html" class="thumb-link">
          <img src="{{SITEURL}}/theme/images/thumbs/concert.jpg" alt="concert">
      </a>
    
      <div class="audio-wrap">
        <audio id="player" src="{{SITEURL}}/theme/media/AirReview-Landmarks-02-ChasingCorporate.mp3" width="100%" height="42" controls="controls"></audio>
      </div>
    </div>
    
    <div class="entry-text">
    <div class="entry-header">
    
        <div class="entry-meta">
            <span class="cat-links">
                <a href="#">Design</a>
                <a href="#">Music</a>
            </span>
        </div>
    
        <h1 class="entry-title"><a href="single-audio.html">This Is a Audio Format Post.</a></h1>
    
    </div>
            <div class="entry-excerpt">
                Lorem ipsum Sed eiusmod esse aliqua sed incididunt aliqua incididunt mollit id et sit proident dolor nulla sed commodo est ad minim elit reprehenderit nisi officia aute incididunt velit sint in aliqua cillum in consequat consequat in culpa in anim.
            </div>
    </div>
</article> <!-- /article -->
```

Quote 
```html
<article class="brick entry format-quote animate-this" >

    <div class="entry-thumb">
       <blockquote>
            <p>Good design is making something intelligible and memorable. Great design is making something memorable and meaningful.</p>
    
            <cite>Dieter Rams</cite>
       </blockquote>
    </div>

</article> <!-- end article -->
```

Gallery
```html
<article class="brick entry format-gallery group animate-this">
    <div class="entry-thumb">
        <div class="post-slider flexslider">
            <ul class="slides">
                <li>
                    <img src="{{SITEURL}}/theme/images/thumbs/gallery/work1.jpg">
                </li>
                <li>
                    <img src="{{SITEURL}}/theme/images/thumbs/gallery/work2.jpg">
                </li>
                <li>
                    <img src="{{SITEURL}}/theme/images/thumbs/gallery/work3.jpg">
                </li>
            </ul>
        </div>
    </div>
    
    <div class="entry-text">
        <div class="entry-header">
            <div class="entry-meta">
                <span class="cat-links">
                    <a href="#">Branding</a>
                    <a href="#">Wordpress</a>
                </span>
            </div>
        
            <h1 class="entry-title"><a href="single-gallery.html">Workspace Design Trends and Ideas.</a></h1>
        </div>
        <div class="entry-excerpt">
        Lorem ipsum .
        </div>
    </div>
</article> <!-- end article -->
```

Video
```html
<article class="brick entry format-video animate-this">
    <div class="entry-thumb video-image">
        <a href="http://player.vimeo.com/video/14592941?title=0&amp;byline=0&amp;portrait=0&amp;color=F64B39" data-lity>
            <img src="{{SITEURL}}/theme/images/thumbs/ottawa-bokeh.jpg" alt="bokeh">
        </a>
    </div>
    <div class="entry-text">
        <div class="entry-header">
            <div class="entry-meta">
                <span class="cat-links">
                    <a href="#">Design</a>
                    <a href="#">Branding</a>
                </span>
            </div>
            <h1 class="entry-title"><a href="single-video.html">This Is a Video Post Format.</a></h1>
        </div>
        <div class="entry-excerpt">
            culpa in anim.
        </div>
    </div>
</article> <!-- end article -->
```