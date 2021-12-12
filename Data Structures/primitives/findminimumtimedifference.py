class Solution:
    def timeDifference(self, times):
        '''
        :type times: list of str
        :rtype: int
        '''
        seen = [False] * (24 * 60)

        for time in times:
            n = self.time_to_int(time)
            # If the time has already occured before ans should be 0
            if seen[n]:
                return 0

            seen[n] = True
        #Calculate the answer using the previous value
        prev = -1
        min_diff = (24 * 60) + 1
        first = -1
        for i in range(0, len(seen)):
            if seen[i]:
                if prev != -1:
                    min_diff = min(min_diff, i - prev)
                else:
                    first = i

                prev = i

        # Wrap-around check
        min_diff = min(min_diff, first + 1440 - prev)

        return min_diff
    # Store the time as minutes
    def time_to_int(self, time):
        # time format - HH:mm
        hours = time[0:2]
        minutes = time[3:5]

        return int(hours) * 60 + int(minutes)

a = Solution()
b = a.timeDifference(["00:03", "23:59", "12:03"])
print(b)