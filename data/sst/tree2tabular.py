# Load data
import pytreebank
import os
import sys

out_path = os.path.join(sys.path[0], 'sst_{}.txt')
dataset = pytreebank.load_sst('./raw_data')


# Store train, dev and test data in separate files
for category in ['train', 'dev', 'test']:
    with open(out_path.format(category), 'w') as outfile:
        for item in dataset[category]:
            outfile.write("__label__{}\t{}\n".format(
                item.to_labeled_lines()[0][0] + 1,
                item.to_labeled_lines()[0][1]
            ))

# Print the length of the training set
print(len(dataset['train']))