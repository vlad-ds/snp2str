import csv
import json
import os
from collections import OrderedDict
import pandas as pd


# TODO make header optional (.map)

def process_files(ped_path: str,
                  pop_path: str = None,
                  map_path: str = None,
                  output_path: str = "output.csv") -> None:
    """

    :param ped_path:
    :param pop_path:
    :param map_path:
    :param output_path:
    :return:
    """
    with open(os.path.join(os.path.dirname(__file__), 'bases_coding.json')) as file:
        bases_coding = json.load(file)

    header = pd.read_csv(map_path, sep="\t", header=None)[1].values.tolist()

    if pop_path:
        populations = pd.read_csv(pop_path, header=None)[0].tolist()
    else:
        populations = None

    sequences = OrderedDict()

    with open(ped_path) as file:
        for line in file.readlines():
            elements = line.split()
            cultivar_name = elements[1]
            sequence = elements[6:]
            sequences[cultivar_name] = list(map(lambda x: bases_coding[x], sequence))

    n_bases_set = set([len(val) for val in sequences.values()])
    n_bases = next(iter(n_bases_set))

    assert len(n_bases_set) == 1, "Not all species have the same number of bases!"

    print("Parsed %i species with %i bases each" % (len(sequences), n_bases))

    assert len(header) == n_bases / 2, "Header size %s does not correspond with chromosome count %s" % (len(header), n_bases / 2)

    if populations:
        assert len(sequences) == len(populations), "Population number does not correspond"

    with open(output_path, "w") as file:
        writer = csv.writer(file, delimiter=" ")
        # write header
        writer.writerow([None, None] + header)
        # write each line
        for i, species in enumerate(sequences):
            strand1 = sequences[species][::2]
            strand2 = sequences[species][1::2]

            assert len(strand1) == len(strand2), "The two strands contain an unequal number of elements! %i and %i" % (len(strand1), len(strand2))

            # TODO if populations absent, populations[i]] is not here

            if populations:
                row1 = [species, populations[i], *strand1]
                row2 = [species, populations[i], *strand2]
            else:
                row1 = [species, *strand1]
                row2 = [species, *strand2]

            writer.writerow(row1)
            writer.writerow(row2)

    print("Output saved at: %s" % os.path.abspath(output_path))
