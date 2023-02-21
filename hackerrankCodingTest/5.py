#!/bin/python3

import math
import os
import random
import re
import sys
import json
import requests


#
# Complete the 'getUsernames' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts INTEGER threshold as parameter.
# API URL: https://jsonmock.hackerrank.com/api/article_users?page=<pageNumber>
#

def getUsernames(threshold):

    usernames = []
    page = 1
    totalPages = 1

    while page <= totalPages:
        apiRequest = requests.get(
            'https://jsonmock.hackerrank.com/api/article_users?page=' + str(page))
        articles = apiRequest.json()['data']

        if page == 1:
            totalPages = apiRequest.json()['total_pages']

        for value in articles:
            submissionCount = value['submission_count']

            if submissionCount > threshold:
                usernames.append(value['username'])

        page += 1

    return usernames


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    threshold = int(input().strip())

    result = getUsernames(threshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
