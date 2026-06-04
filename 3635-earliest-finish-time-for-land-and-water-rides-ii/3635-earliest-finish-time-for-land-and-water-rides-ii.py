from bisect import bisect_right

class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):

        def find_min_finish(firstStart, firstDuration,
                            secondStart, secondDuration):

            secondRides = sorted(zip(secondStart, secondDuration))

            sortedStarts = [start for start, _ in secondRides]

            minDurationPrefix = [0] * len(secondRides)
            minDurationPrefix[0] = secondRides[0][1]

            for i in range(1, len(secondRides)):
                minDurationPrefix[i] = min(
                    minDurationPrefix[i - 1],
                    secondRides[i][1]
                )

            minStartPlusDurationSuffix = [0] * len(secondRides)
            minStartPlusDurationSuffix[-1] = (
                secondRides[-1][0] + secondRides[-1][1]
            )

            for i in range(len(secondRides) - 2, -1, -1):
                minStartPlusDurationSuffix[i] = min(
                    minStartPlusDurationSuffix[i + 1],
                    secondRides[i][0] + secondRides[i][1]
                )

            answer = float("inf")

            for start, duration in zip(firstStart, firstDuration):

                firstRideFinishTime = start + duration

                splitIndex = bisect_right(
                    sortedStarts,
                    firstRideFinishTime
                )

                if splitIndex > 0:
                    answer = min(
                        answer,
                        firstRideFinishTime +
                        minDurationPrefix[splitIndex - 1]
                    )

                if splitIndex < len(secondRides):
                    answer = min(
                        answer,
                        minStartPlusDurationSuffix[splitIndex]
                    )

            return answer

        return min(
            find_min_finish(
                landStartTime,
                landDuration,
                waterStartTime,
                waterDuration
            ),
            find_min_finish(
                waterStartTime,
                waterDuration,
                landStartTime,
                landDuration
            )
        )