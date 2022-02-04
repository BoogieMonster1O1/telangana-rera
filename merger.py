import glob
import pandas as pd

combined_csv = pd.concat([pd.read_csv(f) for f in glob.glob('old_out/*.csv')])

combined_csv.to_csv("data.csv", index=False, encoding='utf-8-sig')
