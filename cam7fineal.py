from cam7Final_withoutMail import *

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepath.qqqqqqqqqqqqqqqqqqqqqqq

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(filename)
            file_paths.append(filepath)  # Add it to the list.
    return file_paths

def objectdetectionVideo(video1):
    finaldetect(video1)

def finalRunProgram():
    videos1 = get_filepaths("videos/22th-sep")


    for i in videos1:
        x = "videos/22th-sep/"+i

        objectdetectionVideo(x)
# objectdetectionVideo('1IVISUSAJ1004C1_20-11-2021-06-00_20-11-2021-07-00215.mp4','1IVISUSAJ1004C1_20-11-2021-06-00_20-11-2021-07-00215.mp4','1IVISUSAJ1004C1_20-11-2021-06-00_20-11-2021-07-00215.mp4','1IVISUSAJ1004C1_20-11-2021-06-00_20-11-2021-07-00215.mp4')
finalRunProgram()