#!/usr/bin/env python3

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from statannot import add_stat_annotation
#from pandas.compat import StringIO

sns.set(style="whitegrid")
df = sns.load_dataset("tips")
x = "day"
y = "total_bill"
order = ['Sun', 'Thur', 'Fri', 'Sat']

ax = sns.boxplot(data=df, x=x, y=y, order=order)
ax, test_results = add_stat_annotation(ax, data=df, x=x, y=y, order=order,
                                   box_pairs=[("Thur", "Fri"), ("Thur", "Sat"), ("Fri", "Sun")],
                                   #comparisons_correction="fdr_bh",
                                   test='Mann-Whitney', text_format='star', loc='outside', verbose=2)
#plt.savefig('example_non-hue_outside.png', dpi=300, bbox_inches='tight')
