name="FormReply"
rm -rf push/$name.zip
sleep 1
(cd Formget && zip -r ../push/$name.zip .) 
aws lambda update-function-code --function-name $name --zip-file fileb://push/$name.zip
aws s3 cp HTML/form/ s3://bukkit.aws.ltek.me/proj/form --recursive
