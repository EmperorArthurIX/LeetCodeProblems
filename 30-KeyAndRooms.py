class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis = set()
        q = []
        if len(rooms[0]) == 0:
            return False
        q.extend(rooms[0])
        ls = rooms[0]
        vis.add(0)
        while q:
            room = q.pop(0)
            if room not in vis:
                vis.add(room)
                q.extend(rooms[room])
            print(q)
        if len(rooms) != len(vis):
            return False
        
        return True