class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        arr = []
        check = set()
        for i in range(len(transactions)):
            transaction = transactions[i]
            name, time, amount, city = transaction.split(",")
            arr.append((name, time, amount, city, i))
        arr.sort()
        def to_string(tup):
            return tup[0] + "," + tup[1] + "," + tup[2] + "," + tup[3]

        i = 0
        while i < len(arr):
            j = i+1
            if int(arr[i][2]) > 1000 and arr[i] not in check:
                check.add(arr[i])
                invalid.append(to_string(arr[i]))
            while j < len(arr) and arr[i][0] == arr[j][0]:
                if abs(int(arr[j][1])-int(arr[i][1])) <= 60 and arr[j][3] != arr[i][3]:
                    if arr[j] not in check:
                        check.add(arr[j])
                        invalid.append(to_string(arr[j]))
                    if arr[i] not in check:
                        check.add(arr[i])
                        invalid.append(to_string(arr[i]))
                j += 1
            i += 1
        return invalid