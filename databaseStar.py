import pandas as pd


def save(starScore):
    idx = len(pd.read_csv("databaseStar.csv"))
    new_df = pd.DataFrame({"starScore": starScore}, index=[idx])
    new_df.to_csv("databaseStar.csv", mode="a",  header=False)
    return None


def now_index():
    df = pd.read_csv("databaseStar.csv")
    return len(df)-1


def load_list():
    house_list = []
    df = pd.read_csv("databaseStar.csv")
    for i in range(len(df)):
        house_list.append(df.iloc[i].tolist())
    print(house_list)
    return house_list


if __name__ == "__main__":
    load_list()