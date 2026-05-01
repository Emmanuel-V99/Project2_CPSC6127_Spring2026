REM Enter each of these lines of code, one by one, into a Command Prompt as an administrator.
REM Additional Command Prompt windows will pop up, continue your input on the first window you opened

REM Start Hadoop services
start start-dfs.cmd
start start-yarn.cmd
REM If you want to check to ensure the commands above are running as expected, enter:
::jps

REM IF YOU ARE RE-RUNNING THE BELOW COMMAND AGAIN, DELETE THE OUTPUT FOLDER FIRST:
:: hdfs dfs -rm -r /emmanuel/output
REM IF YOU WANT TO DELETE EVERYTHING:
::hdfs dfs -rm -r /emmanuel
::hdfs dfs -rm -r /tmp

REM Create directory in HDFS
hdfs dfs -mkdir /emmanuel

REM Put file into HDFS
hdfs dfs -put "C:/Users/vande/OneDrive/Documents/Spring_2026_Semester/CPSC_6127_Contemporary_Issues_in_DB_Management_Systems/Project_2/data/cleaned_emails.txt" /emmanuel/

REM Run Hadoop streaming job
hadoop jar "C:/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar" -input "/emmanuel/cleaned_emails.txt" -output "/emmanuel/output" -mapper "python C:/hadoop_scripts/mapper.py" -reducer "python C:/hadoop_scripts/reducer.py"

REM Run Hadoop streaming job WITH COMBINER
::hadoop jar "C:/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar" -input "/emmanuel/cleaned_emails.txt" -output "/emmanuel/output" -mapper "python C:/hadoop_scripts/mapper.py" -reducer "python C:/hadoop_scripts/reducer.py" -combiner "C:/hadoop_scripts/combiner.py"
