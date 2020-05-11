import bisect

class Solution:
    def videoStitching(self, clips, t):
        end_time_clips = sorted(clips, key=lambda x: (x[1], x[0]))
        unique_end_time_clips = [end_time_clips[0]]
        for clip in end_time_clips:
            if clip[1] != unique_end_time_clips[-1][1]:
                unique_end_time_clips.append(clip)

        start = -1
        for i in range(len(unique_end_time_clips)):
            if unique_end_time_clips[i][0] == 0:
                start = i

        if start == -1:
            return -1
        elif unique_end_time_clips[start][1] >= t:
            return 1

        end_times = [unique_end_time_clips[start][1]]
        length = 1
        min_length = len(clips) + 1

        for video in unique_end_time_clips[start+1:]:
            if end_times[length-1] >= video[0]:
                i = bisect.bisect_left(end_times, video[0], hi=length)
                if len(end_times) == i + 1:
                    end_times.append(video[1])
                else:
                    end_times[i + 1] = video[1]

                length = i + 2

                if end_times[length-1] >= t:
                    min_length = min(min_length, length)

        return min_length if min_length <= len(clips) else -1

    # solution from others
    def videoStitching2(self, clips, T):
        end, end2, res = -1, 0, 0
        for i, j in sorted(clips):
            if end2 >= T or i > end2:
                break
            elif end < i <= end2:
                res, end = res + 1, end2
            end2 = max(end2, j)
        return res if end2 >= T else -1
