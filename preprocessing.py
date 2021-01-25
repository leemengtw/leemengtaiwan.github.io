import os
from shutil import copyfile
import glob

OUTPUT_PATH = 'output'


def main():

    templates = [
        'googleb61e79b00fce6520.html'
    ]

    if not os.path.exists(OUTPUT_PATH):
        os.mkdir(OUTPUT_PATH)

    for template in templates:
        copyfile('./{}'.format(template), './output/{}'.format(template))

    print('Done: Processed {} additional templates.'.format(len(templates)))

    # add ipynb from other projects
    # extension = 'ipynb'
    # source_dir = './projects'
    # destination_dir = './content/projects'
    # num_files_copied = 0
    #
    # ipynb_paths = glob.iglob(os.path.join(source_dir, '**', '*.%s' % extension), recursive=True)
    # for ipynb_p in ipynb_paths:
    #     destination_p = ipynb_p.replace(source_dir, destination_dir)
    #     # create new project folder for the ipynb file in content folder if not exist
    #     sub_destination_dir = '/'.join(destination_p.split('/')[:-1])
    #     if not os.path.exists(sub_destination_dir):
    #         os.makedirs(sub_destination_dir)
    #
    #     copyfile(ipynb_p, destination_p)
    #     num_files_copied += 1
    #
    # print('Done: Processed {} additional ipynb files from other projects.'.format(num_files_copied))

    # copy deep-learning-resources repo content
    dl_filename = "./content/20190105-deep-learning-resources.md"
    copyfile('../deep-learning-resources/README.md', dl_filename)
    dl_matadata_and_pretext = """Title: 由淺入深的深度學習資源整理
Date: 2019-01-08 08:00
Tags: 深度學習, Python, Keras, TensorFlow
Slug: deep-learning-resources
Author: Lee Meng
Summary: 這裡紀錄了我在學習深度學習時蒐集的一些線上資源。內容由淺入深，而且會一直被更新，希望能幫助你順利地開始學習：）
Description: 這裡紀錄了我在學習深度學習時蒐集的一些線上資源。內容由淺入深，而且會一直被更新，希望能幫助你順利地開始學習：）
Image: joshua-newton-214848-unsplash.jpg
Image_credit_url: https://unsplash.com/photos/g4_IymCiD-k?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText

<style>
    h3 {
        margin-top: 3rem;
    }
    h3 a {
        font-size: 18px;
    }
</style>

<div class="cell border-box-sizing code_cell rendered">
    <div class="input">
        <div class="inner_cell">
            <div class="input_area">
                <div class=" highlight hl-ipython3">
                    <blockquote>
                        <p>
                            不聞不若聞之，聞之不若見之，見之不若知之，知之不若行之，學至於行之而止矣。
                            <br/>
                            <span style="float:right">── 《荀子．儒效》<span>
                        </p>
                    </blockquote>
                </div>
            </div>
        </div>
    </div>
</div>
<div class="cell border-box-sizing text_cell rendered" style="margin-top: 8rem">
    <p>
        這段話翻成白話文就是「沒聽過比不上聽過；聽過比不上實際看過；看過則比不上實際了解；而了解又不如動手實踐。唯有身體力行才能真正地學到東西。」
    </p>
    <p>
        這句古老的諺語向我們傳達了「實踐」的重要以及學習的幾個過程。
    </p>
    <p>
        做為一門學問，<a href="https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0" target="_blank">深度學習</a>也是同樣道理。
        僅說自己對深度學習有興趣或是有關注（聞、見），但卻沒有實際花時間去深入了解或實際應用（知、行）是無法真正學會深度學習的。
    </p>
    <div class="inner_cell">
        <div class="text_cell_render border-box-sizing rendered_html">
            <img src="/images/patrick-tomasso-71909-unsplash.jpg"/>
            <br/>
        </div>
    </div>
    <p>
        雖說如此，不了解深度學習能拿來做什麼的人或許還不少。
    </p>
    <p>
        我嘗試將自己在學習過程中蒐集到的重要資源由淺入深地做些整理。
        希望透過此文，能讓在各個學習階段的你都能從這裡獲得些什麼，並實際動手學習、探索發展快速的深度學習世界。
    </p>
    <p>
        本文內容會持續被更新，你可以定期回來看看或是關注這個 
        <a href="https://github.com/leemengtaiwan/deep-learning-resources" target="_blank">Github Repo</a>。
    </p>
</div>
"""
    dl_posttext = """<div class="cell border-box-sizing text_cell rendered" style="margin-top: 2rem">
    <div class="inner_cell">
        <div class="text_cell_render border-box-sizing rendered_html">
            <img src="/images/general/maxwell-ridgeway-685077-unsplash.jpg"/>
            <br/>
        </div>
    </div>
    <p>
        最後，如果你覺得本文實用，還請幫我分享此文並給 <a href="https://github.com/leemengtaiwan/deep-learning-resources" target="_blank">Github Repo</a> 一個小星星。
        這樣可以讓更多人注意到這些寶貴資源的存在並開始有方向的學習，謝謝！
    </p>
    <p>
        有再多資源，沒有親自動手做都是無法真正地學到東西的。因此，最後的最後讓我再次強調主動學習的重要：
    </p>
</div>
<div class="cell border-box-sizing code_cell rendered">
    <div class="input">
        <div class="inner_cell">
            <div class="input_area">
                <div class=" highlight hl-ipython3">
                    <blockquote>
                        <p>
                            告訴我資訊，我只會忘記；教導我知識，我會記得；讓我實際參與，我將能真正地學到東西。
                            <br/>
                            <span style="float:right">── 班傑明·富蘭克林<span>
                        </p>
                    </blockquote>
                </div>
            </div>
        </div>
    </div>
</div>
<div class="cell border-box-sizing text_cell rendered" style="margin-top: 8rem">
    <p>
        所以，現在就開始學習吧！
    </p>
</div>
"""

    with open(dl_filename, 'r') as original:
        # lines = original.readlines()
        # github_readme_content = '\n'.join(lines[2:])  # remove github repo title
        github_readme_content = original.read()

    with open(dl_filename, 'w') as modified:
        modified.write(f"{dl_matadata_and_pretext}\n" + github_readme_content + f'{dl_posttext}')

    print('Done: Copied README.md from deep-learning-resources repository.')

    # process image files
    extensions = ['png', 'jpg', 'gif']
    source_dir = '../deep-learning-resources/images'
    destination_dir = './content/images'
    num_files_copied = 0

    paths = []
    for ext in extensions:
        cur_paths = glob.iglob(os.path.join(source_dir, '**', '*.%s' % ext), recursive=True)
        paths += cur_paths

    for path in paths:
        destination_p = path.replace(source_dir, destination_dir)
        sub_destination_dir = '/'.join(destination_p.split('/')[:-1])
        if not os.path.exists(sub_destination_dir):
            os.makedirs(sub_destination_dir)

        copyfile(path, destination_p)
        num_files_copied += 1

    print('Done: Copied {} image files from deep-learning-resources repository.'.format(num_files_copied))


if __name__ == "__main__":
    main()

