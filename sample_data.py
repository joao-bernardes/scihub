import pandas

def sampleData(filenames, count):
    samples = []

    for filename in filenames:
        data = pandas.read_table(filename,  header=None)

        samples.append(data.sample(count))

    return pandas.concat(samples)


def main():
    dataFilenames = [
        "sep2015.tab",
        "oct2015.tab",
        "nov2015.tab",
        "dec2015.tab",
        "jan2016.tab",
        "feb2016.tab"
    ]

    count = 1000

    res = sampleData(dataFilenames, count)

    res.to_csv("sample.tab", header=False, sep="\t", index=False)

    print(res)


main()
