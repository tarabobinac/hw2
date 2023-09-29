import math


def MakeSubtree(data):
    # Organize the data
    candidates = [[], []]
    f1 = []
    f2 = []
    for item in data:
        f1.append([item[0], item[2]])
        f2.append([item[1], item[2]])

    # Get the candidate splits for each respective feature
    candidates[0] = DetermineCandidateSplits(f1)
    candidates[1] = DetermineCandidateSplits(f2)

    # Initialize node -> node.val is in the form of [feature index, threshold]
    node = Node([0, 0])

    # If node is empty
    if len(data) == 0:
        node.val = 1

    # If entropy of all splits is 0 (there are no candidate splits)
    elif len(candidates[0]) == 0 and len(candidates[1]) == 0:
        pos = 0
        neg = 0
        for item in data:
            if item[2] == 1:
                pos = pos + 1
            else:
                neg = neg + 1
        if pos >= neg:
            node.val = 1
        else:
            node.val = 0

    # All splits have no information gain
    else:
        # All splits have no information gain
        if NoGainRatio(candidates, data):
            pos = 0
            neg = 0
            for item in data:
                if item[2] == 1:
                    pos = pos + 1
                else:
                    neg = neg + 1
            if pos >= neg:
                node.val = 1
            else:
                node.val = 0
        # There is a best split
        else:
            # Create node with highest gain ratio
            # Determine what its left and right children should be
            best_split = FindBestSplit(candidates, data)
            node.val = best_split

            left_branch_data = []
            right_branch_data = []
            for entry in data:
                if entry[best_split[0] - 1] >= best_split[1]:
                    left_branch_data.append(entry)
                else:
                    right_branch_data.append(entry)
            node.left = MakeSubtree(left_branch_data)
            node.right = MakeSubtree(right_branch_data)

    return node


def NoGainRatio(splits, data):
    gain_ratio_array = []
    feature1_candidates = splits[0]
    feature2_candidates = splits[1]

    for candidate in feature1_candidates:
        gain_ratio_array.append([0, 1, candidate])
    for candidate in feature2_candidates:
        gain_ratio_array.append([0, 2, candidate])

    feature1_data = []
    feature2_data = []
    for entry in data:
        feature1_data.append([entry[0], entry[2]])
        feature2_data.append([entry[1], entry[2]])

    for candidate in gain_ratio_array:
        if candidate[1] == 1:
            candidate[0] = GainRatio(feature1_data, candidate[2])
        elif candidate[1] == 2:
            candidate[0] = GainRatio(feature2_data, candidate[2])

    best_split = 0
    for candidate in gain_ratio_array:
        if candidate[0] > best_split:
            best_split = candidate[0]

    if best_split == 0:
        return True
    return False


def FindBestSplit(splits, data):
    gain_ratio_array = []
    feature1_candidates = splits[0]
    feature2_candidates = splits[1]

    for candidate in feature1_candidates:
        gain_ratio_array.append([0, 1, candidate])
    for candidate in feature2_candidates:
        gain_ratio_array.append([0, 2, candidate])

    feature1_data = []
    feature2_data = []
    for entry in data:
        feature1_data.append([entry[0], entry[2]])
        feature2_data.append([entry[1], entry[2]])

    for candidate in gain_ratio_array:
        if candidate[1] == 1:
            candidate[0] = GainRatio(feature1_data, candidate[2])
        elif candidate[1] == 2:
            candidate[0] = GainRatio(feature2_data, candidate[2])

    best_split = [0, 0, 0]
    for candidate in gain_ratio_array:
        if candidate[0] > best_split[0]:
            best_split[0] = candidate[0]
            best_split[1] = candidate[1]
            best_split[2] = candidate[2]

    return [best_split[1], best_split[2]]


def GainRatio(data, threshold):
    info_gain = InfoGain(data, threshold)
    split_entropy = SplitEntropy(data, threshold)
    if split_entropy == 0:
        return 0
    return info_gain / split_entropy


def InfoGain(data, threshold):
    entropy = Entropy(data)
    left_branch = []
    right_branch = []

    for item in data:
        if item[0] >= threshold:
            left_branch.append(item)
        else:
            right_branch.append(item)

    entropy_left = Entropy(left_branch)
    entropy_right = Entropy(right_branch)

    left_frac = 0
    right_frac = 0
    if len(data) != 0:
        left_frac = len(left_branch) / len(data)
        right_frac = len(right_branch) / len(data)

    return entropy - ((left_frac * entropy_left) + (right_frac * entropy_right))


