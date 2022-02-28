_default:
	@echo "make"
sources:
	@echo "make sources"
	tar cvf - yum-conf-fermilab | gzip --best > yum-conf-fermilab.tar.gz
srpm: sources
	rpmbuild -bs --define '_sourcedir .' --define '_srcrpmdir .' yum-conf-fermilab.spec
