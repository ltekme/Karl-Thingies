name="MessagesSubmission"
rm -rf $name/$name.zip
sleep 1
(cd $name && zip -r $name.zip .) 
aws lambda update-function-code --function-name $name --zip-file fileb://$name/$name.zip