def DetermineCandidateSplits(data):
    C = []
    for entry in data:
        if entry[0] not in C and SplitEntropy(data, entry[0]) != 0:
            C.append(entry[0])
    return C


def SplitEntropy(data, threshold):
    if len(data) == 0:
        return 0

    go_left = 0
    go_right = 0
    for item in data:
        if item[0] >= threshold:
            go_left = go_left + 1
        else:
            go_right = go_right + 1

    if go_left == 0 or go_right == 0:
        return 0

    return -1 * ((go_left / len(data) * math.log(go_left / len(data), 2)) + (
            go_right / len(data) * math.log(go_right / len(data), 2)))


def Entropy(data):
    # There are no data items, entropy/uncertainty is 0
    if len(data) == 0:
        return 0

    pos_inst = 0
    for item in data:
        if item[1] == 1:
            pos_inst = pos_inst + 1

    pos_frac = pos_inst / len(data)
    neg_frac = (len(data) - pos_inst) / len(data)

    # Cannot execute log on 0, preemptively return 0
    if pos_frac == 0 or neg_frac == 0:
        return 0

    # In most cases, though:
    return -1 * (pos_frac * math.log(pos_frac, 2) + neg_frac * math.log(neg_frac, 2))


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def VisualizeTree(node):
    num_nodes = 1
    if node.left is not None and node.right is not None:
        print("[x" + str(node.val[0]) + " >= " + str(node.val[1]) + "]")
        print(" /  \  ")

        left_leaf = False
        right_leaf = False
        if node.left.left is None and node.left.right is None:
            left_leaf = True
        if node.right.left is None and node.right.right is None:
            right_leaf = True

        if left_leaf and right_leaf:
            print("[" + str(node.left.val) + "] [" + str(node.right.val) + "]")
        elif left_leaf and not right_leaf:
            print("[" + str(node.left.val) + "] [x" + str(node.right.val[0]) + " >= " + str(node.right.val[1]) + "]")
        elif right_leaf and not left_leaf:
            print("[x" + str(node.left.val[0]) + " >= " + str(node.left.val[1]) + "] [" + str(node.right.val) + "]")
        else:
            print("[x" + str(node.left.val[0]) + " >= " + str(node.left.val[1]) + "] [x" + str(node.right.val[0]) + " >= " + str(node.right.val[1]) + "]")


        print("-----------------------")
        if not left_leaf:
            num_nodes = num_nodes + VisualizeTree(node.left)
        else:
            num_nodes = num_nodes + 1
        if not right_leaf:
            num_nodes = num_nodes + VisualizeTree(node.right)
        else:
            num_nodes = num_nodes + 1

    else:
        print("[" + str(node.val) + "]")

    return num_nodes

def TFPosNeg(item, node):
    x1 = item[0]
    x2 = item[1]
    y = item[2]

    if isinstance(node.val, int):
        if y == 0 and node.val == 0:
            return 1
        elif y == 0 and node.val == 1:
            return 2
        elif y == 1 and node.val == 0:
            return 3
        elif y == 1 and node.val == 1:
            return 0
    else:
        feature = node.val[0]
        if feature == 1:
            if x1 >= node.val[1]:
                return TFPosNeg(item, node.left)
            else:
                return TFPosNeg(item, node.right)
        elif feature == 2:
            if x2 >= node.val[1]:
                return TFPosNeg(item, node.left)
            else:
                return TFPosNeg(item, node.right)

if __name__ == '__main__':
    # Parse data
    dataFile = open("./D512.txt", "r")
    data = []
    for line in dataFile:
        xxy = []
        for element in line.split():
            xxy.append(float(element))
        data.append(xxy)
        xxy = []

    # Make tree
    tree_at_root_node = MakeSubtree(data)
    num_nodes = VisualizeTree(tree_at_root_node)

    dataFile = open("./D1808.txt", "r")
    data = []
    for line in dataFile:
        xxy = []
        for element in line.split():
            xxy.append(float(element))
        data.append(xxy)
        xxy = []

    TP, TN, FP, FN = 0, 0, 0, 0
    for item in data:
        tf_pos_neg = TFPosNeg(item, tree_at_root_node)
        if tf_pos_neg == 0:
            TP = TP + 1
        elif tf_pos_neg == 1:
            TN = TN + 1
        elif tf_pos_neg == 2:
            FP = FP + 1
        elif tf_pos_neg == 3:
            FN = FN + 1

    accuracy = (TP + TN) / (TP + TN + FP + FN)
    err = 1 - accuracy
    print(err)
