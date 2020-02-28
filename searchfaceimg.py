# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:02:10 2020

@author: ddaniel4363
"""

import boto3

if __name__ == "__main__":

    bucket='ddpython13547'
    collectionId='myCollection'
    fileName='badri2.jpg'
    threshold = 10
    maxFaces=2

    client=boto3.client('rekognition')

  
    response=client.search_faces_by_image(CollectionId=collectionId,
                                Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
                                FaceMatchThreshold=threshold,
                                MaxFaces=maxFaces)

                                
    faceMatches=response['FaceMatches']
    print ('Matching faces')
    for match in faceMatches:
            print ('FaceId:' + match['Face']['FaceId'])
            print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
            print