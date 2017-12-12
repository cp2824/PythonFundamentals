# Schedule breaks
# - Time between breaks
# - Run through your shift
# - Open a browser and play your favorite video/music at break
# What do we need?
# - Track the time
# - Open URL
# - Sleep (then loop 3? times)
from webbrowser import open as openw
import time

def set_breaks(sleep_time=5, total_breaks=3, url="https://www.youtube.com/watch?annotation_id=annotation_2406068509&feature=iv&src_vid=cUYSGojUuAU&v=AruWNRVZfyk"):
    """
    Opens a web page at specific intervals (for tracking breaks)
    :param sleep_time: seconds between breaks
    :param total_breaks: total number of breaks
    :param url: web page to visit
    :return: none
    """
    #total_breaks = 3
    break_count = 0
    #url = "https://www.youtube.com/watch?annotation_id=annotation_2406068509&feature=iv&src_vid=cUYSGojUuAU&v=AruWNRVZfyk"

    while break_count < total_breaks:
        openw(url)
        time.sleep(sleep_time)
        break_count += 1

def my_break(break_info = None):
    """
    Function to keep track of breaks
    :param break_info: a dictionary with the following keys:
        t_break <int> default is 3
        url <string> default "https://www.youtube.com/watch?annotation_id=annotation_2406068509&feature=iv&src_vid=cUYSGojUuAU&v=AruWNRVZfyk"
        t_sleep <int> in seconds, default = 1 hour
    :return:
    """
    if break_info is None:
        break_info = {}
        break_info['t_breaks'] = 3
        break_info['url'] = "https://www.youtube.com/watch?annotation_id=annotation_2406068509&feature=iv&src_vid=cUYSGojUuAU&v=AruWNRVZfyk"
        break_info['t_sleep'] = 60 * 60 # one hour
        #break_info['t_sleep'] = 5 # one hour

    break_count = 0
    while break_count < break_info['t_breaks']:
        openw(break_info['url'])
        time.sleep(break_info['t_sleep'])
        break_count += 1

if __name__ == '__main__':
    my_break()
