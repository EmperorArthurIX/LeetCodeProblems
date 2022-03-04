def dailyTemperatures(temperatures: list) -> list:
    notwarm = []
    ans = [0]*len(temperatures)
    for i in range(len(temperatures)):
        while notwarm and temperatures[i] > temperatures[notwarm[-1]]:    # Update distance from this one for all the previous nodes in the stack
            curr = notwarm.pop()
            ans[curr] = i - curr
        notwarm.append(i)          # Keep adding nodes which are not greater than their previous
    return ans


if __name__ == "__main__":
    print(*dailyTemperatures([1,1,1,1,1,1,1,1,1,1,2,1,10,]))