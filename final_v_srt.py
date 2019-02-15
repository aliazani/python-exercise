import re
import datetime

data = open("F:\\New folder (2)\\S06_assignment_Three.Billboards.Outside.Ebbing.Missouri.2017.WEB-DL.x264-FGT.srt",
            'a+')
reading_data = data.read()
srt_pattern = re.compile(r"\d+\n(^\d+:\d+:\d+,\d+)\s+-->\s+(\d+:\d+:\d+,\d+)\n", flags=re.MULTILINE)
find = srt_pattern.findall(reading_data)
find = list(find)

for start_time, end_time in find:
    start_time = datetime.datetime.strptime(start_time, '%H:%M:%S,%f')
    end_time = datetime.datetime.strptime(end_time, '%H:%M:%S,%f')
    time_plus = datetime.timedelta(0, 1)
    start_time += time_plus
    end_time += time_plus
    res = "\n" + str(start_time) + "\n" + str(end_time) + "\n"
    res = res.replace('1900-01-01', '')

data.close()
