AC_PREREQ(2.53)
AC_INIT(python-gudev, 147.1)
AC_CONFIG_SRCDIR(gudev.defs)
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE(AC_PACKAGE_NAME, AC_PACKAGE_VERSION)

AM_MAINTAINER_MODE
AC_PROG_MAKE_SET

AC_PROG_CC
AM_PROG_CC_STDC
AC_HEADER_STDC

AM_PROG_LIBTOOL

AC_ARG_ENABLE(more-warnings,
	      [  --disable-more-warnings  Inhibit compiler warnings],
	      set_more_warnings=no)

if test "$GCC" = "yes" -a "$set_more_warnings" != "no"; then
	CFLAGS="$CFLAGS \
		-Wall -Wstrict-prototypes -Wmissing-declarations \
		-Wmissing-prototypes -Wnested-externs -Wpointer-arith"
fi


AM_PATH_PYTHON()
AM_CHECK_PYTHON_HEADERS(,AC_MSG_ERROR([install python-devel]))

PKG_CHECK_MODULES(PYGOBJECT, [pygobject-2.0 >= 2.18.0])

AC_MSG_CHECKING(for pygobject defs)
PYGOBJECT_DEFSDIR=`$PKG_CONFIG --variable=defsdir pygobject-2.0`
AC_SUBST(PYGOBJECT_DEFSDIR)
AC_MSG_RESULT($PYGOBJECT_DEFSDIR)

AC_MSG_CHECKING(for pygobject codegen)
PYGOBJECT_CODEGEN="$PYTHON `$PKG_CONFIG --variable=codegendir pygobject-2.0`/codegen.py"
AC_SUBST(PYGOBJECT_CODEGEN)
AC_MSG_RESULT($PYGOBJECT_CODEGEN)

AC_MSG_CHECKING(for pygobject h2def)
PYGOBJECT_H2DEF="$PYTHON `$PKG_CONFIG --variable=codegendir pygobject-2.0`/h2def.py"
AC_SUBST(PYGOBJECT_H2DEF)
AC_MSG_RESULT($PYGOBJECT_H2DEF)

PKG_CHECK_MODULES(GUDEV, gudev-1.0 >= 147)

AC_OUTPUT([Makefile])

echo
echo $PACKAGE v$VERSION

echo
echo "Now type make to compile"
echo

