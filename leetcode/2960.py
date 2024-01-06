class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        n = len(batteryPercentages)
        sub = 0
        test = 0
        for i in range(n):
            batteryPercentages[i] = max(batteryPercentages[i]-sub, 0)
            if batteryPercentages[i] > 0:
                test += 1
                sub += 1
        return test