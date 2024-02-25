## read the data from datasource
## save it in the data/raw for further process


import os
from get_data import read_params, get_data
import argparse


def load_sand_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(" ", "_") for col in df.columns]
    #print(new_cols)
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path, index=False, header=new_cols)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_path", default="params.yaml")
    args = parser.parse_args()
    load_sand_save(args.config_path)