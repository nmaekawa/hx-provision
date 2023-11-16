#!/bin/bash

#
# compress and transfer local source file to s3 bucket/prefix
#
# expects to be run in ubuntu; stat command will not work in macos
#

#
# functions
#
usage()
{
    cat << EOF
usage: $0 --source <path> --s3-bucket <bucket> --s3-prefix <prefix> [--prefix <prefix>] [--workdir <dir>]
  compress and transfer local source file to s3://bucket/prefix;
  adds "last modification date" and "prefix" name to final target s3 object name

  --source     fullpath for source to be copied
  --s3-bucket  s3 bucket name of copy target
  --s3-prefix  s3 prefix for copy target
  --prefix     optional; prefix to be added to final target s3 object name
  --workdir    optional, defaults to /tmp; path to dir where source file will be compressed

EOF
}

WORKDIR="/tmp"

while [ "$1" != "" ]; do
    case $1 in
        --source )          shift
                            SOURCE_FILEPATH=$1
                            ;;
        --s3-bucket )       shift
                            TARGET_S3_BUCKET=$1
                            ;;
        --s3-prefix )       shift
                            TARGET_S3_PREFIX=$1
                            ;;
        --prefix )          shift
                            TARGET_FILE_PREFIX=$1
                            ;;
        --workdir )         shift
                            WORKDIR=$1
                            ;;
        -h | --help )       usage
                            exit
                            ;;
        * )                 usage
                            exit 1
    esac
    shift
done

if [ -z $SOURCE_FILEPATH ] || [ -z $TARGET_S3_BUCKET ] || [ -z $TARGET_S3_PREFIX ]
then
    echo "missing input; src:$SOURCE_FILEPATH - bkt:$TARGET_S3_BUCKET - pre:$TARGET_S3_PREFIX"
    echo
    usage
    exit 1
fi

echo "source filepath is $SOURCE_FILEPATH"
echo "target s3 bucket is $TARGET_S3_BUCKET"
echo "target s3 prefix is $TARGET_S3_PREFIX"
echo "target file prefix is $TARGET_FILE_PREFIX"
echo "workdir is $WORKDIR"

# get formatted last modification date
mod_date=$(stat "$SOURCE_FILEPATH" --format="%y" | awk -F"." '{print $1}' |  sed "s/ /T/g" | sed "s/://g")
date_prefix=$(echo $mod_date | awk -F"T" '{print $1}')
target_filename=$(basename $SOURCE_FILEPATH)

if [ -z $mod_date ] || [ -z $target_filename ]
then
    echo "error formatting target backup filename"
    exit 1
fi

if [ -z $TARGET_FILE_PREFIX ]; then
    target_backup_filename="${mod_date}_${target_filename}.gz"
else
    target_backup_filename="${mod_date}_${TARGET_FILE_PREFIX}_${target_filename}.gz"
fi
echo "backup filename is $target_backup_filename"

# compress file
gzip -c $SOURCE_FILEPATH > $WORKDIR/$target_backup_filename
if [ $? -ne 0 ]; then
    echo "error compressing: gzip -c $SOURCE_FILEPATH > ${WORKDIR}/${target_backup_filename}"
    exit 1
fi

# copy to s3
# STANDARD_IA == infrequent access
/usr/bin/aws s3 cp $WORKDIR/$target_backup_filename \
    s3://${TARGET_S3_BUCKET}/${TARGET_S3_PREFIX}/${date_prefix}/${target_backup_filename} \
    --storage-class STANDARD_IA
if [ $? -ne 0 ]; then
    echo "error cp to s3:" \
         " aws s3 cp ${WORKDIR}/${target_backup_filename} " \
         "s3://${TARGET_S3_BUCKET}/${TARGET_S3_PREFIX}/$date_prefix/$target_backup_filename" \
         "--storage-class STANDARD_IA"
fi

# cleanup
rm $WORKDIR/$target_backup_filename
echo "cleaned up $WORKDIR/$target_backup_filename"

echo "$(date +"%F %T") copy to s3 DONE"

exit 0

