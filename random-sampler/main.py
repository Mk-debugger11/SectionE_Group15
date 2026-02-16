import pandas as pd


def main():
    raw = pd.read_csv("../raw_datasets/original_dataset.csv")

    samples = raw.sample(n=25000)

    samples.to_csv("../raw_datasets/raw_dataset.csv", index=False)


if __name__ == "__main__":
    main()
