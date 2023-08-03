import numpy as np

def create_matrix(str1, str2, gap_penalty):
    matrix = np.zeros((len(str1) + 1, len(str2) + 1))

    for x in range(len(str2)):
        matrix[0, x + 1] = matrix[0, x] - gap_penalty

    for z in range(len(str1)):
        matrix[z + 1, 0] = matrix[z, 0] - gap_penalty

    return matrix

def global_alignment(str1, str2, match_bonus=1, mismatch_penalty=1, gap_penalty=1):
    print("Global Alignment:")
    print("Sequence 1:", str1)
    print("Sequence 2:", str2)

    matrix = create_matrix(str1, str2, gap_penalty)

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                match_score = matrix[i - 1, j - 1] + match_bonus
            else:
                match_score = matrix[i - 1, j - 1] - mismatch_penalty

            delete_score = matrix[i - 1, j] - gap_penalty
            insert_score = matrix[i, j - 1] - gap_penalty

            matrix[i, j] = max(match_score, delete_score, insert_score)

    print(matrix)
    print_alignment(matrix, str1, str2, mismatch_penalty, gap_penalty)
    print_score(matrix)

def local_alignment(str1, str2, match_bonus=1, mismatch_penalty=1, gap_penalty=1):
    print("Local Alignment:")
    print("Sequence 1:", str1)
    print("Sequence 2:", str2)

    matrix = create_matrix(str1, str2, gap_penalty)

    max_score = 0
    max_i, max_j = 0, 0

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                match_score = matrix[i - 1, j - 1] + match_bonus
            else:
                match_score = matrix[i - 1, j - 1] - mismatch_penalty

            delete_score = matrix[i - 1, j] - gap_penalty
            insert_score = matrix[i, j - 1] - gap_penalty

            matrix[i, j] = max(0, match_score, delete_score, insert_score)

            if matrix[i, j] > max_score:
                max_score = matrix[i, j]
                max_i, max_j = i, j

    print(matrix)
    print_alignment(matrix, str1, str2, mismatch_penalty, gap_penalty, max_i, max_j)
    print_score(matrix)

def print_alignment(matrix, str1, str2, mismatch_penalty, gap_penalty, end_i=None, end_j=None):
    i, j = len(str1), len(str2)

    aligned_str1, aligned_str2 = [], []

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            aligned_str1.append(str1[i - 1])
            aligned_str2.append(str2[j - 1])
            i -= 1
            j -= 1
        elif matrix[i, j] == matrix[i - 1, j - 1] - mismatch_penalty:
            aligned_str1.append(str1[i - 1])
            aligned_str2.append(str2[j - 1])
            i -= 1
            j -= 1
        elif matrix[i, j] == matrix[i - 1, j] - gap_penalty:
            aligned_str1.append(str1[i - 1])
            aligned_str2.append("-")
            i -= 1
        else:
            aligned_str1.append("-")
            aligned_str2.append(str2[j - 1])
            j -= 1

    while i > 0:
        aligned_str1.append(str1[i - 1])
        aligned_str2.append("-")
        i -= 1

    while j > 0:
        aligned_str1.append("-")
        aligned_str2.append(str2[j - 1])
        j -= 1

    aligned_str1.reverse()
    aligned_str2.reverse()

    print("Alignment:")
    print("".join(aligned_str1))
    print("".join(aligned_str2))

def print_score(matrix):
    rows, cols = matrix.shape
    score = matrix[rows - 1, cols - 1]
    print(f"Alignment Score: {score}")

if __name__ == "__main__":
    str1 = "GGTTCGTGGA"
    str2 = "GATCGTGAATT"

    # Global Alignment
    global_alignment(str1, str2, match_bonus=1, mismatch_penalty=1, gap_penalty=1)

    # Local Alignment
    local_alignment(str1, str2, match_bonus=1, mismatch_penalty=1, gap_penalty=1)
