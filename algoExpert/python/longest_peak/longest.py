"""
https://www.algoexpert.io/questions/Longest%20Peak
"""

def longestPeak(array):

    peaks = get_peaks(array)

  
    totals = []
    i = 0 
  
    low = peaks[i]
    high = peaks[i]
    while i <= len(array): 
        peak =peaks[i]
        for t in reversed(array[:array[peaks[i]]]):
            if array[t] == low:
                break
            if peak > array[t]:
                low = t
            else:
                i += 1
                break 
            
        
        import pdb; pdb.set_trace()
        # for s in array[array[peaks[i]]:
        #     print(s)

    #     #import pdb; pdb.set_trace()
    #     print(array[a], array)

    # for b in array[array[1]:]:
    #     print(b)
    # while i <= len(peaks):
    #     low = i 
    #     high = i 
    #     import pdb; pdb.set_trace()
    #     for t in reversed(array[:array[i]]):
    #         if peaks[i] > array[t]:
    #             low = t
    #         else:
    #             break
    #
    #     for k in range(array[array[i]:]):
    #         if peaks[i] > array[k]:
    #             high = k
    #         else:
    #             break 
    #     totals.append(high-low)
    #     i += 1
    #     low = i
    #     high = i
    # return totals




def get_peaks(array):
    peaks = []

    for i in range(1, len(array) -1):
        curr = array[i]
        prev = array[i-1]
        next_num = array[i+1]

        if curr > prev and curr > next_num:
            peaks.append(curr)
    return peaks


longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])
