import pandas as pd

def sampleData(filename, count):
    samples = []

    data = pd.read_table(filename,  header=None)

    samples.append(data.sample(count))

    return pd.concat(samples)


def main():
    

    count = 6000

    res = sampleData("./data/full/2017.statistics.tab", count)

    res.to_csv("./data/sample/2017sample.tab", header=False, sep="\t", index=False)

    print(res)


main()
