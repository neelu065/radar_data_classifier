import os
import warnings

from utils import load_data, set_classifier

warnings.filterwarnings("ignore")


def main(obs_data, g_truth):
    # load data

    obs, gt = load_data(obs_data, g_truth)

    # breakpoint()

    # fetch radar parameters
    obs = set_classifier(obs)

    # eliminate the noise rows with radar_ID < -1 remove
    
    breakpoint()
    print("hi")


if __name__ == "__main__":
    folder_name = "inputs"

    obs_data = (
        "Observations_001.xlsx"  #'Observations_011.xlsx'  #'Observations_012.xlsx'
    )

    truth_data = "Ground_Truth_001.xlsx"

    main(os.path.join(folder_name, obs_data), os.path.join(folder_name, truth_data))
