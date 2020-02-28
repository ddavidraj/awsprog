import boto3
import json
def detect_faces(photo, bucket):

    client=boto3.client('rekognition')

    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},Attributes=['ALL'])

    print('Detected faces for ' + photo)    
    for faceDetail in response['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) 
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        print('Here are the other attributes:')
        print(json.dumps(faceDetail, indent=4, sort_keys=True))
    return len(response['FaceDetails'])
def compare_faces(bucket,sourceFile, targetFile):

    client=boto3.client('rekognition')
   
    
    

    response=client.compare_faces(SimilarityThreshold=80,
                                  SourceImage={'S3Object':{'Bucket':bucket,'Name':sourceFile}},
                                  TargetImage={'S3Object':{'Bucket':bucket,'Name':targetFile}})
    
    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The face at ' +
               str(position['Left']) + ' ' +
               str(position['Top']) +
               ' matches with ' + similarity + '% confidence')

    
         
    return len(response['FaceMatches'])

def main():
    photo='badri2.jpg'
    sourceFile='badri.jpg'
    targetFile='badri2.jpg'
    bucket='ddpython13547'
    #face_count=detect_faces(photo, bucket)
    face_count=compare_faces(bucket,sourceFile,targetFile)
    print("Faces detected: " + str(face_count))


if __name__ == "__main__":
    main()