class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = [(p, s) for p, s in zip(position, speed)]
        st.sort(reverse = True)
        fleet = []
        for p,s in st:
            t = (target - p) / s
            if not fleet or t > fleet[-1]:
                fleet.append(t)
        return len(fleet)