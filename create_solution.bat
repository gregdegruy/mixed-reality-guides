pac auth create --url https://msott.crm.dynamics.com

# cd to RevTwoGuides dir the cds solution
# local solution xml file
pac solution init --publisher-name RevTwo --publisher-prefix revtwo

# cd to RevTwoPlugin dir
pac plugin init
msbuild

# cd to RevTwoGuides dir the cds solution
pac solution add-reference –path <path to your plugin project>
# generate solutoin zip
msbuild /t:build /restore