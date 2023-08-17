class Solution:
    def mostBooked(self, n, meetings):
        available = [i for i in range(n)]
        occupied = []
        res = [0] * n
        for start, end in sorted(meetings):
            while occupied and occupied[0][0] <= start:
                _, room_num = heappop(occupied)
                heappush(available, room_num)
            if available:
                room_num = heappop(available)
                heappush(occupied, [end, room_num])
            else:
                room_end_time, room_num = heappop(occupied)
                heappush(occupied, [room_end_time + end - start, room_num])
            res[room_num] += 1
        return res.index(max(res))
