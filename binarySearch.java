private int binSearch(int[] commitIds, int start, int end) {
    // We know the first bad commit is between start and end
    if (start + 1 == end) {
        if executeTests(commitIds[start]) {
            return end;
        }
        else {
            return start;
        }
    }
    else if (start == end) {
        return start;
    }
    else {
        int length = (end - start);
        int half = start + length / 2;
        
        if executeTests(commitIds[half]) {
            return binSearch(commitIds, half + 1, end);
        }
        else {
            return binSearch(commitIds, start, half);
        }
    }
}

public int findBadCommit(int[] commitIds) {
    int index = binSearch(commitIds, 0, commitIds.length - 1);
    return commitIds[index];
}