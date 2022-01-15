from os.path import dirname,join

DIR = dirname(__file__)
AC_ROOT = join(DIR,'..')
CSV_DIR = join(AC_ROOT,'csv')

PATH_TO_FAILED_CSV = f'{CSV_DIR}/failed.csv'
PATH_TO_SOLVED_CSV = f'{CSV_DIR}/solved.csv'

KEYWORDS = ['dp','dfs','tree','unionfind','bfs','math','other','cumulative']

