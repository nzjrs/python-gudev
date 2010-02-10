defsdir = $(datadir)/pygobject/2.0/defs
defs_DATA = gudev.defs

ACLOCAL_AMFLAGS = -I m4

INCLUDES = \
	$(GUDEV_CFLAGS) \
	$(GOBJECT_CFLAGS) \
	$(PYGOBJECT_CFLAGS) \
	$(PYTHON_INCLUDES)

pkgpythondir = $(pyexecdir)
pkgpyexecdir = $(pyexecdir)

pkgpyexec_LTLIBRARIES = gudev.la
gudev_la_LDFLAGS = -module -avoid-version -export-symbols-regex initgudev
gudev_la_LIBADD = $(GUDEV_LIBS) $(GOBJECT_LIBS) $(PYGOBJECT_LIBS)
gudev_la_SOURCES = gudevmodule.c gudev.c
#nodist_gudev_la_SOURCES = gudev.c

CLEANFILES = gudev.c
EXTRA_DIST = NEWS ChangeLog gudev.override $(defs_DATA) test.py

gudev.c: gudev.defs gudev.override
.defs.c:
	(cd $(srcdir)\
	 && $(PYGOBJECT_CODEGEN) \
		--override $*.override \
		--prefix py$* $*.defs) > gen-$*.c \
	&& cp gen-$*.c $*.c \
	&& rm -f gen-$*.c

update-defs:
	$(PYGOBJECT_H2DEF) /usr/include/gudev-1.0/gudev/*.h > gudev-new.defs

# ChangeLog generation from nautils
distclean-local:
	if test "$(srcdir)" = "."; then :; else \
		rm -f ChangeLog; \
	fi

ChangeLog:
	@echo Creating $@
	@if test -d "$(srcdir)/.git"; then \
	  (GIT_DIR=$(top_srcdir)/.git ./missing --run git log 147.1.. --stat -M -C --name-status  --date=short --no-color) | fmt --split-only > $@.tmp \
	  && mv -f $@.tmp $@ \
	  || ($(RM) $@.tmp; \
	      echo Failed to generate ChangeLog, your ChangeLog may be outdated >&2; \
	      (test -f $@ || echo git-log is required to generate this file >> $@)); \
	else \
	  test -f $@ || \
	  (echo A git checkout and git-log is required to generate ChangeLog >&2 && \
	  echo A git checkout and git-log is required to generate this file >> $@); \
	fi

release: dist
	scp @PACKAGE@-@VERSION@.tar.gz root@greenbirdsystems.com:/var/www/johnstowers.co.nz/files/python-gudev/

.PHONY: ChangeLog update-defs
