class Solution:
    def __get_rise_run(self, p0, p1):
        rise = p1[1] - p0[1]
        run  = p1[0] - p0[0]

        if not rise:
            return (0, 0)
        elif not run:
            return (0, 1)
        else:
            return rise / run

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        rise_run = self.__get_rise_run(coordinates[0], coordinates[1])

        for i in range(2, len(coordinates)):
            new_ror = self.__get_rise_run(coordinates[0], coordinates[i])
            
            if new_ror != rise_run:
                return False

        return True