# cicd-jbosscli
This ansible playbook and module created for send commands to embadded host contoller of JBoss CLI.

Sample usage:

ansible-playbook jboss-config.pb \
-e jboss_jks_pass="changeit" \
-e USERNAME=DBSCHEMAUSERFORNONXADATASOURCE \
-e PASSWORD=DBSCHEMAPASSWORDFORNONXADATASOURCE \
-e XAUSERNAME=DBSCHEMAUSERFORXADATASOURCE \
-e XAPASSWORD=DBSCHEMAPASSWORDFORXADATASOURCE \
-e DBIP=TARGETDBIP \
-e DBPORT=1521FORDEFAULT \
-e DBSN=TESTDB \

non of parameters are required in above, i added to datasource / SSL configuration for sample. you can remove in playbook and parameter list if those are not required for you.
