#!/bin/bash

echo "Enter the commit message: "
read commitMessage

git add .
git commit -m "$commitMessage"
git push

echo "Commit and push complete!"
