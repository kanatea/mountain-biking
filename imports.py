#installing the rest of the dependencies into our environment

# for api
from flask import Flask, jsonify, render_template, request
#from  psycopg2 - for api
import psycopg2
#from python - for strava api and etl
import time, os, requests
#from datetime - for timestamps
from datetime import datetime, timedelta
