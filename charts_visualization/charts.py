import matplotlib.pyplot as plt
import json


def f_score(precision, recall):
    if precision + recall == 0.0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)


def best_f_score(precision, recall):
    return max([f_score(p, r) for p, r in zip(precision, recall)])


def main(filename='precision_recall_coco.json', labels_name='labels_coco'):
    data = json.load(open(filename))
    labels = open(labels_name, 'r').read().split('\n')
    plt.title('Precision&Recall per class')
    plt.xlabel('Recall')
    plt.ylabel('Precision')

    f_scores = [(i, best_f_score(p, r)) for i,(p,r) in enumerate(data)]
    f_scores.sort(key=lambda e: -e[1])
    for i, (uid, f) in enumerate(f_scores[:10]):
        print('{}. {} f: {}'.format(i+1, labels[uid], f))
    print('...')
    for i, (uid, f) in list(enumerate(f_scores))[-10:]:
        print('{}. {} f: {}'.format(i+1, labels[uid], f))

    for p, r in data:
        if min(p) < 0.1:
            continue
        plt.plot(r, p)
    plt.show()


if __name__ == '__main__':
    main()
    print()
    main(filename='precision_recall_raccoon.json', labels_name='labels_raccoon')
