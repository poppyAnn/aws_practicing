#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3

def create_bucket():
    client = boto3.client('s3')

    response = client.create_bucket(
        ACL = 'public-read',
        Bucket = 'annluhomework',
        CreateBucketConfiguration={
            'LocationConstraint':'us-west-2'
        }
        # GrantFullControl= '',
    )

def upload_file():
    s3 = boto3.resource('s3')

    s3.Object('annluhomework','log_consumerInfo.txt').upload_file('/home/luyunfang/workspace/awshomework/awshomework/log_consumerInfo.txt')


if __name__ == '__main__':

    create_bucket()
    upload_file()