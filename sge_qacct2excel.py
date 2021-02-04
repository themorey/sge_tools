#import pandas as pd
from sge_tools import sge_qacct_parse

df = sge_qacct_parse("qacct_output.txt")
df['wait_time'] = df['qsub_time'] - df['start_time']
df.to_excel(r'/Users/jmorey/Documents/MSFT/Docs/HPC/Schedulers/Gridengine/sge_tools/UTRGV_SGE_jobs_2020.xlsx', index = False)
