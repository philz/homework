#!/bin/bash

set -e
set -x

HADOOP=$HOME/src/desktop/build/hadoop/build/hadoop-0.20.2-dev/bin/hadoop
INPUT=scowiki-20090929-one-page-per-line
OUTPUT_PREFIX=sco
STREAMING=$HOME/src/desktop/build/hadoop/build/hadoop-0.20.2-dev/contrib/streaming/hadoop-0.20.2-dev-streaming.jar

#$HADOOP jar $STREAMING -input $INPUT -output sco/links -mapper "python extract_links.py map" -numReduceTasks 0 -file extract_links.py -file common.py
#$HADOOP jar $STREAMING -input sco/links -output sco/pr0 -mapper "python calculate_pagerank.py map" -reducer "python calculate_pagerank.py reduce" -numReduceTasks 2 -file calculate_pagerank.py -file common.py
#$HADOOP jar $STREAMING -input sco/pr0 -output sco/pr1 -mapper "python calculate_pagerank.py map" -reducer "python calculate_pagerank.py reduce" -numReduceTasks 2 -file calculate_pagerank.py -file common.py
#$HADOOP jar $STREAMING -input sco/pr1 -output sco/pr2 -mapper "python calculate_pagerank.py map" -reducer "python calculate_pagerank.py reduce" -numReduceTasks 2 -file calculate_pagerank.py -file common.py
#$HADOOP jar $STREAMING -input sco/pr2 -output sco/pr3 -mapper "python calculate_pagerank.py map" -reducer "python calculate_pagerank.py reduce" -numReduceTasks 2 -file calculate_pagerank.py -file common.py
#$HADOOP jar $STREAMING -input sco/pr3 -output sco/pr4 -mapper "python calculate_pagerank.py map" -reducer "python calculate_pagerank.py reduce" -numReduceTasks 2 -file calculate_pagerank.py -file common.py
#$HADOOP jar $STREAMING -input sco/pr4 -output sco/pr5 -mapper "python calculate_pagerank.py map" -reducer "python calculate_pagerank.py reduce" -numReduceTasks 2 -file calculate_pagerank.py -file common.py
#$HADOOP jar $STREAMING -input sco/pr5 -output sco/pr6 -mapper "python calculate_pagerank.py map" -reducer "python calculate_pagerank.py reduce" -numReduceTasks 2 -file calculate_pagerank.py -file common.py
#$HADOOP jar $STREAMING -input sco/pr6 -output sco/pr7 -mapper "python calculate_pagerank.py map" -reducer "python calculate_pagerank.py reduce" -numReduceTasks 2 -file calculate_pagerank.py -file common.py
#$HADOOP jar $STREAMING -input sco/pr7 -output sco/pr8 -mapper "python calculate_pagerank.py map" -reducer "python calculate_pagerank.py reduce" -numReduceTasks 2 -file calculate_pagerank.py -file common.py
#$HADOOP jar $STREAMING -input sco/pr8 -output sco/pr9 -mapper "python calculate_pagerank.py map" -reducer "python calculate_pagerank.py reduce" -numReduceTasks 2 -file calculate_pagerank.py -file common.py
$HADOOP jar $STREAMING -input sco/pr9 -output sco/final -mapper "python cleanup.py map" -reducer "python cleanup.py reduce" -numReduceTasks 1 -file cleanup.py -file common.py
