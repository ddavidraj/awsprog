# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:09:47 2020

@author: ddaniel4363
"""

import boto3
sns = boto3.client('sns')
def detect_labels(photo, bucket):
    client = boto3.client('rekognition')
    response = client.detect_labels(Image = {
    'S3Object': {
      'Bucket': bucket,
      'Name': photo
    }
  },
  MaxLabels = 10)
    print('Detected labels for ' + photo)
    print()
    labellist=[]
    for label in response['Labels']:
        
        if label['Confidence'] > 90 and label['Name']=='Person':
            print("Label: " + label['Name'])
            print("Confidence: " + str(label['Confidence']))
            labellist.append(label['Name'])
    print("Instances:")
    for instance in label['Instances']:
        print(" Bounding box")
        print(" Top: " + str(instance['BoundingBox']['Top']))
        print(" Left: " + str(instance['BoundingBox']['Left']))
        print(" Width: " + str(instance['BoundingBox']['Width']))
        print(" Height: " + str(instance['BoundingBox']['Height']))
        print(" Confidence: " + str(instance['Confidence']))
        print()
    print("Parents:")
    for parent in label['Parents']:
        print(" " + parent['Name'])
    print("----------")
    print()
    return len(labellist)

def main():
    photo = 'lowlight.jpg'
    bucket = 'ddpython13547'
    label_count = detect_labels(photo, bucket)
    if label_count > 0:
        resp = sns.publish(TopicArn='arn:aws:sns:us-east-1:125733266075:survdd', 
							Message='Suspicious activity detected'
						  )
    print(resp)
    
    
    
    print("Labels detected: " + str(label_count))
    
if __name__ == "__main__":
    main()