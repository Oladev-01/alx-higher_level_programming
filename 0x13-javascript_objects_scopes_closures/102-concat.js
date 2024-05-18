#!/usr/bin/node
/* this script accepts two arguments
 files and concatenates the content of the
  two files into a destination file */

const fs = require('fs');

function concatFiles(sourceFile1, sourceFile2, destinationFile) {
    try {
        const content1 = fs.readFileSync(sourceFile1, 'utf-8');
        const content2 = fs.readFileSync(sourceFile2, 'utf-8');
        const concatenatedFile = content1 + content2;
        fs.writeFileSync(destinationFile, concatenatedFile, 'utf-8');
    }
    catch (error) {
        console.error('this is the error:', error.message);
    }
}

const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;
if (sourceFile1 && sourceFile2) {
    concatFiles(sourceFile1, sourceFile2, destinationFile);
}
