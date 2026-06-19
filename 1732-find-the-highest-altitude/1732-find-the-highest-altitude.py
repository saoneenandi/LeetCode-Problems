class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude=[0]
        srt=0
        i=0
        for i in range (len(gain)):
            srt=srt+gain[i]
            altitude.append(srt)
            i+=1

        return max(altitude)
