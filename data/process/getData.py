import time
import pandas as pd
from pandas import DataFrame


def barrageData(barragesFile):
    pass



def commentData(commentsFile):
    df = pd.read_csv(commentsFile)
    return df


if __name__ == '__main__':
    df = commentData(commentsFile='../comments/1818-1.csv')
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(df['ctime'][0]))
    print(t)
