name="MsgSubPost"
file="$name.zip"
rm -rf ./$name.zip
sleep 3
(cd ./$name && zip -r ../$file .) 
aws lambda update-function-code --function-name $name --zip-file fileb://$name.zip

aws s3 cp ${name}HTML s3://bukkit.aws.ltek.me/proj/msgp --recursive