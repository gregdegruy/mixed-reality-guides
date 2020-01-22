pac auth create --url https://msott.crm.dynamics.com

# cd to RevTwoGuides dir
# local solution xml file
pac solution init --publisher-name RevTwo --publisher-prefix revtwo

# cd to guides plugin dir
pac plugin init

pac solution add-reference –path <path to your plugin project>
