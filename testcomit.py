# Databricks notebook source
import pandas as pd

d = {'val': [1,2,3]}

pd.DataFrame(d).to_csv('/Workspace/Repos/a.tarasov@dodopizza.com/analytic_images/images/test_file.csv')
