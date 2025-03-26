# FastInjest_test
Oracle23ai has new feature of FastInjest. Its a NON ACID insert that could be useful in some cases.
This code is a supporting document for the blog on the same topic.
https://medium.com/@vbalebai/oracle-23ai-fast-ingest-high-speed-data-loading-when-should-you-use-it-a0284a2b25b2

## Create a table 
CREATE TABLE test_fast_ingest (
    id        NUMBER  ,
    test_col  VARCHAR2(100)
) SEGMENT CREATION IMMEDIATE
  MEMOPTIMIZE FOR WRITE;

## Configure 
#change the username,password and connect string.

## Install driver
pip install oracledb

## Run test 
python  fastInjest1.py
