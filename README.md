## Voiceover Generation

Run this [python function](https://github.com/jossTripoli/gen-text-to-speech/blob/main/aws_lambda/main/LambdaHandler.py) in AWS Lambda make sure to give it full access to polly and s3 bucket (configuartion -> permissions -> click the role name -> add permissions -> add policies).

Replace the variables "bucket_name" with your bucket, "folder" with the name of the folder in the bucket

Replace "page" variable with the name of the page where the text it is found.

Add the desired text to the "text_source" variable.

Click on the "Deploy" Button

Then run it by clicking the "Test" button

This will create the voice over mp3s and speech marks for the three avatars and save it into the s3 bucket.

## Highlighting Speech JSON Creation

Clone this [python program for formating AWS speechmark JSON](https://github.com/jossTripoli/formatPollyJson)

Download the agent daring, valiant, and intrepid speech marks (json) from the AWS bucket for the page you are working on.

Move the json files to  aws_downloads/ .

Now run

```
export filename={filename} 
run_daring.sh
 # Ex. filename=intro 
 # i.e. it ignores the voice name attached to the file 
```

Go to the index_format/ .

Next open the generated daring.json and copy it to your modules narration.json for the page's daring JSON. Copy the id's for each pug element to the corresponding words to fill in the "element" values (for titles the id should be on the title span itself while for all other text it should be on the parent element). They will be in the format "narrate-pageNumber-pageName". When you're done this run locally to ensure the sync is good. Most of the times it is great but I've found some words the speech marks are a little off. Like for the word "number" I will subtract 200ms to fix it.

When the daring JSON is perfect copy it into index_format/daring.json.

```
sh run_scripts.sh
```

Go to the final-format/ folder.

Copy the json from daring.json, intrepid.json and valiant.json into narration.json for the page's intrepid and valiant JSON and you're good!
