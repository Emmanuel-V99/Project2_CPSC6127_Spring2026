# Project2_CPSC6127
# Emmanuel Vanderson
# May 1st, 2026

Goal is to conduct a large-scale data analysis using Hadoop MapReduce, focusing on distributed data processing.

INSTRUCTIONS
-To install Hadoop and Java on your Windows machine, and configure your environmental variables as needed:
    Carefully follow the instructions given from this link: https://github.com/ruslanmv/How-to-install-Hadoop-on-Windows/tree/master?tab=readme-ov-file within the README.md file
-If this proves to be unsuccessful for you, please utilize the following YouTube links to assist you in Hadoop environment setup
    -How to Install Hadoop on Windows: Step-by-Step Guide | SPPU DSBDA LAB ( https://www.youtube.com/watch?v=Dp2-dAftD1Q )
    -Hadoop HDFS Commands and MapReduce with Example: Step-by-Step Guide | Hadoop Tutorial | IvyProSchool ( https://www.youtube.com/watch?v=7O56u3LyPTY )
-Due to file size restrictions, user must download the enron email data set from the provided link, and place it within the empty /data folder --> https://www.kaggle.com/datasets/wcukierski/enron-email-dataset

-In order to preprocess the data from the Enron emails (because the file is much too large, and is more preferrable in a .txt file anyway), run:
    -python scripts\preprocess_enron.py
    -This should generate data/cleaned_emails.txt with non-zero size.
-It is imperative that you run the following lines in Command Prompt as an Administrator in order to format the namenode and start Hadoop:
    start-dfs.cmd
    start-yarn.cmd  
-Check if Local Host is up by opening a web browser and inputting "localhost:9870".
    -(Should display a site with a green nav bar at the top)
-(Check if NameNode and DataNode are working by inputting the 'dfs' command)
-Please use HDFS for Input/Output:
If your goal is to process files using Hadoop’s distributed architecture, first place the files in HDFS, then reference them.

Quick pre-run checklist (recommended each run):
1. Confirm local preprocessed input is not empty:
python scripts\preprocess_enron.py
powershell -Command "Get-Item .\data\cleaned_emails.txt | Select-Object Length,LastWriteTime"

2. Replace the HDFS input file with the latest local file:
hdfs dfs -test -e /emmanuel/cleaned_emails.txt
hdfs dfs -rm /emmanuel/cleaned_emails.txt
hdfs dfs -put "C:/Users/vande/OneDrive/Documents/Spring_2026_Semester/CPSC_6127_Contemporary_Issues_in_DB_Management_Systems/Project_2/data/cleaned_emails.txt" /emmanuel/
hdfs dfs -ls /emmanuel

3. Remove prior output directory before rerun:
hdfs dfs -rm -r /emmanuel/output

1. Upload your data file to HDFS
Run these command in Command Prompt:

First, make a directory in HDFS
hdfs dfs -mkdir /emmanuel

Navigate to the 'Utilities' dropdown and select "Browse the File System"
Click the 'Go!' button. You should now see the directory that you've just made. The name of the folder will be all the way to the right, under the 'Name' column. It should be empty for now (click the highlighted folder name and make sure).

Then, upload your data file that you will be running MapReduce on to HDFS

hdfs dfs -put "C:/Users/vande/OneDrive/Documents/Spring_2026_Semester/CPSC_6127_Contemporary_Issues_in_DB_Management_Systems/Project_2/data/cleaned_emails.txt" /emmanuel/

(Ensure the newly created folder now stores data (cleaned_emails.txt))

2. Update your Hadoop streaming command
Now, reference the HDFS paths instead of local Windows paths:

hadoop jar "C:/hadoop/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar" -file scripts/mapper.py -file scripts/reducer.py -input "/emmanuel/cleaned_emails.txt" -output "/emmanuel/output" -mapper "python mapper.py" -reducer "python reducer.py"

IF YOU ARE RE-RUNNING THE ABOVE COMMAND AGAIN, DELETE THE OUTPUT FOLDER FIRST: hdfs dfs -rm -r /emmanuel/output

TO RUN THE HADOOP MAPREDUCE PROGRAM WITH COMBINER
hadoop jar "C:/hadoop/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar" -file scripts/mapper.py -file scripts/reducer.py -file scripts/combiner.py -input "/emmanuel/cleaned_emails.txt" -output "/emmanuel/output" -mapper "python mapper.py" -reducer "python reducer.py" -combiner "python combiner.py"

-Included "part-00000" within the output folder to provide you with a reference to how the output should look