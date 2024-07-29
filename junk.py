import json
from boto3 import Session

moduleID = "grandparent-narration/"
folder = "techniques/"
page = "types-3"

def generateAudioUsingText(plainText, filename, myVoiceId):
    # Generate audio using Text
    session = Session(region_name="us-east-1")
    polly = session.client("polly")
    response = polly.synthesize_speech( Text=plainText,
                                        Engine = "neural",
                                        TextType = "text",
                                        OutputFormat="mp3",
                                        VoiceId=myVoiceId)
    s3 = session.resource('s3')
    bucket_name = "dart-store"
    bucket = s3.Bucket(bucket_name)
    filename = moduleID + folder + filename
    stream = response["AudioStream"]
    bucket.put_object(Key=filename, Body=stream.read())
    
    
def generateSpeechMarksUsingText(plainText, filename, myVoiceId):
    # Generate audio using Text
    session = Session(region_name="us-east-1")
    polly = session.client("polly")
    response = polly.synthesize_speech( Text=plainText,
                                        Engine = "neural",
                                        TextType = "text",
                                        OutputFormat="json",
                                        SpeechMarkTypes=["word"],
                                        VoiceId=myVoiceId)
    s3 = session.resource('s3')
    bucket_name = "dart-store"
    bucket = s3.Bucket(bucket_name)
    filename = moduleID + folder + filename
    stream = response["AudioStream"]
    bucket.put_object(Key=filename, Body=stream.read())
    
def generateAudioUsingSSML(ssmlText, filename, myVoiceId):
    # Generate audio using Text
    session = Session(region_name="us-east-1")
    polly = session.client("polly")
    response = polly.synthesize_speech( Text=ssmlText,
                                        Engine = "neural",
                                        TextType = "ssml",
                                        OutputFormat="mp3",
                                        VoiceId=myVoiceId)
    s3 = session.resource('s3')
    bucket_name = "dart-store"
    bucket = s3.Bucket(bucket_name)
    filename = moduleID + folder + filename
    stream = response["AudioStream"]
    bucket.put_object(Key=filename, Body=stream.read())

def generateSpeechMarksUsingSSML(ssmlText, filename, myVoiceId):
    # Generate audio using Text
    session = Session(region_name="us-east-1")
    polly = session.client("polly")
    response = polly.synthesize_speech( Text=ssmlText,
                                        Engine = "neural",
                                        TextType = "ssml",
                                        OutputFormat="json",
                                        SpeechMarkTypes=["word"],
                                        VoiceId=myVoiceId)
    s3 = session.resource('s3')
    bucket_name = "dart-store"
    bucket = s3.Bucket(bucket_name)
    filename = moduleID + folder + filename
    stream = response["AudioStream"]
    bucket.put_object(Key=filename, Body=stream.read())

def lambda_handler(event, context):

    avatars = ["intrepid", "daring", "valiant"]
    voice_ids = ["Ruth", "Danielle", "Matthew"]

    for avatar, myVoiceId in zip(avatars, voice_ids):


        text_source =  '''
Prey on Vulnerable Moments.

The initial contact from the scammer will often come late at night when people may be disoriented or less alert, making them more vulnerable to being confused or misled.

Scammers may reach out during times of bad weather, natural disasters, or other concerning events when people are already in a heightened state of worry about their loved ones' safety. This preys on the grandparents’ emotional vulnerability.  


'''


        generateAudioUsingText(text_source, f'{page}_{avatar}.mp3', myVoiceId)
        generateSpeechMarksUsingText(text_source, f'{page}_{avatar}.json', myVoiceId)
        
    return {
        'statusCode': 200,
        'body': json.dumps('Successful Generation using AWS Polly! Your audio files are so good, even Beyonce is taking notes.')
    }