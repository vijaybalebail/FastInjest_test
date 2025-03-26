# FastInjest_test
Oracle23ai has new feature of FastInjest. Its a NON ACID insert that could be useful in some cases.

## Create a table 
CREATE TABLE test_fast_ingest (
    id        NUMBER  ,
    test_col  VARCHAR2(100)
) SEGMENT CREATION IMMEDIATE
  MEMOPTIMIZE FOR WRITE;

## configure 
#change the username,password and connect string.

## install priver
pip install oracledb

## run test 
python  fastInjest1.py
