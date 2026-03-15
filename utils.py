import polars as pl
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


def load_data(obs_data, g_truth):
    columns = ["Freq", "PRI", "PW", "Lat", "Lon", "Angle"]
    # obs = pl.read_excel(obs_data)
    ## TODO: convert files to csv and use scan_csv method()

    obs = pl.read_excel(obs_data).select(columns)
    gt = pl.read_excel(g_truth)

    return obs, gt


def set_classifier(obs):
    features = obs.select(["Freq", "PRI", "PW"])

    # normalize the features
    scaler = StandardScaler()
    X = scaler.fit_transform(features)

    # DBSCAN clustering
    model = DBSCAN(eps=0.6, min_samples=10)

    radar_id = model.fit_predict(X)

    obs = obs.with_columns(pl.Series("radar_ID", radar_id))
    # breakpoint()
    return obs
