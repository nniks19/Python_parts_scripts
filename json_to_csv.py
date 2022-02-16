import pandas as pd
import glob

for filename in glob.glob("data/*.json"):
    df = pd.read_json(r'' + filename)
    df.to_csv(r'converted/' + filename.replace("data/","").replace(".json",".csv"), header=None, index=False)