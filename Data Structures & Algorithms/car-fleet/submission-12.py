class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = [(p, s) for p, s in zip(position, speed)]
        st.sort(reverse = True)
        fleet = []
        for p,s in st:
            fleet.append((target - p) / s)
            if len(fleet) >= 2 and fleet[-1] <= fleet[-2]:
                fleet.pop()
        return len(fleet)