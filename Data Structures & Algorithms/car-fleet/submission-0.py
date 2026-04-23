class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired_info = zip(position, speed)
        sorted_info = sorted(paired_info, key=lambda x : x[0], reverse=True)

        fleet_count = 0
        cur_fleet_arival = 0

        for pos, speed in sorted_info:
            arival = float(target - pos) / speed
            if cur_fleet_arival >= arival:
                continue
            cur_fleet_arival = arival
            fleet_count += 1
        
        return fleet_count



        

        
