import pandas as pd


def get_clean_data():
    data = pd.read_csv("/data/data.csv")
    print(data.head())
    return data


def main():
    # create the model
    data = get_clean_data()

    # evaluate the model


if __name__ == "__main__":
    main()
