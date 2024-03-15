class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        a=[]
        kelvin=celsius+273.15
        fa=celsius*1.80 +32.00
        a.append(kelvin)
        a.append(fa)


        return a
        
