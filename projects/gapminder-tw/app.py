# encoding: utf-8
import os
import glob
import urllib
import argparse
import pandas as pd
from bs4 import BeautifulSoup


COUNTRY_CSV_PATH = "statistics/lang/zh-TW/ddf--entities--geo--country.csv"
CONCEPT_CSV_PATH = "statistics/ddf--concepts.csv"
TAG_CSV_PATH = "statistics/ddf--entities--tag.csv"


def main():
    args = get_args()
    crawler()

def translater():
    pass


def generate_chinese_country_names():
    """Generate Chinese names for UN states by fetching (ISO State Code, Chinese Name) mapping on Wikipedia
    and save the result as a csv file for GapMinder rendering.
    """

    # create a dataframe containing mapping of ISO country codes and chinese names
    html = urllib.request.urlopen("https://zh.wikipedia.org/zh-tw/ISO_3166-1").read()
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'class': 'wikitable sortable'})

    columns = [th.text.replace('\n', '') for th in table.find('tr').find_all('th')]

    trs = table.find_all('tr')[1:]
    rows = list()
    for tr in trs:
        rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])
    df = pd.DataFrame(data=rows, columns=columns)

    # read existing country csv and find the corresponding chinese country names by ISO 3361 country codes
    df_countries = pd.read_csv(COUNTRY_CSV_PATH)
    chinese_names = list()
    for _, row in df_countries.iterrows():

        df_mapped = df[df['三位代碼'] == row['country'].upper()]
        if not df_mapped.empty:
            chinese_names.append(df_mapped['中文名稱'].iloc[0])
        else:
            chinese_names.append("")
    df_countries.name = chinese_names

    # manually adjust Taiwan's name
    df_countries.loc[df_countries.country == 'twn', 'name'] = '台灣'

    # save result
    df_countries.to_csv(COUNTRY_CSV_PATH, index=False)


def ddf_parser():
    """Generate Mata-data of all DDF files provided by GapMinder including (1) how much Taiwan statistics are available,
    (2) what are these indicators/ concepts and their concept structure.
    """
    num_available, total = 0, 0
    indicator_twn_tuples = list()  # format of a single tuple: (indicator_name, #twn rows, earliest available year)
    concept_metadata = dict()  # {top_tag: second_layer_tag:

    # parse all ddf files provided by GapMinder and find how many of them with Taiwan statistics
    for f_path in glob.glob(os.path.join('statistics', '*datapoints*.csv')):
        total += 1
        df = pd.read_csv(f_path)
        if 'twn' in df.geo.unique():
            num_available += 1
            indicator = f_path.replace('statistics/ddf--datapoints--', '').replace('--by--geo--time.csv', '')
            # print('[Indicator]', indicator)
            print(f"\t{len(df[df.geo == 'twn'])} indicators including Taiwan statistics.")

            # stat_name = df.columns[-1]
            # df_p = df.pivot(index='geo', columns='time')[stat_name]
            # df_p.insert(loc=0, column='indicator', value=stat_name)
            # df_p.to_csv(f'statistics_transformed/{stat_name}.csv', sep=';')

            indicators.append(indicator)


    # print("{:.1f}% datapoints have Taiwan statistics".format(num_available / float(total) * 100))



    df_c = pd.read_csv(CONCEPT_CSV_PATH)
    df_t = pd.read_csv(TAG_CSV_PATH)
    df = pd.merge(df_c, df_t, how='left', left_on='tags', right_on='tag')
    for idr, num_rows, earliest_year in indicator_twn_tuples:
        ancestors = list()

        row_values = df[df['concept'] == idr].values[0]
        name_catalog, parent, ancestor = (row_values[i] for i in [9, 17, 18])
        if type(parent) is str:
            ancestors.append(parent)

        # get ancestors recursively
        while type(ancestor) is str:
            tag_row_values = df_t[df_t['tag'] == ancestor].values[0]
            ancestors.append(tag_row_values[1])
            ancestor = tag_row_values[2]

        # build concept structure
        ancestors.insert(0, name_catalog)
        print('/'.join(ancestors[::-1]))



def get_args():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    ddf_parser()